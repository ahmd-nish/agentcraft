# MC-199467: Certain entity animations stop after they've existed in world for too long

**Mojira URL:** [https://bugs.mojang.com/browse/MC-199467](https://bugs.mojang.com/browse/MC-199467)

## Report details

- **Mojira categories:** Rendering
- **Project:** MC
- **Issue key:** MC-199467
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-09-01T19:27:11.262-0700
- **Updated:** 2025-10-30T06:36:35.201-0700
- **Resolution date:** 2025-10-30T06:36:35.138-0700
- **Affects versions:** 1.16.2; 1.18.1; 22w11a; 22w13a; 1.19 Pre-release 1; 1.19.2; 22w43a; 1.19.3; 23w03a; 1.20.1; 1.20.2; 23w44a; 1.20.4
- **Fix versions:** 25w45a
- **Area:** Platform
- **Labels:** animation; overflow
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2020-09-01_23.59.05.png; 2023-07-11 16-24-36.mp4; bat_wings.mp4; bee_wings.mp4
- **Issue links:** Relates:inward:MC-130960:Phantom is often not animated (only Multiplayer?) | Relates:outward:MC-245895:View Bobbing stops working after long elytra flight | Duplicate:inward:MC-264170:Walking animation breaks after walking for too long

## Description

The bug
Certain Entities such as Bee and Bat stop their animations of their wings after they've been in the world for too long. I noticed this bug when I was making a mod for forge that extended the bee entity and I noticed that my bees wouldn't flap their wings after being in world for a while so I tested it in vanilla (unmodified) Minecraft and noticed it had the same problem so I went back to the vanilla bees model code and noticed it was using ageInTicks(tickexisted + partialticks) which back traced back to ticks existed so I tested again using a command block on repeat to see how long it would take for the bee it takes about 98000 ticks - 98200 ticks for the bee to stop flapping the wings while for the bat it took from 158400 ticks - 158600 ticks. the value is not random between these values its consistent I'm just giving a range due to my scoreboard taking a couple extra ticks to start the repeating of adding 1 to the scoreboard. This is likely due to the ticks existed variable multiplied by whatever value you guys set per entity model to then be used in your math classes cos method and then the method returning the same index every time due to the input value being so big. This could also happen on the phantom in theory but it would take about a full day according to calculations so I didn't test it but in theory it has the same code as the bat and the bee do for the cos method implementation so it should happen on it too.
Expected result
Bees and Bats and other entities that have animations that use the cos method not stop after they exceed a certain value.
Observed result
The bees and bats stopped their wing animations, you can see this happening in the videos provided.
Reproduce
- Go into a world and spawn a bee and you can also spawn a bat if you wanna see it happen to that but you'll have to wait longer.

- Wait about 81 min

- then you'll see a bee not flapping its wings anymore

- and you can wait about another 51 min if you spawned the bat

- then you'll see a bat not flapping its wings anymore

Code analysis and potential fix
Code analysis by  can be found in this comment.
Potential fix by  can be found in this comment.

## Comments (12)

### Comment 1: migrated (2020-09-01T19:27:11.262-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Jeuv (2021-12-04T19:16:50.617-0800)

Confirmed for 1.18.

### Comment 3: ampolive (2021-12-17T17:17:17.229-0800)

Code analysis: the issue is exactly as stated, some entity renderers use the entity's tick count for calculation, resulting in an eventual integer overflow as they use Mth.cos(). This is using Mojang mappings.
In LivingEntityRenderer#render(...), the animation is set up with this line: ((EntityModel)this.model).setupAnim($$0, $$16, $$15, $$14, $$8, $$11);
In the case of bees, the relevant value is $$14 (which I will call entityBob here), as it is the value called to set up the wings’ Z rotation. Said rotation is a float set to Mth.cos(entityBob * 120.32113f * ((float)Math.PI / 180)) * (float)Math.PI * 0.15f, as can be found in BeeModel#setupAnim(...). entityBob is LivingEntityRenderer#getBob(Entity, $$2), which returns (float)((LivingEntity)Entity).tickCount + $$2.
The problem is that Mth.cos() uses a float to int conversion:

```public static float cos(float $$0) {
        return SIN[(int)($$0 * 10430.378f + 16384.0f) & 0xFFFF];
    }```
And this results in an overflow when entityBob * 120.32113 * (pi / 180) * 10430.378 + 16384 > 2147483647, which is the int limit. This happens when entityBob exceeds approximately 98040.88, which happens around 82 minutes after the entity is spawned in.
The issue is the same for bats. The wings' Y rotation is set to Mth.cos(entityBob * 74.48451f * ((float)Math.PI / 180)) * (float)Math.PI * 0.25f in BatModel#setupAnim(...), which overflows when entityBob exceeds approximately 158373.73, which happens around 132 minutes after the entity is spawned in.
Edit: fixed some values, but they might still be off by around 100.

### Comment 4: muzikbike (2022-03-21T07:46:04.260-0700)

Relates to  and

### Comment 5: isXander (2022-04-02T12:06:24.049-0700)

Couldn't this be solved by using

```return SIN[(int)((($$0 * 10430.378f + 16384.0f) & 0xFFFF) % Integer.MAX_VALUE)]```
basically just wrapping the value back to zero if it reaches the limit

### Comment 6: ampolive (2022-04-02T12:39:02.342-0700)

Yes, I think that in theory that would work.

### Comment 7: isXander (2022-04-02T13:35:43.053-0700)

After testing further, it seems that float 32 loses loads of precision by then and would not be desirable. I will look further into solutions.

### Comment 8: ampolive (2022-04-04T03:22:54.807-0700)

Mth.sin() would also need to be fixed.

### Comment 9: isXander (2022-04-04T03:39:44.128-0700)

There are no instances where this would affect anything and would simply just be an extra division calculation

### Comment 10: ampolive (2022-04-04T03:45:15.404-0700)

It is used in the guardian renderer. But I suppose that it would become irrelevant if  were fixed.

### Comment 11: isXander (2022-09-24T04:38:50.401-0700)

After more testing, I came up with this...
In sin and cos methods, modulo by TAU (2PI)

```public static float cos(float value) {
   value %= TAU; // TAU = 2PI
   return SINE_TABLE[(int)(value * 10430.378F + 16384.0F) & 65535];
}

public static float sin(float value) {
   value %= TAU; // TAU = 2PI
   return SINE_TABLE[(int)(value * 10430.378F) & 65535];
}```

### Comment 12: migrated (2023-01-15T07:18:08.616-0800)

Can confirm in 1.19.3.

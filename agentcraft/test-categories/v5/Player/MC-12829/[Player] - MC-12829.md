# MC-12829: Flying through climbable blocks in creative mode slows you down

**Mojira URL:** [https://bugs.mojang.com/browse/MC-12829](https://bugs.mojang.com/browse/MC-12829)

## Report details

- **Mojira categories:** Player
- **Project:** MC
- **Issue key:** MC-12829
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2013-03-25T07:29:59.906-0700
- **Updated:** 2025-04-26T02:45:51.047-0700
- **Resolution date:** 2024-11-02T03:48:38.910-0700
- **Affects versions:** Minecraft 1.5.1; Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.7; Minecraft 15w46a; Minecraft 1.10.2; Minecraft 16w40a; Minecraft 16w41a; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 18w20c; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; 1.14.4; 19w45a; 1.15 Pre-release 1; 1.15.2; 20w16a; 20w17a; 20w18a; 20w22a; 1.16 Pre-release 2; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16.1; 20w27a; 20w28a; 1.16.2 Pre-release 1; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 20w46a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w08b; 21w11a; 21w15a; 21w17a; 1.17; 1.17.1; 21w43a; 1.18 Pre-release 1; 1.18; 1.18.1 Pre-release 1; 1.18.1; 1.18.2; 22w12a; 1.19; 1.19.2; 1.19.3; 1.19.4; 1.20; 1.20.1; 23w33a; 24w11a; 1.20.6; 1.21; 1.21.1; 24w36a; 1.21.2 Pre-Release 3
- **Fix versions:** 24w44a
- **Area:** Platform
- **Game mode:** Creative
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** MC-12829.mp4; MC-12829.png; MC-12829 - Current Code.png; MC-12829 - Fixed Code.png
- **Issue links:** Relates:outward:MC-165168:Flying creative players get pushed by mobs | Relates:inward:MC-194417:Doing certain actions while flying on creative mode slows the player down | Duplicate:inward:MC-225549:Creative ladder speed | Relates:outward:MC-5410:In creative mode, flying down is stopped when brushing up against ladders or vines. | Duplicate:inward:MC-192044:Flying through scaffhold in creative slows you down | Duplicate:inward:MC-182128:Vines are still slowing you down when flying throught them in creative mode. | Duplicate:inward:MC-179323:Feeling obstructed when flying through the weeping/twisting vines | Duplicate:inward:MC-74800:Flying through ladders slows you down

## Description

The Bug:
Flying through climbable blocks in creative mode slows you down.
Steps to Reproduce:
- Summon a wall of climbable blocks, for example, a wall of scaffolding by using the command provided below.

```
/fill ~2 ~ ~1 ~2 ~6 ~15 minecraft:scaffolding
```

- Switch into creative mode if not already and begin flying.

- Fly through the scaffolding and as you do this, pay close attention to the speed at which you travel through them.

- Take note as to whether or not flying through climbable blocks in creative mode slows you down.

Observed Behavior:
Flying through climbable blocks in creative mode slows you down.
Expected Behavior:
Flying through climbable blocks in creative mode would not slow you down.
Code Analysis:
Code analysis by  can be found below. An additional code analysis by  can be found in this comment.
The following is based on a decompiled version of Minecraft 1.19.2 using MCP-Reborn.
net.minecraft.world.entity.LivingEntity.java

```
public abstract class LivingEntity extends Entity {
   ...
   public boolean onClimbable() {
      if (this.isSpectator()) {
         return false;
      } else {
         BlockPos blockpos = this.blockPosition();
         BlockState blockstate = this.getFeetBlockState();
         if (blockstate.is(BlockTags.CLIMBABLE)) {
            this.lastClimbablePos = Optional.of(blockpos);
            return true;
         } else if (blockstate.getBlock() instanceof TrapDoorBlock && this.trapdoorUsableAsLadder(blockpos, blockstate)) {
            this.lastClimbablePos = Optional.of(blockpos);
            return true;
         } else {
            return false;
         }
      }
   }
   ...
```
If we look at the above class, we can see that there is only one check that is carried out before allowing a living entity to climb a climbable block. This check is to see if the living entity is in spectator mode, and if they are, they won't be able to climb climbable blocks, and if they're not, they will be able to climb climbable blocks. The game doesn't check if the living entity is currently flying before allowing them to climb climbable blocks, therefore resulting in this problem occurring.
Fix:
Simply adding an "if else" statement to the "if" statement to check if the living entity is a player and if they're flying before allowing them to climb climbable blocks will resolve this problem.
Current "if" statement:

```
if (this.isSpectator()) {
   return false;
} else {
...
```
Fixed "if" statement:

```
if (this.isSpectator()) {
   return false;
} else if (this instanceof Player player && player.getAbilities().flying) {
   return false;
} else {
...
```

## Comments (49)

### Comment 1: migrated (2013-03-25T07:29:59.906-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2013-03-25T11:45:27.073-0700)

I have a feeling that this might be related to how one can climb vines.
Are these jungle vines or swamp vines?

### Comment 3: migrated (2013-03-25T16:46:35.362-0700)

Duplicate of MC-5410, please use the search function to see if your bug has already been submitted. Currently over 55% of tickets are being closed as duplicate.

### Comment 4: migrated (2015-03-15T05:50:14.440-0700)

I'm not sure why this was reopened. This is clearly the same issue as MC-5410.

### Comment 5: migrated (2015-03-15T09:15:21.946-0700)

MC-5410 is about flying down on a ladder, which stops you. This issue is about flying up or sideways, which simply makes you go slower.

### Comment 6: migrated (2015-11-15T03:18:59.194-0800)

Confirmed for 15w46a

### Comment 7: FaRo1 (2016-10-15T09:04:02.321-0700)

Duplicate of MC-5410.

### Comment 8: migrated (2016-10-16T07:43:45.773-0700)

No, it's not. See the comments above.

### Comment 9: FaRo1 (2016-10-16T08:13:44.718-0700)

Ah, it's up. Sorry. Didn't ever see this, will test in a few minutes.

### Comment 10: migrated (2018-08-30T06:51:19.093-0700)

Confirmed for 1.13.1.

### Comment 11: muzikbike (2019-04-09T08:17:15.126-0700)

Affects 19w14b

### Comment 12: migrated (2019-11-07T14:43:35.913-0800)

Affects 19w45a

### Comment 13: migrated (2019-11-07T18:14:02.542-0800)

Relates to MC-90212

### Comment 14: FaRo1 (2019-11-07T23:36:51.188-0800)

I wouldn't say so. Those two behaviours are pretty much opposites. This one makes you do laddery stuff where you would not expect it and the other one makes you ignore the ladder where you would expect to be able to use it.

### Comment 15: migrated (2019-11-08T05:58:43.637-0800)

Okay, depends on how you look at it. Both of these bugs relates to unexpected behavior regarding flying of some sort and ladders/vines. My idea is just so Mojang easier can find somewhat similar bugs to fix.

### Comment 16: migrated (2019-11-22T07:05:48.618-0800)

Affects 1.15-pre1 and 1.14.4

### Comment 17: migrated (2020-05-31T07:16:34.507-0700)

Confirmed for 20w22b. Twisting vines slow you down in creative mode.

### Comment 18: migrated (2020-06-07T07:42:20.795-0700)

Confirmed in 1.16 Pre-release 2.

### Comment 19: migrated (2020-06-12T05:48:54.546-0700)

Confirmed in 1.16-pre4.

### Comment 20: migrated (2020-06-12T14:52:20.323-0700)

Confirmed in 1.16-pre5.

### Comment 21: migrated (2020-06-16T06:44:30.542-0700)

Confirmed in 1.16-pre6. I'd like to request ownership - I'll keep this ticket updated.

### Comment 22: [Mod]Les3awe (2020-06-16T08:19:13.605-0700)

Completed.

### Comment 23: anthony cicinelli (2020-07-04T06:59:59.871-0700)

Affects 20w27a

### Comment 24: Avoma (2020-12-20T04:17:14.013-0800)

Can confirm in 20w51a.

### Comment 25: Avoma (2021-01-28T06:17:55.908-0800)

Can confirm in 21w03a.

### Comment 26: Avoma (2021-02-05T12:15:20.570-0800)

Can confirm in 21w05b.

### Comment 27: Avoma (2021-02-12T05:14:46.281-0800)

Can confirm in 21w06a.

### Comment 28: Avoma (2021-02-18T11:06:32.189-0800)

Can confirm in 21w07a. Video attached.

### Comment 29: Avoma (2021-03-04T04:57:15.038-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 30: migrated (2021-03-22T21:41:40.704-0700)

Can confirm in 21w11a. Includes glow berry vines

### Comment 31: migrated (2021-04-09T07:47:24.303-0700)

Not just flying through them slows you down. Climable blocks slow you down in general when moving, not just when flying, which is annoying.

### Comment 32: Avoma (2021-04-19T01:58:13.895-0700)

Can confirm in 21w15a.

### Comment 33: Avoma (2021-04-30T06:15:22.727-0700)

Can confirm in 21w17a.

### Comment 34: Avoma (2021-06-16T12:02:56.526-0700)

Can confirm in 1.17.

### Comment 35: Avoma (2021-07-08T11:05:40.915-0700)

Can confirm in 1.17.1.

### Comment 36: SoloAlguien (2021-10-27T11:51:15.051-0700)

Can confirm in 21w43a.

### Comment 37: SoloAlguien (2021-11-11T11:47:36.793-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 38: SoloAlguien (2021-12-03T16:10:28.755-0800)

Can confirm in 1.18 and 1.18.1 Pre-release 1.

### Comment 39: SoloAlguien (2021-12-17T22:17:28.800-0800)

Can confirm in 1.18.1.

### Comment 40: Avoma (2022-01-16T08:48:13.041-0800)

I can also confirm this behavior in 1.18.1. Here's a code analysis of this issue along with a fix.
Code Analysis:
The following is based on a decompiled version of Minecraft 1.19.2 using MCP-Reborn.
net.minecraft.world.entity.LivingEntity.java

```public abstract class LivingEntity extends Entity {
   ...
   public boolean onClimbable() {
      if (this.isSpectator()) {
         return false;
      } else {
         BlockPos blockpos = this.blockPosition();
         BlockState blockstate = this.getFeetBlockState();
         if (blockstate.is(BlockTags.CLIMBABLE)) {
            this.lastClimbablePos = Optional.of(blockpos);
            return true;
         } else if (blockstate.getBlock() instanceof TrapDoorBlock && this.trapdoorUsableAsLadder(blockpos, blockstate)) {
            this.lastClimbablePos = Optional.of(blockpos);
            return true;
         } else {
            return false;
         }
      }
   }
   ...```
If we look at the above class, we can see that there is only one check that is carried out before allowing a living entity to climb a climbable block. This check is to see if the living entity is in spectator mode, and if they are, they won't be able to climb climbable blocks, and if they're not, they will be able to climb climbable blocks. The game doesn't check if the living entity is currently flying before allowing them to climb climbable blocks, therefore resulting in this problem occurring.
Fix:
Simply adding an "if else" statement to the "if" statement to check if the living entity is a player and if they're flying before allowing them to climb climbable blocks will resolve this problem.
Current "if" statement:

```if (this.isSpectator()) {
   return false;
} else {
...```
Fixed "if" statement:

```if (this.isSpectator()) {
   return false;
} else if (this instanceof Player player && player.getAbilities().flying) {
   return false;
} else {
...```

### Comment 41: SoloAlguien (2022-03-01T13:27:37.159-0800)

Can confirm in 1.18.2.

### Comment 42: migrated (2022-04-09T13:36:43.198-0700)

Code analysis based on 1.18.2 with yarn mappings.
The easiest way to fix this would be to make net.minecraft.entity.LivingEntity#isClimbing() (or this.onClimbable() in 's analysis) return false if the player is flying. In fact, this method already checks if the entity is in spectator mode. We just need to add a check if the entity is a player and they are flying.
To do this, override that method in net.minecraft.entity.player.PlayerEntity as follows:

```@Override
public boolean isClimbing() {
    if (this.abilities.flying) {
        return false;
    }
    return super.isClimbing();
}```

### Comment 43: Avoma (2022-06-08T06:50:14.603-0700)

Can confirm in 1.19.

### Comment 44: Avoma (2022-09-10T10:44:58.677-0700)

Can confirm in 1.19.2.

### Comment 45: Avoma (2022-10-09T07:05:04.962-0700)

Following on from mine and 's code analyses, I've double-checked our proposed fix and I can confidently confirm that it's fully functioning and works as expected, so I've attached two screenshots to this report, one of which shows the current code and the other that shows the fixed code. I feel this information may be quite insightful hence my reasoning for providing it.

### Comment 46: Avoma (2022-10-09T07:12:11.090-0700)

Also, if it isn't too much to ask, would it be okay if I could take ownership of this ticket since the current reporter has been inactive since June 2020 (over 2 years)?

### Comment 47: Gullyman4 (2024-10-30T07:44:26.021-0700)

This is not fixed in 24w44a. Please reopen. I still able to reproduce this.

### Comment 48: Avoma (2024-10-31T00:26:44.843-0700)

In my testing, the issue appears to be fixed correctly. Could you please clarify exactly what is not fixed?

### Comment 49: Gullyman4 (2024-11-02T03:48:38.910-0700)

The issue be not fixed. Scaffolding slows me down for no reason. Actually is slow down any #climbable. Ladder, vine, scaffolding. Even air if I datapack add air climbing.

# MC-44280: Entities don't receive knockback from projectiles fired from dispensers

**Mojira URL:** [https://bugs.mojang.com/browse/MC-44280](https://bugs.mojang.com/browse/MC-44280)

## Report details

- **Mojira categories:** Entities; Projectiles
- **Project:** MC
- **Issue key:** MC-44280
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2014-01-07T13:52:06.427-0800
- **Updated:** 2025-04-29T09:42:30.230-0700
- **Resolution date:** 2024-05-02T04:29:45.350-0700
- **Affects versions:** Minecraft 1.7.4; Minecraft 1.7.9; Minecraft 1.8; Minecraft 1.8.3; Minecraft 15w47c; Minecraft 1.9 Pre-Release 2; Minecraft 1.9.2; Minecraft 1.9.3 Pre-Release 1; Minecraft 1.9.3 Pre-Release 2; Minecraft 1.9.4; Minecraft 16w20a; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w43a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w15a; Minecraft 1.12.2; Minecraft 17w45b; Minecraft 17w46a; Minecraft 17w47a; Minecraft 17w47b; Minecraft 18w02a; Minecraft 18w11a; Minecraft 18w16a; Minecraft 18w20c; Minecraft 18w21a; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 1.14 Pre-Release 5; 1.14.4; 19w36a; 19w37a; 20w06a; 1.16.2; 1.16.3; 1.16.4 Pre-release 2; 1.16.4; 20w46a; 20w51a; 21w05b; 21w06a; 21w07a; 21w11a; 21w14a; 21w17a; 1.17; 1.17.1; 21w39a; 1.18.1; 1.18.2; 22w17a; 1.19; 1.19.2; 1.19.3 Release Candidate 3; 1.19.3; 1.20; 1.20.1; 1.20.2; 1.20.4
- **Fix versions:** Minecraft 16w02a; 24w18a
- **Area:** Gameplay
- **Labels:** dispenser; egg; knockback; snowball
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2019-09-12_11.24.30.png; MC-44280.mp4; MC-44280.png; setup.png
- **Issue links:** Relates:inward:MC-78473:Mobs don't panic when hit with a summoned or dispensed potion of harming | Duplicate:inward:MC-124119:Mobs Dispenser Knockback | Duplicate:inward:MC-164573:Chickens don't take knockback with eggs. | Duplicate:inward:MC-202767:Snowball fired from Dispenser dont causes players to knock | Relates:outward:MC-125936:When projectiles spawn inside a hitbox, they don't hit the hitbox of the entity they are inside | Relates:inward:MC-94978:Throwable items fired from dispenser do not hit mobs for the first two ticks | Relates:inward:MC-3179:Snowballs, Enderpearls and Eggs do not knockback players in multiplayer

## Description

Fireworks, eggs, snowballs, and splash potions of harming fired from dispensers don't knock back mobs, but they do when thrown by the player or a mob such as a snow golem or witch.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Place some snowballs inside of the dispenser.

- Summon a husk on the diamond block.

- Use the lever to activate the dispenser and watch the husk closely.

Observed Behavior:
Projectiles fired from dispensers don't deal any knockback to entities.
Expected Behavior:
Projectiles fired from dispensers would deal knockback to entities.
Note
Arrows are not affected by this bug, as they knock back mobs when fired either from a bow or a dispenser.
Code analysis
Code analysis by  can be found in this comment.

## Comments (44)

### Comment 1: migrated (2014-01-07T13:52:06.427-0800)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2014-01-17T09:47:50.334-0800)

Here's a proof video : http://www.youtube.com/watch?v=mkR7gTR30xg

### Comment 3: Sonicwave (2014-09-20T20:40:02.087-0700)

Confirmed in 1.8. Also affects Splash Potions of Harming.

### Comment 4: migrated (2016-02-22T09:10:57.483-0800)

confirmed for 1.9 pre2. snowballs fly through mobs now. It's worse than before.

### Comment 5: marcono1234 (2016-03-07T08:50:02.678-0800)

Please link to this comment in the description
The following is based on decompiled version of Minecraft 1.9 using MCP 9.24 beta. All method and class names are the names used in the decompiled version.
The reason why for this bug is that the net.minecraft.entity.EntityLivingBase.attackEntityFrom(DamageSource, float) method only knockbacks mobs if the indirect damage has an entity as owner. This is not the case for projectiles fired from a dispenser. The problem is that currently the coordinates of the thrower are used to determine the knockback.
This allows "exploits" like [[Tutorial] Guided & Regular Rocket Launcher in Vanilla Minecraft Using Fireballs! [MC 1.8]|https://www.youtube.com/watch?v=548wxRDL1U8].
A possible solution would be to use the motion of the projectile. This means however that the distance does not determine the strength completely anymore.
The following shows how this could be done, but the motion values very likely need to be adjusted.

```// Added this
if (source instanceof net.minecraft.util.EntityDamageSourceIndirect && source.getSourceOfDamage() != null) {
    Entity damagingEntity = source.getSourceOfDamage();
    double d1 = -damagingEntity.motionX;
    double d0;

    for (d0 = -damagingEntity.motionZ; d1 * d1 + d0 * d0 < 1.0E-4D; d0 = (Math.random() - Math.random()) * 0.01D)
    {
        d1 = (Math.random() - Math.random()) * 0.01D;
    }

    this.attackedAtYaw = (float)(MathHelper.atan2(d0, d1) * (180D / Math.PI) - (double)this.rotationYaw);
    this.knockBack(entity, 0.4F, d1, d0);

}
// Replaced this
//if (entity != null)
else if (entity != null)
{
    double d1 = entity.posX - this.posX;
    double d0;

    for (d0 = entity.posZ - this.posZ; d1 * d1 + d0 * d0 < 1.0E-4D; d0 = (Math.random() - Math.random()) * 0.01D)
    {
        d1 = (Math.random() - Math.random()) * 0.01D;
    }

    this.attackedAtYaw = (float)(MathHelper.atan2(d0, d1) * (180D / Math.PI) - (double)this.rotationYaw);
    this.knockBack(entity, 0.4F, d1, d0);
}
else
{
    this.attackedAtYaw = (float)((int)(Math.random() * 2.0D) * 180);
}```

### Comment 6: migrated (2016-05-02T04:31:40.588-0700)

Still present in 1.9.3-pre2.

### Comment 7: migrated (2016-05-23T12:50:11.509-0700)

Still present in 16w20a

### Comment 8: marcono1234 (2016-08-10T08:53:56.407-0700)

Confirmed for
- 16w32a

### Comment 9: migrated (2016-11-05T04:43:45.806-0700)

@Marcono1234
If knockback requires an entity as the damage source, why do arrows fired from dispensers work as expected?
Can we copy the knockback strength and direction from the arrows code, or is that too tied up with damage > 0 hearts or something?

### Comment 10: Skylinerw (2016-11-05T05:09:53.783-0700)

@ Arrows will set themselves as the attacker if no "owner" is present:

```if (this.shootingEntity == null)
{
    damagesource = DamageSource.causeArrowDamage(this, this);
}
else
{
    damagesource = DamageSource.causeArrowDamage(this, this.shootingEntity);
}```
Theoretically the same could be done with the eggs and snowballs (example below is from eggs, with the commented code being an addition, though I have not actually tried this myself):

```if (result.entityHit != null)
{
    //if (this.getThrower() == null)
    //{
        result.entityHit.attackEntityFrom(DamageSource.causeThrownDamage(this, this), 0.0F);
    //}
    //else
    //{
    //    result.entityHit.attackEntityFrom(DamageSource.causeThrownDamage(this, this.getThrower()), 0.0F);
    //}
}```

### Comment 11: JUE13 (2017-04-13T19:32:07.913-0700)

Confirmed for 17w15a

### Comment 12: Sonicwave (2017-11-23T23:07:08.960-0800)

Confirmed for 1.12.2 and 17w47b.

### Comment 13: migrated (2018-08-31T14:12:47.035-0700)

Confirmed for 1.13.1. Please, if you don't mind, I'd like to be the reporter of this ticket, I'll update it accordingly.

### Comment 14: migrated (2018-09-02T01:00:58.259-0700)

Actually, I am still around, and I do wish to be acknowledged as the discoverer of the bug.
@Kraif What changes did you feel need to be made?
@Torabi You've been changing the reporter to Kraif on quite a few bugs recently. Maybe he should be made a mod instead?

### Comment 15: migrated (2018-09-02T03:12:09.616-0700)

: I asked to be the reporter because your ticket was outdated. I'll update it accordingly. BTW: Everyone can see that you are the original reporter of this ticket by clicking "History" or "Activity", so don't worry!

### Comment 16: Torabi (2018-09-02T04:07:33.055-0700)

You haven't updated the issue for the past three years, and your last activity on the tracker was in december, nine months ago. The fact that you created the issue is still listed in the issue history, and the reporter field just allows regular users to update the issue directly, rather than leaving a comment for someone else to take care of it. Unfortunately, the JIRA software the tracker runs on does not allow for multiple users to have edit permissions on a single issue, without having those permissions across entire projects, like our helpers and mods do.
We have an internal selection process for bringing on new helpers and mods, and consider not only how active a user is, but the quality and tone of their interactions with the tracker and other users. We like to watch a user over a period of time, to see how well they understand the tracker and the community, before we consider offering them additional roles.

### Comment 17: migrated (2018-12-02T17:55:04.085-0800)

Confirmed for version 1.13.2

### Comment 18: migrated (2019-09-09T08:39:56.619-0700)

Confirmed for version 1.14.4

### Comment 19: migrated (2019-09-09T08:42:51.526-0700)

Still present in 19w36a

### Comment 20: migrated (2019-09-12T03:28:24.396-0700)

Still present in 19w37a.
Also attached screenshot of my test setup.

### Comment 21: migrated (2020-06-11T17:14:01.157-0700)

Still exists in 1.16 Pre-release 4, I would also like to add that splash potions are not listed above as one of the projectiles that fail to inflict knockback but I found out that they don't inflict knockback either.

### Comment 22: migrated (2020-06-25T14:35:52.976-0700)

Still present in 1.16.1, including splash potions as noted by @Dobbi

### Comment 23: migrated (2020-09-24T11:42:31.362-0700)

Still present in 1.16.3
Would it be possible to change me back to the reporter of this bug, so I can keep the affected versions up to date and add info regarding splash potions?

### Comment 24: migrated (2020-09-30T15:47:46.217-0700)

can u add 1.16.3 i also checked

### Comment 25: migrated (2021-01-27T14:51:17.946-0800)

Probably related to .

### Comment 26: Avoma (2021-02-06T05:40:38.081-0800)

Can confirm in 21w05b.

### Comment 27: Avoma (2021-02-12T05:50:24.569-0800)

Can confirm in 21w06a.

### Comment 28: Avoma (2021-02-19T03:09:08.807-0800)

Can confirm in 21w07a.

### Comment 29: Avoma (2021-02-20T08:42:43.541-0800)

Video attached.

### Comment 30: Avoma (2021-03-29T05:41:52.435-0700)

Can confirm in 21w11a.

### Comment 31: Avoma (2021-04-11T03:49:53.867-0700)

Can confirm in 21w14a.

### Comment 32: Avoma (2021-05-01T07:48:18.027-0700)

Can confirm in 21w17a.

### Comment 33: migrated (2021-05-15T01:46:22.188-0700)

Possibly same root cause as MC-225541

### Comment 34: Avoma (2021-06-17T04:43:10.881-0700)

Can confirm in 1.17.

### Comment 35: Avoma (2021-07-13T04:20:29.060-0700)

Can confirm in 1.17.1.

### Comment 36: Avoma (2021-09-27T10:40:21.838-0700)

This ticket relates to .

### Comment 37: Avoma (2021-10-06T04:06:42.630-0700)

Can confirm this behavior in 21w39a. Here are some extra details regarding this problem.
The Bug:
Projectiles fired from dispensers don't deal any knockback to entities.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Place some snowballs inside of the dispenser.

- Summon a husk on the diamond block.

- Use the lever to activate the dispenser and watch the husk closely.

Observed Behavior:
Projectiles fired from dispensers don't deal any knockback to entities.
Expected Behavior:
Projectiles fired from dispensers would deal knockback to entities.

### Comment 38: Avoma (2022-01-01T06:28:42.848-0800)

Can confirm in 1.18.1.

### Comment 39: Avoma (2022-03-12T07:33:13.367-0800)

Can confirm in 1.18.2.

### Comment 40: Avoma (2022-04-30T10:44:00.487-0700)

Can confirm in 22w17a.

### Comment 41: Avoma (2022-06-13T05:16:29.420-0700)

Can confirm in 1.19.

### Comment 42: Avoma (2022-08-17T09:03:20.544-0700)

Can confirm in 1.19.2.

### Comment 43: migrated (2022-12-06T08:42:21.642-0800)

Can Confirm 1.19.3 Release Candidate 3

### Comment 44: Avoma (2022-12-06T08:56:33.525-0800)

, 1.19.3 Release Candidate 3 is already marked as affected.

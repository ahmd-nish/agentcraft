# MC-225365: Pointed dripstone can be destroyed by tridents in adventure mode

**Mojira URL:** [https://bugs.mojang.com/browse/MC-225365](https://bugs.mojang.com/browse/MC-225365)

## Report details

- **Mojira categories:** Player; Projectiles
- **Project:** MC
- **Issue key:** MC-225365
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-05-12T07:55:25.464-0700
- **Updated:** 2026-06-15T06:07:57.311-0700
- **Resolution date:** 2023-12-11T02:49:48.994-0800
- **Affects versions:** 21w19a; 1.17 Release Candidate 1; 1.17; 1.17.1; 1.18.1; 1.18.2; 1.19; 1.19.1; 1.19.2; 1.19.3; 23w06a; 1.20.1; 23w33a; 23w41a
- **Fix versions:** 23w42a
- **Game mode:** Adventure
- **Labels:** pointed_dripstone; trident
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2021-05-15_18.43.38.png; MC-225365.mp4
- **Issue links:** Relates:outward:MC-265758:Decorated pots can be destroyed by projectiles in adventure mode | Duplicate:inward:MC-227612:trident's break dripstone in adventure mode, inconvenient for map makers. | Duplicate:inward:MC-229696:Pointed Dripstone Adventure Mode Oversight | Relates:inward:MCPE-175950:Pointed dripstone can be destroyed by a trident in adventure mode | Relates:outward:MC-308789:Pointed dripstone and sulfur spikes can be destroyed by tridents in Adventure mode

## Description

The Bug:
Pointed dripstone can be destroyed by tridents in adventure mode.
Steps to Reproduce:
- Place down some pointed dripstone and obtain a trident.

- Switch to adventure mode and shoot the trident at the pointed dripstone.

- Take note as to whether or not pointed dripstone can be destroyed by tridents in adventure mode.

Observed Behavior:
Pointed dripstone can be destroyed.
Expected Behavior:
Pointed dripstone would not be able to be destroyed.
Code Analysis:
Code analysis by  can be found in this comment.

## Comments (13)

### Comment 1: migrated (2021-05-12T07:55:25.464-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Avoma (2021-05-12T08:56:08.551-0700)

Can confirm.

### Comment 3: Avoma (2021-06-09T05:23:43.489-0700)

Can confirm in 1.17.

### Comment 4: Avoma (2021-07-06T10:27:15.727-0700)

Can confirm in 1.17.1.

### Comment 5: Avoma (2021-12-23T04:11:52.114-0800)

Can confirm in 1.18.1.

### Comment 6: Avoma (2022-01-16T04:53:39.985-0800)

Here's a code analysis along with a potential fix regarding this issue.
Code Analysis:
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.world.level.block.PointedDripstoneBlock.java

```public class PointedDripstoneBlock extends Block implements Fallable, SimpleWaterloggedBlock {
   ...
   public void onProjectileHit(Level $l, BlockState $bs, BlockHitResult $bhr, Projectile $p) {
      BlockPos blockpos = $bhr.getBlockPos();
      if (!$l.isClientSide && $p.mayInteract($l, blockpos) && $p instanceof ThrownTrident && $p.getDeltaMovement().length() > 0.6D) {
         $l.destroyBlock(blockpos, true);
      }

   }
   ...```
If we look at the above class, we can see that no checks are carried out to see what abilities the player possesses when using a thrown trident to destroy pointed dripstone. The only checks that are in place are as follows:
- Was the action non-client-side?

- Can the pointed dripstone be interacted with? (Is the pointed dripstone outside of spawn protection and within the world border?)

- Does the trident have enough velocity to destroy the pointed dripstone?

These checks are evident through the following line of code:

```if (!$l.isClientSide && $p.mayInteract($l, blockpos) && $p instanceof ThrownTrident && $p.getDeltaMovement().length() > 0.6D)```

```!$p.getAbilities().mayBuild```

### Comment 7: Avoma (2022-01-16T05:39:03.425-0800)

This ticket relates to .

### Comment 8: Avoma (2022-03-09T06:43:50.908-0800)

Can confirm in 1.18.2.

### Comment 9: isXander (2022-04-18T07:40:07.060-0700)

Avoma your potential fix is incorrect. $p is referring to the projectile, which doesn't have getAbilities() you would need to first check if the trident had an owner, then check if that owner is a Player and then get the abilities.

### Comment 10: Avoma (2022-04-18T07:47:26.678-0700)

Hmm, yes, you're right, my bad. I've removed the potential fix but have kept the code analysis. Thanks

### Comment 11: Avoma (2022-06-08T03:00:35.596-0700)

Can confirm in 1.19.

### Comment 12: Avoma (2022-08-02T09:16:29.893-0700)

Can confirm in 1.19.1.

### Comment 13: Avoma (2022-09-01T05:06:00.758-0700)

Can confirm in 1.19.2.

# MC-225364: Chorus flowers can be destroyed by projectiles in adventure mode

**Mojira URL:** [https://bugs.mojang.com/browse/MC-225364](https://bugs.mojang.com/browse/MC-225364)

## Report details

- **Mojira categories:** Player; Projectiles
- **Project:** MC
- **Issue key:** MC-225364
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-05-12T07:51:37.394-0700
- **Updated:** 2025-04-29T11:25:21.112-0700
- **Resolution date:** 2023-12-11T02:50:01.594-0800
- **Affects versions:** 1.16.5; 21w19a; 1.17; 1.17.1; 21w37a; 1.18.1; 1.18.2; 1.19; 1.19.1; 1.19.3; 23w03a; 1.19.4; 23w18a; 23w41a
- **Fix versions:** 23w42a
- **Area:** Gameplay
- **Game mode:** Adventure
- **Labels:** chorus_flower
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2021-05-15_18.44.00.png; MC-225364.mp4
- **Issue links:** Relates:outward:MC-265758:Decorated pots can be destroyed by projectiles in adventure mode | Relates:inward:MC-176161:Striders unaffected by speed while riding | Relates:inward:MCPE-176161:Chorus flowers can be destroyed by projectiles in adventure mode

## Description

The Bug:
Chorus flowers can be destroyed by projectiles in adventure mode.
Steps to Reproduce:
- Place down a chorus flower and obtain a bow and some arrows.

- Switch to adventure mode and shoot the arrow at the chorus flower.

- Take note as to whether or not chorus flowers can be destroyed by projectiles in adventure mode.

Observed Behavior:
Chorus flowers can be destroyed.
Expected Behavior:
Chorus flowers would not be able to be destroyed.
Code Analysis:
Code analysis by  can be found in this comment.

## Comments (11)

### Comment 1: migrated (2021-05-12T07:51:37.394-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Avoma (2021-05-12T09:37:48.926-0700)

Can confirm.

### Comment 3: Avoma (2021-06-09T05:23:49.509-0700)

Can confirm in 1.17.

### Comment 4: Avoma (2021-07-06T10:27:09.957-0700)

Can confirm in 1.17.1.

### Comment 5: Avoma (2021-09-22T04:08:45.032-0700)

Can also confirm in 21w37a. This ticket relates to MC-225365 and MC-223322. Here are some additional details regarding this issue.
The Bug:
Chorus flowers can be broken with projectiles in adventure mode.
Steps to Reproduce:
- Place down a chorus flower and obtain a projectile.

- Switch into adventure mode and shoot the projectile at the chorus flower.

- →  Notice how chorus flowers can be broken with projectiles in adventure mode.

Expected Behavior:
The expected behavior would be that chorus flowers cannot be broken with projectiles in adventure mode.

### Comment 6: Avoma (2022-01-16T05:47:45.407-0800)

I can confirm this behavior in 1.18.1.
Here's a code analysis along with a potential fix regarding this issue.
Code Analysis:
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.world.level.block.ChorusFlowerBlock.java

```public class ChorusFlowerBlock extends Block {
   ...
   public void onProjectileHit(Level $l, BlockState $bs, BlockHitResult $bhr, Projectile $p) {
      BlockPos blockpos = $bhr.getBlockPos();
      if (!$l.isClientSide && $p.mayInteract($l, blockpos) && $p.getType().is(EntityTypeTags.IMPACT_PROJECTILES)) {
         $l.destroyBlock(blockpos, true, $p);
      }

   }
   ...```
If we look at the above class, we can see that no checks are carried out to see what abilities the player possesses when using projectiles to destroy chorus flowers. The only checks that are in place are as follows:
- Was the action non-client-side?

- Can the chorus flower be interacted with? (Is the chorus flower outside of spawn protection and within the world border?)

- Is the projectile a part of the IMPACT_PROJECTILES entity tag?

These checks are evident through the following line of code:

```if (!$l.isClientSide && $p.mayInteract($l, blockpos) && $p.getType().is(EntityTypeTags.IMPACT_PROJECTILES))```
Potential Fix:
Simply adding a line of code that checks what abilities the player possesses before a projectile can destroy a chorus flower, should resolve this problem. The following line of code could be used in order to fix this:

```!$p.getAbilities().mayBuild```

### Comment 7: Avoma (2022-03-09T06:43:44.202-0800)

Can confirm in 1.18.2.

### Comment 8: Avoma (2022-06-08T03:00:41.369-0700)

Can confirm in 1.19.

### Comment 9: Avoma (2022-08-02T09:16:23.425-0700)

Can confirm in 1.19.1.

### Comment 10: Brain81505 (2023-01-14T06:22:11.684-0800)

Can confirm in 1.19.3

### Comment 11: Brain81505 (2023-01-18T08:05:40.217-0800)

Can confirm in 23w03a

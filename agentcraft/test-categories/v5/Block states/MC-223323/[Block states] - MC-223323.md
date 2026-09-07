# MC-223323: You can trample farmland in spawn protection

**Mojira URL:** [https://bugs.mojang.com/browse/MC-223323](https://bugs.mojang.com/browse/MC-223323)

## Report details

- **Mojira categories:** Block states; Player
- **Project:** MC
- **Issue key:** MC-223323
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-04-15T11:48:30.251-0700
- **Updated:** 2026-06-16T09:16:50.124-0700
- **Resolution date:** 2026-06-16T09:16:50.087-0700
- **Affects versions:** 1.16.5; 21w15a; 21w16a; 21w18a; 21w19a; 21w20a; 1.17; 1.17.1; 1.18.1; 1.18.2 Pre-release 1; 1.18.2; 1.19; 1.19.2; 1.19.3; 1.19.4; 1.20.1; 1.21; 1.21.4; 25w34b
- **Fix versions:** Future Update
- **Area:** Platform
- **Labels:** farmland; spawn-protection
- **Watchers:** 3
- **Attachments:** 4
- **Attachment filenames:** 2021-05-11_09.58.46.png; 2021-05-11_09.58.49.png; MC-223323.mp4; MC-223323.png
- **Issue links:** Relates:inward:MC-138963:You can trample farmland in adventure mode | Duplicate:inward:MC-300585:Farmland Can Be Tread In spawn-protection Radius

## Description

The Bug:
Players without operator permissions cannot normally interact with or destroy blocks inside spawn protection, however, you are able to trample farmland, regardless of whether or not it's inside of spawn protection.
Steps to Reproduce:
- Start a server, join it, give operator permissions to yourself, and switch into creative mode.

- Set the world spawn to your current location and summon some water and farmland nearby by using the commands provided below.

```
/setworldspawn ~ ~ ~
```

```
/setblock ~1 ~-1 ~-2 minecraft:water
```

```
/setblock ~ ~-1 ~-2 minecraft:farmland
```

- Switch into survival mode, remove your operator permissions, and grant anyone else with them in order to activate spawn protection.

- Attempt to trample the farmland by jumping on it.

- Take note as to whether or not you can trample farmland in spawn protection.

Observed Behavior:
Farmland is trampled.
Expected Behavior:
Farmland would not be trampled.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.world.level.block.FarmBlock.java

```
public class FarmBlock extends Block {
   ...
   public void fallOn(Level $l, BlockState $bs, BlockPos $bp, Entity $e, float $f) {
      if (!$l.isClientSide && $l.random.nextFloat() < $f - 0.5F && $e instanceof LivingEntity && ($e instanceof Player || $l.getGameRules().getBoolean(GameRules.RULE_MOBGRIEFING)) && $e.getBbWidth() * $e.getBbWidth() * $e.getBbHeight() > 0.512F) {
         turnToDirt($bs, $l, $bp);
      }

      super.fallOn($l, $bs, $bp, $e, $f);
   }
   ...
```
If we look at the above class, we can see that no checks are carried out to see whether or not the farmland block is within spawn protection, before allowing it to be trampled. The mayInteract() method (a method used for determining whether a block is inside of spawn protection and is within the world border) is never called within this piece of code, thus resulting in the problem of being able to trample farmland in spawn protection.
Potential Fix:
Simply adding some lines of code that check if the farmland block is within spawn protection before allowing it to be trampled, should resolve this problem. This can be achieved by calling the mayInteract() method and adding it appropriately somewhere within the existing "if" statement. The following line of code could be used in order to fix this:

```
$e.mayInteract($l, $bp)
```
The fixed and correct piece of code within its class should look something like the following:
net.minecraft.world.level.block.FarmBlock.java

```
public class FarmBlock extends Block {
   ...
   public void fallOn(Level $l, BlockState $bs, BlockPos $bp, Entity $e, float $f) {
      if (!$l.isClientSide && $l.random.nextFloat() < $f - 0.5F && $e instanceof LivingEntity && ($e instanceof Player || $l.getGameRules().getBoolean(GameRules.RULE_MOBGRIEFING)) && $e.mayInteract($l, $bp) && $e.getBbWidth() * $e.getBbWidth() * $e.getBbHeight() > 0.512F) {
         turnToDirt($bs, $l, $bp);
      }

      super.fallOn($l, $bs, $bp, $e, $f);
   }
   ...
```

## Comments (5)

### Comment 1: migrated (2021-04-15T11:48:30.251-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Avoma (2021-04-16T12:04:57.888-0700)

Relates to .

### Comment 3: migrated (2021-04-17T10:24:20.857-0700)

Can confirm as of 21w15a.

### Comment 4: [MOD] Greymagic27 (2025-08-13T09:40:03.134-0700)

Is this still an issue now spawnchunks have been reworked?

### Comment 5: Avoma (2025-08-22T11:48:23.876-0700)

This is still an issue in 25w34b.

# MC-223321: You can destroy turtle eggs by standing or jumping on them in spawn protection

**Mojira URL:** [https://bugs.mojang.com/browse/MC-223321](https://bugs.mojang.com/browse/MC-223321)

## Report details

- **Mojira categories:** Block states; Player
- **Project:** MC
- **Issue key:** MC-223321
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-04-15T11:48:25.965-0700
- **Updated:** 2026-06-16T09:16:48.476-0700
- **Resolution date:** 2026-06-16T09:16:48.407-0700
- **Affects versions:** 1.16.5; 21w15a; 21w16a; 21w18a; 21w19a; 21w20a; 1.17.1; 1.18.1; 1.18.2 Pre-release 1; 1.18.2; 1.19; 1.19.2; 1.19.3; 1.19.4; 1.20.1; 1.21; 1.21.4
- **Fix versions:** Future Update
- **Area:** Platform
- **Labels:** spawn-protection; turtle_egg
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2021-04-15_18.54.06.png; 2021-05-11_10.00.20.png; MC-223321.mp4

## Description

The Bug:
Players without operator permissions cannot normally interact with or destroy blocks inside spawn protection, however, you are able to destroy turtle eggs by standing or jumping on them, regardless of whether or not they're inside of spawn protection.
Steps to Reproduce:
- Start a server, join it, give operator permissions to yourself, and switch into creative mode.

- Set the world spawn to your current location and summon some turtle eggs nearby by using the commands provided below.

```
/setworldspawn ~ ~ ~
```

```
/setblock ~ ~ ~-2 minecraft:turtle_egg[eggs=4]
```

- Switch into survival mode, remove your operator permissions, and grant anyone else with them in order to activate spawn protection.

- Attempt to destroy the turtle eggs by standing or jumping on them.

- Take note as to whether or not you can destroy turtle eggs by standing or jumping on them in spawn protection.

Observed Behavior:
Turtle eggs are destroyed.
Expected Behavior:
Turtle eggs would not be destroyed.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.world.level.block.TurtleEggBlock.java

```
public class TurtleEggBlock extends Block {
   ...
   private boolean canDestroyEgg(Level $l, Entity $e) {
      if (!($e instanceof Turtle) && !($e instanceof Bat)) {
         if (!($e instanceof LivingEntity)) {
            return false;
         } else {
            return $e instanceof Player || $l.getGameRules().getBoolean(GameRules.RULE_MOBGRIEFING);
         }
      } else {
         return false;
      }
   }
   ...
```
If we look at the above class, we can see that no checks are carried out to see whether or not the turtle egg block is within spawn protection, before allowing it to be trampled. The mayInteract() method (a method used for determining whether a block is inside of spawn protection and is within the world border) is never called within this piece of code, thus resulting in the problem of being able to trample turtle eggs in spawn protection.
Potential Fix:
Simply adding some lines of code that check if the turtle egg block is within spawn protection before allowing it to be trampled, should resolve this problem. This can be achieved by calling the mayInteract() method and adding it appropriately somewhere within the existing "if" statement. The following line of code could be used in order to fix this:

```
$ENTITY.mayInteract($LEVEL, $BLOCKPOS)
```

## Comments (3)

### Comment 1: migrated (2021-04-15T11:48:25.965-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Avoma (2021-04-16T12:01:39.330-0700)

Relates to .

### Comment 3: migrated (2021-04-17T05:09:27.598-0700)

I was able to reproduce in 1.16.5 and 21w15a

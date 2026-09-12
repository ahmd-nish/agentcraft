# MC-182820: Repeaters and comparators use wood sounds for placing/breaking despite being made mostly of stone

**Mojira URL:** [https://bugs.mojang.com/browse/MC-182820](https://bugs.mojang.com/browse/MC-182820)

## Report details

- **Mojira categories:** Sound
- **Project:** MC
- **Issue key:** MC-182820
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-05-06T14:33:04.358-0700
- **Updated:** 2025-04-29T12:15:32.012-0700
- **Resolution date:** 2023-09-22T09:48:54.602-0700
- **Affects versions:** Minecraft 16w44a; 1.15.2; 20w19a; 20w21a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 7; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.4; 20w46a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w11a; 21w15a; 21w18a; 21w20a; 1.17 Pre-release 1; 1.17; 1.17.1; 21w42a; 1.18 Pre-release 8; 1.18; 1.18.2; 22w13a; 1.19.2; 1.19.3; 23w05a; 23w06a; 1.19.4; 23w16a; 1.20 Pre-release 6
- **Fix versions:** 23w33a
- **Area:** Gameplay
- **Labels:** incorrect-block-sound
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2020-05-06_22.32.39.png; 2020-05-06_22.32.40.png; 2020-05-06_22.32.41.png; 2020-05-06_22.32.42.png
- **Issue links:** Relates:outward:MC-200484:Jukeboxes use stone sounds despite being composed predominantly of wood | Duplicate:inward:MC-109755:Jumping on Repeaters and Comparators Gives a Wooden Sound | Duplicate:inward:MC-242781:Repeaters and comparators use wood block sound despite being made of stone | Duplicate:inward:MC-262973:Redstone Comparator and Repeater use Wood Sound Set instead of Stone Sound Set, in addition to missing walking sounds.

## Description

The Bug
Since they are predominantly composed of stone, should they not use the stone sound instead? I'm aware that this has been reported before, and that the ticket it supposedly duplicated was resolved as invalid, but all sound issues being confusingly bundled into the one ticket is not a standard we should currently hold ourselves to, and each sound issue should be given a fair trial by itself.
Steps to Reproduce
-     Obtain some repeaters and comparators.

-     Place them down, break them, and as you do this, pay close attention to the sounds they produce.

-     Take note as to whether or not repeaters and comparators produce wood sounds despite mostly being constructed of stone.

Observed Behavior
Repeaters and comparators produce wood sounds despite mostly being constructed of stone.
Expected Behavior
Repeaters and comparators would produce stone sounds as they're mostly constructed of this material.

## Comments (15)

### Comment 1: migrated (2020-05-06T14:33:04.358-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Avoma (2021-01-15T08:00:49.739-0800)

Can confirm in 20w51a.

### Comment 3: Avoma (2021-02-05T07:04:07.586-0800)

Can confirm in 21w05b.

### Comment 4: Avoma (2021-02-13T08:40:00.435-0800)

Can confirm in 21w06a.

### Comment 5: migrated (2021-03-19T14:32:12.178-0700)

Affects 21w11a.

### Comment 6: Avoma (2021-04-18T08:09:31.707-0700)

Can confirm in 21w15a.

### Comment 7: Avoma (2021-06-28T02:48:46.772-0700)

Can confirm in 1.17.

### Comment 8: ampolive (2021-07-23T16:44:14.384-0700)

Can confirm in 1.17.1.

### Comment 9: Avoma (2021-10-25T01:14:33.385-0700)

Can confirm this behavior in 21w42a. Here are some extra details regarding this problem.
The Bug:
Repeaters and comparators produce wood sounds despite mostly being constructed of stone.
Steps to Reproduce:
- Obtain some repeaters and comparators.

- Place them down, break them, and as you do this, pay close attention to the sounds they produce.

- Take note as to whether or not repeaters and comparators produce wood sounds despite mostly being constructed of stone.

Observed Behavior:
Repeaters and comparators produce wood sounds despite mostly being constructed of stone.
Expected Behavior:
Repeaters and comparators would produce stone sounds as they're mostly constructed of this material.

### Comment 10: Avoma (2021-11-28T03:17:51.372-0800)

I can confirm this behavior in 1.18 Release Candidate 3.
Here's a code analysis along with a potential fix regarding this issue. The following is based on a decompiled version of Minecraft 1.17.1 using MCP-Reborn.
Code Analysis:
net.minecraft.world.level.block.Blocks.java

```public class Blocks {
   ...
   public static final Block REPEATER = register("repeater", new RepeaterBlock(BlockBehaviour.Properties.of(Material.DECORATION).instabreak().sound(SoundType.WOOD)));
   ...
   public static final Block COMPARATOR = register("comparator", new ComparatorBlock(BlockBehaviour.Properties.of(Material.DECORATION).instabreak().sound(SoundType.WOOD)));
   ...```
If we look at the above class, we can see that repeaters and comparators utilize the .sound(SoundType.WOOD) method which is used for determining whether a block should produce wood sounds.
Potential Fix:
Simply replacing the .sound(SoundType.WOOD) method with .sound(SoundType.STONE) within these lines of code should resolve this problem, as repeaters and comparators are predominantly constructed of stone. The correct lines of code within their class should look something like the following:
net.minecraft.world.level.block.Blocks.java

```public class Blocks {
   ...
   public static final Block REPEATER = register("repeater", new RepeaterBlock(BlockBehaviour.Properties.of(Material.DECORATION).instabreak().sound(SoundType.STONE)));
   ...
  public static final Block COMPARATOR = register("comparator", new ComparatorBlock(BlockBehaviour.Properties.of(Material.DECORATION).instabreak().sound(SoundType.STONE)));
   ...```

### Comment 11: Avoma (2021-12-08T06:25:21.469-0800)

Can confirm in 1.18.

### Comment 12: Avoma (2022-04-05T12:07:59.066-0700)

Can confirm in 1.18.2 and 22w13a.

### Comment 13: Avoma (2022-10-02T06:00:24.927-0700)

Can confirm in 1.19.2.

### Comment 14: batbrain55 (2023-02-20T10:48:15.538-0800)

Can confirm in 23w07a.

### Comment 15: migrated (2023-05-26T17:33:55.131-0700)

Can confirm in 1.20 Pre-release 6

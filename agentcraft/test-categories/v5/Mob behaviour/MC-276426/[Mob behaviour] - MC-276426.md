# MC-276426: Slimes or magma cubes spawned by splitting synchronize inherited status effects

**Mojira URL:** [https://bugs.mojang.com/browse/MC-276426](https://bugs.mojang.com/browse/MC-276426)

## Report details

- **Mojira categories:** Mob behaviour
- **Project:** MC
- **Issue key:** MC-276426
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-09-05T23:04:38.070-0700
- **Updated:** 2025-02-24T12:38:31.238-0800
- **Resolution date:** 2024-09-20T01:34:18.572-0700
- **Affects versions:** 24w36a; 24w37a; 24w38a
- **Fix versions:** 24w39a
- **Area:** Expansion B
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 24w36a slime.zip; Minecraft 24w36a - Singleplayer 2024-09-06 14-30-17.mp4

## Description

Description
Since 24w36a, entities that are converted into another entities keep their status effects (see ), including split slimes or magma cubes. For example, when a slime dies, the dead slime's StatusEffectInstance s are added to the newly spawned slimes. Because StatusEffectInstance is mutable, and multiple slimes spawn when splitting, it must be copied, otherwise the same instance is shared between multiple entities. They didn't, causing bugs.
This is observed by:
- Adding an effect to a parent slime

- Killing the parent slime, causing child slimes to spawn with effects

- Observing that the inherited effect of child slimes expires much faster (if 2 slimes spawned when splitting, each has their effect durations effectively halved)

- Observing that, when adding the same effect (with longer durations or higher potency) to only one of the slimes while the inherited effect is still active, each gets the same effect

Steps to Reproduce
Attached is a world used for filming the video. Glowing is added to Slimes for visibility, but this does not affect the reproduction of the bug.
- Summon a slime:

```
/summon slime ~ ~ ~ {Size:4}
```

- Give the slime Invisibility for 60 seconds

```
/effect give @e[type=slime,limit=1] invisibility 60
```

- Kill the slime

```
/kill @e[type=slime]
```

- Give ONE slime Invisibility for 180 seconds

```
/effect give @e[type=slime,limit=1] invisibility 180
```

- (Optionally) tick sprint. For 2 slimes, 80s; for 3, 50s; and for 4, 35s.

```
/tick sprint 50s
```

Expected Behavior
One slime should become visible much later than the rest.
Specifically: after 60 seconds from the time parent slime was made invisible, all but one slime should be visible again. The one slime should be invisible for 180 seconds from the time that slime was made invisible.
Actual Behavior
All slimes become visible at the same time, and none of them becomes invisible for 180 seconds.
Specifically: 180 / numberOfSlime seconds after one of the child slime was given Invisibility, all slimes become visible at the same time.
Code Analysis
24w36a Yarn
In EntityConversionType#copyData, the following line is seen applying old entity's status effects to the newly spawned one:

```
for (StatusEffectInstance lv : oldEntity.getStatusEffects()) {
         newEntity.addStatusEffect(lv);
      }
```
This code is used for both one-to-one conversion (like zombification) and slimes/magma cubes splitting. When used in the splitting context, this is called for each child, reusing the parent's StatusEffectInstance. This causes the entities to share the same StatusEffectInstance.
When each entity ticks their status effects, this StatusEffectInstance gets ticked multiple times per tick, causing it to expire earlier. If the same effect with longer duration or higher potency is applied, the update applies to all entities that share the same effect instance.
To fix this issue, the effect should be copied:

```
for (StatusEffectInstance lv : oldEntity.getStatusEffects()) {
         newEntity.addStatusEffect(new StatusEffectInstance(lv));
      }
```

## Comments (1)

### Comment 1: migrated (2024-09-05T23:04:38.070-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

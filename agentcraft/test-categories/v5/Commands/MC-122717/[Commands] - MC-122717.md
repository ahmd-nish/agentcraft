# MC-122717: Command success messages for some commands include unaffected entities, unlike the command result

**Mojira URL:** [https://bugs.mojang.com/browse/MC-122717](https://bugs.mojang.com/browse/MC-122717)

## Report details

- **Mojira categories:** Commands
- **Project:** MC
- **Issue key:** MC-122717
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2017-11-29T18:12:18.417-0800
- **Updated:** 2026-06-16T09:22:57.318-0700
- **Resolution date:** 2026-06-16T09:16:22.616-0700
- **Affects versions:** Minecraft 17w48a; Minecraft 17w49a; Minecraft 17w49b; Minecraft 17w50a; Minecraft 18w01a; Minecraft 18w06a; Minecraft 18w08b; Minecraft 18w11a; Minecraft 18w16a; Minecraft 18w19b; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre5; Minecraft 1.13-pre9; Minecraft 1.13; Minecraft 18w30a; Minecraft 18w44a; Minecraft 19w02a; Minecraft 19w08a; Minecraft 19w11b; Minecraft 1.14.3; 1.14.4; 19w40a; 19w46b; 20w07a; 20w17a; 1.18.2; 1.19.2; 22w42a; 1.20.6; 24w18a; 24w40a; 1.21.5
- **Fix versions:** Future Update
- **Labels:** command-feedback
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** Bug.mp4; screenshot-1.png
- **Issue links:** Duplicate:inward:MC-277394:Tag remove command returned incorrect count when do not use the target selector variable | Relates:inward:MC-123068:The number of advancements said to be revoked from the player is incorrect | Relates:inward:MC-125061:Feedback text for successful "/recipe take *" doesn't account for locked recipes | Duplicate:inward:MC-271517:Entities immune to some/all effects show as being affected when using @e | Duplicate:inward:MC-155058:/tag in functions broken | Duplicate:inward:MC-131048:Command '/tag @e remove tagname' says it removed tag from all entities, and not just the ones with the tag | Duplicate:inward:MC-124979:/enchant feedback text is inaccurate if not all entities could receive the enchantment | Duplicate:inward:MC-121735:Using /tag add or remove if some entities already have the tag shows that it was successful for all | Duplicate:inward:MC-306519:The /clear command informs about the removal of an item from two players even if only one player had the item | Relates:outward:MC-308014:The success message of /clear reports that it affected more players than it did

## Description

The bug
When a command affects multiple entities, it's often the case that the command fails for some entities and succeeds for others. For example, adding a tag to some entities that already have it and others that don't. The command result usually reflects how many entities were successfully affected, but the command feedback message often includes all entities, even unaffected ones.
Affected commands
Each of these commands behaves similarly:
- result is the number of affected entities.

- If none were affected, an error is shown.

-  If any were affected, the success message includes the total number of entities found by the selector, not just the affected ones.

-  The "single success" message only appears if the selector only found one entity; it does not appear when it found multiple but only one was affected.

Command
An entity is unaffected if...
/tag ... add
It has too many tags, or already has the tag
/tag ... remove
It doesn't have the tag
/scoreboard players enable
The trigger is already enabled for that player
/recipe give
The player already knows the recipe
/recipe take
The player doesn't know the recipe
/playsound
The player is "too far away"
/enchant
It's not a mob/player
It's not holding anything
It's holding an incompatible item
It's holding an item with incompatible enchantments
/effect give
It's not a mob/player
It's immune to the effect
It has a stronger effect already
/effect clear ...
It's not a mob/player
It doesn't have the effect
/effect clear
It's not a mob/player
It doesn't have any effects
/clear ...
No matching items were found
/advancement grant
The player already has the advancement
/advancement revoke
The player doesn't have the advancement
/advancement grant ... only ...
The player already has the criterion
/advancement revoke ... only ...
The player doesn't have the criterion
/advancement poses a unique challenge. The result is simply the number of changes applied to any player, meaning the many-to-many scenario currently does not know (A) how many advancements found were changed on at least one player, and (B) how many players found had at least one advancement changed. Those are the two numbers that should in theory appear in the feedback message.
/recipe and /clear also currently only keep track of a running total for their result. They need to also keep track of how many players were affected to appear in the feedback message.
For all other commands, simply substituting the existing result into the feedback message would resolve the issue.
How to reproduce

```
/tag @e[sort=nearest,limit=5] add test
/tag @e[sort=nearest,limit=6] add test
```
Expected result
Added tag 'test' to 5 entities
Added tag 'test' to (some specific entity)
Observed result
Added tag 'test' to 5 entities
Added tag 'test' to 6 entities

## Comments (4)

### Comment 1: migrated (2017-11-29T18:12:18.417-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: lord.quadrato (2018-06-15T11:47:22.423-0700)

Confirmed for 1.13-pre2

### Comment 3: Viradex (2024-05-04T00:51:34.344-0700)

Can confirm in 24w18a for the /effect command.

### Comment 4: tryashtar (2026-05-10T22:54:57.860-0700)

Per request, I have split this ticket into separate tickets for each affected command:
- /tag:

- /scoreboard players enable:

- /recipe:

- /enchant:

- /effect:

/playsound was fixed in 25w15a. /advancement was fixed in 26.2-snapshot-1.

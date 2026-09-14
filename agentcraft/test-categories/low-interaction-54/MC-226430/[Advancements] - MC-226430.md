# MC-226430: Several 1.17 advancement strings are improperly capitalized

**Mojira URL:** [https://bugs.mojang.com/browse/MC-226430](https://bugs.mojang.com/browse/MC-226430)

## Report details

- **Mojira categories:** Advancements; Text
- **Project:** MC
- **Issue key:** MC-226430
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-05-27T06:55:48.049-0700
- **Updated:** 2025-04-30T08:41:32.583-0700
- **Resolution date:** 2022-04-16T05:29:06.515-0700
- **Affects versions:** 1.17 Pre-release 1; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 1; 1.17.1; 21w38a; 1.18 Pre-release 1; 1.18 Pre-release 8; 1.18 Release Candidate 3; 1.18; 1.18.1; 22w05a; 1.18.2; 22w14a
- **Fix versions:** 22w15a
- **Labels:** capitalization
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** MC-226430.png; MC-226430-1.png; MC-226430-2.png; MC-226430-3.png; MC-226430-4.png; MC-226430-5.png; MC-226430-6.png; MC-226430-7.png
- **Issue links:** Relates:inward:MC-226484:Advancement description for "Wax On" & "Wax Off" are a bit misleading

## Description

The Bug:
Several 1.17 advancement strings are improperly capitalized.
Affected Strings:
Translation Key
Current String
Correct String
advancements.adventure.lightning_rod_with_villager_no_fire.description
Protect a villager from an undesired shock without starting a fire
Protect a Villager from an undesired shock without starting a fire
advancements.adventure.spyglass_at_parrot.description
Look at a parrot through a spyglass
Look at a Parrot through a Spyglass
advancements.adventure.spyglass_at_ghast.description
Look at a ghast through a spyglass
Look at a Ghast through a Spyglass
advancements.adventure.spyglass_at_dragon.description
Look at the Ender Dragon through a spyglass
Look at the Ender Dragon through a Spyglass
advancements.husbandry.axolotl_in_a_bucket.description
Catch an axolotl in a bucket
Catch an Axolotl in a bucket
advancements.husbandry.kill_axolotl_target.description
Team up with an axolotl and win a fight
Team up with an Axolotl and win a fight
advancements.husbandry.wax_on.description
Apply Wax to a Copper block!
Apply Wax to a Copper Block!
advancements.husbandry.wax_off.description
Scrape Wax off of a Copper block!
Scrape Wax off of a Copper Block!
advancements.adventure.walk_on_powder_snow_with_leather_boots.description
Walk on powder snow...without sinking in it
Walk on Powder Snow...without sinking in it
h3. Steps to Reproduce:
- Grant yourself with any of the affected advancements.

```
/advancement grant @s only minecraft:adventure/lightning_rod_with_villager_no_fire
/advancement grant @s only minecraft:adventure/spyglass_at_parrot
/advancement grant @s only minecraft:adventure/spyglass_at_ghast
/advancement grant @s only minecraft:adventure/spyglass_at_dragon
/advancement grant @s only minecraft:husbandry/axolotl_in_a_bucket
/advancement grant @s only minecraft:husbandry/kill_axolotl_target
/advancement grant @s only minecraft:husbandry/wax_on
/advancement grant @s only minecraft:husbandry/wax_off
/advancement grant @s only minecraft:adventure/walk_on_powder_snow_with_leather_boots
```
- Locate the affected words within the advancement descriptions.

- Take note as to whether or not several 1.17 advancement strings are improperly capitalized.

Observed Behavior:
Several 1.17 advancement strings are improperly capitalized.
Expected Behavior:
Several 1.17 advancement strings would be properly capitalized.

## Comments (16)

### Comment 1: migrated (2021-05-27T06:55:48.049-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: Cultist_O (2021-05-27T21:08:17.297-0700)

Actually I think:
-  the powder snow one is correct

- the copper ones don't need "block" to be capitalized, and should instead have "copper" in the lower case

Only proper nouns, mob names and product identity fictional materials are capitalized in advancement descriptions.

### Comment 3: ampolive (2021-07-06T09:13:44.657-0700)

Relates to .

### Comment 4: ElseAirplane891 (2021-07-11T18:35:40.216-0700)

I think all the items and entities should be capitalized.

### Comment 5: Cultist_O (2021-07-12T14:10:43.942-0700)

@Bob Wu Why? Capitalizing all items would be completely inconsistent with the rest of the game, and English as a whole.

### Comment 6: ampolive (2021-07-13T17:45:01.805-0700)

According to  in this comment, in-game names such as "Bee Nest" and "Glass Bottle" should be capitalized, so Avoma's strings are correct. Except the "Light as a Rabbit" advancement should be "Walk on Powder Snow... without sinking in it", with a space after the ellipsis, to be consistent with the "Tactical Fishing" advancement ().

### Comment 7: Cultist_O (2021-09-10T17:45:38.173-0700)

@ampolive I see that it's ambiguous what they meant, but I'm fairly confident that comment refers to the fact item names are title case. As in, those strings are literally the title of the inventory object. That wouldn't apply to sentence case advancement descriptions.

### Comment 8: ampolive (2021-09-25T04:53:31.572-0700)

Can confirm in 21w38a.

### Comment 9: Tinsel (2021-11-11T12:05:16.109-0800)

Can confirm for 1.18. pre-1

### Comment 10: Tinsel (2021-11-24T15:46:07.751-0800)

In 1.18 pre-8

### Comment 11: kg583 (2022-01-08T19:10:37.712-0800)

The reported error with "Wax On" and "Wax Off" is inconsistent with . I'm inclined to suggest that the other report's suggested capitalization ("copper block") is accurate given that the item is called a "Block of Copper" (as discussed in the comments of the other report).

### Comment 12: Tinsel (2022-02-02T12:49:26.456-0800)

In 22w05a

### Comment 13: Avoma (2022-04-07T05:57:17.594-0700)

Since I feel this is worth mentioning and if anyone's curious, I've created a Google Docs Spreadsheet regarding all of the capitalization errors and inconsistencies within the advancement descriptions of advancements throughout Minecraft, which I actively keep updated. Here's the spreadsheet.
https://docs.google.com/spreadsheets/d/1GWz0YAqBH55u-Yw_U1p81evvGXVYBpwSomWYRgr0CHE/edit?usp=sharing

### Comment 14: MMK21 (2022-04-14T02:47:40.046-0700)

Note that the advancements.adventure.walk_on_powder_snow_with_leather_boots.description string is now capitalised correctly (in 22w15a). The remaining issue with the ellipsis is covered by .

### Comment 15: Avoma (2022-04-14T03:42:49.732-0700)

All of the affected strings as listed in this ticket except the "Wax on" and "Wax off" advancements descriptions have been fixed in 22w15a. Additionally, since both the "Wax on" and "Wax off" advancements descriptions will be changed in the near future as stated in , would it be a good idea to resolve this ticket () as fixed in 22w15a, and the remaining issue(s) can be tracked at MC-226484?

### Comment 16: Michael Wobst (2022-04-16T05:29:06.512-0700)

Resolving as fixed in 22w15a. Please create a new issue if there are remaining strings that still need to be fixed.

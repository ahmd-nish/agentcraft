# MC-50605: The pick block function doesn't work with mob spawners

**Mojira URL:** [https://bugs.mojang.com/browse/MC-50605](https://bugs.mojang.com/browse/MC-50605)

## Report details

- **Mojira categories:** Inventory; Items; Player
- **Project:** MC
- **Issue key:** MC-50605
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2014-03-08T07:54:46.616-0800
- **Updated:** 2025-04-30T06:28:16.658-0700
- **Resolution date:** 2022-11-02T07:56:13.892-0700
- **Affects versions:** Minecraft 14w10c; Minecraft 1.8; Minecraft 15w49a; Minecraft 1.8.9; Minecraft 15w50a; Minecraft 16w05b; Minecraft 1.9 Pre-Release 2; Minecraft 1.9.4; Minecraft 1.10 Pre-Release 1; Minecraft 16w42a; 1.15.2; 20w14a; 1.16 Pre-release 6; 1.16 Release Candidate 1; 1.16; 20w27a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 2; 1.16.4; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 1; 1.17.1; 21w38a; 21w39a; 21w40a; 21w42a; 21w43a; 1.18 Pre-release 7; 1.18; 1.18.1; 22w03a; 22w05a; 22w06a; 22w07a; 1.18.2 Release Candidate 1; 1.18.2; 22w16b; 22w17a; 1.19; 1.19.1; 1.19.2; 22w43a
- **Fix versions:** 22w44a
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-50605.mp4; MC-50605.png

## Description

The Bug:
The pick block function doesn't work with mob spawners.
Steps to Reproduce:
- Place down a spawner.

```
/setblock ~1 ~ ~ minecraft:spawner
```
- Attempt to use the pick block function on it.

- Take note as to whether or not the pick block function works with mob spawners.

Observed Behavior:
The pick block function doesn't work with mob spawners.
Expected Behavior:
The pick block function would work with mob spawners.

## Comments (37)

### Comment 1: migrated (2014-03-08T07:54:46.616-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2014-03-08T08:09:50.076-0800)

you aren't supposed to be able to do that, mojang actually had it enabled with the normal pick block in the first snapshot it introdused, but later removed the ability to do that.
works as intended

### Comment 3: migrated (2014-03-08T08:29:49.184-0800)

Do you know why Mojang removed this ability? I can't see any resone why.

### Comment 4: migrated (2014-03-08T10:17:49.638-0800)

people were able to achieve the 52 by doing it and Mojang don't want us to.

### Comment 5: migrated (2014-05-07T12:24:47.814-0700)

Is this still a concern in the current Minecraft version 14w18b / Launcher version 1.3.11 or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 6: migrated (2014-05-07T15:28:20.225-0700)

Confirmed for 14w18b, but I'm pretty sure this is Working As Intended. As I'm not a mod I can't make that decision but it seems pretty obvious Mojang doesn't intend mob spawners to be pickblock-able. Btw custom spawners can be made by using the setblock command in a command block. Here's a simple one:

```/setblock ~2 ~1 ~0 mob_spawner 0 replace {EntityId:Zombie}```
Here's a not so simple one:

```/setblock ~-1 ~-1 ~0 mob_spawner 0 replace {EntityId:Zombie,SpawnData:{Equipment:[{id:276},{},{},{},{id:397,Damage:3,tag:{ench:[{id:1,lvl:4}],SkullOwner:RageLokiCat}}]},SpawnPotentials:[{Type:Zombie,Weight:1,Properties:{Equipment:[{id:278,tag:{ench:[{id:20,lvl:2},{id:21,lvl:10}]}},{},{},{},{id:397,Damage:3,tag:{SkullOwner:MHF_Herobrine},Count:1}]}},{Type:LavaSlime,Weight:1,Count:4},{Type:Blaze,Weight:1,Count:2},{Type:CaveSpider,Weight:1,Count:8},{Type:Skeleton,Weight:1,Properties:{Equipment:[{id:261,tag:{ench:[{id:50,lvl:1}]}},{},{},{},{id:397,Damage:3,tag:{ench:[{id:0,lvl:2}],SkullOwner:MHF_Spider}}],Riding:{id:"EntityHorse",Type:4,Tame:1,SaddleItem:{id:329,Count:1,Damage:0}}},Count:2},{Type:Zombie,Weight:1,Properties:{Equipment:[{id:283,tag:{ench:[{id:20,lvl:2},{id:21,lvl:10}]}},{id:301},{id:300},{id:299},{id:397,Damage:3,tag:{ench:[{id:1,lvl:4}],SkullOwner:MHF_LavaSlime}}]},Count:2},{Type:Skeleton,Weight:1,Properties:{Equipment:[{id:261}],Riding:{id:"Blaze"}},Count:2},{Type:Skeleton,Weight:1,Properties:{Equipment:[{id:261},{id:317},{id:316},{id:315},{id:397,Damage:3,tag:{ench:[{id:1,lvl:4}],SkullOwner:MHF_Villager}}],Riding:{id:"Slime",Size:4}},Count:1},{Type:Zombie,Weight:1,Properties:{Equipment:[{id:283,tag:{ench:[{id:21,lvl:10},{id:34,lvl:3}]}},{id:301},{id:308},{id:299},{id:397,Damage:3,tag:{ench:[{id:1,lvl:4}],SkullOwner:MHF_Pig}}]},Count:5},{Type:PigZombie,Weight:1,Properties:{Equipment:[{id:283,tag:{ench:[{id:21,lvl:10},{id:34,lvl:3}]}}],Anger:1},Count:4},]}```
Note that a recent snapshot changed custom head codes. They'll all be steve heads if broken (or if there's no internet connection). Also I hear the anger tag for zombie pigmen was broken in another recent snapshot (last AI change).

### Comment 7: migrated (2014-05-08T17:11:49.014-0700)

this works as intended

### Comment 8: trazlander (2014-05-27T07:24:25.369-0700)

Duplicate of MC-48668

### Comment 9: migrated (2014-10-10T11:24:32.793-0700)

Confirmed in 1.8. ctrl+pick-block should work on mob spawners, otherwise there would be little reason to keep them in their item form, especially since they don't appear in the creative mode item selection menu.

### Comment 10: trazlander (2014-10-14T07:00:17.069-0700)

Well, thanks for giving us the official "Works as Intended" for this finally, even though I'm highly disappointed in that decision

### Comment 11: marcono1234 (2015-05-25T12:00:07.101-0700)

Confirmed for
- 1.8.6  can you please explain that resolution? Other blocks which aren't accessible in the creative menu like the command block support pick block

### Comment 12: migrated (2015-12-02T09:42:09.378-0800)

Reopening, mob spawners are intended to be available as items.

### Comment 13: migrated (2015-12-16T12:53:02.252-0800)

This bug is still existent in 15w50a.

### Comment 14: migrated (2016-02-05T05:17:55.771-0800)

Confirmed for 16w05b

### Comment 15: SunCat (2016-02-19T12:14:35.946-0800)

Confirmed for 1.9-pre2

### Comment 16: migrated (2016-06-02T20:35:37.618-0700)

Confirmed for 1.10-pre1

### Comment 17: migrated (2016-08-18T15:44:52.265-0700)

Marcono1234
Yeah, but think about full mushroom blocks.

### Comment 18: marcono1234 (2016-08-18T18:48:39.343-0700)

But this is different since you can have the same mob spawner with a BlockEntityTag in your inventory whereas the full mushroom block does not exist in item form.

### Comment 19: migrated (2016-08-18T19:32:35.775-0700)

I'm referring to minecraft:red_mushroom_block and minecraft:brown_mushroom_block.

### Comment 20: marcono1234 (2016-12-06T10:12:27.441-0800)

Grum could you please explain why this is WAI? Other "problematic" blocks clean the exploiting NBT tags as well, for example command blocks with their Command tag.
Or is it that you are afraid non-op players would complain that they cannot pick-block a non-exploiting spawner?

### Comment 21: migrated (2016-12-06T10:19:48.917-0800)

I'd also like to know why this is WaI, unless it's about a possible severe exploit - maybe that shouldn't be public

### Comment 22: migrated (2017-11-10T16:17:08.105-0800)

Confirmed for 1.12. How is this WAI?

### Comment 23: migrated (2020-04-06T11:27:42.693-0700)

Confirmed for 20w14a.

### Comment 24: anthony cicinelli (2020-06-05T07:02:42.740-0700)

Affects 1.16Pre-Release 2

### Comment 25: anthony cicinelli (2020-06-16T06:45:45.327-0700)

Affects 1.16 Pre-Release 6, I would like to request ownership of this ticket.

### Comment 26: anthony cicinelli (2020-06-16T11:19:10.112-0700)

Affects 1.16 Pre-Release 7, I would like to request ownership of this ticket so I can continue to update it.

### Comment 27: anthony cicinelli (2020-06-19T10:22:21.337-0700)

Affects 1.16 rc-1

### Comment 28: anthony cicinelli (2020-07-04T06:43:50.643-0700)

Affects 20w27a

### Comment 29: Avoma (2020-11-23T03:41:40.290-0800)

Can confirm for 20w46a.
I'd like to request ownership of this ticket since the report has been inactive since October 2016.

### Comment 30: Avoma (2020-11-27T10:13:58.947-0800)

Can confirm in 20w48a.

### Comment 31: markderickson (2021-02-10T20:24:36.412-0800)

Can confirm in 21w06a.

### Comment 32: Avoma (2021-03-29T06:57:40.450-0700)

Can confirm in 21w11a.

### Comment 33: migrated (2021-12-02T03:57:58.659-0800)

Affects 1.18

### Comment 34: muzikbike (2022-04-27T07:16:30.604-0700)

Affects 22w16b

### Comment 35: bodakugga (2022-10-26T06:26:06.988-0700)

Affects 22w43a, despite spawners being added to the creative inventory

### Comment 36: muzikbike (2022-11-02T07:54:23.683-0700)

Apparently fixed in 22w44a according to patch notes

### Comment 37: ampolive (2022-11-02T07:56:04.121-0700)

Can confirm fixed in 22w44a.

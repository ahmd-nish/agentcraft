# MC-200991: Soul Speed in minecart uses durability

**Mojira URL:** [https://bugs.mojang.com/browse/MC-200991](https://bugs.mojang.com/browse/MC-200991)

## Report details

- **Mojira categories:** Enchantments; Hitboxes; Minecart
- **Project:** MC
- **Issue key:** MC-200991
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-09-25T00:14:11.268-0700
- **Updated:** 2025-04-29T08:17:40.840-0700
- **Resolution date:** 2024-07-15T02:58:06.149-0700
- **Affects versions:** 1.16.1; 1.16.3; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w07a; 21w13a; 21w16a; 21w17a; 1.17; 1.17.1; 21w40a; 1.20 Pre-release 4
- **Fix versions:** 24w18a
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-200991.mp4; MC-200991.png; setup.png
- **Issue links:** Duplicate:inward:MC-231141:Minecarts traveling on rails on soul sand still use players' Soul Speed boots' durability | Relates:inward:MC-274447:Soul speed can use durability when equipping boots while standing on soul blocks | Duplicate:inward:MC-193282:Soul Speed Effect Triggers While Riding Mounts on Soul Blocks | Duplicate:inward:MC-194186:Strider speeds up from the shower speed boots | Duplicate:inward:MC-202718:Soul Speed Boots lose durability and eventually break when riding minecart over Soul Soil. | Duplicate:inward:MC-209059:Riding Minecart over soulsand damages boots

## Description

The Bug
When wearing boots enchanted with soul speed (any level) and riding a minecart track on soul soil, durability is used on the boots. No speed gain is applied.
Reproduce
See video for example
Observed Behavior
The durability of soul speed boots is consumed whilst riding in minecarts.
Expected Behavior
The durability of soul speed boots would not be consumed whilst riding in minecarts.

## Comments (14)

### Comment 1: migrated (2020-09-25T00:14:11.268-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: anthony cicinelli (2020-09-25T07:14:23.652-0700)

I can confirm for 1.16.3

### Comment 3: migrated (2020-10-04T11:59:54.962-0700)

My FOV changes back and forth between soul speed affected and regular vision in survival and adventure mode.

### Comment 4: migrated (2020-10-28T13:35:32.904-0700)

Relates to

### Comment 5: Avoma (2021-01-14T07:44:25.354-0800)

Can confirm in 20w51a.

### Comment 6: migrated (2021-02-17T12:49:21.098-0800)

Confirmed in 21w07a

### Comment 7: Avoma (2021-04-03T06:25:04.480-0700)

Can confirm in 21w13a.

### Comment 8: Avoma (2021-04-25T11:54:44.300-0700)

Can confirm in 21w16a.

### Comment 9: Avoma (2021-05-04T12:00:07.070-0700)

Can confirm in 1.16.5.

### Comment 10: migrated (2021-06-01T06:32:19.034-0700)

Affects 1.17 Pre-release 2

### Comment 11: migrated (2021-06-08T08:33:02.926-0700)

Affects 1.17

### Comment 12: Avoma (2021-07-11T08:36:51.986-0700)

Can confirm in 1.17.1.

### Comment 13: Avoma (2021-10-11T01:22:04.618-0700)

Can confirm this behavior in 21w40a. Here are some extra details regarding this problem.
The Bug:
The durability of soul speed boots is consumed whilst riding in minecarts.
Steps to Reproduce:
- Build the setup as shown in the attachment below.

- Switch into survival mode, place down a minecart, begin riding it.

- Equip some boots enchanted with soul speed.

```/item replace entity @s armor.feet with minecraft:leather_boots{Enchantments:[{id:"soul_speed",lvl:3}]}```
- After riding around in the minecart for around thirty seconds, take note as to whether or not the boots consumed durability.

Observed Behavior:
The durability of soul speed boots is consumed whilst riding in minecarts.
Expected Behavior:
The durability of soul speed boots would not be consumed whilst riding in minecarts.

### Comment 14: Brevort (2023-05-19T19:10:40.418-0700)

Confirmed in 1.20 Pre-Release 4. A possible fix for this would be to check if you are a passenger when reducing durability of boots due to soul speed.

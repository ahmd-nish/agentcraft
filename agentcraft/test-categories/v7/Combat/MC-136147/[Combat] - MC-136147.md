# MC-136147: Riptide tridents use mainhand item to inflict damage when thrown in the offhand

**Mojira URL:** [https://bugs.mojang.com/browse/MC-136147](https://bugs.mojang.com/browse/MC-136147)

## Report details

- **Mojira categories:** Combat
- **Project:** MC
- **Issue key:** MC-136147
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2018-08-16T19:15:30.531-0700
- **Updated:** 2025-04-26T07:04:58.214-0700
- **Resolution date:** 2024-11-18T09:30:31.038-0800
- **Affects versions:** Minecraft 1.13; Minecraft 1.13.1-pre1; Minecraft 1.13.1-pre2; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w48b; Minecraft 19w07a; Minecraft 19w08b; Minecraft 19w09a; Minecraft 19w11a; Minecraft 19w11b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1 Pre-Release 1; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 2; 1.14.4; 19w35a; 19w36a; 19w40a; 1.15.2; 20w12a; 1.16 Pre-release 1; 1.16.1; 20w30a; 1.16.2 Release Candidate 1; 1.16.3; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 20w51a; 21w05b; 21w06a; 21w07a; 21w11a; 21w15a; 21w19a; 1.17; 1.17.1; 21w39a; 21w42a; 1.18; 1.18.1; 1.18.2; 1.19; 1.19.1 Release Candidate 2; 1.19.2; 22w43a; 1.19.3; 1.19.4 Release Candidate 2; 1.19.4; 1.20 Release Candidate 1; 1.20; 1.20.1; 1.20.2 Release Candidate 1; 1.20.2 Release Candidate 2; 1.20.4; 24w12a; 1.20.6; 24w19a; 24w20a
- **Fix versions:** 24w19a
- **Area:** Gameplay
- **Labels:** durability; enchantment-effect; mainhand; offhand; riptide
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** fixed.mp4; MC-136147.mp4; MC-136147 - Damage when holding trident in main hand.png; MC-136147 - Damage when holding trident in offhand.png
- **Issue links:** Relates:outward:MC-271455:When holding a fire aspect weapon in the mainhand, thrown tridents in the offhand will set mobs on fire | Relates:outward:MC-99063:Looting not working on offhand | Duplicate:inward:MC-263581:Trident in offhand applying damage from main hand | Duplicate:inward:MC-175586:Using Riptide in off hand will deal damage according to the item in your main hand, not the actual trident

## Description

The bug
When you throw a riptide trident in the offhand, you hit with the mainhand item instead. This means that throwing a riptide trident in the offhand while holding nothing in the mainhand will make the trident deal minimal damage. This also means that a sword held in the mainhand will inflict damage, apply most of its enchantments (looting is intended), and take durability damage when you ram into mobs via riptide trident in offhand.
How to reproduce
- Setup a scoreboard to count all damage dealt

```
/scoreboard objectives add Damage minecraft.custom:minecraft.damage_dealt
/scoreboard objectives setdisplay sidebar Damage
/scoreboard players add @s Damage 0
```

- Get a trident with Riptide I and spawn an entity

- Throw the trident in mainhand
→  Score increases with 80

- Throw the trident in offhand while holding nothing in main hand
→  Score increases with 10

## Comments (23)

### Comment 1: migrated (2018-08-16T19:15:30.531-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: gaspoweredpick (2018-08-16T19:17:22.600-0700)

Possibly relates to MC-99063

### Comment 3: migrated (2018-10-03T12:27:51.213-0700)

Can confirm. I'll leave a more detailed way on how to reproduce.
How to reproduce
- Setup a scoreboard to count all damage dealt.

```/scoreboard objectives add Damage minecraft.custom:minecraft.damage_dealt
/scoreboard objectives setdisplay sidebar Damage
/scoreboard players add @s Damage 0```

- Get a trident with riptide I and spawn a sheep.

- Throw the trident in mainhand
   → Score increases with 80.

- Throw the trident in offhand
 → Score increases with 10.

### Comment 4: [Mod] Asteraoth (2018-10-03T14:13:55.121-0700)

I hope you don't mind me updating your ticket.

### Comment 5: gaspoweredpick (2018-10-09T11:54:54.250-0700)

It also seems that Impaling or strength work as they should in the offhand. The trident itself is the only thing that does reduced damage.
Edit: Impaling actually doesn't work in the offhand, but strength does add damage. The reason I thought it didn't was because I had a sword in my mainhand, and I discovered that mainhand weapon damage is applied to the offhand trident attack.

### Comment 6: migrated (2018-10-17T11:03:59.544-0700)

Confirmed for 1.13.2-pre1.

### Comment 7: migrated (2018-10-21T18:02:10.939-0700)

Confirmed for 1.13.2-pre2.

### Comment 8: gaspoweredpick (2018-12-01T19:39:08.857-0800)

I have recently discovered that mainhand tool and weapon damage is applied to the offhand trident attack. Certain weapon enchantments like Sharpness, Smite, Bane of Arthropods, Fire Aspect, and Knockback also apply their effects to the offhand trident attack (Looting is a different case since it intentionally applies to any direct kills when the Looting sword is in the mainhand).

### Comment 9: gaspoweredpick (2019-02-23T13:33:13.182-0800)

Simplified the report.

### Comment 10: migrated (2019-06-10T04:48:30.305-0700)

Confirmed in all 1.14 versions, including 1.14.3 Pre-Release 2.

### Comment 11: migrated (2020-06-04T14:44:07.440-0700)

Confirmed for 1.16 Pre-2

### Comment 12: jamesmoton (2020-08-09T04:40:44.927-0700)

You actually don't need the offhand slot to reproduce this bug. If you throw a trident with Riptide III and switch to another item in your mainhand (such as a golden sword), that sword will still take durability damage and it will be as if you attacked with the sword instead of the trident.

### Comment 13: Avoma (2021-02-10T05:02:29.602-0800)

Can confirm in 21w05b.

### Comment 14: Avoma (2021-02-16T10:15:53.435-0800)

Can confirm in 21w06a.

### Comment 15: Avoma (2021-02-22T01:01:46.182-0800)

Can confirm in 21w07a.

### Comment 16: Avoma (2021-06-14T11:43:13.680-0700)

Can confirm in 1.17.

### Comment 17: Avoma (2021-07-07T10:51:41.098-0700)

Can confirm in 1.17.1.

### Comment 18: Avoma (2022-01-02T10:09:55.429-0800)

Can confirm in 1.18.1.

### Comment 19: Avoma (2022-03-10T10:45:48.341-0800)

Can confirm in 1.18.2.

### Comment 20: Avoma (2022-06-29T05:45:27.861-0700)

Can confirm in 1.19.

### Comment 21: Avoma (2022-10-18T08:26:21.254-0700)

Can confirm in 1.19.2.

### Comment 22: 4ebugger (2024-03-23T09:01:14.039-0700)

Confirm in 24w12a, you can easily kill an enemy with mace while hold trident in the offhand.

### Comment 23: J Z (2024-11-13T10:43:07.218-0800)

I think this was fixed in 24w19a (the part about applying enchantments is still in the game, but covered under MC-3304). This could also be considered fixed in 24w18a, but riptide tridents did not work correctly in that version. In the "Affected Versions", 24w19a and 24w20a are listed; I cannot reproduce the bug in these versions, nor in any version after them.

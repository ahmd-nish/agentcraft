# MC-258360: Horse armor loses its NBT data when equipped on horses via right-clicking

**Mojira URL:** [https://bugs.mojang.com/browse/MC-258360](https://bugs.mojang.com/browse/MC-258360)

## Report details

- **Mojira categories:** Items
- **Project:** MC
- **Issue key:** MC-258360
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-12-07T17:34:25.261-0800
- **Updated:** 2025-04-30T04:30:55.989-0700
- **Resolution date:** 2023-05-16T04:25:50.021-0700
- **Affects versions:** 1.19.3; 23w05a; 1.19.4; 1.20 Pre-release 1
- **Fix versions:** 1.20 Pre-release 2
- **Area:** Platform
- **Labels:** horse; horse_armor
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 1.png; 2.png; 3.png; 4.png; 5.png; MC-258360.png
- **Issue links:** Relates:inward:MC-191591:Saddles lose their NBT data when equipped on horses, zombie horses, skeleton horses, mules or donkeys via right-clicking | Duplicate:inward:MC-258473:Dyed horse armor becomes restored to default color after placed on horse. | Duplicate:inward:MC-258648:When I dye leather horse armor and put it on horses the dyed color disappears | Duplicate:inward:MC-258931:Bug with painted horse armor | Duplicate:inward:MC-259688:Dyed leather horse armor loses its dye when quick-equipped onto a horse ( NBT discarded) | Duplicate:inward:MC-259726:Dyed horse armor loses its color when right click on a horse with it | Duplicate:inward:MC-261476:dyes on leather horse armor is dismissed with the "quick" equip on horse | Duplicate:inward:MC-261914:Horse leather armor looses color on right click equipping | Duplicate:inward:MC-262342:Leather Horse armour loses dye | Duplicate:inward:MC-262578:Leather horse armor resets to normal color when right clicked onto a horse

## Description

The Bug:
Horse armor loses its NBT data when equipped on horses via right-clicking.
It's important to note that this issue does not occur when equipping the horse armor through the horses' inventory. This problem is most noticeable with dyed leather horse armor; when right-clicking a horse with dyed horse armor, the horse armor loses its color.
Steps to Reproduce:
- Summon a tamed horse by using the command provided below.

```
/summon minecraft:horse ~ ~ ~ {NoAI:1b,Tame:1b}
```

- Give yourself some leather horse armor that contains custom NBT data by using the command provided below.

```
/give @s minecraft:leather_horse_armor{display:{Name:'{"text":"MC-258360","italic":"false"}',color:11141290}}
```

- Right-click on the horse while holding the horse armor to equip the horse with the horse armor.

- Take note as to whether or not horse armor loses its NBT data when equipped on horses via right-clicking.

Observed Behavior:
NBT data of the horse armor is lost.
Expected Behavior:
NBT data of horse armor would not be lost.
Video:
https://www.youtube.com/watch?v=2htKzz-VOXc

## Comments (6)

### Comment 1: migrated (2022-12-07T17:34:25.261-0800)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: NBG-bootmgr (2022-12-07T21:18:15.912-0800)

Can you provide a picture please?

### Comment 3: migrated (2022-12-07T22:06:27.325-0800)

I added a photo to the attached file. Do you need any more information?

### Comment 4: Avoma (2022-12-08T08:49:17.313-0800)

The problem here has arisen due to the fix of MC-197150. This ticket very closely relates to .

### Comment 5: Avoma (2022-12-08T09:26:27.027-0800)

This issue isn't just exclusive to colored leather horse armor; it's present with horse armor in general. The problem here is that horse armor loses its NBT data when equipped on horses via right-clicking. I've updated this ticket accordingly to reflect this new information.

### Comment 6: Brevort (2023-03-17T13:34:08.155-0700)

Affects 1.19.4.

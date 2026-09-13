# MC-53602: Projectiles don't collide with the world border

**Mojira URL:** [https://bugs.mojang.com/browse/MC-53602](https://bugs.mojang.com/browse/MC-53602)

## Report details

- **Mojira categories:** Projectiles
- **Project:** MC
- **Issue key:** MC-53602
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2014-04-25T10:45:14.163-0700
- **Updated:** 2025-04-26T03:25:23.213-0700
- **Resolution date:** 2024-08-17T06:37:43.477-0700
- **Affects versions:** Minecraft 14w17a; Minecraft 14w18a; Minecraft 14w18b; Minecraft 14w28b; Minecraft 14w31a; Minecraft 1.8; Minecraft 15w34a; Minecraft 15w34b; Minecraft 15w34c; Minecraft 15w34d; Minecraft 15w47c; Minecraft 1.9.2; Minecraft 1.9.3 Pre-Release 1; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w42a; Minecraft 16w43a; Minecraft 1.11.2; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 18w20c; Minecraft 1.13; Minecraft 1.13.1-pre1; Minecraft 1.13.1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 19w09a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; 20w06a; 1.16.1; 20w27a; 20w29a; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.17; 1.17.1; 21w42a; 21w43a; 1.18 Pre-release 1; 1.18 Pre-release 5; 1.18 Release Candidate 4; 1.18; 1.18.1; 1.18.2; 22w12a; 22w19a; 1.19; 1.19.1; 1.19.2; 22w43a; 1.19.3; 23w03a; 1.19.4; 1.20; 1.20.1; 1.20.2; 23w42a; 1.20.4; 23w51b; 24w11a; 1.20.5 Release Candidate 3; 1.20.5; 1.20.6 Release Candidate 1; 1.20.6; 24w18a; 1.21; 1.21.1
- **Fix versions:** 24w33a
- **Area:** Platform
- **Labels:** arrow; collision; ender_pearl; fireball; projectile; snowball; world-border
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** _BugTracker_ (1.21.1).png; MC-53602.mp4; MC-53602.png
- **Issue links:** Relates:outward:MC-276103:Wind charge explosions can interact with blocks outside the world border | Relates:outward:MC-34074:Use enderpearl to get past 29999999.7 blocks | Duplicate:inward:MC-271049:Can shoot arrows outside of world border's border. | Duplicate:inward:MC-271050:Trident can go through the invisible border outside world border | Duplicate:inward:MC-271348:Shulker bullets can go through the world border. | Duplicate:inward:MC-226612:Ender pearl teleports you out of world border | Duplicate:inward:MC-64711:Enter Farlands in survival | Duplicate:inward:MC-220731:projectiles pass through world border | Duplicate:inward:MC-216025:Can throw projectiles outside world border | Duplicate:inward:MC-208456:Ender pearls let you teleport beyond the world border in survival minecraft | Relates:inward:MC-154082:The world border is no longer solid | Duplicate:inward:MC-114255:You can STILL get out off the world border by trowing en pearl | Duplicate:inward:MC-109075:Shotted Arrow Can Through The World Boarder | Duplicate:inward:MC-53376:World Border doesn't stop arrows | Duplicate:inward:MC-101183:if you launch an ender pearl out of worldborder exit from it | Duplicate:inward:MC-73557:New Added Wall Bug | Duplicate:inward:MC-69069:Enderpearls can be used to go through the world border | Duplicate:inward:MC-62914:You can teleport out of the world border with enderpearls | Duplicate:inward:MC-61819:Teleporting out of the 30,000,000 block world border w/ender pearls | Duplicate:inward:MC-56255:Ender pearls can go outside World Borders | Duplicate:inward:MC-55786:Arrows and enderpearls can be thrown / shoot trough worldborder | Duplicate:inward:MC-53407:World Border - Players can currently ender perl out | Duplicate:inward:MC-54103:Ender pearl thrown through world border.

## Description

The Bug:
Projectiles don't collide with the world border.
This affects all types of projectiles such as arrows, snowballs, eggs, ender pearls, fireballs, etc... This also allows players to get outside of the world border by simply using an ender pearl.
Steps to Reproduce:
- Set the world border's center to your current position and to twenty blocks wide by using the commands provided below.

```
/worldborder center ~ ~
```

```
/worldborder set 20
```

- Obtain any projectile, for example, a snowball.

- Whilst facing the world border, throw/shoot the projectile.

- Take note as to whether or not projectiles collide with the world border.

Observed Behavior:
Projectiles don't collide with the world border.
Expected Behavior:
Projectiles would collide with the world border.

## Comments (27)

### Comment 1: migrated (2014-04-25T10:45:14.163-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: kumasasa (2014-04-26T01:03:51.677-0700)

Cannot confirm.
But this is kinda intended, because it's planned to allow players to go outside of the world barrier, but they take (quickly) damage there.

### Comment 3: migrated (2014-05-08T02:46:53.677-0700)

Confirmed for 14w18b.

### Comment 4: migrated (2014-07-13T20:33:31.302-0700)

I say that the world border is simply the world BORDER, therefore you really shouldn't be able to cross it.

### Comment 5: migrated (2014-07-28T07:18:38.333-0700)

@kumasasa it will be unfair for players to lose all of their equipment just because they accidently shot an ender pearl through the barrier, and because of the damage being dealt they will lose their equipment.
It would be better if you just could be teleported to the closest block of air from the world border after you teleported. For example: the world border is at (50,20+1,40) and you teleport to (60,10+1,40) - the wolrd border is directly in your back and the "+1" comes from the block of air. After you teleported, you will be teleported to (50,20+1,40), thus not losing any items. It would be nice if this could be a possible solution, but if it is impossible then I guess you shouldn't cross the world border with any valueable items in your inventory.

### Comment 6: kumasasa (2014-08-04T12:19:50.261-0700)

This is related, but meant here is the world border.

### Comment 7: migrated (2014-08-05T17:46:56.183-0700)

confirmed for 14w31a

### Comment 8: Sonicwave (2014-10-05T13:00:03.611-0700)

Confirmed for 1.8.

### Comment 9: marcono1234 (2017-02-08T19:33:43.454-0800)

Moved the chorus fruit part to MC-106416 as it uses the same method as endermen.

### Comment 10: [Mod] Asteraoth (2018-08-18T10:47:18.891-0700)

Confirmed for 1.13.1-pre1

### Comment 11: [Mod] Asteraoth (2018-08-22T08:53:44.939-0700)

Confirmed for 1.13.1

### Comment 12: migrated (2018-10-21T04:34:20.023-0700)

Confirmed for 1.13.2-pre2.

### Comment 13: gaspoweredpick (2019-03-09T16:29:14.932-0800)

Confirmed for 1.13.2 and 19w09a. This does not affect fireworks.

### Comment 14: pulpetti (2020-07-06T12:21:15.797-0700)

Affects 1.16.1 and 20w27a

### Comment 15: pulpetti (2020-07-21T17:05:34.450-0700)

In 20w29a

### Comment 16: ampolive (2021-06-08T17:14:25.554-0700)

In 1.17. Also affects tridents.

### Comment 17: Avoma (2021-07-13T01:01:54.813-0700)

Can confirm in 1.17.1.

### Comment 18: Avoma (2021-10-25T03:28:36.866-0700)

Can confirm in 21w42a. I'd like to request ownership of this ticket since the current reporter has been inactive for over a year. I've willing to continue to provide all of the necessary information and will keep this report updated.

### Comment 19: ampolive (2021-10-27T15:46:53.478-0700)

Can confirm in 21w43a.

### Comment 20: muzikbike (2021-11-11T09:38:04.150-0800)

Still affects 1.18pre1

### Comment 21: MMK21 (2021-12-10T08:51:32.693-0800)

Affects 1.18.1

### Comment 22: Avoma (2022-03-24T09:31:58.396-0700)

Can confirm in 1.18.2 and 22w11a.

### Comment 23: Avoma (2022-06-13T05:40:20.464-0700)

Can confirm in 1.19.

### Comment 24: migrated (2022-07-27T09:58:23.999-0700)

Can confirm in 1.19.1-rc3

### Comment 25: migrated (2022-08-03T13:03:52.414-0700)

Confirmed in 1.19.1
Also, because the description of the bug got generalized to all projectiles, I wanted to clarify that this bug allows players to get outside the world border by using an ender pearl.
This is especially annoying for some Mini-games that use the world border to limit the play area, because as it turns out, you only get damage from the world border, when you are 6+ blocks out. This little "gap" of 5 blocks gives players the ability to hide behind the world border without being able to get hit (If the other player doesn't have a Bow)

### Comment 26: Brain81505 (2023-01-18T08:09:01.186-0800)

Can confirm in 23w03a

### Comment 27: migrated (2023-12-19T11:37:35.193-0800)

Still affects 23w51b

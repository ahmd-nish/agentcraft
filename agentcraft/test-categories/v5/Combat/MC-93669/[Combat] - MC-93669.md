# MC-93669: The sweeping attack doesn't ignite other mobs when using the fire aspect enchantment

**Mojira URL:** [https://bugs.mojang.com/browse/MC-93669](https://bugs.mojang.com/browse/MC-93669)

## Report details

- **Mojira categories:** Combat
- **Project:** MC
- **Issue key:** MC-93669
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2015-12-02T14:45:54.108-0800
- **Updated:** 2025-04-16T13:21:18.326-0700
- **Resolution date:** 2024-07-05T13:15:46.244-0700
- **Affects versions:** Minecraft 15w49a; Minecraft 1.10.2; Minecraft 16w43a; Minecraft 1.12; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w09a; 1.15.2; 1.16 Release Candidate 1; 1.16; 1.16.2; 20w46a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 1; 1.17.1; 21w37a; 21w38a; 21w40a; 21w43a; 1.18 Pre-release 1; 1.18; 1.18.1; 22w03a; 22w05a; 22w06a; 22w07a; 1.18.2 Release Candidate 1; 1.18.2; 22w17a; 22w19a; 1.19; 1.19.1; 1.19.2; 22w43a; 1.19.3 Release Candidate 3; 1.19.3; 1.19.4; 1.20; 1.20.1; 1.20.4; 23w51b
- **Fix versions:** 24w18a
- **Area:** Gameplay
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2021-05-02_15.59.35.png; MC-93669.mp4
- **Issue links:** Relates:inward:MC-274187:The sweeping attack from a sword enchanted with Fire Aspect can ignite other players with PVP disabled | Duplicate:inward:MC-119067:Fire Aspect & Sweeping Edge | Duplicate:inward:MC-236774:Animals killed by an indirect hit from a fire-aspect sword drop raw meat | Relates:outward:MC-271653:The sweeping attack doesn't deal increased knockback to other mobs when using the knockback enchantment | Relates:inward:MC-165302:The sweeping attack doesn't apply strength or weakness effects to other mobs | Bonfire Testing:inward:MC-92849:mob kills due to knock back from a sweep attack fail to reward EXP | Duplicate:inward:MCL-17865:sweeping edge + fire aspect bug

## Description

The Bug:
The sweeping attack doesn't ignite other mobs when using the fire aspect enchantment.
Steps to Reproduce:
- Give yourself a sword enchanted with fire aspect by using the command provided below.

```
/give @s minecraft:iron_sword{Enchantments:[{id:"minecraft:fire_aspect",lvl:2}]}
```

- Summon two cows next to one another by using the commands provided below.

```
/summon minecraft:cow ~ ~ ~-2.5 {NoAI:1b}
```

```
/summon minecraft:cow ~1 ~ ~-2.5 {NoAI:1b}
```

- Hit the cow directly in front of you.

- Take note as to whether or not the sweeping attack ignites other mobs when using the fire aspect enchantment.

Observed Behavior:
The sweeping attack doesn't ignite other mobs when using the fire aspect enchantment.
Expected Behavior:
The sweeping attack would ignite other mobs when using the fire aspect enchantment.

## Comments (15)

### Comment 1: migrated (2015-12-02T14:45:54.108-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2016-03-10T08:22:34.220-0800)

Would love to see this resolved.

### Comment 3: NeunEinser (2016-06-21T14:10:56.675-0700)

I don't think this is really a bug, perhaps you should post it as a Suggestion in /r/MinecraftSuggestions

### Comment 4: migrated (2018-09-14T09:30:49.101-0700)

Confirmed for 1.13.1.

### Comment 5: gaspoweredpick (2019-03-09T17:25:13.744-0800)

Confirmed for 1.13.2 and 19w09a. Same thing applies to knockback.

### Comment 6: migrated (2020-06-14T07:29:18.773-0700)

Confirmed in 1.16-pre5.

### Comment 7: j_p_smith (2020-06-23T02:35:07.229-0700)

Confirmed in 1.15.2 and 1.16 Release Candidate 1.

### Comment 8: Avoma (2021-01-24T04:00:56.793-0800)

Can confirm in 21w03a.

### Comment 9: Avoma (2021-02-06T09:45:58.485-0800)

Can confirm in 21w05b.

### Comment 10: Avoma (2021-02-16T07:37:47.615-0800)

Can confirm in 21w06a. Video attached.

### Comment 11: Avoma (2021-02-19T07:48:39.166-0800)

Can confirm in 21w07a.

### Comment 12: Avoma (2021-03-03T07:44:26.731-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 13: Avoma (2021-03-08T06:56:27.411-0800)

I'd like to request ownership of this ticket since the current reporter has been inactive since December 2015. I'm willing to provide all of the necessary information and will keep this report updated.

### Comment 14: migrated (2022-10-28T16:33:16.166-0700)

@ilmango got confused and talked about this bug on his current SkyBlock series: https://youtu.be/m404IWHVZWE?t=1574

### Comment 15: migrated (2022-12-06T10:04:34.235-0800)

Can Confirm 1.19.3 Release Preview 3, severe negative impact on gameplay.

# MC-200899: Players don't receive thorns damage when attacking entities wearing thorns armor with indirect sweeping attacks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-200899](https://bugs.mojang.com/browse/MC-200899)

## Report details

- **Mojira categories:** Combat; Enchantments
- **Project:** MC
- **Issue key:** MC-200899
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-09-23T16:49:06.714-0700
- **Updated:** 2025-03-25T13:01:57.308-0700
- **Resolution date:** 2024-04-30T01:48:01.133-0700
- **Affects versions:** 1.16.3; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 20w51a; 21w03a; 1.16.5; 21w06a; 21w07a; 21w08b; 21w15a; 21w16a; 1.17.1; 1.18.2; 22w18a; 1.19.1; 1.19.4; 23w14a; 1.20.1; 1.20.4
- **Fix versions:** 24w18a
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-200899.mp4; MC-200899.png

## Description

The Bug:
Players don't receive thorns damage when attacking entities wearing thorns armor with indirect sweeping attacks.
Steps to Reproduce:
- Place down a command block and input the command provided below into it.

```
/summon minecraft:zombie ~ ~1 ~ {ArmorItems:[{id:"minecraft:diamond_boots",tag:{Enchantments:[{id:"minecraft:thorns",lvl:3}]},Count:1b},{id:"minecraft:diamond_leggings",tag:{Enchantments:[{id:"minecraft:thorns",lvl:3}]},Count:1b},{id:"minecraft:diamond_chestplate",tag:{Enchantments:[{id:"minecraft:thorns",lvl:3}]},Count:1b},{id:"minecraft:diamond_helmet",tag:{Enchantments:[{id:"minecraft:thorns",lvl:3}]},Count:1b}]}
```

- Activate the command block, obtain a wooden sword, and summon another zombie by using the command provided below.

```
/summon minecraft:zombie ~ ~ ~ {ArmorItems:[{},{},{},{id:"minecraft:iron_helmet",Count:1b}]}
```

- Switch to survival mode and wait for both of the zombies to begin approaching you.

- Using a sweeping attacking, attack the zombie with the iron helmet so that the zombie with the thorns armor is also damaged as well.

- Do this multiple times and observe if you receive thorns damage.

- Take note as to whether or not players receive thorns damage when attacking entities wearing thorns armor with indirect sweeping attacks.

Observed Behavior:
Players don't receive thorns damage.
Expected Behavior:
Players would receive thorns damage.

## Comments (12)

### Comment 1: migrated (2020-09-23T16:49:06.714-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2020-09-23T18:02:56.731-0700)

Hey there, I can confirm

### Comment 3: Avoma (2021-01-17T08:23:28.105-0800)

Can confirm in 20w51a.

### Comment 4: Avoma (2021-01-29T07:08:33.208-0800)

Can confirm in 21w03a.

### Comment 5: migrated (2021-02-16T12:18:13.983-0800)

Affects 21w06a

### Comment 6: Avoma (2021-02-20T11:26:38.398-0800)

Can confirm in 21w07a.

### Comment 7: Avoma (2021-02-28T06:10:21.214-0800)

Can confirm in 21w08b. Video attached.

### Comment 8: Avoma (2021-04-16T05:11:08.608-0700)

Can confirm in 21w15a.

### Comment 9: Avoma (2021-04-24T03:11:52.263-0700)

Can confirm in 21w16a.

### Comment 10: migrated (2021-08-25T10:34:44.644-0700)

Confirmed in 1.17.1.

### Comment 11: Avoma (2022-05-07T09:27:48.115-0700)

Can confirm in 1.18.2 and 22w18a.

### Comment 12: Avoma (2022-08-03T05:27:52.070-0700)

Can confirm in 1.19.1.

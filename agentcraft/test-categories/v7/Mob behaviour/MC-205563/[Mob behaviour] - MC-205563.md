# MC-205563: Endermen holding powder snow drop a powder snow bucket when killed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-205563](https://bugs.mojang.com/browse/MC-205563)

## Report details

- **Mojira categories:** Mob behaviour
- **Project:** MC
- **Issue key:** MC-205563
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-11-13T15:20:56.892-0800
- **Updated:** 2025-04-30T06:17:12.076-0700
- **Resolution date:** 2022-11-16T12:01:16.733-0800
- **Affects versions:** 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w14a; 21w15a; 21w16a; 21w17a; 1.17 Pre-release 1; 1.17; 1.17.1; 21w39a; 1.18; 1.18.1; 1.18.2; 22w19a; 1.19; 1.19.1; 1.19.2
- **Fix versions:** 22w46a
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2021-04-09_13.49.00.png; MC-205563.mp4

## Description

The bug
Upon killing an enderman holding a block of powder snow (minecraft:powder_snow), the enderman drops a powder snow bucket (as well as ender pearls occasionally, as normal). The expected behaviour is for the enderman to only drop ender pearls, because the actual block of powder snow does not include the bucket.
Removing the powder snow bucket drop would make this consistent with other held blocks like water and lava. When an enderman is killed holding one of these blocks, the bucket is not dropped.
If endermen can pick up powder snow in later snapshots, this would be a way to duplicate buckets. Currently, however, this is only accessible through commands.
How to reproduce
- Obtain an enderman holding powder snow by running the command:

```
/summon minecraft:enderman ~ ~ ~ {NoAI:1b,carriedBlockState:{Name:"minecraft:powder_snow"}}
```

- Kill the enderman
   Notice how a powder snow bucket is dropped

## Comments (20)

### Comment 1: migrated (2020-11-13T15:20:56.892-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2020-11-13T15:23:11.577-0800)

Can confirm.

### Comment 3: migrated (2020-11-14T08:08:29.608-0800)

Relates to MC-205077

### Comment 4: migrated (2020-12-02T05:37:05.857-0800)

It will remove powder snow block due that command with carry 'block' state, that changes water, lava, and powder snow, even portal and unobtainable items that enderman carries when used command block or /commands

### Comment 5: Avoma (2021-02-04T08:58:43.568-0800)

Can confirm in 21w05a.

### Comment 6: Avoma (2021-02-21T10:30:25.241-0800)

Can confirm in 21w07a.

### Comment 7: Avoma (2021-02-27T07:15:31.787-0800)

Can confirm in 21w08b. Video attached.

### Comment 8: Avoma (2021-04-10T11:54:01.688-0700)

Can confirm in 21w14a.

### Comment 9: Avoma (2021-04-16T05:43:49.453-0700)

Can confirm in 21w15a.

### Comment 10: Avoma (2021-04-22T10:57:22.893-0700)

Can confirm in 21w16a.

### Comment 11: Avoma (2021-05-01T04:06:12.038-0700)

Can confirm in 21w17a.

### Comment 12: migrated (2021-06-02T11:58:59.226-0700)

Can confirm for 1.17 pre-release 4

### Comment 13: Avoma (2021-06-10T06:35:39.263-0700)

Can confirm in 1.17.

### Comment 14: Avoma (2021-07-08T02:03:34.809-0700)

Can confirm in 1.17.1.

### Comment 15: Avoma (2021-12-06T03:32:40.319-0800)

Can confirm in 1.18.

### Comment 16: MMK21 (2021-12-14T10:35:42.689-0800)

Affects 1.18.1

### Comment 17: Avoma (2022-03-10T08:28:39.714-0800)

Can confirm in 1.18.2.

### Comment 18: Avoma (2022-06-25T05:27:42.027-0700)

Can confirm in 1.19.

### Comment 19: Avoma (2022-08-25T09:03:30.003-0700)

Can confirm in 1.19.2.

### Comment 20: CraftBlade240 (2022-11-16T12:01:16.733-0800)

wouldnt this just be free buckets if you place the snow

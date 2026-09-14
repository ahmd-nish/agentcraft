# MC-236783: Parity Issue: Ravagers still attack baby villagers in Java Edition

**Mojira URL:** [https://bugs.mojang.com/browse/MC-236783](https://bugs.mojang.com/browse/MC-236783)

## Report details

- **Mojira categories:** Mob behaviour; Parity
- **Project:** MC
- **Issue key:** MC-236783
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2021-09-16T01:12:53.237-0700
- **Updated:** 2025-04-29T21:02:28.058-0700
- **Resolution date:** 2021-11-24T06:11:49.135-0800
- **Affects versions:** 21w37a; 1.18 Pre-release 6
- **Fix versions:** 1.18 Pre-release 8
- **Labels:** ravager; vanilla-parity
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2021-09-16_16.07.59.png; MC-236783.mp4; MC-236783.png

## Description

In new snapshots illagers will ignore baby villagers like BE, but ravagers still attack baby villagers.
Steps to Reproduce:
- Summon a ravager and a baby villager.

```
/summon minecraft:ravager ~ ~ ~
 /summon minecraft:villager ~ ~ ~ {Age:-25000}
```

- Wait a couple of seconds.
 →  Notice how ravagers are able to attack baby villagers.

Expected Behavior:
The expected behavior would be that ravagers are not able to attack baby villagers, just like how they can't in Bedrock Edition.*

## Comments (16)

### Comment 1: migrated (2021-09-16T01:12:53.237-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: anthony cicinelli (2021-09-16T06:11:50.943-0700)

That was added in Bedrock before the buzzy bees update therefor this isn't valid parity issue

### Comment 3: ampolive (2021-09-16T06:15:12.481-0700)

This might be considered a valid parity issue as it was added in Java for parity after the Buzzy Bees Update.

### Comment 4: anthony cicinelli (2021-09-16T06:19:55.077-0700)

no still wouldn't be valid please see what is considered valid parity here

### Comment 5: migrated (2021-09-16T06:23:21.327-0700)

That illagers no longer attack in java is new, a post-buzzy bees change; the feature has as such been changed since that update, so it should be valid.

### Comment 6: ampolive (2021-09-16T06:25:06.668-0700)

It fulfills all the criteria cited in the parity issue guidelines:
- The feature affected by the parity issue is present in both Bedrock Edition and Java Edition in the latest release or development version.

- The feature behaves differently in one edition than in the other.

- The parity issue was introduced in Buzzy Bees (Bedrock Edition 1.14 / Java Edition 1.15) or later and was not present before.

### Comment 7: ampolive (2021-09-16T06:25:33.092-0700)

Can confirm.

### Comment 8: anthony cicinelli (2021-09-16T06:27:10.310-0700)

"The parity issue was introduced in Buzzy Bees (Bedrock Edition 1.14 / Java Edition 1.15) or later and was not present before." Was present before the buzzy bees.

### Comment 9: Sniper1.1 (2021-09-16T06:29:20.319-0700)

Respectfully, this should be valid. The most recent 1.18 snapshots (post 1.15) made illagers not attack children and is a parity change. They likely forgot to change ravagers too.

### Comment 10: ampolive (2021-09-16T06:31:42.852-0700)

I think that this is a matter of interpretation. Now that I think about it, technically  is correct that the parity issue existed before the Buzzy Bees update, but the change made in 21w37a created a new parity issue, and this one should be valid? I don't know, this seems confusing.

### Comment 11: Sniper1.1 (2021-09-16T06:40:38.375-0700)

Yeah, they may be technically right, but it feels more like the devs accidentally forgot to change this than a deliberate parity difference. This feels like something someone from Mojang (a dev) should have the final say for. If they say they intended it, then ok, it’s a feature request. If they say they just forgot this, then it’s a bug that they can probably easily patch.

### Comment 12: migrated (2021-09-16T08:59:05.662-0700)

There are multiple issues related to illagers no longer attacking baby villagers.
For example raids are no longer win-able by illagers if there are any baby villagers present in the village.
And "Johnny" vindicators no longer attacks baby villagers.
It seems the change was done a bit too hastily and someone forgot to look at related mechanics.
(I also wonder why this change was done now, since it has nothting to do with 1.18 as a whole)

### Comment 13: Avoma (2021-09-22T11:24:28.563-0700)

I can also confirm this behavior. Here are some extra details regarding this issue.
The Bug:
Parity issue: Ravagers are able to attack baby villagers.
Steps to Reproduce:
- Summon a ravager and a baby villager.

```/summon minecraft:ravager ~ ~ ~
/summon minecraft:villager ~ ~ ~ {Age:-25000}```
- Wait a couple of seconds.

- →  Notice how ravagers are able to attack baby villagers.

Expected Behavior:
The expected behavior would be that ravagers are not able to attack baby villagers, just like how they can't in Bedrock Edition.

### Comment 14: migrated (2021-10-22T16:45:54.179-0700)

Add 3 labels:
ravager
baby-villager
vanilla-parity

### Comment 15: Avoma (2021-11-23T07:16:45.143-0800)

Can confirm in 1.18 Pre-release 6.

### Comment 16: Sniper1.1 (2021-11-23T08:35:31.630-0800)

Just make sure that if this gets fixed, the bug making it impossible for pillagers to win a raid if babies are present also gets fixed as currently ravagers are the only way for a pillager victory.

https://bugs.mojang.com/browse/MC-236645

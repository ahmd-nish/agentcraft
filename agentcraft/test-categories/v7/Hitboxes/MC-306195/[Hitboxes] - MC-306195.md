# MC-306195: Camel husks with the "Age" tag set below -24000 use their removed baby variant's hitbox size and animation speed

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306195](https://bugs.mojang.com/browse/MC-306195)

## Report details

- **Mojira categories:** Hitboxes; Mob behaviour
- **Project:** MC
- **Issue key:** MC-306195
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2026-02-03T13:05:27.523-0800
- **Updated:** 2026-02-10T01:19:16.052-0800
- **Resolution date:** 2026-02-10T01:19:15.950-0800
- **Affects versions:** 26.1 Snapshot 6
- **Fix versions:** 26.1 Snapshot 7
- **Area:** Expansion A
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2026-02-03_16.34.16-20260203-213416.png; 2026-02-03_21.56.26.png
- **Issue links:** Duplicate:inward:MC-306267:Hardcoded forced adult behavior is inconsistent between Wandering Traders and Camel Husks

## Description

Camel Husk can have a small hitbox, despite its baby variant being removed.
To reproduce:
- Write

```
/summon minecraft:camel_husk ~ ~ ~ {NoAI:1,Age:-24000}
/summon minecraft:camel_husk ~ ~ ~ {NoAI:1}
```

- Compare hitboxes

Expected results:
- Camel Husk have a constant hitbox.

Observed results:
- Camel Husk with a 'young' age has a small hitbox.

## Comments (6)

### Comment 1: Automation for Jira (2026-02-03T13:05:38.954-0800)

Thank you for helping us improve Minecraft! We saved your files:

### Comment 2: kyleisNOTmyname (2026-02-03T13:34:51.752-0800)

Can confirm as of 26.1-snapshot-6

### Comment 3: TheCJBrine (2026-02-03T14:59:39.385-0800)

It also still moves and behaves like a baby would (faster animation speed + follows adult).

### Comment 4: Custom Name (2026-02-04T02:34:13.979-0800)

Its still a baby variant, just with the appearance of a adult camel husk. Pretty sure this is not intentional.

### Comment 5: Custom Name (2026-02-05T08:01:28.553-0800)

Important to note that the baby variant also won’t drop anything when killed, like all other baby mobs, despite being supposed to be removed.

### Comment 6: Creeper Juice (2026-02-06T10:06:43.727-0800)

It’d probably make the most sense to simply remove the Age tag entirely since it’s not intended to be used for the Camel Husk anymore.

# MC-273281: "projectile_spawned" Enchantment Component runs predicates and effects on projectiles before all of their data has been assigned

**Mojira URL:** [https://bugs.mojang.com/browse/MC-273281](https://bugs.mojang.com/browse/MC-273281)

## Report details

- **Mojira categories:** Data Packs; Enchantments; Projectiles
- **Project:** MC
- **Issue key:** MC-273281
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-06-12T10:03:11.446-0700
- **Updated:** 2025-04-16T13:01:55.072-0700
- **Resolution date:** 2024-07-08T03:00:51.446-0700
- **Affects versions:** 1.21; 1.21 Release Candidate 1
- **Fix versions:** 24w33a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** projectile_spawned_bug_example_latest.zip
- **Issue links:** Cloners:outward:MC-271562:"projectile_spawned" Enchantment component triggers the enchantment effects BEFORE setting the projectile's default NBT

## Description

If you detect a projectile with the "projectile_spawned" enchantment component, you won't be able to detect certain properties of that projectile, because those properties are set by the game immediately AFTER the enchantment effect is called. I've provided an example datapack which highlights this bug.
The datapack provides an enchantment for Bows which detects when you fire an arrow, and tries to determine whether that arrow is a crit arrow. If it is, a message will appear saying it is a crit arrow, and if not, another message will appear saying it's not. Finally, the function sets the arrow's NBT so it is no longer a crit arrow.
Steps to reproduce:
- Install the provided datapack.

- Enchant a bow with "test:arrow_crit_detection":

```
/enchant @s test:arrow_crit_detection
```

- Shoot the bow before fully charging it.

- Shoot the bow after fully charging it.

Observed result:
The message I am NOT a crit arrow appears twice. The first arrow does not display critical charge particles, while the second arrow does display critical charge particles.
Expected result:
The message I am NOT a crit arrow appears once and after it I AM a crit arrow appears once. Both arrows do not display critical charge particles.
This is a re-report of MC-271562, which says it was fixed, but the issue is not fixed. I requested for that report to be reopened, and was told to make a new report.

## Comments (2)

### Comment 1: migrated (2024-06-12T10:03:11.446-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: Jarl-Penguin (2024-06-12T10:24:44.901-0700)

An updated datapack for 1.21-rc1 (with functions -> function) has been attached.

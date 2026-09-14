# MC-178383: Horses, donkeys, mules and llamas spawned from spawn eggs or /summon command have 53 health

**Mojira URL:** [https://bugs.mojang.com/browse/MC-178383](https://bugs.mojang.com/browse/MC-178383)

## Report details

- **Mojira categories:** Mob spawning
- **Project:** MC
- **Issue key:** MC-178383
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-04-12T06:24:22.253-0700
- **Updated:** 2026-04-15T11:14:15.260-0700
- **Resolution date:** 2024-05-20T12:14:50.609-0700
- **Affects versions:** 20w15a; 20w20b; 1.16.1; 20w30a; 1.16.2; 1.16.4; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w08a; 21w08b; 21w15a; 1.17; 1.17.1; 1.18 Pre-release 1; 1.18 Pre-release 8; 1.18.1; 22w03a; 1.18.2; 22w19a; 1.19; 1.19.2; 22w42a; 1.20.2; 1.20.4; 23w51b; 24w07a; 24w14a
- **Fix versions:** 24w19a
- **Labels:** data; horse; summon
- **Watchers:** 2
- **Attachments:** 4
- **Attachment filenames:** Crazy Total Hearts For a Mule.png; Crazy Total Hearts For a Mule 2.png; MC-178383.png; MC-178383-1.png
- **Issue links:** Relates:outward:MC-103250:Horse / Donkey / Mule health points is 26 ♥ by command to spawn | Relates:inward:MC-195931:Incorrect amount of damage heart particles shown when hitting some entities for the first time | Duplicate:inward:MC-203414:Summoned horses, donkeys, llamas and mules don't take damage on first hit | Duplicate:inward:MC-216959:Horses/Donkeys/Mules from spawn eggs spawn with 53 health points, but after hitting they get a normal amount of health points | Duplicate:inward:MC-232846:Summoned Minecraft Horses Variants Wrong Health | Problem/Incident:outward:MC-195931:Incorrect amount of damage heart particles shown when hitting some entities for the first time

## Description

The Bug
AbstractHorse entities can have up to 53 health points.
Expected Behavior
Any AbstractHorse creature should have a maximum of 25 health points.
How to reproduce
- Use a spawn egg to spawn a horse

- Inspect the horse's health:

```
/data get entity @e[type=horse,limit=1,sort=nearest] Health
```
→  The horse has 53 health

Code Analysis
The questionable value can be found in the AbstractHorse class:

```
public static AttributeSupplier.Builder createBaseHorseAttributes() {
    return Mob.createMobAttributes().add(Attributes.JUMP_STRENGTH).add(Attributes.MAX_HEALTH, 53.0D).add(Attributes.MOVEMENT_SPEED, 0.22499999403953552D);
}
```

## Comments (22)

### Comment 1: migrated (2020-04-12T06:24:22.253-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: j_p_smith (2020-05-18T21:52:46.516-0700)

Confirmed in 20w20b. All horses, donkeys and mules spawned using /summon have 53 health.

### Comment 3: j_p_smith (2020-05-25T02:55:18.928-0700)

Duplicate of MC-103250.

### Comment 4: j_p_smith (2020-07-21T03:36:25.869-0700)

This should probably be reopened, as it actually affects horses, donkeys and mules spawned using spawn eggs. This was not the case in 1.15.2 or earlier.

### Comment 5: Avoma (2020-12-03T10:46:29.070-0800)

Can confirm in 20w49a.

### Comment 6: Avoma (2021-01-17T10:12:00.192-0800)

Can confirm in 20w51a.

### Comment 7: Avoma (2021-02-01T00:35:39.964-0800)

Can confirm in 21w03a.

### Comment 8: Avoma (2021-03-01T01:18:13.228-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 9: Avoma (2021-04-18T10:25:42.248-0700)

Can confirm in 21w15a.

### Comment 10: Avoma (2021-06-13T10:02:24.919-0700)

Can confirm in 1.17.

### Comment 11: migrated (2021-07-22T20:53:02.288-0700)

Occurs in both 1.16.5 and 1.17.1.

Not just horses.  it's anything based on the abstract horse class.
I.e.  That means horses, donkeys, mules, llamas... and anything else I might have forgotten.

### Comment 12: Avoma (2021-11-12T08:08:40.584-0800)

I'd like to request ownership of this ticket since the current reporter has been inactive since April of 2020. I'm willing to keep this report updated and will continue to provide all of the necessary information.

### Comment 13: TkainMinecraft (2021-11-12T14:30:02.319-0800)

Found the code issue that gives way to this bug; there's this method below in the (Official MojMap) AbstractHorse class, and...

```public static AttributeSupplier.Builder createBaseHorseAttributes() {
    return Mob.createMobAttributes().add(Attributes.JUMP_STRENGTH).add(Attributes.MAX_HEALTH, 53.0D).add(Attributes.MOVEMENT_SPEED, 0.22499999403953552D);
}```
...well, I'll let you guys find the odd number out. (Hint: It's not the second one.)

### Comment 14: ampolive (2021-11-13T09:25:12.445-0800)

Can confirm in 1.18 Pre-release 1.

### Comment 15: Avoma (2022-05-16T02:33:43.390-0700)

Can confirm in 1.18.2 and 22w19a.

### Comment 16: Avoma (2022-07-26T08:21:29.904-0700)

Can confirm in 1.19.

### Comment 17: Avoma (2022-09-06T10:46:41.574-0700)

Can confirm in 1.19.2.

### Comment 18: [Mod] Jingy (2023-10-04T20:44:59.576-0700)

Can confirm in 1.20.2

### Comment 19: [Mod] Jingy (2023-11-20T20:11:24.649-0800)

Requesting ownership of this issue as the original poster has not been active in the last 3 years.

### Comment 20: Wilf233 (2024-01-12T18:46:15.121-0800)

Naturally spawned horse is sometimes 53 in health, sometimes not.

### Comment 21: Wilf233 (2024-01-12T19:10:54.280-0800)

If you exit the game and reenter, the health returns normal.

### Comment 22: Wilf233 (2024-01-12T19:15:05.150-0800)

The root of this bug is that health value is not initiated in NBT when spawned. Instead, only maximum health value is initiated.
To fix this bug, just to initiate both health value and maximum health value when spawned.

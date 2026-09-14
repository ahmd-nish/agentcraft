# MC-302663: Any form of attacking non-player entities always produces the “weak attack” sound instead of the appropriate sound

**Mojira URL:** [https://bugs.mojang.com/browse/MC-302663](https://bugs.mojang.com/browse/MC-302663)

## Report details

- **Mojira categories:** Combat; Sound
- **Project:** MC
- **Issue key:** MC-302663
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-10-09T07:39:20.939-0700
- **Updated:** 2025-11-04T05:31:09.802-0800
- **Resolution date:** 2025-11-03T04:38:18.083-0800
- **Affects versions:** 25w41a; 25w42a; 25w43a; 25w44a
- **Fix versions:** 25w45a
- **Area:** Expansion A
- **Votes:** 14
- **Watchers:** 3
- **Attachments:** 3
- **Attachment filenames:** 2025-10-21 11.mp4; 2025-10-29 13-50-54.mp4; MC-302663.png
- **Issue links:** Duplicate:inward:MC-302720:All attacks play the "Weak Attack" sound effect  | Duplicate:inward:MC-302723:Critical hit sound removed | Duplicate:inward:MC-302744:crit sound not playing in the newest snapshot (mounts of mayhem) | Duplicate:inward:MC-302749:Attacking sounds are broken | Duplicate:inward:MC-302765:Incorrect critical hit sound when attacking mobs | Duplicate:inward:MC-302766:Every non-Spear melee attack plays the "Weak Attack" sound, regardless of the attack cooldown | Duplicate:inward:MC-302762:Crit Sounds | Duplicate:inward:MC-302771:The sounds when hitting an enemy are broken and each attack produces the same weak hit sound effect | Duplicate:inward:MC-302831:Sounds of strong attacks, sweepeing attacks and critical attacks no longer play. | Duplicate:inward:MC-302731:Critical Attacks Don't Work | Duplicate:inward:MC-302914:There are now hit sounds besides weak attack playing | Duplicate:inward:MC-302956:Wrong sound event is played while making a critical attack | Duplicate:inward:MC-302928:mobs do not play critical hit sound | Duplicate:inward:MC-302965:Sounds Register Critical, Strong and Knockback Attack for a Weak attack  | Duplicate:inward:MC-302976:Critical Hit Sound doesn't play when it occours. | Duplicate:inward:MC-302977:Attacking bug | Duplicate:inward:MC-303270:The strong attack sound doesnt play anymore | Duplicate:inward:MC-303158:sweep hit/critical hit sound missing | Duplicate:inward:MC-303339:Every Attack except for Knockback Attacks make the Weak Attack sound. | Duplicate:inward:MC-303300:Attacking Audio Incorrect | Duplicate:inward:MC-303438:All attacks play the "weak attack" sfx | Duplicate:inward:MC-303495:I don't hear the crit and hit sound effect | Duplicate:inward:MC-303712:Sweep attack, Critical Hit, and Normal Attack sounds aren't playing at all | Duplicate:inward:MC-303787:Attack sounds missing or playing incorrectly... | Duplicate:inward:MC-303867:Damage type sound effect missing | Duplicate:inward:MC-303878:When I attack after the reload time for attacking completely fills up, it deals a weak attack, when it should be a strong attack. | Duplicate:inward:MC-303939:Crit Sound Does not play since the Mounts of Mayhem Snapshots

## Description

The Bug:
Any form of attacking non-player entities always produces the “weak attack” sound instead of the appropriate sound.
Steps to Reproduce:
- Summon a copper golem.

- Critically attack the copper golem and observe if a crit sound was played.

Observed Behavior:
Any form of attacking non-player entities always produces the “weak attack”.
Expected Behavior:
Attacking non-player entities should play the appropriate attack sound.

## Comments (6)

### Comment 1: Avoma (2025-10-09T10:21:35.486-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: SeaOfPixels (2025-10-14T20:06:36.660-0700)

In 25w42a. Note that this issue does not happen for attacking boats for some reason.

### Comment 3: Ellivers (2025-10-21T08:06:30.692-0700)

Can reproduce in 25w43a. The “knockback attack“ sound still plays as normal though.

### Comment 4: N8GO (2025-10-21T11:58:53.912-0700)

Just to show more then a screenshot

### Comment 5: Bliubbeain (2025-10-30T09:22:44.295-0700)

in 25w44a

### Comment 6: BastienLeft (2025-10-30T18:53:29.105-0700)

Same here

# MC-266441: Multiple trial chamber templates have missing or incorrect blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-266441](https://bugs.mojang.com/browse/MC-266441)

## Report details

- **Mojira categories:** Structures
- **Project:** MC
- **Issue key:** MC-266441
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-11-08T07:56:32.941-0800
- **Updated:** 2025-05-29T09:08:50.300-0700
- **Resolution date:** 2024-08-16T18:40:50.485-0700
- **Affects versions:** 23w45a; 23w46a; 1.20.3 Pre-Release 1; 1.20.3 Pre-Release 2; 1.20.4 Release Candidate 1; 1.20.4; 24w03b; 24w11a; 24w12a; 24w13a; 24w14a; 1.20.5 Pre-Release 1; 24w21b; 1.21
- **Fix versions:** 24w33a
- **Area:** Expansion B
- **Labels:** trial_chamber
- **Votes:** 1
- **Watchers:** 2
- **Attachments:** 30
- **Attachment filenames:** 2023-11-08_10.55.08.png; 2023-11-08_11.32.43.png; 2023-11-08_11.34.13.png; 2023-11-08_11.39.04.png; 2023-11-08_11.52.20.png; 2023-11-08_12.02.31.png; 2023-11-08_12.06.24.png; 2023-11-08_12.07.16.png; 2023-11-10_10.19.53.png; 2023-11-11_10.55.54.png; 2023-11-11_10.56.22.png; 2023-11-11_15.30.45.png; 2024-04-10_23.17.51.png; 2024-04-10_23.18.09.png; 2024-04-10_23.18.21.png; 3 oxidized copper blocks on right.png; 3 tuff bricks on ceiling entrance_3.png; 6 tuff bricks on ceiling entrance_3.png; copper is not waxed.png; cut copper is not waxed in chamber_1 and chamber_2.png; ld2.png; missing block of copper entrance_3.png; missing block of copper in corner.png; missing cut copper in corner.png; missing oxidized copper on floor.png; no oxidized cut copper on floor on left.png; oxidized copper instead of oxidized cut copper in corner.png; oxidized copper instead of oxidized cut copper next to ice.png; screenshot-1.png; tuff brick ceiling.png
- **Issue links:** Relates:outward:MC-275402:Multiple templates in trial chambers still have missing/incorrect blocks (after 24w33a) | Relates:inward:MC-270536:Trial chamber powder snow rooms have missing powder snow near the ominous vault | Relates:inward:MC-272122:Trial chambers missing ladders | Duplicate:inward:MC-269500:Missing and random blocks in new Trial Chambers rooms | Duplicate:inward:MC-266992:Missing block in the new Trial Chambers structure. No caves or anything else nearby making it disappear. | Relates:inward:MCPE-176952:Multiple trial chamber structures have missing or incorrect blocks

## Description

The bug
Several trial chamber templates have missing or incorrect blocks.
Chambers
- assembly
- One of the blocks in left_staircase_2 and right_staircase_2 is tuff bricks instead of chiseled tuff bricks.

- chamber_2 generates without six copper bulbs (top and bottom) on three of its pillars on one corner.

- chamber_4 has one of its pillars missing a tuff bricks block.

- chamber_8 has an incorrectly rotated trapdoor (MC-270614).

- eruption
- One of the pillars is missing two waxed copper blocks on the top.

- One of the pillars is missing one waxed copper block on the top.

- A block of tuff bricks is misplaced near the top of two of its pillars.

- A block on the copper floor of quadrant_1 is incorrect, with waxed oxidized cut copper instead of waxed oxidized copper.

- slanted has several tuff bricks instead of polished tuff on the roof between pillars near the center.

Corridors
- end_1
- There is a misplaced waxed copper block instead of tuff bricks.

- One of the sides is missing middle and lower waxed copper bulbs, making the room asymmetrical.

- end_2
- There are four apparently misplaced tuff bricks on the roof.

- straight_6 has inconsistent copper blocks on the corner of staircases.

Hallways
- corner_staircase has a waxed copper block instead of a tuff bricks block in one corner.

- left_corner is still missing several blocks.

- right_corner is still missing chiseled tuff bricks, and does not replace certain blocks with air.

- straight_staircase has chiseled tuff bricks instead of tuff bricks behind one of the waxed oxidized cut copper stairs.

- upper_hallway_connector
- There is a waxed copper block on the top floor instead of waxed oxidized copper.

- The placement of the top copper bulb is offset one block compared to the bottom one, unlike other templates.

Intersections
- intersection_3 has nine tuff bricks on the roof near the top of its pillars instead of polished tuff.

## Comments (14)

### Comment 1: migrated (2023-11-08T07:56:32.941-0800)

This comment contained multiple image attachments (30), please login to view the attachments.

### Comment 2: migrated (2023-11-10T10:24:01.926-0800)

Also in intersection 2, the top of one of the columns has a misplaced tuff bricks, which should instead be chiseled tuff bricks. I have attached a screenshot showing this.

### Comment 3: migrated (2023-11-17T11:10:22.726-0800)

minecraft:trial_chambers/corridor/straight_1-5 all have a jigsaw block with an unexistant target minecraft:addon_upper from minecraft:trial_chambers/chamber/addon pool. Possibly it should target minecraft:addon_upper on minecraft:trial_chambers/corridors/addon/middle_upper pool.
minecraft:trial_chambers/chamber/chamber_2 contains a jigsaw block with no target.

### Comment 4: QWERTY 52 38 (2023-11-21T07:53:40.242-0800)

Can confirm in 1.20.3-pre1.

### Comment 5: QWERTY 52 38 (2023-11-22T08:05:31.791-0800)

Can confirm in 1.20.3-pre2.

### Comment 6: QWERTY 52 38 (2023-12-06T06:45:59.810-0800)

Can confirm in 1.20.3

### Comment 7: QWERTY 52 38 (2024-01-18T08:14:06.069-0800)

Still in 1.20.4 and 23w51b

### Comment 8: Magicwaterz (2024-04-10T08:23:45.540-0700)

The New Dispenser traps are also generating behind walls. This is in Pre-release 1 for 1.20.5

### Comment 9: ampolive (2024-04-10T17:30:52.374-0700)

That could be a separate issue.

### Comment 10: DrHmom_3k (2024-04-14T06:18:10.576-0700)

There is also a problem with misplaced ladders in assembly and slanted chambers - they are placed in such a way that it is impossible to climb them without placing blocks by the player.

### Comment 11: sandro38 (2024-05-22T05:30:54.474-0700)

entrance_1:
- one of the trapdoors in unwaxed

- has a missing cut copper block around the tree

entrance_2:
- has a tuff brick ceiling instead of polished tuff (inconsistent with all other parts of the structure)

- has a missing cut copper block around the tree

- has an oxidized copper block instead of normal one in the corner of the lower area

entrance_3:
- has tuff bricks instead of polished tuff in some parts of the ceiling

- walls don't have chiseled tuff bricks past the first layer

- has a missing copper block near the lower vault

unlike entrance_1, both entrance_2 and entrace_3 don't have cut copper on floor between wall pillars and don't have chiseled tuff above copper bulbs.
Assembly:
- has oxidized copper instead of regular on one of the sides of the central vault area

chamber_8
- has a misplaced oxidized copper block on the second floor

grand_staircase_3 has unwaxed copper blocks.
two of the entrances in chamber_1 and chamber_2 have unwaxed oxidized cut copper

### Comment 12: Moesh (2024-05-29T06:10:16.749-0700)

Things like missing ladders or situations which looks like we obviously want the player to place a block to continue should not be included in this bug report. I'm trying to sort through what is and isn't valid. Some of these are WAI.

### Comment 13: Moesh (2024-05-29T06:10:41.855-0700)

It would certainly help if the screenshots references the area or structure name, but I recognize most of these.

### Comment 14: Moesh (2024-06-05T00:47:18.001-0700)

Many to all of these will be fixed in an upcoming release. Please do not reopen this bug when it is closed, and instead open a new report. Thanks!

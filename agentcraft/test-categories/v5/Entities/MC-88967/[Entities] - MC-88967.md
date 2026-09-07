# MC-88967: Most NBT tags are not kept when a mob converts to another mob

**Mojira URL:** [https://bugs.mojang.com/browse/MC-88967](https://bugs.mojang.com/browse/MC-88967)

## Report details

- **Mojira categories:** Entities
- **Project:** MC
- **Issue key:** MC-88967
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2015-09-17T17:38:15.199-0700
- **Updated:** 2025-10-30T07:29:59.352-0700
- **Resolution date:** 2024-09-04T15:57:49.750-0700
- **Affects versions:** Minecraft 15w38b; Minecraft 15w44b; Minecraft 1.9 Pre-Release 2; Minecraft 16w42a; Minecraft 1.12; Minecraft 1.12.2; Minecraft 18w02a; Minecraft 18w11a; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w02a; Minecraft 19w12b; Minecraft 19w13b; 1.14.4; 19w34a; 19w35a; 19w39a; 1.15.1; 1.15.2; 20w08a; 20w09a; 20w10a; 20w11a; 20w12a; 20w15a; 20w17a; 20w18a; 20w19a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 5; 1.16.1; 20w27a; 20w30a; 1.16.2; 1.16.3; 1.16.4; 20w46a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w13a; 1.17; 1.17.1; 1.18; 1.18.1; 1.18.2; 1.19 Pre-release 1; 1.19; 1.19.1 Release Candidate 2; 1.19.2; 1.19.3; 1.20.1; 1.20.2; 23w42a; 23w43b; 1.20.3 Pre-Release 1; 1.20.4; 23w51b; 24w13a; 1.21 Pre-Release 2
- **Fix versions:** 24w36a
- **Area:** Gameplay
- **Labels:** conversion; lightning; lightning_bolt; mob; nbt; scoreboard; scoreboard-tag
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2019-01-10_17.41.48.png; 2019-01-10_17.42.27.png; 2019-01-10_17.43.39.png; 2019-01-10_17.44.13.png; 2019-01-10_17.45.35.png; 2019-01-10_17.46.57.png; 2019-01-10_17.47.25.png; MC-88967.mp4
- **Issue links:** Relates:outward:MC-261666:Armor given to Villagers is lost when they convert to Zombie Villagers | Relates:inward:MC-149679:Zombie Villagers cured into regular villagers lose numeric values on trades | Relates:inward:MC-270842:Scores are not kept when a mob converts to another mob | Relates:inward:MC-276295:Zombies always kill villagers | Duplicate:inward:MC-265679:Baby slimes/magma cubes do not inherit parent's velocity | Duplicate:inward:MC-267526:Converted mobs lose attributes | Duplicate:inward:MC-264717:Villagers lose their heads when zombified and cured. | Duplicate:inward:MC-174843:Mooshrooms lose velocity and rotation when sheared | Duplicate:inward:MC-160146:zombified villagers despawn even when named | Duplicate:inward:MC-221538:Mooshroom looses EntityTags | Duplicate:inward:MC-220614:Issue | Relates:inward:MC-136776:Some NBT tags are not kept when fish or axolotl mobs are caught in water buckets | Duplicate:inward:MC-210921:Zombies turned into drown have reset health | Relates:inward:MC-159300:Villagers that have been infected by a zombie can despawn, even if they have been traded with | Duplicate:inward:MC-199995:Entities gain gravity when they convert | Duplicate:inward:MC-193389:Piglin brute loses health after converting to zombified piglin | Duplicate:inward:MC-193069:Zombified piglin doesn't keep Piglin Brute statistics | Duplicate:inward:MC-193072:Piglin bruts not keep value of health in 45 HP after zombification | Duplicate:inward:MC-192485:Mobs that turn into other mobs dont keep attributes | Duplicate:inward:MC-193068:Left handed Piglin Brutes turn to right handed pigmen | Duplicate:inward:MC-189750:When NoAI mooshrooms are sheared, they lose their NoAI tag | Relates:inward:MC-183860:Zombie villager converted from villager gets PersistenceRequired depending on whether attacking zombie had it | Duplicate:inward:MC-183724:Zombie Villager Despawning | Duplicate:inward:MC-180471:Piglins and Hoglins lose potion effects after zombification | Duplicate:inward:MC-176388:Zombie villagers despawning | Relates:outward:MC-6773:Renaming a slime or Magma cube, Once it splits it no longer has its custom name. | Duplicate:inward:MC-174190:If you breed mooshroom cows and then shear them to normal cows you can breed them again | Duplicate:inward:MC-103290:Mooshrooms face south after shearing | Duplicate:inward:MC-173037:When A Piglin Is Named Using A Name Tag, It Will Despawn When It Becomes a Zombie Pigman | Duplicate:inward:MC-172677:Piglins transformed into Zombified Piglins do not keep facing the same direction as they previously were | Duplicate:inward:MC-172196:Portal Cooldown Resets when Mobs Transform | Duplicate:inward:MC-170726:Zombie villagers despawning after curing. | Duplicate:inward:MC-170509:Named Villagers lose their PersistenceRequired data value when converted into Zombies | Duplicate:inward:MC-170501:Lost NBT data when converting to and from Villager and Zombie Villager | Duplicate:inward:MC-166749:Villagers, when name tagged and then subsequently are converted into Zombie Villagers retain their name tag but can despawn. | Duplicate:inward:MC-163938:Zombie villagers despawn after cure | Duplicate:inward:MC-162500:Named Villagers converted to Zombie Villagers despawn | Duplicate:inward:MC-160551:Named Villagers converted to Zombie Villagers can despawn | Duplicate:inward:MC-159298:Villagers that have been infected by a zombie can despawn, even if they were named before they were converted | Duplicate:inward:MC-160196:Named Villagers can despawn when converted to Zombie Villagers. | Duplicate:inward:MC-160149:Named Zombie Villagers despawn | Duplicate:inward:MC-160139:Renamed Zombie villagers despawn | Duplicate:inward:MC-142032:Persistence loss of mobs changing into other mobs, thus also despawn | Duplicate:inward:MC-138009:When a zombie turns into a drowned, the drowned faces south | Duplicate:inward:MC-136089:Name Tagged Villager despawns if converted to a Zombie Villager when >128 blocks away | Duplicate:inward:MC-134924:nametaged zombies can despawn after turned in drawn | Duplicate:inward:MC-133997:Dropchances not carrying over with drowned conversion | Duplicate:inward:MC-132613:NBT is removed when zombies/husks convert | Duplicate:inward:MC-132087:Zombies that turn into drowned regain health | Duplicate:inward:MC-129122:Named Zombies become despawnable after turning into drowned. | Duplicate:inward:MC-127307:Zombies lose some properties after converting to a drowned | Duplicate:inward:MC-97752:Converting Villager to Zombie | Duplicate:inward:MC-91898:If you shear the mushroom cow with tag "NoAI", normal cow will be without the tag "NoAI" | Duplicate:inward:MC-248044:Mob conversion rerandomizes the random name of a mob used to target for commands

## Description

The bug
When a mob transforms into another mob (ex. zombie villager → villager, mooshroom → cow), it loses most of its NBT tags. This also affects conversions to the same mob, like slimes and magma cubes splitting.
It is worth noting CustomName and NoAI are preserved (MC-6773 & MC-67437), so other tags are expected to be saved as well.
Examples
The following is a list of tags that aren't transferred between entities.
From
Husk
Zombie
Skeleton
Zombie Villager
Villager
Villager
Pig
Piglin
Piglin Brute
Hoglin
Slime
Magma Cube
Tadpole
Mooshroom
To
Zombie
Drowned
Stray
Villager
Zombie Villager
Witch
Zombified Piglin
Zombified Piglin
Zombified Piglin
Zoglin
Smaller Slime
Smaller Magame Cube
Frog
Cow
AbsorptionAmount

active_effects

Age, IsBaby

N/A
7
7
N/A

N/A

N/A
N/A
N/A

AngrTime, Brain.memories.minecraft:angry_at.ttl
N/A
N/A
N/A
N/A
N/A
N/A
N/A

N/A
N/A
N/A
N/A
N/A
AngryAt, Brain.memories.minecraft:angry_at.value
N/A
N/A
N/A
N/A
N/A
N/A
N/A

N/A
N/A
N/A
N/A
N/A
ArmorItems

8
8
8
8

N/A19
N/A19
8
8
ArmorDropChances

Attributes

CanBreakDoors

N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
CanPickUpLoot

9

CustomName

20
20

CustomNameVisible

DeathLootTable

DeathLootTableSeed

FallFlying

8
8
8
8

N/A19
N/A19
8
8
Fire

N/A5

N/A15
N/A15
N/A15
N/A15

N/A23

ForcedAge
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A

Gossips
N/A
N/A
N/A

N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
HandItems

8
8
8
8

N/A19
N/A19
8
8
HandDropChances

Health

N/A10

N/A21
N/A21

HurtByTimestamp

HurtTime

)
Invulnerable

N/A10

Leash

LeftHanded

Motion

NoAI
N/A4
N/A4
N/A6

11
13
13
N/A17
N/A17
N/A18

NoGravity

Offers
N/A
N/A
N/A

N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
OnGround

Passengers1

N/A
N/A

PersistenceRequired

14
16

16

PortalCooldown

RootVehicle2

12

Rotation3

22
22

SleepingX, SleepingY, SleepingZ

Silent

Tags

UUID

23
23

VillagerData
N/A
N/A
N/A

N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
Xp
N/A
N/A
N/A

N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
wasOnGround
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A
N/A

N/A
N/A
1 See MC-193083.
2 Not an actual tag saved on mobs, but it's the corresponding tag name on player data: the vehicle this entity rides, see also MC-193083.
3 Desynced, see MC-248587.
4 Cannot be converted (even when setting DrownedConversionTime with commands), see MC-148935, consider to only not trigger/count down the timer if NoAI is present, and allow value 0 to convert.
5 Skeletons MUST be in powdered snow to convert, even via commands. Powdered snow extinguishes burning mobs.
6 Cannot be converted (even when setting StrayConversionTime with commands), consider to only not trigger/count down the timer if NoAI is present, and allow value 0 to convert.
7 Since zombie villagers use IsBaby instead of Age, the time until growing up/being able to breed again is lost. Age gets set to 0 for adults and -24000 for babies upon converting to villagers.
8 The equipment is not dropped, nor brought over to the new form.
9 Always 1b, .
10 Mob needs to die to convert, cannot be converted by creative players.
11 MC-183860, fixed.
12 MC-163767,fixed
13 MC-67437, fixed.
14 Always 1b, MC-239883, this could be resolved by making all villagers that spawned naturally be persistent instead and copying the value over.
15 Converted-to mob cannot burn, if this behavior will ever be toggle-able (for example via entity type tag), this should be synchronized though.
16 Always 1b.
17 Cannot be converted (even when setting TimeInOverworld with commands), see MC-172077, consider to only not trigger/count down the timer if NoAI is present, and allow value 0 to convert.
18 Cannot be converted (even when setting TimeInOverworld with commands), consider to only not trigger/count down the timer if NoAI is present, and allow value 0 to convert.
19 Loot is dropped due to mob death.
20 MC-6773, fixed.
21 Mob needs to die to convert, can be converted by creative players.
22 Desynced, and randomized, see MC-248587.
23 Mob splits into multiple mobs, so UUID cannot be preserved for all. However, 1 of the mob should be capable to get it.
24 Magma cubes can't burn, if this behavior will ever be toggle-able (for example via entity type tag), this should be synchronized though.
Since zombie villagers can be converted to villagers and vise versa, the following data is problematic due to not being stored on one of the 2 parties, causing loss of data upon converting and converting back to the original form. This should probably be it's own report, but until the rest of this is fixed, it's just another "tags lost on conversion" entry.
- Zombie villagers don't have ForcedAge, InLove, Inventory, LastGossipDecay, LastRestock, LoveCause, RestocksToday and Willing.

- Zombie villagers don't use Brain.memories.minecraft:home, Brain.memories.minecraft:job_site, Brain.memories.minecraft:last_woken, Brain.memories.minecraft:last_worked_at_poi, Brain.memories.minecraft:meeting_point and Brain.memories.minecraft:potential_job_site.

- Villagers don't have CanBreakDoors.

How to reproduce
- Summon a mob with any of the above tags, and convert it.

```
/summon minecraft:zombie_villager ~ ~ ~ {Health:10.0f,Invulnerable:1b,Fire:100s,Tags:["foo","bar"],ConversionTime:0}
```

- Once the mob converted, look at its NBT data

```
/data get entity @e[type=villager,limit=1,sort=nearest]
```
→  Note that the tags marked with  do not persist

## Comments (64)

### Comment 1: migrated (2015-09-17T17:38:15.199-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: mrpingouin1 (2015-09-17T18:12:16.079-0700)

Confirmed, but the title is wrong, it only apply to mobs that turn into an other one : Pigs and Villagers.
Kinda related to MC-67437.

### Comment 3: kumasasa (2015-09-17T23:06:25.396-0700)

This is MC-67437 (reopened that)

### Comment 4: qmagnet (2015-09-18T02:34:39.152-0700)

Okay but NoAI status does remain.

### Comment 5: kumasasa (2015-09-18T15:29:37.146-0700)

Yes, I was wrong.

### Comment 6: migrated (2015-09-21T04:49:42.282-0700)

The "villager -> zombie villager" case is covered by MC-11883.
edit: But only the profession and maybe the trades, your ticket is about tags in general.

### Comment 7: marcono1234 (2015-10-18T06:37:56.564-0700)

Something like this could work to "fix" this:
- For all tags in the entity:
- If the tag is also a tag of the target entity (for example Witch), use the value for the tag

- If the tag is not a tag of the target entitiy, ignore the tag

### Comment 8: JUE13 (2017-06-25T04:28:16.515-0700)

Confirmed for 1.12 release.

### Comment 9: [Mod] violine1101 (2018-03-14T14:58:34.629-0700)

Zombie → Drowned is also affected by this, see MC-127307.

### Comment 10: tryashtar (2018-03-14T22:05:46.449-0700)

Is the set of tags that are transferred over the same between all current conversions?

### Comment 11: migrated (2018-07-03T18:50:15.798-0700)

Can confirm for 1.13-pre5.

### Comment 12: migrated (2018-07-05T12:12:58.967-0700)

Can confirm for 1.13-pre6.

### Comment 13: migrated (2019-01-10T14:17:46.184-0800)

Confirmed for 19w02a.

### Comment 14: migrated (2019-08-17T12:57:16.333-0700)

this creates a noticeable issue in the 1.14.4 version; as players infect and cure villagers for cheaper trades, named villagers become able to despawn when in the zombie villager state despite still having their names (appearing to the player to have Persistence).

### Comment 15: migrated (2019-08-31T05:22:49.059-0700)

Just watched MumboJumbo's video where his named villagers were converted to zombies and despawned. The player expectation is if you name the villager it makes the zombie villager safe, and given how much effort goes into unlocking the villagers this would be a very frustrating bug for anyone who's making villager trading setups.

### Comment 16: Misode (2020-01-05T09:31:44.258-0800)

Affects 1.15.1
Also effects zombie -> drowned conversion, but interestingly, not their PersistenceRequired tag, which gets transferred correctly.

### Comment 17: Misode (2020-01-09T05:42:12.093-0800)

Drowned
Villager
Cow
Slime
Zombie Villager
Fire

DeathLootTable

Tags

Rotation

Motion

Silent

Health

 intended
PersistenceRequired

Invulnerable

?
CustomName

### Comment 18: migrated (2020-01-27T22:19:26.570-0800)

I can confirm that this affects version 1.15.2. Another important nbt tag that gets lost when converting a Zombie Villager into a villager is the “CanPickUpLoot” tag.

### Comment 19: migrated (2020-01-28T10:40:42.157-0800)

Drowned
Villager
Cow
Slime
Zombie Villager
Fire

DeathLootTable

Tags

Rotation

Motion

Silent

Health

 intended
PersistenceRequired

Invulnerable

?
CustomName

CanPickUpLoot

-
-

### Comment 20: Gatinh0 (2020-01-30T18:37:52.863-0800)

Of note, in 1.15.2 this still affects tags. Tags are lost when villager converts to zombie, and rescued back to villager.

```Tags:["test_tag"]```

### Comment 21: Misode (2020-02-15T04:36:14.806-0800)

Could I have ownership of this ticket to keep it up-to-date?

### Comment 22: [Mod] violine1101 (2020-02-15T07:30:14.012-0800)

According to MC-172196, PortalCooldown is affected as well.

### Comment 23: qmagnet (2020-02-15T09:18:51.262-0800)

Yes you can have this. It's been 4 years and nothing has happened with this bug so I lost interest long ago.

### Comment 24: Feranogame (2020-02-18T13:06:11.650-0800)

Same happens for the zombification of Piglins.

### Comment 25: Tinsel (2020-03-04T14:20:01.454-0800)

In 20w10a

### Comment 26: Tinsel (2020-03-11T14:20:55.093-0700)

In 20w11a

### Comment 27: Tinsel (2020-03-18T14:32:50.911-0700)

In 20w12a

### Comment 28: FaRo1 (2020-04-08T15:04:37.533-0700)

Apparently NoAI affects cows again (in 20w15a): https://youtu.be/-mfiua5M6qg?t=236

### Comment 29: migrated (2020-04-15T03:31:56.504-0700)

I  have noticed this with the direction the mob is looking. Mobs that convert into another mob don't keep the direction they are looking. This issue does not affect mobs that change the variant. For example if a mooshroom gets stuck by a lightning it keeps the direction, because it is not a seperate mob it is just a variant. Other data of the mooshroom should be also be kept.

### Comment 30: Tinsel (2020-04-29T11:01:07.471-0700)

In 20w18a

### Comment 31: Tinsel (2020-05-06T11:39:00.793-0700)

In 20w19a

### Comment 32: Tinsel (2020-06-06T16:11:41.627-0700)

In 1.16 pre-2

### Comment 33: Tinsel (2020-06-10T10:52:00.454-0700)

In 1.16 Pre 3

### Comment 34: migrated (2020-06-29T16:03:56.098-0700)

Confirmed for 1.16.1

### Comment 35: supeika (2020-07-03T09:43:45.181-0700)

you should add an image of piglins and piglin brutes transformed into zombified piglins, because that image with a zombie pigman refers to an old version, and with the 1.16 is useful having two images of that.

### Comment 36: Avoma (2021-01-09T03:11:59.595-0800)

Can confirm in 20w51a.

### Comment 37: Avoma (2021-01-24T03:45:17.027-0800)

Can confirm in 21w03a.

### Comment 38: Avoma (2021-02-06T09:15:41.993-0800)

Can confirm in 21w05b.

### Comment 39: Avoma (2021-02-12T08:18:19.103-0800)

Can confirm in 21w06a.

### Comment 40: Avoma (2021-02-19T07:34:14.418-0800)

Can confirm in 21w07a.

### Comment 41: Avoma (2021-02-20T09:55:49.045-0800)

I've attached an example video.

### Comment 42: Avoma (2021-04-06T10:51:58.854-0700)

Can confirm in 21w13a.

### Comment 43: ampolive (2021-08-21T15:12:01.293-0700)

Also affects the Attributes tag.

### Comment 44: Avoma (2021-09-05T08:03:40.376-0700)

This ticket is actively updated by , so I don't think there is any need to transfer ownership.

### Comment 45: migrated (2021-09-05T12:17:48.735-0700)

Wouldn't it just be easy to save the NBT data the mob had, and merge the data into the new mob (and apply other changes like the regeneration effect for villagers, and the dropping of equipment for drowned after that)?
(as permanent fix for this issue with all conversions)

### Comment 46: Avoma (2021-12-08T05:10:45.066-0800)

Can confirm in 1.18.

### Comment 47: Avoma (2022-03-10T10:50:21.521-0800)

Can confirm in 1.18.2.

### Comment 48: migrated (2022-05-09T06:30:56.323-0700)

This also affects Shulker Mob Duplication, tags like the colour are kept, but things like the DeathLootTable get deleted. Can confirm this on 1.18.2 (MC-251930)

### Comment 49: migrated (2022-05-09T06:33:36.260-0700)

I'd suggest reporting that separately, as it isn't a mob converting to another, but a new mob being spawned in.

### Comment 50: migrated (2022-05-09T06:34:20.236-0700)

Also affects villager to witch, husk to zombie, skeleton to stray, magma cube to smaller magma cube and hoglin to zoglin.
Also for slime to smaller slime, health should be "-" as that only happens on death.

### Comment 51: ampolive (2022-05-19T09:17:21.546-0700)

Slimes and magma cubes should also not get the bigger mob's UUID because that would result in several entities with duplicated UUIDs.

### Comment 52: ampolive (2022-05-20T15:15:51.294-0700)

This might also affect red mooshroom / brown mooshroom conversion.

### Comment 53: Misode (2022-05-20T17:47:58.853-0700)

This might also affect red mooshroom / brown mooshroom conversion.
That should not be the case since that conversion is done with an NBT tag rather than changing the entity ID.

### Comment 54: ampolive (2022-05-20T18:14:58.991-0700)

Oops, I thought that they were separate entities  You're right.

### Comment 55: migrated (2022-07-23T08:00:22.364-0700)

Zombie villager to villager does keep rotation, it's just desynced on the client: MC-248587.

### Comment 56: migrated (2022-08-05T06:25:47.473-0700)

Don't forget Pigs to Zombified Piglins via lightning

### Comment 57: Avoma (2022-08-11T03:42:49.015-0700)

Can confirm in 1.19.2.

### Comment 58: migrated (2023-07-12T09:02:29.027-0700)

Villager to zombie villager keeps rotation, but it is desynced; only client believes it faces south.

### Comment 59: migrated (2023-08-08T04:27:59.796-0700)

Needs a HandItems/ArmorItems row, see MC-264717.

### Comment 60: 4ebugger (2023-11-21T04:36:34.200-0800)

Confirm in 1.20.2 pre1, aslo affect trial spawners.

### Comment 61: migrated (2023-11-21T04:43:08.263-0800)

Spawn method has no relation to convertion.

### Comment 62: migrated (2024-02-15T23:57:21.657-0800)

Attrobites are also affected.

### Comment 63: Xfrtrex (2024-06-04T18:40:04.589-0700)

Can confirm in 1.21-pre2.

### Comment 64: Ray (2024-09-04T15:57:49.750-0700)

Villagers to witches one still does not work: ArmorItems-8 The equipment is not dropped, nor brought over to the new form.

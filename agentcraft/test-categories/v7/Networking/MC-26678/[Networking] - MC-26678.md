# MC-26678: Damage wobble no longer shows direction of incoming damage

**Mojira URL:** [https://bugs.mojang.com/browse/MC-26678](https://bugs.mojang.com/browse/MC-26678)

## Report details

- **Mojira categories:** Networking; Rendering
- **Project:** MC
- **Issue key:** MC-26678
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2013-07-19T12:07:19.461-0700
- **Updated:** 2025-04-26T03:03:19.663-0700
- **Resolution date:** 2025-01-21T00:51:31.087-0800
- **Affects versions:** Minecraft 1.5.2; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.6.3; Minecraft 13w37b; Minecraft 1.7.4; Minecraft 14w04b; Minecraft 14w07a; Minecraft 14w18a; Minecraft 1.7.10; Minecraft 14w29b; Minecraft 14w32b; Minecraft 14w34d; Minecraft 1.8-pre3; Minecraft 1.8; Minecraft 1.8.1-pre3; Minecraft 1.8.7; Minecraft 1.8.8; Minecraft 15w46a; Minecraft 15w47a; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 1.11.2; Minecraft 17w16a; Minecraft 17w16b; Minecraft 17w17a; Minecraft 1.12 Pre-Release 6; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 17w50a; Minecraft 18w11a; Minecraft 1.13-pre1; Minecraft 1.14; 1.15.1; 1.15.2 Pre-release 2; 1.15.2; 20w08a; 1.16.1; 20w29a; 1.16.2; 1.19.3
- **Fix versions:** 23w03a
- **Game mode:** Survival
- **Labels:** 12w18a; damage; shake
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2014-10-30_22.38.46.png; minecraftarmcomparison.gif
- **Issue links:** Relates:outward:MC-120545:Teleportation wraps rotation angles causing first-person hand to rotate incorrectly | Relates:inward:MC-200474:Entities do not tilt in the direction of a killing blow upon death | Duplicate:inward:MC-231021:Damage Needs to be Fixed! | Duplicate:inward:MC-227955:Camera does not tilt towards damage direction | Duplicate:inward:MC-73853:Damage wobble no longer shows direction of incoming damage | Duplicate:inward:MC-212835:Directional camera when hit via mob not working correctly. | Duplicate:inward:MC-212359:Telling the serever to send the camera the angle(PLS  fix this fast. It is only onle little piece of code.) | Duplicate:inward:MC-212154:Camara tilt | Duplicate:inward:MC-204851:Damage Tilt Indicator | Duplicate:inward:MC-205503:damage shake issue | Duplicate:inward:MC-204809:Damage tilt always towards left | Duplicate:inward:MC-204669:screen tilts to the left when taking damage | Duplicate:inward:MC-202355:Damage screen tilt is de-synced, defaulting to tilt left | Duplicate:inward:MC-203742:Directional Damage Indicator | Duplicate:inward:MC-203715:Damage tilt indicator does not work correctly | Duplicate:inward:MC-204269:Attacked Camera Angle Tilt | Duplicate:inward:MC-203793:Directional damage indicator has not worked properly of EIGHT YEARS | Duplicate:inward:MC-203760:This bug has been here since 1.3 has been released | Duplicate:inward:MC-203526:Incorrect attack angle communication from server to client. | Duplicate:inward:MC-203482:Screen Tilts Towards Damage doesn't work | Duplicate:inward:MC-202616:Damage tilt always tilts to the left, and not towards the source of the damage | Duplicate:inward:MC-203265:Damage tilt still not working | Duplicate:inward:MC-203260:Directional screen tilt damage indicator hasn't been working since 1.3 java edition | Duplicate:inward:MC-202922:camera doesn't tilt to damage | Duplicate:inward:MC-143964:Player's arm and camera only jerk to the left when getting hurt

## Description

Note
The comment section in the bug tracker is only meant for providing additional information regarding a bug report, it's not meant to be used as a forum for discussion. Please see 's comment on where you can hold discussions.
If you don't respect the rules of the bug tracker, you may be banned.
's comment
The bug
In 1.2.5 SSP and before the little wobble to the whole viewport that occurs when you take damage used to indicate the direction the damage came from. As part of the 1.3 client/server merge, this behavior was lost.
Steps to view correct behavior
- Revert to 1.2.5 SSP and start a new creative world

- Build the contraption as shown in the image attachment below

- Fill the dispensers with arrows.

- Exit MC and use NBTExplorer to change the world to survival mode (alternatively play survival until you obtain those items or open a copy of a current world)

- Facing forward, strafe left into the left pressure plate. Arrow will hit you and the viewport will tilt to the right, simulating the head whiplash.

- Facing forward, strafe right into the right pressure plate. Arrow will hit you and the viewport will tilt to the left, simulating the head whiplash.

- Facing forward, walk into the front pressure plate. Arrow will hit you and the viewport will tilt DOWN, simulating being hit in the top of the head by something

- Facing forward, back into the rear pressure plate, Arrow will hit you and the viewport will tilt UP, simulating being hit in the back of the head and having forward whiplash.

- This seemingly "cool aesthetic" actually has real gameplay value because it indicates to fighters where incoming damage is originating from.

- Repeat all steps in latest version (no need to use NBT editors just open to lan with cheat mode to switch gamemode). Notice how the viewport will always tilt right no matter what.

Code analysis (MCP Names)
EntityLivingBase.attackedAtYaw is not synced to the client, causing an animation present in the client to not be correctly rendered.

## Comments (42)

### Comment 1: migrated (2013-07-19T12:07:19.461-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: kumasasa (2013-07-19T15:19:27.331-0700)

Confirmed.

### Comment 3: migrated (2014-04-30T18:57:19.678-0700)

Confirmed all the way up to 14w18a

### Comment 4: migrated (2014-07-17T08:32:24.994-0700)

Confirmed all the way up to 14w29b

### Comment 5: migrated (2014-09-01T14:24:41.420-0700)

Confirmed to 1.8-pre3. please fix!

### Comment 6: migrated (2015-11-12T07:42:02.447-0800)

Confirmed tup to 15w46a. Please fix.

### Comment 7: shufboyardee (2015-11-12T08:51:54.884-0800)

This would be great to have back, yes!

### Comment 8: migrated (2015-11-18T18:11:54.990-0800)

Confirmed to latest snapshot (November 18).
This would really really be a good (re)addition to combat. Please fix it!
It's just syncing one more field back to the client.
Thanks

### Comment 9: migrated (2016-08-13T13:54:37.305-0700)

Confirmed up to 16w32b

### Comment 10: JUE13 (2017-04-26T03:10:21.038-0700)

Confirmed for 17w16b

### Comment 11: JUE13 (2017-04-27T05:34:36.362-0700)

Confirmed for 17w17a

### Comment 12: migrated (2017-06-11T11:32:36.710-0700)

Confirmed for 1.12

### Comment 13: migrated (2019-04-25T21:09:48.044-0700)

Confirmed for 1.13.x and 1.14

### Comment 14: pulpetti (2020-07-06T11:27:44.104-0700)

Affects 1.16.1

### Comment 15: pulpetti (2020-07-06T11:27:52.102-0700)

Affects 20w27a

### Comment 16: migrated (2020-07-08T21:02:10.804-0700)

Confirmed for 20w28a

### Comment 17: migrated (2020-07-15T20:25:35.549-0700)

Confirmed in 20w29a.

### Comment 18: muzikbike (2020-07-17T11:23:30.333-0700)

Did the direction dead mobs fall ever depend on the direction of incoming damage?

### Comment 19: migrated (2020-08-14T05:18:23.070-0700)

Confirmed in 1.16.2

### Comment 20: migrated (2020-09-05T08:15:09.893-0700)

So sad to see "won't fix".

### Comment 21: migrated (2020-10-21T22:11:28.004-0700)

I know you don't have to do this, but do you have a reason for marking this "Won't Fix?" I'm more than familiar with some bugs just not being worth fixing, but when the problem and solution has been pinpointed by forge developers in the video here, I don't think it can fall in that category.

### Comment 22: migrated (2020-10-22T12:12:36.235-0700)

Please fix this! It would be immensely helpful! Why "wont fix"? Even if you won't fix it, just give a reason!

### Comment 23: slicedlime (2020-10-23T05:13:57.725-0700)

The issue tracker is not a discussion forum. If you disagree with an issue resolution, please bring it up on the MOJIRA subreddit or discord.

### Comment 24: marcono1234 (2020-10-25T08:17:33.501-0700)

/r/Mojira post for discussion

### Comment 25: migrated (2020-10-28T07:03:36.464-0700)

Why it can't be a toggleable option in Accessibility options ;-:

### Comment 26: migrated (2020-10-28T10:44:43.987-0700)

If you REALLY want it back, install this mod.

### Comment 27: migrated (2020-11-01T06:36:42.167-0800)

Look. I never knew that screen tilt was ever a thing so I never actually saw that as a bug, just a feature. I wouldn't actually think that this would be a bug in some way before I read about it and saw this video: https://youtu.be/pAJPc71YOnY
For PVP community this would be a good feature and without having to install mods in order to fix the bug, it would be great to have that in game. I think that servers that do not run modded version running this mod will still work the same, even if you have the mod installed, but I don't know if it actually works just by sending that piece of information to the client or it actually uses some clever math tricks to compute that kind of missing information in case that information is missing.
If the later is true, then using this mod may actually result in ban on some PVP competitive servers (Factions, UHC, Skywars, etc.) because this isn't just a visual effect like resource pack lowering fire and shortening swords (which is purely aesthetics to better see around you) which everybody can install and if someone doesn't have them - well that's their fault. This is actually real gameplay feature and it can give serious piece of information about whereabouts of other players attacking you. Kind of like minimap mod showing you whereabouts of other players in your proximity. There are players that for some reason cannot install mods, or don't want to. If you fix that bug and maybe add a little toggle option to turn it off (return back to the now classic left-tilt feature - actually bug), those who opt it out and turn it off won't be entitled to accuse players using that feature for cheating, because it will be vanilla game feature now. Of course, x-ray is something that doesn't exist in vanilla game, or at least nothing intentional. In previous versions, you could x-ray caves by putting your head into a glowstone or (in case of fast graphics) in leaves, though you wouldn't see unexposed ores anyway, just where the caves are, this is now considered bug (that has been fixed anyway) and many servers prohibit abusing bugs for your advantage.
However, screen tilting towards the inflicted damage is something that should be in game and as it turns out it has been before, it didn't work on servers though as the code for sending that bit of information to the client was missing. Seriously, how hard is to add I guess one little line of code to send that information to client amongst other ones?

### Comment 28: slicedlime (2020-11-02T00:39:29.382-0800)

I'll repeat myself: The issue tracker is not a discussion forum. If you disagree with an issue resolution, please bring it up on the MOJIRA subreddit or discord.

### Comment 29: Adrian Östergård (2020-11-04T07:41:50.915-0800)

The comment section in the bug tracker is only meant for providing additional information regarding a bug report, it's not meant to be used as a forum for discussion. Please see  previous comment on where you can hold discussions.
If you don't respect the rules of the bug tracker, you may be banned.

### Comment 30: GolfinhoVoador (2020-11-09T06:18:16.423-0800)

Confirmed for: 1.16.3, 1.16.4, 20w45a

### Comment 31: SPGoding (2020-11-09T08:16:42.866-0800)

, the ticket was already resolved as Won't Fix, thus we generally no longer add new affected versions to it.

### Comment 32: migrated (2020-11-10T08:42:15.220-0800)

@SPGoding I thought a mod mentioned in the Mojira subreddit this was internally marked for reassessment

### Comment 33: [Mod] violine1101 (2020-11-11T12:07:52.746-0800)

I thought a mod mentioned in the Mojira subreddit this was internally marked for reassessment
internally being the key word here. This bug report remains resolved until Mojang decides to reopen it.

### Comment 34: numeritos (2020-12-01T02:01:16.295-0800)

I've seen a lot of emails regarding new comments on this report.
You can discuss about this issue on the Mojira subreddit post: https://www.reddit.com/r/Mojira/comments/jhd3aa/why_was_mc26678_marked_as_wont_fix/

### Comment 35: migrated (2021-04-09T16:13:24.122-0700)

The thread linked above will soon be archived, as it will soon be 6 months old. I've created a proactive reddit thread so when the thread is inevitably archived, people can still comment their gripes without clogging up the comment section.

### Comment 36: MishaGold (2023-01-18T06:19:17.788-0800)

IT GOT FIXEDDDDDDDDDD

### Comment 37: migrated (2023-01-18T09:43:26.708-0800)

FINALLY! WOW! AMAZING!

### Comment 38: migrated (2023-01-18T10:07:51.292-0800)

Been watching this one for years. Thank you for finally fixing it.

### Comment 39: Kokonut (2023-01-18T10:11:02.305-0800)

only took 9 years

### Comment 40: muzikbike (2023-08-26T01:28:17.563-0700)

MC-265044 can probably be marked as related - both reports involve the camera not tilting under specific circumstances while they used to in previous versions.

### Comment 41: migrated (2024-04-04T05:31:51.779-0700)

Relates to MC-269238.

### Comment 42: muzikbike (2024-12-27T04:25:33.151-0800)

Also relates to MC-225335.

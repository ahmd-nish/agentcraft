# MC-18060: Several realms strings are untranslatable

**Mojira URL:** [https://bugs.mojang.com/browse/MC-18060](https://bugs.mojang.com/browse/MC-18060)

## Report details

- **Mojira categories:** Text; UI
- **Project:** MC
- **Issue key:** MC-18060
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2013-06-15T11:47:26.835-0700
- **Updated:** 2025-04-26T02:53:02.541-0700
- **Resolution date:** 2024-08-13T04:14:20.384-0700
- **Affects versions:** Minecraft 1.5.1; Minecraft 1.5.2; Snapshot 13w23b; Snapshot 13w24a; Snapshot 13w24b; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.6.4; Minecraft 1.7.1; Minecraft 1.7.2; Minecraft 1.7.4; Minecraft 14w05b; Minecraft 14w06b; Minecraft 14w07a; Minecraft 14w08a; Minecraft 1.7.5; Minecraft 1.7.10; Minecraft 14w34c; Minecraft 1.8; Minecraft 1.8.8; Minecraft 15w37a; Minecraft 1.10.2; Minecraft 16w33a; Minecraft 16w44a; Minecraft 1.11; Minecraft 1.11.2; Minecraft 17w17b; Minecraft 17w18a; Minecraft 17w18b; Minecraft 1.12.1; Minecraft 1.13.1; 1.15.2; 1.16.1; 20w29a; 1.18.1; 1.18.2 Release Candidate 1; 1.18.2; 22w13a; 22w16b; 22w17a; 1.19; 22w24a; 1.19.1; 1.19.2; 22w43a; 1.19.3; 1.19.4 Pre-release 3; 1.19.4
- **Fix versions:** 1.20 Pre-release 1
- **Labels:** mojang_internal_1; multiplayer; realms; translatability
- **Watchers:** 1
- **Attachments:** 9
- **Attachment filenames:** 2013-07-06_16.36.49.png; 2013-07-11_19.30.04.png; 2013-07-11_19.34.11.png; 2013-07-11_19.34.56.png; 2014-04-13_14.29.34.png; 2014-04-13_14.32.20.png; 2014-06-16_10.49.28.png; screenshot-1.jpg; screenshot-2.jpg
- **Issue links:** Relates:outward:MC-263562:World types in Realms backup info screen are untranslatable | Relates:inward:MC-275157:The Realms error message "Invalid session id" is untranslatable | Relates:inward:MC-112602:"disconnect.spam" kick message is untranslated | Relates:inward:MC-119873:The text used for the credits button within the title screen is untranslatable | Relates:inward:MC-133088:Missing translation string death.attack.magic.player | Duplicate:inward:MC-195465:"Connection throttled..." string not localized | Duplicate:inward:MC-190690:Missing translation in Realms | Relates:inward:MC-142621:"Invalid book tag" is not translatable | Relates:inward:MC-124942:"Invalid book tag" is not translatable | Relates:outward:MC-5002:Some texts can't be translated in a language file | Duplicate:inward:MC-29391:Some GUI text isn't translated | Relates:outward:REALMS-1130:Hardcoded string "Info!"

## Description

The Bug:
Several realms strings are untranslatable.
Affected Strings:
Before reading the table, please note that there may be more strings affected by this that aren't listed below.

String(s)
Context
Translatable?
String Location
"UNKNOWN"
This string is displayed when details within the realms backup information menu are unknown.
No
Realms Backup Information Screen
"Changes from last backup"
This is the title displayed within the realms backup information menu.
No
Realms Backup Information Screen
"Uploaded"
This string is displayed when a backup was successful within the realms backup menu.
No
Realms Backup Screen
"Backup (" & ")"
These two strings of text are displayed in the title of fields within the realms world backups menu.
No
Realms Backup Screen
": "
This string is part of the minigame prefix displayed within the realms configure world screen. This string is displayed just after the "mco.configure.current.minigame" string.
No
Realms Configure World Screen
"%"
This string is displayed within the progress bar when a download is in progress within the realms download lastest world menu.
No
Realms Download Latest World Screen
"(" & "/s)"
These strings are displayed to show the download speed when a download is in progress within the realms download lastest world menu.
No
Realms Download Latest World Screen
"%"
This string is displayed within the progress bar when an upload is in progress within the realms upload menu.
No
Realms Upload Screen
"(" & "/s)"
These strings are displayed to show the upload speed when an upload is in progress within the realms upload menu.
No
Realms Upload Screen
"An error occurred (" & "):"
These strings are displayed when the player receives a "null" realms error.
No
Realms Generic Error Screen
"Realms (" & "):"
These strings are displayed when the player receives a generic realms error.
No
Realms Generic Error Screen
"An error occurred: "
This string is displayed when the player receives a generic realms error.
No
Realms Generic Error Screen
"Ok"
This string is displayed in the button within the realms generic error screen.
No
Realms Generic Error Screen
"Failed to download resource pack!"
This string is displayed when resource packs are failed to be loaded.
No
Realms Generic Error Screen
"Warning!"
The string is displayed as a title within any "long confirmation realms menu" that contains a warning.
No
Realms Long Confirmation Screen
"Info!"
The string is displayed as a title within any "long confirmation realms menu" that contains some information.
No
Realms Long Confirmation Screen
"Question", " '", & "' ?"
These strings are used alongside the "mco.configure.world.uninvite.question" string and are displayed when a player wishes to uninvite someone from a realm.
No
Realms Player Screen
"(" & ")"
These strings are used to show the number of players that have been invited to a realm.
No
Realms Player Screen
"Unable to load worlds"
This string is displayed when worlds are failed to be loaded within the realms upload screen.
No
Realms Select File To Upload Screen
"(" & ")"
These strings are used to show the worlds displayed within the realms upload screen.
No
Realms Select File To Upload Screen
", "
This string is used in the description of worlds within the realms upload screen if cheats are enabled on them.
No
Realms Select File To Upload Screen
", "
This string is used in the description of how long a realm has left before it expires.
No
Realms Subscription Information Screen
"Minigame"
This string is displayed within the realms world button slot.
No
Realms World Slot Menu?
"right now"
I believe this string is used within realms invitations, backups, and potentially some other areas, to show the amount of time elapsed since a given invitation, backup, etc...
No
Realms Utility Menu?
"1 second", " seconds", & "ago"
I believe these strings are used within realms invitations, backups, and potentially some other areas, to show the amount of time elapsed since a given invitation, backup, etc...
No
Realms Utility Menu?
"1 minute", " minutes", & "ago"
I believe these strings are used within realms invitations, backups, and potentially some other areas, to show the amount of time elapsed since a given invitation, backup, etc...
No
Realms Utility Menu?
"1 hour", " hours", & "ago"
I believe these strings are used within realms invitations, backups, and potentially some other areas, to show the amount of time elapsed since a given invitation, backup, etc...
No
Realms Utility Menu?
"1 day", "days", & " ago"
I believe these strings are used within realms invitations, backups, and potentially some other areas, to show the amount of time elapsed.
No
Realms Utility Menu?
h3. Steps to Reproduce:
- Attempt to search for the existence of any of the affected strings as listed above on the official Minecraft crowdin project.

- Take note as to whether or not several realms strings are untranslatable.

Observed Behavior:
Several realms strings are untranslatable.
Expected Behavior:
All realms strings are untranslatable.

## Comments (38)

### Comment 1: migrated (2013-06-15T11:47:26.835-0700)

This comment contained multiple image attachments (9), please login to view the attachments.

### Comment 2: kumasasa (2013-06-16T01:06:11.941-0700)

Confirmed.

### Comment 3: migrated (2013-07-07T09:56:39.505-0700)

As of 1.6.1, "Scanning for games on your local network" is translated.
As of 1.6.2pre, "Polling..." ,"Can't reach server" and maybe "Communication error" are not translated.
(en_US.lang doesn't have these entries.)

### Comment 4: migrated (2013-07-09T11:02:36.963-0700)

I can confirm what ANBO Motohiko said

### Comment 5: migrated (2013-07-11T03:52:36.361-0700)

Another screenshots (confirmed on 1.6.2 release server/client). Also untranslatable:
- Tooltip for status: '(no connection)'

- 'Outdated server!' (in the case of server:1.6.1, client:1.6.2)

- 'Server closed' (when the server is shut downed.)

- 'Illegal position' (When a player goes further than 32,000,000 blocks. This occurs not only on multiplayer but also singleplayer.)

@Ezekiel What can I do for it? I don't have any rights to update info, so may I clone this issue?

### Comment 6: migrated (2014-02-23T04:06:20.866-0800)

Still in 08a

### Comment 7: migrated (2014-02-26T06:56:05.256-0800)

I've added screens made in 1.7.5. And all the same for S14w08a.

### Comment 8: migrated (2014-04-13T05:37:25.812-0700)

I've added a screen of the hardcore game over menu.
I'd love to see this fixed as soon as possible. We should be able to translate everything!

### Comment 9: migrated (2014-04-13T07:32:34.199-0700)

I've added other three screenshots: in the twitch server list, "(preferred)", "(default)" and "kbps" can't be translated; in the new 1.7.6 streaming start confirmation screen, the main text can't be transalted; the new 1.7.6 server resource pack button can't be translated. It's a shame having a half translatable game.

### Comment 10: migrated (2014-04-13T15:09:01.803-0700)

F3+H detailed tooltips (tool durability, map info) can't be translated as well.

### Comment 11: migrated (2014-06-16T01:54:01.045-0700)

The message on the "buy a Realm" screen can't be translated.
I'd suggest to change the title to "Some messages can't be translated".

### Comment 12: migrated (2014-08-19T10:31:12.127-0700)

Superflat presets nanes can't be translated (customized ones are translatable). Still a (big IMO) issue in 14w34c...

### Comment 13: kumasasa (2014-08-25T13:35:52.606-0700)

Superflat presets nanes are available now, see MC-46341

### Comment 14: Bentroen (2014-09-01T15:42:13.032-0700)

The "Down!" message in the Twitch servers are also not translated.

### Comment 15: marcono1234 (2014-09-21T05:54:43.845-0700)

Confirmed for
- 1.8 also for the "Back" when you are using an outdated Minecraft Version

### Comment 16: Bentroen (2014-11-07T09:50:20.015-0800)

The "... and X more ..." text in the Multiplayer screen!

### Comment 17: marcono1234 (2015-09-11T07:54:12.835-0700)

Confirmed for
- 15w37a for the incompatible client message when clicking on "Minecraft Realms" with a snapshot version

### Comment 18: marcono1234 (2016-03-19T07:02:49.204-0700)

Please include "... and X more ..." (player preview) in the multiplayer screen (see 's comment)

### Comment 19: migrated (2016-08-23T21:56:46.798-0700)

Confirmed for 16w33a

### Comment 20: migrated (2016-08-24T01:26:26.900-0700)

Removed screenshots that were supposed to be in MC-46341, as well as the twitch server screenshot (as twitch support is removed).

### Comment 21: migrated (2016-11-04T13:09:49.710-0700)

Still in 16w44a.

### Comment 22: migrated (2017-05-07T06:18:37.233-0700)

Another not translated message :
Server out of date!

### Comment 23: migrated (2017-05-16T06:36:06.607-0700)

Still in 1.12 pre-2

### Comment 24: migrated (2017-05-29T06:56:54.865-0700)

Partially fixed in 1.12-pre6: only game messages were made available, the hardcoded Realms strings are still hardcoded

### Comment 25: migrated (2018-09-17T10:08:38.440-0700)

"Realms News" is translated for 1.13.1.
"(no connection)" is translated for 1.13.1.
"Incompatible client" message is translated for 1.13.1. (tested with 18w33a)

### Comment 26: migrated (2020-04-29T08:54:33.402-0700)

Hi Adrian,
I don't know why I have received your mail ?  [JIRA] Mises à jour de  : Missing translation for some multiplayer server connection / Realms messages

Kind Regard, Vincent

### Comment 27: marcono1234 (2020-04-29T09:09:14.958-0700)

@, Adrian updated the report and set a priority. If you don't want to be informed about further updates to this report, please click the "Stop watching this issue" link in the top right corner.

### Comment 28: migrated (2020-04-29T12:10:56.289-0700)

Hi Marcono1234, well get it, but thinks something else happen .. .

### Comment 29: migrated (2020-04-29T13:04:41.553-0700)

A few more untranslatable strings:
- "Banned by an operator." (default ban reason shown when trying to enter a server from which you were banned)

- "%s minutes ago", "%s days ago" (shown in Realms in a bunch of different menus, such as invites, backups, and backup restore confirmation - "%s hours ago" might exist but I haven't seen it during my Realms trial)

- "%s player", "%s-%s players", "%s+ players" (shown in Realms in the minigame selection screen)

- "Info!" and "Warning!" (shown in Realms in a bunch of different confirmation screens, such as restoring a backup or leaving a realm)

- "Minigame" (shown in Realms in the world slot used to select a minigame)

- "Backup" (shown in Realms as the name of each backup in the "World backups" screen)

- "Enabled Packs", "Seed", "Game Server Version", "Game Difficulty" (and maybe more too, shown in Realms by going to "World backups", then pressing the little + button on a backup)

### Comment 30: Avoma (2022-01-15T05:50:55.241-0800)

Can confirm in 1.18.1.

### Comment 31: Avoma (2022-02-26T04:49:12.662-0800)

Would it be okay if I can request ownership of this ticket?
This issue has changed substantially as time has gone by, and some of the currently provided details in this report are incorrect and outdated. I'm willing to update and refine this ticket to include all of the necessary information, such as listing all of the new strings of text this issue affects and where they can be seen throughout the game.
The current reporter has been inactive since June of 2019, and I'm inclined to update and shed some additional light on this issue, with the new information I've gathered through looking at decompiled versions of the game's code and researching the affected strings on the official Minecraft crowdin project. Thank you

### Comment 32: Avoma (2022-03-13T03:02:22.269-0700)

This comment by  states that characters that represent icons should not be translated, so I've removed all of the "▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃" and related strings from this ticket for this reason and also for documentation purposes. Additionally, the resolution of MC-248840 implies that characters/symbols used for loading animations should not be translatable.

### Comment 33: migrated (2022-06-18T08:48:12.672-0700)

^ you forgot to remove some, the dots for downloading and uploading.

### Comment 34: Avoma (2022-06-18T09:15:51.781-0700)

, I've intentionally left them in since some languages translate symbols differently. For example, take the "options.controls" translatable text component which reads "Controls..." in English (US), and "按鍵設定⋯⋯" in Chinese Traditional, Hong Kong. As you can see the periods/full stops used within the Chinese Traditional, Hong Kong translation are completely different from the ones used in the English (US) translation. With string like "▃ ▄ ▅ ▆ ▇ █ ▇ ▆ ▅ ▄ ▃" however, it's different because these characters are meant to represent icons, unlike the dot symbols.

### Comment 35: migrated (2022-06-18T09:48:53.510-0700)

The thing is, they're used as loading symbols here, like the blocks, and not as punctuation like the controls string.
You said it yourself:
Additionally, the resolution of MC-248840 implies that characters/symbols used for loading animations should not be translatable.
They're used as loading animation.

### Comment 36: Avoma (2022-06-18T10:03:15.711-0700)

Ahhh I see. I forgot that they were used for a loading animation; I overlooked this. I've edited this report accordingly; thank you!

### Comment 37: [Mod] turbo (2023-03-06T14:35:49.902-0800)

Can confirm in 1.19.4 Pre-release 3; relates to REALMS-1130.

### Comment 38: Avoma (2023-05-05T08:40:12.016-0700)

Updated this ticket to purely mention the realms strings since these were the only strings that were fixed in throughout this bug report. The untranslatable multiplayer strings are now being tracked separately at MC-262370.

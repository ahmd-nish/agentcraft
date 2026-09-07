# MC-72687: There are no shadows on text displayed within the action bar

**Mojira URL:** [https://bugs.mojang.com/browse/MC-72687](https://bugs.mojang.com/browse/MC-72687)

## Report details

- **Mojira categories:** Accessibility; Text; UI
- **Project:** MC
- **Issue key:** MC-72687
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2014-10-04T11:42:28.853-0700
- **Updated:** 2025-04-26T03:47:59.147-0700
- **Resolution date:** 2024-10-22T11:43:30.317-0700
- **Affects versions:** Minecraft 1.8; Minecraft 1.10.2; Minecraft 16w41a; Minecraft 1.13.2; Minecraft 19w08b; Minecraft 19w09a; Minecraft 19w11a; Minecraft 19w11b; 1.14.4; 1.15.1; 1.15.2; 20w06a; 20w07a; 20w20a; 20w46a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w08b; 21w14a; 21w17a; 1.17.1; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 7; 1.18; 1.18.1; 22w03a; 22w05a; 22w06a; 22w07a; 1.18.2 Release Candidate 1; 1.18.2; 22w17a; 22w18a; 1.19 Release Candidate 2; 1.19
- **Fix versions:** 22w24a
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** Capture d’écran 2014-10-04 à 20.36.20.png; javaw 2016-10-15 11-09-21-800.png; javaw 2016-10-15 11-32-01-351.png; MC-72687.mp4; MC-72687.png; MC-72687 - 22w24a (Fixed).png; MC-72687 - Comparison.png
- **Issue links:** Relates:outward:MC-240724:There are no shadows on text displayed within the subtitles overlay | Cloners:inward:MC-92012:Action Bar messages are barely visible

## Description

The Bug:
There are no shadows on text displayed within the action bar.
This is an issue because the text can be quite difficult to read, so having a shadow displayed on all text within the action bar would resolve this problem.
Steps to Reproduce:
- Display some text on the action bar and look at it closely.

```
/title @a actionbar {"text":"MC-72687","color":"white"}
```
- Take note as to whether or not there are any shadows on text displayed within the action bar.

Observed Behavior:
There are no shadows on text displayed within the action bar.
Expected Behavior:
There would be shadows on text displayed within the action bar.
Code Analysis:
Code analysis by  can be found in this comment.

## Comments (31)

### Comment 1: migrated (2014-10-04T11:42:28.853-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: migrated (2014-10-06T08:07:11.405-0700)

its Cops and Crims on hypixel, isn't it? ;D
Could be a problem on their side, because its not the vanilla minecraft, but a "modded" server.

### Comment 3: migrated (2015-02-09T12:42:21.672-0800)

@Thijmen F
Sure, because servers control client-side text rendering...

### Comment 4: migrated (2015-02-09T13:01:21.839-0800)

The action bar doesn't exist in vanilla, therefore, not vanilla's problem.

### Comment 5: migrated (2015-02-09T14:44:10.599-0800)

@Carl Nathans
Yes, because that screen is a modded minecraft client... PLS. It IS minecraft. The action bar EXIXTS. Try to right click a Horse, for example.

### Comment 6: migrated (2015-02-09T14:55:53.286-0800)

Carl is right. There is no action bar in vanilla Minecraft. The vanilla Minecraft equivalent is a tooltip which can be disabled in options.txt.
Invalid as it relates to a modified server.

### Comment 7: kumasasa (2015-02-09T15:07:49.815-0800)

This ticket is invalid as it relates to a modified or 3rd party client, server, or launcher.
- Any non-standard client/server/launcher build needs to be taken up with the appropriate team, not Mojang.

- Any plugin issues need to be addressed to the creator of the plugin or resource pack.

- This site is for addressing issues related to the base unmodded Minecraft; Bukkit, Forge, Optifine, or any other modded system invalidates your ticket, unless it can be shown to happen in Vanilla.

- Additionally, if you have problems on large-scale modded servers, please report it to their site. It's probably not a bug in Vanilla Minecraft.

### Comment 8: Squid Eevee (2015-02-09T15:33:45.549-0800)

The action bar is used when displaying the name of a song when a jukebox is used. Or is that something else?

### Comment 9: migrated (2015-02-10T07:31:09.688-0800)

http://i.imgur.com/rtXcFeV.png
Confirmed in Vanilla. Open the game before marking as "invalid".

### Comment 10: kumasasa (2015-02-10T11:19:11.028-0800)

This is intended.
This feature is meant as a minimal message and it's less annoying to look without shadow.

### Comment 11: migrated (2016-10-15T02:38:09.806-0700)

As of 16w32b shadow should be present because of command block contraptions which can use actionbar now.

### Comment 12: migrated (2016-10-15T02:47:54.459-0700)

Agreed.
Reopening and letting a dev decide as action bar messages are barrely noticeable without shadows. (At least the command ones with colors.)
Edit:
Never mind: see the "is cloned by" link.

### Comment 13: migrated (2016-10-15T03:17:50.516-0700)

I checked "is cloned by" link but there's nothing about text showing by "/title actionbar" command. Maybe it should be discussed?
I think that text showing by command blocks should be clearly readable. It's various text, not only few predefined sentences.
This could be as non-default, maybe as "/title actionbar withshadow" option.

### Comment 14: migrated (2020-12-19T07:02:53.771-0800)

Confirmed in 20w51a.

### Comment 15: Avoma (2021-01-23T03:17:24.093-0800)

Can confirm in 21w03a. You can use the following command to reproduce this issue:

```/title @a actionbar {"text":"MC-72687","color":"dark_red"}```

### Comment 16: Avoma (2021-02-06T07:12:09.585-0800)

Can confirm in 21w05b.

### Comment 17: Avoma (2021-02-12T06:33:43.259-0800)

Can confirm in 21w06a.

### Comment 18: Avoma (2021-02-19T04:42:48.913-0800)

Can confirm in 21w07a. Video attached.

### Comment 19: Avoma (2021-03-03T06:29:52.922-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 20: Avoma (2021-03-29T07:11:01.939-0700)

Can confirm in 21w11a.

### Comment 21: Avoma (2021-04-13T11:27:53.786-0700)

Can confirm in 21w14a.

### Comment 22: Avoma (2021-05-01T07:28:43.723-0700)

Can confirm in 21w17a.

### Comment 23: Avoma (2021-07-15T04:13:52.332-0700)

Can confirm in 1.17.1.

### Comment 24: Avoma (2021-10-15T12:14:46.232-0700)

I'd like to request ownership of this ticket since the current reporter has been inactive since October 2014.

### Comment 25: Avoma (2021-11-03T09:00:40.795-0700)

Can confirm this in 21w43a.

### Comment 26: Avoma (2021-11-05T11:11:37.500-0700)

This ticket relates to MC-240722 and MC-240724.

### Comment 27: Avoma (2021-11-17T11:25:21.871-0800)

This ticket also relates to MC-241520.

### Comment 28: haykam (2022-06-05T09:11:57.944-0700)

Can confirm in 1.19 release candidate 2. One line fix in the InGameHud class (Yarn mappings):

```// Current render call
textRenderer.draw(matrices, this.overlayMessage, (float)(-n / 2), -4.0f, k | m);

// Render call that draws the text shadow
textRenderer.drawWithShadow(matrices, this.overlayMessage, (float)(-n / 2), -4.0f, k | m);```

### Comment 29: Avoma (2022-06-15T10:38:08.865-0700)

This issue has been fixed in 22w24a.

### Comment 30: migrated (2022-06-15T16:53:33.643-0700)

I have a concern with this being fixed in 22w24a, many datapack creators will use custom fonts with /title actionbar to display a custom HUD without the shadow getting in the way, this being fixed will leave no method to do this at the current moment

I'd suggest either the ability to enable/disable the shadow inside the /title command, or the ability to set a font to have a shadow or not have a shadow in the font's json file

### Comment 31: ampolive (2022-07-29T08:27:54.639-0700)

Suggestions should be submitted to the Feedback website.

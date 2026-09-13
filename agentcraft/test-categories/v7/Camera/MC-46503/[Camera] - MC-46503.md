# MC-46503: You can retain entities' shaders by running the "/kill" command while in spectator mode

**Mojira URL:** [https://bugs.mojang.com/browse/MC-46503](https://bugs.mojang.com/browse/MC-46503)

## Report details

- **Mojira categories:** Camera
- **Project:** MC
- **Issue key:** MC-46503
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2014-01-30T10:06:50.512-0800
- **Updated:** 2025-08-12T09:55:07.609-0700
- **Resolution date:** 2025-08-07T04:30:13.022-0700
- **Affects versions:** Minecraft 14w05a; Minecraft 14w34d; Minecraft 1.8; Minecraft 1.8.1-pre3; Minecraft 1.8.8; Minecraft 1.9.3 Pre-Release 1; Minecraft 16w41a; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w08b; Minecraft 19w09a; 1.15.2; 20w20b; 1.16 Pre-release 2; 1.16.3; 1.16.4; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 21w05b; 21w06a; 21w07a; 21w11a; 21w17a; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 1; 1.17.1; 21w38a; 21w39a; 21w40a; 21w41a; 21w42a; 21w43a; 1.18; 1.18.1; 22w03a; 22w05a; 1.18.2 Release Candidate 1; 1.18.2; 22w17a; 1.19; 1.19.1; 1.19.2; 22w43a; 1.19.3; 1.19.4; 1.20; 1.20.1; 24w11a; 1.20.6; 1.21; 1.21.1; 1.21.2 Pre-Release 3; 1.21.3; 1.21.4; 25w08a; 1.21.5; 1.21.6; 1.21.7
- **Fix versions:** Minecraft 14w05b; Minecraft 15w45a; 25w33a
- **Area:** Platform
- **Game mode:** Spectator
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** 2014-01-31_01.05.55.png; 2016-04-22_16.17.23.png; bug2.mp4; MC-46503.mp4; MC-46503.png
- **Issue links:** Duplicate:inward:MC-274577:Shaders of creepers, endermen and spiders in Spectator mode will still be present, even while not spectating the mob | Relates:outward:MC-46594:Debug menu not updating shader description correctly | Bonfire Testing:outward:MC-220842:Opening game mode switcher while spectating a mob with shader effect toggles the effect | Duplicate:inward:MC-271392:Spectator mode bug of F3+F4 | Duplicate:inward:MC-233521:you can get spider vision | Duplicate:inward:MC-296693:Mob POV Effect Persists After Death via /kill in Spectator Mode | Duplicate:inward:MC-201771:/kill while spectator mode causes isssue | Duplicate:inward:MC-145316:Spectator Mode tints stay the same when you die | Duplicate:inward:MC-136498:Mob shaders stuck until another creature is spectated | Relates:inward:MC-46410:Changing gamemode while in the view of a mob in spectator mode does not perform as expected. | Duplicate:inward:MC-112220:Spectator Mode Glitch | Duplicate:inward:MC-101172:Enderman see | Duplicate:inward:MC-53162:Spectator mode glitch/bug. | Relates:inward:MC-47987:Entering a mobs view in spectator mode does not change if world is changed | Duplicate:inward:MC-62967:Keep Shader after /kill command while spectating in mob | Duplicate:inward:MC-46645:Shader is not reset if the spectator host dies | Duplicate:inward:MC-49230:Typing /kill when spectating a mob with a shader effect | Duplicate:inward:MC-46671:Spectator mode | Duplicate:inward:MC-296927:Special effect remains after respawn | Duplicate:inward:MC-298892:Spectator mode retains enderman view if spectating an enderman as it dies from void damage

## Description

The Bug:
You can retain entities' shaders by running the "/kill" command while in spectator mode.
Steps to Reproduce:
- Summon a creeper, switch into spectator mode, and begin spectating it.

- Run the "/kill" command on yourself, respawn, and observe your surroundings.

- Take note as to whether or not you can retain entities' shaders by running the "/kill" command while in spectator mode.

Observed Behavior:
You can retain entities' shaders.
Expected Behavior:
You would not be able to retain entities' shaders.

## Comments (28)

### Comment 1: migrated (2014-01-30T10:06:50.512-0800)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: galaxy_2alex (2014-01-30T10:31:01.420-0800)

Caused by MC-46410
You shouldn't be able to be in Survival mode and be in a mob.

### Comment 3: migrated (2014-01-30T10:47:33.766-0800)

try pressing F4 to clear the shader

### Comment 4: galaxy_2alex (2014-07-23T03:59:37.397-0700)

Reopened and Confirmed for 14w29b
MC-62967

### Comment 5: migrated (2015-11-11T04:22:09.153-0800)

Fixed between 1.8.8 and 15w45a

### Comment 6: migrated (2015-11-11T08:54:57.555-0800)

Fixed somewhere between 1.8.8 and 15w45a.

### Comment 7: migrated (2016-04-22T06:57:26.598-0700)

Reopening because of ​MC-101172
Edit: Nvm, video attached is from 1.8.4
Edit 2: See comment below.

### Comment 8: migrated (2016-04-22T07:18:19.086-0700)

Still have it in 1.9.3-pre1 (enderman at least) (now actually tested it).

### Comment 9: migrated (2016-04-22T07:42:54.473-0700)

So found i the bug?? in 1.9.3-pre1?

### Comment 10: Michael Wobst (2016-10-13T10:43:23.067-0700)

Still an issue with 16w41a. But the bug's reproduce steps aren't right, because as soon as you switch to survival mode, you'll get detached from the mob and the filter resets to normal. For the proper steps/description, see: MC-62967

### Comment 11: migrated (2018-08-25T11:04:46.911-0700)

Confirmed for 1.13.1.

### Comment 12: migrated (2018-09-01T04:59:37.988-0700)

Please, if you don't mind, I'd like to be the reporter of this ticket, it was very outdated. I'll update it accordingly.

### Comment 13: j_p_smith (2020-05-17T13:40:38.850-0700)

Confirmed in 1.15.2 and 20w20b.

### Comment 14: migrated (2020-06-07T06:14:11.307-0700)

Confirmed in 1.16 Pre-release 2.

### Comment 15: migrated (2020-10-13T17:42:34.712-0700)

confirmed for 1.16.3

### Comment 16: Avoma (2020-11-23T03:30:54.441-0800)

Can confirm for 20w46a.
I'd like to request ownership of this report since the reporter has been inactive since October 2018.

### Comment 17: Avoma (2020-11-26T10:32:04.783-0800)

Can confirm in 20w48a.

### Comment 18: Avoma (2020-12-07T09:42:11.213-0800)

Can confirm in 20w49a.

### Comment 19: Avoma (2021-01-28T07:15:15.265-0800)

Can confirm in 21w03a.

### Comment 20: Avoma (2021-02-06T05:46:15.132-0800)

Can confirm in 21w05b.

### Comment 21: Avoma (2021-02-12T05:53:42.595-0800)

Can confirm in 21w06a.

### Comment 22: Avoma (2021-02-19T03:15:02.057-0800)

Can confirm in 21w07a.

### Comment 23: migrated (2021-03-25T13:08:16.070-0700)

Confirmed for 21w11a.

### Comment 24: Avoma (2021-05-01T09:44:19.840-0700)

Can confirm in 21w17a.

### Comment 25: Avoma (2021-06-17T04:44:35.115-0700)

Can confirm in 1.17.

### Comment 26: migrated (2021-06-25T19:00:08.112-0700)

After running /kill, if you toggle perspective two times and then return to first person, the mob shader will disappear and return to normal player view without shader.
This occurs in creepers, endermen, spiders, and cave spiders.

### Comment 27: migrated (2021-08-09T17:09:34.961-0700)

Pressing F4 after doing this will toggle the effect

### Comment 28: MNight_4 (2025-08-12T09:55:07.609-0700)

Man, why… It was fun to use ¬¬

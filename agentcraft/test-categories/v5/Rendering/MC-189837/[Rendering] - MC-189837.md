# MC-189837: Nether fog is dark after rejoining a world that is thunder storming in the Overworld

**Mojira URL:** [https://bugs.mojang.com/browse/MC-189837](https://bugs.mojang.com/browse/MC-189837)

## Report details

- **Mojira categories:** Rendering
- **Project:** MC
- **Issue key:** MC-189837
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-06-15T07:48:13.073-0700
- **Updated:** 2025-11-05T09:47:29.227-0800
- **Resolution date:** 2025-11-05T09:47:29.098-0800
- **Affects versions:** 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16.1; 20w28a; 20w29a; 1.16.2 Pre-release 2; 1.16.2; 1.16.3; 20w49a; 1.16.5; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 3; 1.17.1; 21w38a; 1.18 Pre-release 5; 1.18.1; 1.19.2; 1.20.2; 1.21; 1.21.5; 25w20a
- **Fix versions:** 25w45a
- **Area:** Platform
- **Labels:** rendering
- **Votes:** 3
- **Watchers:** 3
- **Attachments:** 8
- **Attachment filenames:** 2020-12-03_10.03.48.png; crash-2020-06-15_11.24.49-client.txt; crash-2020-06-15_12.50.55-client.txt; dark nether fog.png; MC-189837 - After reloading the world whilst it's thundering in the overworld.png; MC-189837 - Before reloading the world whilst it's thundering in the overworld.png; Nether fog.gif; normal nether fog.png
- **Issue links:** Duplicate:inward:MC-214260:Java 1.16.5 Nether lighting seems like it is stuck on 'Moody". | Duplicate:inward:MC-199273:Nether background appears black | Duplicate:inward:MC-183097:Nether fog is sometimes too dark | Duplicate:inward:MC-192107:Raining in Nether and Nether Fog Darker | Duplicate:inward:MC-298045:Weather changes in the overworld affect the fog in the nether | Duplicate:inward:MC-299544:Black Nether backround | Relates:outward:MC-303836:Nether fog is dark on some systems, except for a brief flash when the weather changes | Relates:outward:MC-303838:The rain overlay renders in the end while the ender dragon fog is present

## Description

What I expected to happen:
When I logged on to a Minecraft world that was thunder storming in the Overworld, I went into the Nether and expected the fog to be the normal color.
What actually happened:
The Nether fog was a lot darker than usual
Steps to Reproduce:
- Create a new world

- Set the weather to rain and thunder({color:#505f79}/weather thunder{color}{color:#172b4d}){color}

- Go into the nether

- Quit the world and enter it again

The nether fog appears a lot darker. This will stay like this until it stops raining in the overworld and you quit and re-enter the world again.

## Comments (24)

### Comment 1: migrated (2020-06-15T07:48:13.073-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: Michael Wobst (2020-06-15T07:56:47.942-0700)

Please force a crash by pressing F3 + C for 10 seconds while in-game and attach the crash report (minecraft/crash-reports/crash-<DATE>-client.txt) here.

### Comment 3: markderickson (2020-06-15T08:27:53.751-0700)

Hey there! Same results here. When looking at the standard nether fog, the RGB color is 56 0 4, but this darkened fog is RGB 15 1 2. The numbers may not be so different, but the color sure is much darker. I'm attaching the crash report for when I crashed the game while in the nether. To be honest, I never would've seen this bug without reading the bug report!

### Comment 4: Michael Wobst (2020-06-15T08:31:25.775-0700)

Please attach the requested crash report as well, .

### Comment 5: gameo7 (2020-06-15T09:52:21.163-0700)

Thank you for letting me know, I attached a crash report ^^

### Comment 6: gameo7 (2020-06-16T06:57:29.373-0700)

Confirmed for 1.16 Pre-Release 6

### Comment 7: markderickson (2020-06-25T19:55:32.983-0700)

Can confirm for 1.16.1.

### Comment 8: markderickson (2020-07-02T09:07:01.144-0700)

Hi there!
Can confirm for 20w27a.

### Comment 9: migrated (2020-08-16T14:02:50.657-0700)

Can confirm for 1.16.2. It does not have to be thundering; regular rain also causes this.

### Comment 10: Pythagoras_314 (2020-09-25T17:01:58.026-0700)

Can confirm for 1.16.3.

### Comment 11: Avoma (2020-12-03T02:05:06.934-0800)

I can confirm in 20w49a. I've attached a screenshot which shows how the fog in a soul sand valley biome, is unusually dark.

### Comment 12: migrated (2021-06-26T17:11:57.126-0700)

Affects 1.17
Relates to   ?

### Comment 13: migrated (2021-06-26T19:22:25.216-0700)

Can confirm in 1.17.1 Pre-release 1.

### Comment 14: migrated (2021-06-30T13:11:19.509-0700)

Can confirm in 1.17.1 Pre-release 3.

### Comment 15: migrated (2021-07-05T14:06:25.771-0700)

Can confirm in 1.17.1 Release Candidate 2.

### Comment 16: migrated (2021-07-06T12:53:18.356-0700)

Can confirm in 1.17.1.

### Comment 17: migrated (2021-09-24T19:17:24.833-0700)

Can confirm in 21w38a.

### Comment 18: migrated (2021-11-20T11:43:44.862-0800)

Can confirm in 1.18 Pre-release 5.

### Comment 19: migrated (2021-12-17T19:43:01.220-0800)

Can confirm in 1.18.1. As stated by Rus Ares above, regular rain also causes this.

### Comment 20: Avoma (2022-10-02T11:20:43.707-0700)

Can confirm in 1.19.2.

### Comment 21: PurPur134 (2023-08-04T13:35:55.147-0700)

Can confirm in 23w31a.

### Comment 22: KirbAvion (2023-11-22T21:30:44.510-0800)

Can confirm in 1.20.2.

### Comment 23: Viradex (2024-07-09T23:30:58.791-0700)

Can confirm in 1.21.

### Comment 24: clamlol (2025-11-05T09:47:29.186-0800)

This has been fixed in 25w45a.

# MC-148795: Ghost blocks can occasionally be created when placing scaffolding too quickly

**Mojira URL:** [https://bugs.mojang.com/browse/MC-148795](https://bugs.mojang.com/browse/MC-148795)

## Report details

- **Mojira categories:** Block states
- **Project:** MC
- **Issue key:** MC-148795
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2019-04-19T10:18:21.598-0700
- **Updated:** 2025-04-30T05:51:25.376-0700
- **Resolution date:** 2023-01-12T15:28:59.251-0800
- **Affects versions:** Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1; 1.14.4; 19w39a; 19w41a; 19w45b; 1.15 Pre-Release 2; 1.15.1; 1.15.2; 20w18a; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w30a; 1.16.2; 1.16.4; 20w45a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w07a; 21w08a; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 1; 1.17.1; 21w37a; 21w38a; 21w39a; 21w41a; 21w42a; 21w43a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 2; 1.18 Pre-release 4; 1.18 Pre-release 5; 1.18; 1.18.1; 22w03a; 22w06a; 1.18.2
- **Fix versions:** 22w11a
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 2019-04-20_00.55.54.png; 2020-12-21_14.45.56.png; javaw 2021-11-17 12-12-45-454.mp4; javaw 2021-11-17 12-12-55-715.mp4; javaw 2021-11-17 12-19-48-484.jpg; javaw 2021-11-17 12-19-57-905.jpg; MC-148795.mp4; MC-148795.png
- **Issue links:** Relates:inward:MC-143167:Scaffolding creates ghost blocks at the height limit | Relates:outward:MC-219875:You can cause a desync when repeatably picking up liquids | Duplicate:inward:MC-142966:Builds two scaffolding blocks when 1 is placed | Duplicate:inward:MC-146893:Scaffolding falling | Duplicate:inward:MC-148963:Scaffolding not falling. After general placing of the block. | Duplicate:inward:MC-149090:Scaffolding block can float in air | Duplicate:inward:MC-149107:Scaffolding | Duplicate:inward:MC-149317:Scaffolding Floats and Deletes Blocks When Placing | Duplicate:inward:MC-149348:Scaffolding | Duplicate:inward:MC-149807:.. | Duplicate:inward:MC-149810:bugged scaffolding | Duplicate:inward:MC-150619:Баг с подмостками(строительными лесами) | Duplicate:inward:MC-150890:Scaffolding bug | Duplicate:inward:MC-151020:Floating scaffolding. | Duplicate:inward:MC-151872:You can place scaffolding in the air without any support | Duplicate:inward:MC-152620:Bug with scaffolding | Duplicate:inward:MC-153692:Quickly placing scaffolding will create fake scaffolding | Duplicate:inward:MC-154067:Spamming Scaffolding fast creates floating Scaffolding Block | Duplicate:inward:MC-155341:Travelling, by levitating scaffolding. | Duplicate:inward:MC-155852:"Phantom" Scaffolding | Duplicate:inward:MC-156634:Bug Scaffoldings (they fly) | Duplicate:inward:MC-162254:Floating Scaffolding | Duplicate:inward:MC-162734:Floating scaffolding | Duplicate:inward:MC-163433:flying scraffolding | Duplicate:inward:MC-167005:Flying scaffolding | Duplicate:inward:MC-167168:Scaffolding remains flying | Duplicate:inward:MC-168696:Server kick for Flying because of Scaffolding | Duplicate:inward:MC-171508:Fly'ing scaffolding | Duplicate:inward:MC-171527:Ошибка с подмостками | Duplicate:inward:MC-173341:Scaffolding creates a glitch that lets you make a bridge in the air, and when you die you get all the blocks back | Duplicate:inward:MC-175558:Scaffolding can be placed in midair | Duplicate:inward:MC-176754:Scaffholding flying | Duplicate:inward:MC-177484:Ghost scaffolding able to be placed on mid-air | Duplicate:inward:MC-180725:Flying scaffolding | Duplicate:inward:MC-182279:Floating scaffolding | Duplicate:inward:MC-184691:Scaffolding glitch | Duplicate:inward:MC-188369:Scaffolding vanishing client side | Duplicate:inward:MC-190751:Levitating scaffolding | Duplicate:inward:MC-198037:Scaffolding fly glitch | Duplicate:inward:MC-204964:some times scafondin floats | Duplicate:inward:MC-205531:Ghost Scaffoldings | Duplicate:inward:MC-209257:You can fly but not really. | Duplicate:inward:MC-215435:if u place build up and place a scafholding next to 4 scafholding on a side if u keep doing it it will create a gost block wich u can walk on air | Duplicate:inward:MC-217154:Flight bug with scaffolding | Duplicate:inward:MC-228515:Phantom Scaffolding | Duplicate:inward:MC-228914:Placing Horizontal Scaffolding Via Shortcut Makes Gap Plus Ghost Scaffold | Duplicate:inward:MC-235580:Ghost Scaffolding | Duplicate:inward:MC-241719:Floating scaffolding can generate in 1.18 Pre-release 2 and can be moved around. | Duplicate:inward:REALMS-3003:I found a way to place scaffolding in the air.

## Description

The Bug:
Ghost blocks can occasionally be created when placing scaffolding too quickly.
Steps to Reproduce:
- Place down some scaffolding really quickly.

- Take note as to whether or not ghost blocks can occasionally be created when placing scaffolding too quickly.

Observed Behavior:
Ghost blocks can occasionally be created when placing scaffolding too quickly.
Expected Behavior:
Ghost blocks would not be able to occasionally be created when placing scaffolding too quickly.

## Comments (34)

### Comment 1: migrated (2019-04-19T10:18:21.598-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2019-05-01T13:50:11.491-0700)

Can confirm. This can be easily reproduced by changing your controls to use a keyboard key instead of a mouse button to place down blocks. When holding down that key while building scaffolding, the issue occasionally occurs.

### Comment 3: migrated (2019-10-11T09:58:11.752-0700)

I can confirm this is still an issue on 19w41a.

### Comment 4: migrated (2020-05-04T14:01:20.816-0700)

Confirmed for latest snap - 20w18a

### Comment 5: migrated (2020-06-17T08:15:57.018-0700)

Confirmed in 1.16 pre-release 7
when a flying scaffolding is updated, he disappears but don't drop item
edit: but place a ghost scaffolding don't use item

### Comment 6: migrated (2020-10-29T13:31:07.712-0700)

Confirmed in 1.16.3 and 1.16.4 Release Candidate 1
In the 1.16.4 Release Candidate, if you click fast enough, you can create multiple ghost blocks.

### Comment 7: migrated (2020-11-10T11:12:51.935-0800)

and my report is gona be a copy

### Comment 8: Sebexan (2020-12-21T05:44:07.005-0800)

in 20w51a

### Comment 9: Avoma (2021-01-22T12:11:34.461-0800)

Can confirm in 21w03a.

### Comment 10: Sebexan (2021-02-05T05:50:19.874-0800)

I can confirm for 21w05b

### Comment 11: Sebexan (2021-02-11T07:39:53.196-0800)

in 21w06a

### Comment 12: Sebexan (2021-02-17T11:14:36.354-0800)

I can confirm for 21w07a

### Comment 13: Sebexan (2021-02-24T12:04:45.159-0800)

I can confirm for 21w08a

### Comment 14: Sebexan (2021-03-11T05:23:04.802-0800)

I can confirm for 21w10a

### Comment 15: Sebexan (2021-03-18T03:19:36.840-0700)

I can confirm for 21w11a

### Comment 16: Sebexan (2021-03-31T14:02:41.143-0700)

I can confirm for 21w13a

### Comment 17: Sebexan (2021-04-07T08:33:00.266-0700)

I can confirm for 21w14a

### Comment 18: Avoma (2021-04-10T05:58:55.928-0700)

I'd like to request ownership of this ticket since the current reporter has been inactive since April 2019. I'm willing to provide all of the necessary information and will keep this report updated.

### Comment 19: Sebexan (2021-04-14T11:24:21.067-0700)

I can confirm for 21w15a

### Comment 20: Sebexan (2021-04-21T11:58:07.542-0700)

I can confirm for 21w16a

### Comment 21: Sebexan (2021-05-12T06:42:26.975-0700)

I can confirm for 21w19a

### Comment 22: Sebexan (2021-05-19T10:34:25.442-0700)

I can confirm for 21w20a

### Comment 23: Sebexan (2021-05-27T07:05:39.843-0700)

I can confirm for 1.17 Pre-release 1

### Comment 24: Sebexan (2021-05-31T10:27:29.257-0700)

I can confirm for 1.17 Pre-release 2

### Comment 25: migrated (2021-11-17T04:30:33.473-0800)

this is also in 1.18 pre-release 2

### Comment 26: migrated (2021-11-17T04:38:50.998-0800)

you can also by the way move the ghost bocks around by right-clicking while holding scaffolding in your main hand which is pretty weird.

I posted my videos to check that out

### Comment 27: migrated (2021-11-18T03:08:03.462-0800)

This is in 1.18 pre-release 3

### Comment 28: migrated (2021-11-18T03:14:23.845-0800)

confirm for 1.18 pre-release 4

also, you can use them as normal blocks and stand on them in survival mode and if you use the keyboard buttons instead of mouse buttons then you can create a big giant line of ghost blocks without needing support

### Comment 29: migrated (2021-11-20T04:42:26.340-0800)

can confirm for 1.18 pre-release 5

### Comment 30: migrated (2021-12-03T04:13:54.555-0800)

Mojang knows about this report but still hasn't fixed this for some reason.

### Comment 31: migrated (2022-01-09T12:44:26.833-0800)

Had a couple players kicked for flying while using scaffolding on my 1.18.1 server.
Both times players logged back in to have fallen to their deaths

### Comment 32: migrated (2022-05-05T13:01:29.038-0700)

Unable to reproduce, even with auto-clicker.
I think this issue depends on hardware read/write speed.

### Comment 33: Sebexan (2022-05-05T15:15:58.620-0700)

Not sure but fixed on 22w11a due to improvement

### Comment 34: Avoma (2023-01-12T04:43:16.940-0800)

This issue was present in 1.18.2, but no longer occurs in versions above or equal to 22w11a . With this being said, this issue has been fixed in 21w11a.
I tried to reproduce this in 22w11a for over ten minutes while having placed over 500 blocks of scaffolding without success. In 1.18.2, I was able to reproduce this problem within seconds, so I'm confident in saying that the issue here has been resolved in 22w11a.

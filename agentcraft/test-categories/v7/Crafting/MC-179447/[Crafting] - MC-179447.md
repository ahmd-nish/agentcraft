# MC-179447: More than six banner patterns can be added to a banner

**Mojira URL:** [https://bugs.mojang.com/browse/MC-179447](https://bugs.mojang.com/browse/MC-179447)

## Report details

- **Mojira categories:** Crafting
- **Project:** MC
- **Issue key:** MC-179447
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-04-19T06:08:50.089-0700
- **Updated:** 2025-05-29T09:18:24.314-0700
- **Resolution date:** 2022-07-21T09:58:48.759-0700
- **Affects versions:** 1.15.2; 20w16a; 20w17a; 20w18a; 1.16.4; 20w45a; 20w46a; 1.17.1; 1.18.1; 22w06a
- **Fix versions:** 22w18a
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** Screenshot 2022-07-21 011344.png; Screenshot 2022-07-21 011746.png

## Description

The bug
It's possible to add more banner patterns after the making the 6th one by putting a different banner in the loom UI, pressing one of the banner patterns and swapping it to the banner that has 6 patterns and then you have a 7th banner pattern that isn't the ominous banner.
How to reproduce
- Create a banner with 6 patterns.

- On a second banner, select another pattern

- Without taking the second banner out of the right side of the GUI, swap in the first banner
 The 7th pattern should now be applied to first banner.

Videos:
- https://b23.tv/BV1Pg4y1z7Sv

- https://www.youtube.com/watch?v=qPkcEQNsEVg

## Comments (16)

### Comment 1: migrated (2020-04-19T06:08:50.089-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: marcono1234 (2020-04-20T08:13:33.247-0700)

Please either upload the video here or link to a more common video host, e.g. YouTube

### Comment 3: ZYX_2D (2020-04-21T17:48:56.604-0700)

@[Mod] Marcono1234
It's almost impossible 4 me 2 visit YT since I'm Chinese, but I can try 2 reproduce this sense. If successful, I'll upload a video recorded by myself here.

### Comment 4: migrated (2020-04-21T19:40:47.288-0700)

Can confirm on bug in 1.15.2. I'll record a short video and show the process.

### Comment 5: migrated (2020-04-21T19:50:52.252-0700)

Steps to reproduce:
1. Create a banner with 6 patterns.
2. On a second banner, select another pattern
3. Without taking the second banner out of the right side of the GUI, swap in the first banner
4. The 7th pattern should now be applied to first banner.
Using the same bug you can get more than 7 patterns as well

### Comment 6: migrated (2020-04-21T20:02:13.461-0700)

Here is the video:  https://www.youtube.com/watch?v=qPkcEQNsEVg

### Comment 7: migrated (2020-04-21T20:13:07.845-0700)

Can confirm. I have rewritten the ticket.

### Comment 8: migrated (2021-02-18T11:52:29.789-0800)

Apperantly you can theoretically add an infinite amount of patterns to the banner, however if you have more than 6 patterns, it will only ever show a maximum of 6 patters when hovering over it in the inventory.

### Comment 9: migrated (2021-08-24T08:00:16.060-0700)

Can confirm in 19w02a
Can confirm in 1.17.1

### Comment 10: anthony cicinelli (2021-08-24T08:02:00.214-0700)

there is no need to confirm reports in older version such as 19w02a just 1.17.1 is fine

### Comment 11: migrated (2022-02-09T16:23:43.014-0800)

Can confirm in 22w06a.

### Comment 12: SoloAlguien (2022-02-21T00:26:08.306-0800)

Can confirm in 1.18.1.

### Comment 13: migrated (2022-07-20T16:26:34.125-0700)

This bug was fixed in 22w18a

### Comment 14: migrated (2022-07-20T16:40:57.766-0700)

as much as I want this bug to stay as a "feature" when you are in creative, sadly this is confirmed fixed

### Comment 15: ZYX_2D (2022-07-20T17:09:15.883-0700)

@Howard
Nothing cannot be solved by commands.

### Comment 16: markderickson (2022-07-21T09:58:48.758-0700)

I can confirm that this has been fixed.

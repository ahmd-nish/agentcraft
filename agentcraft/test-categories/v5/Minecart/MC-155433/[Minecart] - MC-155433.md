# MC-155433: Minecart with hopper not picking matching items from a mixed pile

**Mojira URL:** [https://bugs.mojang.com/browse/MC-155433](https://bugs.mojang.com/browse/MC-155433)

## Report details

- **Mojira categories:** Minecart
- **Project:** MC
- **Issue key:** MC-155433
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2019-06-27T03:59:23.377-0700
- **Updated:** 2025-03-25T12:32:15.377-0700
- **Resolution date:** 2023-01-18T11:51:16.501-0800
- **Affects versions:** Minecraft 1.14.3; 1.17.1 Release Candidate 1; 1.17.1; 1.19.3 Pre-release 2; 1.19.3 Pre-release 3
- **Fix versions:** 23w03a
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** 2019-06-27_12.34.59.png; 2019-06-27_12.36.26.png; 2019-06-27_12.37.42.png; 2021-07-02 18-05-23.mp4; MC-155433.zip

## Description

Minecarts with hopper with items in all slots but enough room to stack more of that kind of item, eventually fail to pick up matching items from the ground when other (not matching) items are present together with the matching ones.

Reproducing:
- Create a powered rail track. Create a pile of items: about 20 stacks of stone and about 8 other "junk" items (in screenshot: cauldron, water bucket, comparator, repeater, redstone dust, observer, red terracotta) within a single block on the rail track - attached screenshot 2019-06-27_12.36.26

- Summon a minecart containing 5 blocks of stone in its 5 slots onto the track ( /summon hopper_minecart 61 57 95 {Items:[ {Slot:0,id:"minecraft:stone",Count:1b},{Slot:1,id:"minecraft:stone",Count:1b},{Slot:2,id:"minecraft:stone",Count:1b},{Slot:3,id:"minecraft:stone",Count:1b},{Slot:4,id:"minecraft:stone",Count:1b}]} ) , screenshot 2019-06-27_12.34.59 and let it drive through the pile

- Repeat step 2. about 5 times.

Since the minecarts have room for 5*63 items, all the stone should be sucked up. Instead, first 2-4 minecarts behave as expected (filling up with stone) but after that and with all consecutive minecarts we have the situation from screenshot 2019-06-27_12.37.42 - the minecart drove through the pile without changing contents, the stone is still present on the rail.  You can even stop a minecart right on top of the pile of items and it will still fail to suck anything in.
This is not 100% repeatable - may be a matter of performance. The more of the 'base item' is there the more likely it happens; with 12 stacks happened never, but with 40 always; 20 stacks is about 80% cases.

## Comments (7)

### Comment 1: migrated (2019-06-27T03:59:23.377-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: migrated (2021-05-30T02:50:42.473-0700)

This is interesting, I wonder if you can pick those items left on rail. Maybe this bug was caused by the same reason as Bedrock Edition have.

### Comment 3: migrated (2021-05-30T08:02:15.443-0700)

Yes, you can; a minecart without items in it will pick them too - after picking the "non-matching" ones first.

### Comment 4: osfanbuff63 (2021-06-18T03:55:58.607-0700)

Is this still an issue in the latest version (1.17)? Also, could you attach a video?
If you are on Windows, you can use Windows+Alt+R to open a built-in app for recording game footage.
If you are on Mac (Mojave or later), you can use Shift+Command+5 to open a built-in app for recording your screen.
In case you don't have a program to record videos, we recommend using the free recording software OBS.
In case the resulting video file is too large to be uploaded to the bug tracker directly, please upload it elsewhere (e.g. as unlisted video on YouTube) and link to it here.
This issue is being temporarily closed as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 5: ampolive (2021-07-02T14:03:16.541-0700)

Can confirm this still happens in 1.17.1 Release Candidate 1.

### Comment 6: migrated (2021-07-03T01:24:42.006-0700)

Attached a test world download. Instructions on signs.
Add or remove items to the lower of two chests (varied items, not more of same type) to make the effect more pronounced or weaker.

### Comment 7: migrated (2023-01-18T11:51:16.501-0800)

Was there an "order" that the items had to be picked up in then?

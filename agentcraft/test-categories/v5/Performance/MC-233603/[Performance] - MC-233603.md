# MC-233603: HUD / Hotbar rendering can heavily impact frame rate performance

**Mojira URL:** [https://bugs.mojang.com/browse/MC-233603](https://bugs.mojang.com/browse/MC-233603)

## Report details

- **Mojira categories:** Performance
- **Project:** MC
- **Issue key:** MC-233603
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2021-08-01T22:41:01.228-0700
- **Updated:** 2025-04-26T13:43:49.898-0700
- **Resolution date:** 2024-08-17T12:48:05.855-0700
- **Affects versions:** 1.17.1; 1.18.1; 22w06a; 1.18.2; 22w11a; 22w12a; 22w16b; 22w19a; 1.19 Pre-release 4; 1.19; 22w24a; 1.19.2; 1.19.3 Pre-release 2; 1.19.3; 23w04a; 23w05a; 23w06a; 1.19.4 Pre-release 1; 1.19.4; 23w16a; 23w18a; 1.20.1; 23w31a; 1.20.2; 23w44a; 1.21.1
- **Fix versions:** 24w33a
- **Labels:** hotbar
- **Watchers:** 1
- **Attachments:** 13
- **Attachment filenames:** 2021-08-01_21.05.00.png; 2021-08-01_21.05.42.png; 2022-03-23_15.02.47.png; 2022-03-23_15.02.54.png; 2022-03-23_15.03.04.png; 2022-05-13_19.11.58.png; 2022-05-13_19.13.59.png; 2022-05-13_19.18.17.png; 2022-05-13_19.18.50.png; 2024-08-17_12.26.14.png; hearts_1.png; hearts_2.png; MC-233603_1.18.1.mp4
- **Issue links:** Relates:outward:MC-249635:Text rendering has a considerable impact on performance | Duplicate:inward:MC-231504:Performance issues with the GUI

## Description

The game experiences a large frame rate decrease when there's a large amount of HUD/hotbar elements displayed on the screen, in this case hearts. I assume this is also the case with other elements like the hunger, armor, and oxygen icons, but only noticeable with hearts due to the use of certain effects (health boost & absorption) at high amplifiers, as well as with the use of the max_health attribute. Fairly small example:

As can be seen in the images the performance hit is somewhat high just for a few more hearts added to the screen. Apparently each element (heart/hunger/defense icon) is counted as a draw call, and this number can increment in certain survival scenarios, making rendering of a simple status bar resource intensive. Even more intensive if items are rendered on the slots (MC-233604).
I considered this a different issue from  for two reasons:
- There aren't any uninteded effects at high amplifiers gameplay-wise, and can be reproduced with the max_health attribute, not only effects.

- This is a performance concern with something as simple as the HUD, which as i said before can be reproduced in a survival setting.

While this issue might not be very noticeable in vanilla at first hand, some servers and datapacks make use of high health effects, making this issue very apparent. Here you can see the worst case scenario to demonstrate how it can impact frame rate times:

You can only imagine how many draw calls are being made here to end up with these frame times in a void world. You can also check the attachments for more examples. Word from some modders say that this can be mitigated by applying batching when rendering the status bar.
How to reproduce
- Create a void world, and run either one or both of the next commands.

-

```
/effect give @s minecraft:absorption 100 255 true
```

-

```
/attribute @s minecraft:generic.max_health base set 1000
```

- Press ALT+F3 and notice the lag on the FPS graph.

## Comments (10)

### Comment 1: migrated (2021-08-01T22:41:01.228-0700)

This comment contained multiple image attachments (13), please login to view the attachments.

### Comment 2: anthony cicinelli (2021-08-02T13:02:43.677-0700)

Thank you for your report!
We're tracking this issue as MC-10755, so this ticket is being resolved and linked as a duplicate.
That ticket has already been resolved as Won't Fix, which means this is considered a bug but won't be fixed. The description of that ticket or the comments might explain the rationale. Please do not leave a comment on the linked ticket.
If you haven't already, you might like to make use of the search feature to see if the issue has already been mentioned.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: syarumi (2021-08-02T17:33:35.026-0700)

You could say it is a duplicate, but i'd argue that in this case it is different because these two effects, unlike the other ones, can effectively cause client-side performance degradation and even in some cases it could crash the game, i can see this being the case on servers where this can't be controlled by the player directly.
From what i understand, i think  is more tied to the gameplay perspective (due to how high levels of effects don't work as intended). While here we're talking of the performance perspective, because the more rows of hearts are shown, the worse. It can even apply on low levels like 10 or 5, but the degradation isn't as drastic. So i don't think it would be correct to close it as a dupe.

### Comment 4: ampolive (2021-08-02T17:38:04.970-0700)

This was previously reported as MC-231504, and it was marked as a duplicate of .

### Comment 5: syarumi (2021-08-02T17:41:24.593-0700)

i've checked, yeah, it seems i couldn't find it when searching, but my point on my previous comment still stands.

### Comment 6: syarumi (2021-10-22T22:21:30.117-0700)

After some time of thinking, i still think this should be reopened, same reasons as my previous comment above.
Also, another reason as to why this is not a duplicate is that this issue can be reproduced without status effects, as you only need to use the /attribute command to change the max_health value to the max value.
I haven't seen a statement on which attributes with the max value aren't supported, and it's also even used for datapacks.

### Comment 7: migrated (2021-12-19T15:55:50.366-0800)

Can confirm on 1.18.1

### Comment 8: migrated (2022-06-16T11:20:09.981-0700)

How is this duplicate of

### Comment 9: ampolive (2022-06-16T11:24:03.465-0700)

See this comment. It was resolved as a duplicate because there is no way to verify this without giving yourself effects/attributes way above the default values. However, this is now considered to be a separate issue.

### Comment 10: syarumi (2024-08-17T12:37:10.822-0700)

This seems to be fixed in 24w33a.

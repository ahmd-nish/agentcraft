# MC-307585: The `fall_after_explosion` advancement trigger does not work with TNT anymore

**Mojira URL:** [https://bugs.mojang.com/browse/MC-307585](https://bugs.mojang.com/browse/MC-307585)

## Report details

- **Mojira categories:** Advancements
- **Project:** MC
- **Issue key:** MC-307585
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2026-04-16T14:33:16.006-0700
- **Updated:** 2026-05-07T23:07:12.463-0700
- **Resolution date:** 2026-05-07T23:07:12.357-0700
- **Affects versions:** 26.1.2
- **Fix versions:** 26.2 Snapshot 7
- **Area:** Platform HC
- **Votes:** 4
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** tnt test 1.21.11-26.1.zip; We_Have_Liftoff_1_21_11.mp4; We_Have_Liftoff_26_1_x.mp4

## Description

Affected Versions: 26.1+

In snapshot 24w12a for the Minecraft Update 1.20.5 a new advancement trigger was added called 'fall_after_explosion'. Internally, it was used for the Who Needs Rockets? advancement which was to launch yourself 8 blocks or higher using wind charges. For datapacks, it allowed to detect using TNT cannons to launch yourself upwards, which is exactly what the BlazeandCave's Advancement Pack did. The advancement pack added an advancement called "We Have Liftoff!" to launch yourself 100 blocks upwards using TNT, clearly implying the use of TNT cannons to achieve the goal. Below you may find the difference in triggers between Who Needs Rockets? and We Have Liftoff!

Who Needs Rockets?
        "trigger": "minecraft:fall_after_explosion",
        "conditions": {
            "cause": [
                {
                    "condition": "minecraft:entity_properties",
                    "entity": "this",
                    "predicate": {
                        "type": "minecraft:wind_charge"
                    }
                }
            ],
            "distance": {
                "y": {
                    "min": 8.0

We Have Liftoff!
        "trigger": "minecraft:fall_after_explosion",
        "conditions": {
            "cause": [
                {
                    "condition": "minecraft:entity_properties",
                    "entity": "this",
                    "predicate": {
                        "type": "minecraft:tnt"
                    }
                }
            ],
            "distance": {
                "y": {
                    "min": 100.0

As you can see, the difference is very minimal.

Steps to reproduce:
You may replicate this advancement in your world in one of the 3 ways:
1) Use the custom datapack attached to this bug report compatbile with both Minecraft 1.21.11 and 26.1
2) Change the Who Needs Rockets advancement to be 1:1 We Have Liftoff
3) Download the BlazeandCave’s Advancement Pack 1.20.2 for Minecraft 1.21.11 and BlazeandCave’s Advancement Pack 1.20.3 for Minecraft 26.1.x
After you have chosen a method, follow these steps to reproduce the issue:

1) Create a world with the attached datapack, modified advancement, or the BlazeandCave’s Advancement Pack in Minecraft version 1.21.11;
2) Recreate the following contraption as shown in the video attached;
3) Create a world with the attached datapack, modified advancement, or the BlazeandCave’s Advancement Pack in Minecraft version 26.1;
4) Recreate the following contraption as shown in the video attached.

Expected Behaviour:
Upon the Player launching themselves in the air, they get the advancement in both versions of the game

Observed Behaviour:
The Player only gets the advancement to trigger in an earlier version

Key notes:
a) the trigger has not changed since its release in 1.21
b) the trigger only does not work for TNT rather than Wind Charges as you are still able to obtain the vanilla advancement on the latest version

## Comments (1)

### Comment 1: Automation for Jira (2026-04-16T14:33:27.715-0700)

Thank you for helping us improve Minecraft! We saved your files:

# MC-250943: minecraft.used:minecraft.goat_horn doesn't increase when using goat horns

**Mojira URL:** [https://bugs.mojang.com/browse/MC-250943](https://bugs.mojang.com/browse/MC-250943)

## Report details

- **Mojira categories:** Statistics
- **Project:** MC
- **Issue key:** MC-250943
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-04-27T10:06:57.587-0700
- **Updated:** 2025-04-30T06:26:13.948-0700
- **Resolution date:** 2022-11-04T02:02:48.860-0700
- **Affects versions:** 22w17a; 22w18a; 22w19a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19; 1.19.1 Pre-release 1; 1.19.1 Pre-release 2; 1.19.1 Pre-release 5; 1.19.1; 1.19.2
- **Fix versions:** 22w42a
- **Labels:** goat_horn
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** MC-250943.mp4; MC-250943.png; MC-250943 - Current Code.png; MC-250943 - Fixed Code.png

## Description

The Bug:
minecraft.used:minecraft.goat_horn doesn't increase when using goat horns.
Steps to Reproduce:
- Create a scoreboard objective for tracking the use of a goat horn and set it to display on the sidebar.

```
/scoreboard objectives add UseGoatHorn minecraft.used:minecraft.goat_horn
```

```
/scoreboard objectives setdisplay sidebar UseGoatHorn
```
- Obtain a goat horn and use it.

- Take note as to whether or not minecraft.used:minecraft.goat_horn increases when using goat horns.

Observed Behavior:
The scoreboard doesn't increase.
Expected Behavior:
The scoreboard would increase.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.19 Pre-release 2 using Mojang mappings.
net.minecraft.world.item.InstrumentItem.java

```
public class InstrumentItem extends Item {
   ...
   @Override
      public InteractionResultHolder<ItemStack> use(Level level, Player player, InteractionHand interactionHand) {
         ItemStack itemStack = player.getItemInHand(interactionHand);
         Optional<Holder<Instrument>> optional = this.getInstrument(itemStack);
         if (optional.isPresent()) {
            Instrument instrument = optional.get().value();
            player.startUsingItem(interactionHand);
            InstrumentItem.play(level, player, instrument);
            player.getCooldowns().addCooldown(this, instrument.useDuration());
            return InteractionResultHolder.consume(itemStack);
         }
         return InteractionResultHolder.fail(itemStack);
      }
      ...
```
If we look at the above class, we can see that the awardStat() method (the method responsible for incrementing player statistics) is never called throughout this piece of code, thus making minecraft.used:minecraft.goat_horn not increase when using goat horns.
Fix:
Simply calling the awardStat() method where appropriate within this piece of code will resolve this problem. The following line of code can be used to fix this issue.

```
player.awardStat(Stats.ITEM_USED.get(this));
```

## Comments (9)

### Comment 1: migrated (2022-04-27T10:06:57.587-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2022-06-09T21:12:05.482-0700)

I got the same problem

### Comment 3: migrated (2022-06-24T05:07:19.235-0700)

Yep I found the same bug while testing, I hope this gets fixed quickly

### Comment 4: migrated (2022-07-04T00:33:42.292-0700)

I also had same problem. I was using command and goat horn with scoreboard, but it didn't work. I hope this could be fixed in 1.19.1.

### Comment 5: migrated (2022-07-27T13:13:20.643-0700)

Same problem, this issue is also present in 1.19.1

### Comment 6: PokeJake1127 (2022-08-06T12:42:48.700-0700)

Can confirm in 1.19.2, I really hope they fix this swiftly.

### Comment 7: Avoma (2022-10-04T10:01:17.840-0700)

Following on from my code analysis, I've double-checked my proposed fix and I can confidently confirm that it's fully functioning and works as expected, so I've attached two screenshots to this report, one of which shows the current code and the other that shows the fixed code. I feel this information may be quite insightful hence my reasoning for providing it.

### Comment 8: migrated (2022-11-03T20:17:07.910-0700)

Hi, just wanted to confirm I experience the bug as well in 1.19.2.
Set up a scoreboard objective to test for 'minecraft.used:minecraft.goat_horn' and the score does not increase after using a goat horn.
The number of times used in statistics also does not increase for goat horns.
Hope this gets fixed soon!

### Comment 9: migrated (2022-11-04T02:02:48.860-0700)

This is already fixed in the snapshots.

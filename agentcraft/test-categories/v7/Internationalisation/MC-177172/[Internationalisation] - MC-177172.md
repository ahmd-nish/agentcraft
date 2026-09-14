# MC-177172: Dash in villager/trader UI is hardcoded / untranslatable

**Mojira URL:** [https://bugs.mojang.com/browse/MC-177172](https://bugs.mojang.com/browse/MC-177172)

## Report details

- **Mojira categories:** Internationalisation; Text
- **Project:** MC
- **Issue key:** MC-177172
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-04-02T14:00:05.251-0700
- **Updated:** 2025-04-30T03:37:09.245-0700
- **Resolution date:** 2023-09-01T04:26:30.872-0700
- **Affects versions:** 1.15.2; 20w14a; 20w15a; 20w16a; 20w17a; 20w18a; 20w19a; 20w20a; 20w20b; 20w21a; 20w22a; 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 5; 1.16 Pre-release 6; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 21w05a; 21w06a; 21w07a; 21w08a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 2; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Release Candidate 1; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 21w37a; 21w38a; 21w40a; 21w41a; 21w42a; 21w43a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 4; 1.18 Release Candidate 3; 1.18; 1.18.1 Release Candidate 2; 1.18.1; 22w03a; 22w05a; 22w06a; 22w07a; 1.18.2 Pre-release 2; 1.18.2 Pre-release 3; 1.18.2 Release Candidate 1; 1.18.2; 22w11a; 22w13a; 22w15a; 22w17a; 22w18a; 22w19a; 1.19 Pre-release 1; 1.19 Pre-release 2; 1.19 Pre-release 3; 1.19; 1.19.1 Pre-release 2; 1.19.1 Release Candidate 2; 1.19.2; 22w44a; 1.19.4 Pre-release 3; 1.19.4; 23w12a; 23w13a; 23w18a; 1.20 Pre-release 1; 1.20 Pre-release 4; 1.20 Pre-release 5; 1.20 Pre-release 6; 1.20 Pre-release 7; 1.20 Release Candidate 1; 1.20; 1.20.1 Release Candidate 1; 1.20.1; 23w31a; 23w32a; 23w33a
- **Fix versions:** 1.20.2 Pre-release 1
- **Labels:** gui; text; trade-gui
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2020-04-02_14.54.31.png
- **Issue links:** Relates:outward:MC-119873:The text used for the credits button within the title screen is untranslatable

## Description

The Bug
The dash / separator between the villager's profession and level is untranslatable in the trade GUI.
Among other things, this means resource packs are unable to alter this part of the interface. This is particularly jarring with packs that recolour text.
Expected Result
The dash / separator would be translatable.
Note:
Even better: "<profession> - <career level>" should be translatable (%s - %s), so that languages can change the word order and spacing if needed
Code analysis (tentative)
net.minecraft.client.gui.screens.inventory.MerchantScreen.java (Mojang mappings, 1.18, variable renaming)

```
...
private static final Component LEVEL_SEPARATOR = new TextComponent(" - ");
...
protected void renderLabels(PoseStack poseStack, int a, int b) {
        int traderLevel = ((MerchantMenu)this.menu).getTraderLevel();
        if (traderLevel > 0 && traderLevel <= 5 && ((MerchantMenu)this.menu).showProgressBar()) {
            MutableComponent traderLabel = this.title.copy().append(LEVEL_SEPARATOR).append(new TranslatableComponent("merchant.level." + traderLevel));
            ...
        }
    ...
    }
...
```
LEVEL_SEPARATOR should be a TranslatableComponent instead of a hardcoded TextComponent.

## Comments (9)

### Comment 1: migrated (2020-04-02T14:00:05.251-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: SeaOfPixels (2020-06-04T19:01:39.866-0700)

Would LOVE to see this fixed. You should probably reword this and say that the dash in the villager GUI is hardcoded

### Comment 3: migrated (2020-09-09T19:17:49.313-0700)

What you mean with this issue?

### Comment 4: Cultist_O (2020-09-10T06:15:53.846-0700)

I mean:
Most in-game text is "translatable", which is to say: There are text files (language files), which tell the game what word to put there. So if you set your language to Russian, the text in the screenshot would say "Картограф - Новичок" instead of "Cartographer - Novice". You can make your own language files for your own language if it isn't supported, or you just want to change a couple things. Maybe for a resource pack that changes hoes to scythes, you could change the translation to "wooden scythe". You can even change the colour in these files, so the text at the top of the trade GUI would look blue for example, instead of Grey.
Now the problem: "Cartographer" can be translated (just by changing "merchant.level.1" to whatever you want in the file), and "Novice" can be translated ("entity.minecraft.villager.cartographer"). The dash that separates them however, cannot be.
What this means: If for some reason, a language used hyphens diferently, they would be unable to change this part of the text. Furthermore, if you want to make the text in the trade UI green, there would be no way to change the hyphen, and it would say "Cartographer - Novice" (The colour thing can be important for resource packs that change the colour of this GUI, as dark grey might not be as visible.)

### Comment 5: ampolive (2021-11-30T15:40:00.463-0800)

Can confirm.

### Comment 6: Avoma (2022-01-12T10:49:02.563-0800)

Can confirm in 1.18.1.

### Comment 7: bodakugga (2022-03-08T05:30:02.286-0800)

Just a note for Mojang so that they can fix it properly: the complete string "<profession> - <career level>" should be translatable (%s - %s), so that languages can change the word order or spacing if needed. You might want to write that in the OP.

### Comment 8: Avoma (2022-06-26T11:37:30.386-0700)

Can confirm in 1.19.

### Comment 9: Avoma (2022-09-06T10:26:20.396-0700)

Can confirm in 1.19.2.

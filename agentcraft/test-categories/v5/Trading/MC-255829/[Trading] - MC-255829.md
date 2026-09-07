# MC-255829: Villager trades air if it has a totem of undying trade and uses the held totem

**Mojira URL:** [https://bugs.mojang.com/browse/MC-255829](https://bugs.mojang.com/browse/MC-255829)

## Report details

- **Mojira categories:** Trading
- **Project:** MC
- **Issue key:** MC-255829
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-09-09T12:03:53.852-0700
- **Updated:** 2025-04-29T09:37:34.623-0700
- **Resolution date:** 2024-05-05T12:51:32.610-0700
- **Affects versions:** 1.19.2; 22w42a; 22w43a; 22w44a; 22w45a; 22w46a; 1.19.3 Pre-release 2; 1.19.3 Release Candidate 1; 1.19.3; 23w03a; 23w04a; 1.19.4 Pre-release 1; 1.19.4 Pre-release 3; 1.19.4; 23w12a; 23w13a; 23w14a; 23w16a; 23w17a; 23w18a; 1.20 Pre-release 1; 1.20 Pre-release 2; 1.20 Pre-release 4; 1.20 Pre-release 5; 1.20 Pre-release 6; 1.20 Pre-release 7; 1.20 Release Candidate 1; 1.20; 1.20.1; 23w31a
- **Fix versions:** 1.20.2 Pre-Release 3
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** Villager trading air.png; Villager trading totem.png
- **Issue links:** Relates:inward:MC-271598:Killing a villager while it offers a Totem of Undying uses the totem and removes it from its hand

## Description

If you hold an item that the villager is buying, it will hold out an item that its selling corresponding to the item you were holding. Now if that item were to be a totem of undying the villager holds, you can kill it and make it use it to glitch out that trade. I would expect a different result like either the trade being removed or the totem still being able to be traded, but it just transforms the totem item into air in the trade.
To replicate this, summon a villager that is selling a totem for any item, using the command below, and hold out the item it's selling, like the emerald using the command, then kill the villager and watch it use the totem. Now you can open its trading menu and see that the totem item has been replaced with air. I wouldn't expect it to be like that and would expect a different outcome or even having the villager not able to use the totem. But I guess this is what happens if you perform these very specific steps.
/summon minecraft:villager ~ ~ ~ {VillagerData:
{type:plains,profession:farmer,level:2}
,Offers:{Recipes:[{buy:
{id:emerald,Count:1}
,sell:{id:totem_of_undying,Count:1}}]},Health:1,Attributes:[{Name:"generic.max_health",Base:1f}]}

## Comments (9)

### Comment 1: migrated (2022-09-09T12:03:53.852-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Raconteur (2022-09-09T14:10:33.381-0700)

I think this comment sounds more like a feature request than a bug report. This is not the right place for that.

### Comment 3: migrated (2022-09-09T14:14:21.168-0700)

It's not; villagers shouldn't be able to trade air, yet they can this way.

### Comment 4: Raconteur (2022-09-09T14:47:13.182-0700)

I tested and yes, in the left list of items on the left, it say you can trade air. But if you try to trade, you can see that it's not possible, there is nothing to pick up in the trade result and the emerald is not consumed.
I assume that "air" is the default display when, for some reason, the item to trade is unavailable or invalid. For example this reddit post, the guy enter a wrong command and the item traded by the villager is invalid, and replaced by "Air": https://www.reddit.com/r/Minecraft/comments/ehgy6l/help_with_custom_villager_keeps_trading_air/
So I think it work as intended. I personally consider it as a unwanted easter egg.

### Comment 5: Raconteur (2022-09-09T15:24:58.258-0700)

Update: the only problem that I can find is that the trade is blocked after that. You may consider that as a bug... I don't know.

### Comment 6: migrated (2022-09-09T22:06:40.650-0700)

The problem is that a valid trade turns invalid, rather than being removed from the list; it's also the only trade that can change (seemingly unintentionally) due to item consumption.
There's several things that say "bug" here, none that say "easter egg".

### Comment 7: Brain81505 (2023-02-13T05:18:02.153-0800)

Can confirm in 23w06a

### Comment 8: matthewdog6 (2023-10-12T09:13:21.011-0700)

I just tested this bug in the latest version, 23w41a, and it appears to be working as intended now

### Comment 9: CreeperFriend (2024-04-19T12:25:32.378-0700)

Can confirm this is fixed, with the exact fix version being 1.20.2 Pre-Release 3.
The villager now correctly keeps the totem of undying instead of replacing it with air.

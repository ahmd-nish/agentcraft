# MC-269191: Old villagers can't trade

**Mojira URL:** [https://bugs.mojang.com/browse/MC-269191](https://bugs.mojang.com/browse/MC-269191)

## Report details

- **Mojira categories:** Datafixer; Trading
- **Project:** MC
- **Issue key:** MC-269191
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2024-03-07T19:30:13.959-0800
- **Updated:** 2025-05-29T09:06:11.138-0700
- **Resolution date:** 2024-10-22T05:56:34.147-0700
- **Affects versions:** 24w10a; 24w11a; 24w12a; 24w13a; 24w14a
- **Fix versions:** 1.20.5 Pre-Release 1
- **Area:** Platform
- **Watchers:** 2
- **Attachments:** 8
- **Attachment filenames:** 1.20.4-villager.txt; 2024-03-08_00.17.25.png; 2024-03-08_00.17.32.png; 2024-03-08_00.19.20.png; 2024-03-13_20.12.40.png; 2024-03-27_14.55.34.png; 24w14a-Villager.txt; Villager bug.mp4
- **Issue links:** Relates:inward:MC-271254:Villagers can't be interacted with and lose their trades ("Failed to load offers") | Duplicate:inward:MC-270318:Villagers trading is broken | Duplicate:inward:MC-270152:Villager trades work only when 2 items are traded | Duplicate:inward:MC-270145:There are issues with the transactions of villagers | Duplicate:inward:MC-269843:minecraft villager refuses to accept rade | Duplicate:inward:MC-270013:Villagers don't trade | Duplicate:inward:MC-269992:Unable to trade with villagers | Duplicate:inward:MC-269869:Older Villagers do not work | Duplicate:inward:MC-269829:Villager Trading broken - All trades require 2 slots | Duplicate:inward:MC-269224:Villager trades air for air. | Duplicate:inward:MC-269540:Cleric villager buys air | Duplicate:inward:MC-269462:Some villager transactions are not available | Duplicate:inward:MC-269429:Villager trades not working after updating world to snapshot | Duplicate:inward:MC-269468:Previously existing Villagers (prior 24w10a) wont show their trades in realm | Duplicate:inward:MC-269450:Trades do not work | Duplicate:inward:MC-269406:Old Villagers can't trade | Duplicate:inward:MC-269402:Existing Villager Trades Blocked | Duplicate:inward:MC-269416:Villagers won't trade with player | Duplicate:inward:MC-269314:Villager Trade Issues with 24w10a | Duplicate:inward:MC-269292:Villagers are not trading even though trading is open

## Description

I was trying to trade with my villager but it didn't work, I have all the items needed but it just doesn't show up so I gave a villager a job and it was working with it

## Comments (20)

### Comment 1: migrated (2024-03-07T19:30:13.959-0800)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: [MOD] Greymagic27 (2024-03-08T11:41:11.059-0800)

We do not have enough information to find the cause of this issue.
Please record a video of this happening and attach it to this report.
If you are on Windows, you can use Windows+Alt+R to open a built-in app for recording game footage.
If you are on Mac (Mojave or later), you can use Shift+Command+5 to open a built-in app for recording your screen.
In case you don't have a program to record videos, we recommend using the free recording software OBS.
In case the resulting video file is too large to be uploaded to the bug tracker directly, please upload it elsewhere (e.g. as unlisted video on YouTube) and link to it here.
This issue is being temporarily resolved as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support (Technical Issues) – 📧 Microsoft Support (Account Issues)
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: Sgbs (2024-03-08T13:27:02.217-0800)

The Video:
https://youtu.be/gj4TuwraYNQ

### Comment 4: haykam (2024-03-08T15:18:43.651-0800)

Could you show the NBT of the villagers? (/data get entity @e[type=villager,sort=nearest,limit=1])

### Comment 5: Sgbs (2024-03-08T15:33:20.397-0800)

Here's the nbt
 1.20.4 Villager has the following entity data: {Brain: {memories: {"minecraft:last_worked_at_poi": {value: 26332L}, "minecraft:job_site": {value: {pos: [I; -58, 72, 31], dimension: "minecraft:overworld"}}}}, HurtByTimestamp: 0, Attributes: [{Base: 48.0d, Modifiers: [{Amount: -0.013233750057890462d, Operation: 1, UUID: [I; -1134045425, -507688179, -1912325114, -1462673189], Name: "Random spawn bonus"}], Name: "minecraft:generic.follow_range"}, {Base: 0.5d, Name: "minecraft:generic.movement_speed"}], FoodLevel: 0b, Invulnerable: 0b, FallFlying: 0b, ForcedAge: 0, Gossips: [{Target: [I; -1666807936, -830519434, -1508254147, 1611017848], Type: "trading", Value: 8}], PortalCooldown: 0, AbsorptionAmount: 0.0f, LastRestock: 26030L, FallDistance: 0.0f, DeathTime: 0s, Xp: 376, LastGossipDecay: 4069L, HandDropChances: [0.085f, 0.085f], PersistenceRequired: 1b, UUID: [I; -1155492370, -1499971357, -1404270544, -39725950], Age: 0, Motion: [0.0d, -0.0784000015258789d, 0.0d], Health: 20.0f, LeftHanded: 0b, Air: 300s, OnGround: 1b, Offers: {Recipes: [{maxUses: 16, buyB: {count: 1, id: "minecraft:air"}, sell: {count: 1, id: "minecraft:emerald"}, buy: {count: 15, id: "minecraft:beetroot"}, xp: 2, priceMultiplier: 0.05f, demand: -32}, {maxUses: 16, buyB: {count: 1, id: "minecraft:air"}, sell: {count: 6, id: "minecraft:bread"}, buy: {count: 1, id: "minecraft:emerald"}, priceMultiplier: 0.05f}, {maxUses: 12, buyB: {count: 1, id: "minecraft:air"}, sell: {count: 1, id: "minecraft:emerald"}, buy: {count: 6, id: "minecraft:pumpkin"}, xp: 10, priceMultiplier: 0.05f, demand: -24}, {maxUses: 12, buyB: {count: 1, id: "minecraft:air"}, sell: {count: 4, id: "minecraft:pumpkin_pie"}, buy: {count: 1, id: "minecraft:emerald"}, xp: 5, priceMultiplier: 0.05f}, {maxUses: 12, buyB: {count: 1, id: "minecraft:air"}, sell: {count: 1, id: "minecraft:emerald"}, buy: {count: 4, id: "minecraft:melon"}, xp: 20, priceMultiplier: 0.05f, demand: -24}, {maxUses: 12, buyB: {count: 1, id: "minecraft:air"}, sell: {count: 18, id: "minecraft:cookie"}, buy: {count: 3, id: "minecraft:emerald"}, xp: 10, priceMultiplier: 0.05f}, {maxUses: 12, buyB: {count: 1, id: "minecraft:air"}, sell: {components: {"minecraft:suspicious_stew_effects": [{duration: 140, id: "minecraft:weakness"}]}, count: 1, id: "minecraft:suspicious_stew"}, buy: {count: 1, id: "minecraft:emerald"}, xp: 15, priceMultiplier: 0.05f, demand: 12}, {maxUses: 12, buyB: {count: 1, id: "minecraft:air"}, sell: {components: {"minecraft:suspicious_stew_effects": [{duration: 100, id: "minecraft:night_vision"}]}, count: 1, id: "minecraft:suspicious_stew"}, buy: {count: 1, id: "minecraft:emerald"}, xp: 15, priceMultiplier: 0.05f, demand: -12}, {maxUses: 12, buyB: {count: 1, id: "minecraft:air"}, sell: {count: 3, id: "minecraft:golden_carrot"}, buy: {count: 3, id: "minecraft:emerald"}, xp: 30, priceMultiplier: 0.05f, demand: -12}, {maxUses: 12, buyB: {count: 1, id: "minecraft:air"}, sell: {count: 3, id: "minecraft:glistering_melon_slice"}, buy: {count: 4, id: "minecraft:emerald"}, xp: 30, priceMultiplier: 0.05f, demand: -12}]}, Rotation: [304.91663f, -33.577244f], HandItems: [{}, {}], RestocksToday: 0, ArmorDropChances: [0.085f, 0.085f, 0.085f, 0.085f], CustomName: '"1.20.4 Villager"', Pos: [-56.38214247321418d, 72.0d, 31.480934292015206d], Fire: -1s, ArmorItems: [{}, {}, {}, {}], CanPickUpLoot: 1b, VillagerData: {profession: "minecraft:farmer", level: 5, type: "minecraft:plains"}, HurtTime: 0s, Inventory: []}

### Comment 6: migrated (2024-03-13T11:44:22.523-0700)

Can confirm I'm seeing this in my snapshot world with the experiments turned on too.

### Comment 7: migrated (2024-03-13T17:12:11.761-0700)

this is the same issue i'm having! i just set up a bunch of new villagers in 1.20.4 and then changed my world into 24w10a and moved all the guys around (which is such a pain) and when i finally went to trade, none of them would work. i have a world backup but then I'm gonna have to get all the guys back in minecarts again

### Comment 8: migrated (2024-03-14T18:08:25.342-0700)

https://drive.google.com/file/d/1CunwOtP3dRsZ89T37MGgoyejNgk-CaSV/view?usp=drive_link

Does this link work?
Upon making this video I realized it is not ALL villagers if you listen carefully you can hear my gasp as I realized that.
It seems that villagers whom I have never traded with still trade.

### Comment 9: Sgbs (2024-03-14T18:36:56.697-0700)

i tried this too but for me even the ones i never trade wont work
it can be that this villager was unemployed and got a job on the snapshot

### Comment 10: migrated (2024-03-15T09:03:17.272-0700)

Yes that would make sense.
I also want to note that I tried downgrading, first to the last full version, and then to the previous snapshot, to fix the bug and it deleted all of the items in my inventory and chests (which makes sense but I just wanted to add that ).

### Comment 11: migrated (2024-03-17T10:15:55.287-0700)

Here's a video as requested. This is in 24w11a

### Comment 12: migrated (2024-03-22T00:52:53.337-0700)

this is happening to me too

### Comment 13: migrated (2024-03-23T03:51:37.890-0700)

Same issue

### Comment 14: Sgbs (2024-03-27T10:03:59.848-0700)

i was testing in previous snapshots to see if the bug was happening so apparently if you create a world on 1.20.4 and upgrade it to 24w04a and start upgrading to next snapshots the bug will not happen you have to create a world on 1.20.4 and go to 24w10a

### Comment 15: Sgbs (2024-03-27T10:57:15.770-0700)

Just found out that 2 item trades still work

### Comment 16: sakura-ryoko (2024-03-27T23:45:15.528-0700)

I can confirm this for 24w13a.
Offers:
{Recipes:
[{maxUses: 12,
buyB: {count: 1, id: "minecraft:air"},
sell: {count: 2, id: "minecraft:redstone"},
buy: {count: 1, id: "minecraft:emerald"},
priceMultiplier: 0.05f, demand: 2},

So in order to fix the problem you either need to:
a) Delete the world.  Only anything 1.20.4 and below is effected.
b) Wait for Mojang to fix it
c) Code a mod to fix it yourself on every villager you come across.
d) Remove the "BuyB" tag manually, or any other invalid "Offers" NBT data on the villager.
Have fun.

### Comment 17: migrated (2024-03-30T10:24:26.299-0700)

Had this issue happen last night on 1.20.2 setting up a new trading hall.
Moving villagers from villager breeder, to zombification station, to trading hall.  Have some existing Librarians and a Fletcher which were converted and moved in, working fine.
Proceeded to move a few new villagers, converted and assigned to Librarians and Farmers, a single Armorsmith and single Toolsmith. The Farmers, Armorsmith, Toolsmith and Fletcher were all upgraded to Master rank.
Proceed with the same setup for next villager, setup as a Weaponsmith, got to Apprentice rank and accidentally flipped a trap door and they got out. Broke grindstone workstation and proceeded to catch in mine cart to bring back to cell.  When I place the workstation again, the dual item trade bug appeared and I could no longer trade with the Weaponsmith.
I checked every other existing villager (again some already at Master rank) and they all displayed the same window with two spots. Tried placing emeralds in both slots and still can no longer trade with any villagers who have previously been traded with.
Not sure if the issue was breaking the workstation while it was upgrading from Apprentice to Journeyman, or something else, but was hoping some extra details may help resolve this issue.
I am able to replicate the issue in a creative world following the same steps. Set villager in cell, give workstation, trade, break workstation, can no longer trade due to dual trade spots displaying even for emerald only trades.

### Comment 18: sakura-ryoko (2024-04-03T11:36:13.116-0700)

Confirmed 24w14a is still effected.
Will attach entire F3+I tags of the same bugged villager's NBT post 1.20.4 ->> 24w14a World Upgrade.

### Comment 19: sakura-ryoko (2024-04-10T18:01:47.471-0700)

Looks good using the "EmptyItemInVillagerTradeFix" and it works ideally moving forward;
But I also wanted to mention that the "matchesBuyItems() under "TradeOffer" was the main culprit, where the
"!this.secondBuyItem.isPresent()" logic should have been inverted and tested for this.secondBuyItem.get().match(ItemStack.EMPTY) as well, because reading in the
"Optional<TradedItem>this.secondBuyItem" does not check for minecraft:air, it only checks for the presence of data, which lead to this bug since 1.20.4 and below writes minecraft:air to any "Empty" trade slots.

### Comment 20: migrated (2024-10-22T05:56:34.147-0700)

I seem to be having this issue in 1.21.1, what do I do?

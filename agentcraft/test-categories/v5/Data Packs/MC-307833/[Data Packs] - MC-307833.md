# MC-307833: The world freezes when villagers with specific trade sets level up

**Mojira URL:** [https://bugs.mojang.com/browse/MC-307833](https://bugs.mojang.com/browse/MC-307833)

## Report details

- **Mojira categories:** Data Packs
- **Project:** MC
- **Issue key:** MC-307833
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2026-04-29T16:52:16.393-0700
- **Updated:** 2026-05-18T07:13:37.644-0700
- **Resolution date:** 2026-05-18T07:13:37.592-0700
- **Affects versions:** 26.1.2
- **Fix versions:** 26.2 Snapshot 8
- **Area:** Platform HC
- **Votes:** 1
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** hangover trades.zip

## Description

When a villager levels up, this may causes the server side of the game to freeze indefinitely. This happens only if the villager has a trade set which:
- Allows duplicate trades

- Contains only trades that will fail to generate offers (e.g: map trades in worlds with no structures)

AFAIK those conditions do not exist with the vanilla trades, but can be created with a simple datapack, containing this single file: (See attachments for the zipped pack.)
data/minecraft/trade_set/cartographer/level_2.json

```
{
	"amount": 2.0,
	"random_sequence": "minecraft:trade_set/cartographer/level_2",
	"//": "Same as vanilla, but with duplicates enabled, and keeping only the map trades.",
	"allow_duplicates": true,
	"trades": [
		"minecraft:cartographer/2/emerald_and_compass_village_taiga_map",
		"minecraft:cartographer/2/emerald_and_compass_explorer_swamp_map",
		"minecraft:cartographer/2/emerald_and_compass_village_snowy_map",
		"minecraft:cartographer/2/emerald_and_compass_village_savanna_map",
		"minecraft:cartographer/2/emerald_and_compass_village_plains_map",
		"minecraft:cartographer/2/emerald_and_compass_explorer_jungle_map",
		"minecraft:cartographer/2/emerald_and_compass_village_desert_map"
	]
}
```
Reproduction steps:
- Make a new creative world using the attached datapack. Make sure to set “Generate Structures” to OFF.

- Spawn a villager, and make it a cartographer.

- Trade with the cartographer until it reaches the next level. Close the trade interface and wait for the level up to occur.

Expected result: Anything, so long as the game keeps playing.
Actual result: The world freezes. The freeze is only server-side, as it’s still possible to move around, but you can’t interact with anything anymore.
Code review:
This is caused by an endless while loop in AbstractVillager::addOffersFromItemListings. The game tries to roll new trades until either it has created sufficiently many offers, or until the pool of potential trades is empty. However the given set will never generate any offer at all, and potential trades are never removed from the pool. Thus the game will endlessly attempt to recreate the same trades over and over.
This could be fixed by making the function closer to its WithoutDuplicates counterpart, but whith trades being removed from the pool only if they fail to generate an offer:

```
private static void addOffersFromItemListings(LootContext lootContext, MerchantOffers merchantOffers, HolderSet<VillagerTrade> potentialOffers, int numberOfOffers) {
    ArrayList<Holder<VillagerTrade>> leftoverOffers = Lists.newArrayList(potentialOffers);
	int offersFound = 0;
	while (offersFound < numberOfOffers && !leftoverOffers.isEmpty()) {
		int roll = lootContext.getRandom().nextInt(leftoverOffers.size());
		Holder<VillagerTrade> villagerTrade = leftoverOffers.get(roll);
		MerchantOffer offer = villagerTrade.value().getOffer(lootContext);

		if (offer == null){
    		// This is the important bit !!
			leftoverOffers.remove(roll);
			continue;
		}

		merchantOffers.add(offer);
		++offersFound;
	}
}
```
(Based on CFR-decompiled code. Take this snippet with a grain of salt.)

## Comments (1)

### Comment 1: Automation for Jira (2026-04-29T16:52:28.352-0700)

Thank you for helping us improve Minecraft! We saved your files:

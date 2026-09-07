# MC-182814: Drinking honey bottles increases "minecraft.used:minecraft.honey_bottle" by a value of two and runs the "minecraft:consume_item" advancement trigger twice

**Mojira URL:** [https://bugs.mojang.com/browse/MC-182814](https://bugs.mojang.com/browse/MC-182814)

## Report details

- **Mojira categories:** Statistics
- **Project:** MC
- **Issue key:** MC-182814
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2020-05-06T14:16:02.617-0700
- **Updated:** 2025-04-26T09:58:39.605-0700
- **Resolution date:** 2024-11-08T05:25:42.874-0800
- **Affects versions:** 1.15.2; 20w19a; 20w21a; 20w22a; 1.16 Pre-release 4; 1.16 Pre-release 6; 1.16; 1.16.2; 1.16.3; 20w46a; 20w49a; 21w03a; 1.16.5; 21w08b; 21w15a; 21w16a; 21w17a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17 Release Candidate 2; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Pre-release 3; 1.17.1 Release Candidate 1; 1.17.1; 21w38a; 21w40a; 21w44a; 1.18 Pre-release 1; 1.18; 1.18.1; 22w05a; 22w06a; 1.18.2 Pre-release 2; 1.18.2; 22w14a; 22w17a; 1.19; 1.19.2; 22w43a; 22w45a; 1.19.3 Pre-release 2; 1.19.3; 1.19.4 Release Candidate 3; 1.19.4; 1.20; 1.20.1; 1.20.4; 23w51b; 1.21
- **Fix versions:** 24w34a
- **Area:** Gameplay
- **Labels:** consume_item; honey_bottle
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-182814.mp4; MC-182814.png
- **Issue links:** Duplicate:inward:MC-217242:Honey bottle counts as 2 usages in statistics and scoreboards | Duplicate:inward:MC-225191:Minecraft is too stupid to count how often you drink honey | Duplicate:inward:MC-201387:Honey Bottle Scoreboard Bug | Duplicate:inward:MC-187154:Honey Bottle used stat counts twice

## Description

The Bug:
Drinking honey bottles increases "minecraft.used:minecraft.honey_bottle" by a value of two and runs the "minecraft:consume_item" advancement trigger twice.
Steps to Reproduce:
- Create a scoreboard objective for tracking the use of a honey bottle and set it to display on the sidebar by using the commands provided below.

```
/scoreboard objectives add UseHoneyBottle minecraft.used:minecraft.honey_bottle
```

```
/scoreboard objectives setdisplay sidebar UseHoneyBottle
```

- Obtain a honey bottle and drink it.

- Take note as to whether or not drinking honey bottles increases "minecraft.used:minecraft.honey_bottle" by a value of two and runs the "minecraft:consume_item" advancement trigger twice.

Observed Behavior:
"minecraft.used:minecraft.honey_bottle" increases by a value of two and the "minecraft:consume_item" advancement trigger runs twice.
Expected Behavior:
"minecraft.used:minecraft.honey_bottle" would be increased by a value of one and the "minecraft:consume_item" advancement trigger would only be run once.
Code Analysis:
Code analysis by  can be found in this comment.

## Comments (10)

### Comment 1: migrated (2020-05-06T14:16:02.617-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: Avoma (2020-11-24T10:28:27.121-0800)

Can confirm in 20w46a.

### Comment 3: Avoma (2021-02-02T00:47:18.028-0800)

Can confirm in 21w03a.

### Comment 4: Avoma (2021-03-06T06:33:33.019-0800)

Can confirm in 21w08b. Video attached.

### Comment 5: Avoma (2021-04-18T08:09:51.338-0700)

Can confirm in 21w15a.

### Comment 6: Avoma (2021-04-22T02:24:32.794-0700)

Can confirm in 21w16a. I'd like to request ownership of this ticket since the current reporter has been inactive since July 2020. I'm willing to provide all of the necessary information and will keep this report updated.

### Comment 7: haykam (2023-02-26T09:13:27.977-0800)

Code analysis (Yarn mappings)
Honey bottles are a custom item with a food component. The HoneyBottleItem class triggers the criterion in its implementation of the Item#finishUsing method:

```@Override
public ItemStack finishUsing(ItemStack stack, World world, LivingEntity user) {
	super.finishUsing(stack, world, user);
	if (user instanceof ServerPlayerEntity serverUser) {
		Criteria.CONSUME_ITEM.trigger(serverUser, stack); // custom item trigger
		serverUser.incrementStat(Stats.USED.getOrCreateStat(this));
	}
}```
However, the base implementation of the Item#finishUsing method already triggers the criterion for foods through the player's implementation of the LivingEntity#eatFood method:

```@Override
public ItemStack eatFood(World world, ItemStack stack) {
	this.getHungerManager().eat(stack.getItem(), stack);
	this.incrementStat(Stats.USED.getOrCreateStat(stack.getItem()));
	world.playSound(null, this.getX(), this.getY(), this.getZ(), SoundEvents.ENTITY_PLAYER_BURP, SoundCategory.PLAYERS, 0.5f, world.random.nextFloat() * 0.1f + 0.9f);

	if (this instanceof ServerPlayerEntity serverPlayer) {
		Criteria.CONSUME_ITEM.trigger(serverPlayer, stack); // food trigger
	}

	return super.eatFood(world, stack);
}```
One recommended fix is to simply remove the unnecessary criterion trigger from the HoneyBottleItem class.

### Comment 8: haykam (2023-03-14T06:21:45.110-0700)

This issue still exists in Minecraft 1.19.4 release candidate 3.

### Comment 9: migrated (2023-12-19T04:45:28.674-0800)

This issue still exists in 1.20.4.

### Comment 10: Avoma (2024-11-08T05:25:24.686-0800)

This issue was present in 24w33a but no longer occurs in 24w34a. This issue was fixed in 24w34a.

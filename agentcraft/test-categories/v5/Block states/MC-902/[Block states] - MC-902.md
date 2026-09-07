# MC-902: The end obsidian platform resets every time entities go through the end portal, which can cause blocks to be deleted

**Mojira URL:** [https://bugs.mojang.com/browse/MC-902](https://bugs.mojang.com/browse/MC-902)

## Report details

- **Mojira categories:** Block states
- **Project:** MC
- **Issue key:** MC-902
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-10-27T09:06:30.144-0700
- **Updated:** 2025-10-28T02:46:04.691-0700
- **Resolution date:** 2024-06-28T05:41:40.334-0700
- **Affects versions:** Minecraft 1.4.2; 1.14.4; 1.16.1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4 Release Candidate 1; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w17a; 21w20a; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w39a; 21w42a; 1.18; 1.18.1; 22w05a; 1.18.2 Pre-release 1; 1.18.2 Release Candidate 1; 1.18.2; 22w14a; 1.19 Pre-release 4; 1.19 Pre-release 5; 1.19 Release Candidate 1; 1.19 Release Candidate 2; 1.19; 22w24a; 1.19.1; 1.19.2; 1.19.3; 23w03a; 23w04a; 23w05a; 1.19.4; 1.20 Release Candidate 1; 1.20; 1.20.1; 24w11a; 1.20.6
- **Fix versions:** 1.21 Pre-Release 1
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2021-05-12_14.53.27.png; MC-902.mp4
- **Issue links:** Duplicate:inward:MC-29268:Blocks placed on end spawn platform disappear | Duplicate:inward:MC-32477:Chests vanish | Duplicate:inward:MC-155127:Chests on the End Spawn Plattform disappeared | Duplicate:inward:MC-160847:End obsidian spawn platform resets every time someone goes through the end portal, causing blocks to be deleted | Duplicate:inward:MC-174548:shulker boxes disappear on end spawn platform | Duplicate:inward:MC-178330:Shulker Box dissapearing in end | Duplicate:inward:MC-179176:When I put a box of shulker or water on the obsidian base in "the end", it disappears | Duplicate:inward:MC-181297:Shulkerboxes/ Enderchests despawn in End | Duplicate:inward:MC-181571:Blocks disappear from The End spawn platform when travel thru the portal | Duplicate:inward:MC-197670:Shulker Box and Crafting table despawned, deleted | Duplicate:inward:MC-200425:Died in the end, end base vanished | Duplicate:inward:MC-243018:Endspawn deletes chests when entering the end | Duplicate:inward:MC-244701:Placed Shulker Boxes Disappeared When Switching Dimensions? | Duplicate:inward:MC-244782:some items placed on the end obsidian platform vanish when another player comes thruogh | Duplicate:inward:MC-247851:Dragon Egg Dissapears After Player Teleports On It. | Duplicate:inward:MC-254730:My shulker box disapeared | Duplicate:inward:MC-263144:Chests disappear in the "End" | Duplicate:inward:MC-1314:Obsidian Generator In The End | Duplicate:inward:MC-4102:Chests dissapear if they are placed on the spawning platform in the End | Relates:outward:MC-273945:Unlike end portals, nether portals do not drop replaced blocks, which can result in major item loss | Relates:inward:MC-108605:Attached blocks on End platform sometimes drop | Relates:inward:MC-136525:Structure block destroy blocks instead of replacing blocks | Relates:inward:MC-160140:Shulker boxes on the obsidian platform are destroyed and do not drop when a player enters the End | Relates:inward:MC-256395:Blocks broken by the obsidian platform regenerating do not make breaking sounds or produce particles | Relates:inward:MC-256396:Blocks broken by the obsidian platform regenerating do not drop as items | Relates:inward:MC-272553:Naturally generated End Stone drops in cases where the Obsidian platform generates inside the island | Relates:inward:MC-272790:Shulker boxes and other blocks in the end exit portal when it changes state are not dropped as items | Relates:inward:MCPE-182118:End Obsidian Platform Incorrectly Resets When Entities Go Through The End Portal Causing Blocks To Be Deleted

## Description

The Bug:
The end obsidian platform resets every time entities go through the end portal, which can cause blocks to be deleted.
This notably results in containers like chests or shulker boxes which might contain valuable items within them being deleted.
Steps to Reproduce:
- Enter the end by using an end portal.

- Place some blocks on top of and around the obsidian platform that you spawn on.

- Take note of the blocks that you've just placed.

- Run the "/kill" command.

- Enter the end once again and attempt to locate the blocks you just previously placed.

- Take note as to whether or not the end obsidian platform resets every time entities go through the end portal, which can cause blocks to be deleted.

Observed Behavior:
The end obsidian platform resets every time entities go through the end portal, which can cause blocks to be deleted.
Expected Behavior:
Blocks on the end obsidian platform would not be deleted every time an entity goes through the end portal.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.18.1 using MCP-Reborn.
net.minecraft.world.entity.Entity.java

```
public abstract class Entity implements Nameable, EntityAccess, CommandSource {
   ...
   public Entity changeDimension(ServerLevel $sl) {
      if (this.level instanceof ServerLevel && !this.isRemoved()) {
         ...
         if (portalinfo == null) {
            return null;
         } else {
            ...
            if (entity != null) {
               ...
               if ($sl.dimension() == Level.END) {
                  ServerLevel.makeObsidianPlatform($sl);
               }
            }
            ...
```
If we look at the above class, we can see that when an entity enters the end portal, the makeObsidianPlatform() method is called. This method completely regenerates the end obsidian platform (including the space above), causing blocks previously placed at its position to be deleted.

## Comments (38)

### Comment 1: migrated (2012-10-27T09:06:30.144-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: migrated (2012-10-28T13:22:27.705-0700)

Intended.  The spawn platform and the air above it are reset each time someone enters the end.
Tip:  Don't place your chests on it.

### Comment 3: migrated (2012-10-29T07:46:37.618-0700)

Oh okay thanks.
But isn't it still a bid stupid, that it resets everytime?

### Comment 4: migrated (2012-10-29T12:10:09.712-0700)

If it didn't reset, then someone could fill it with blocks and when you went through, you'd suffocate.
Nether portals have a bit of space in them already so that can't happen with them.

### Comment 5: migrated (2012-10-29T12:18:20.313-0700)

Oh wauw, hadn't thought about that. Well thanks for clarifying this for me.

### Comment 6: migrated (2019-06-24T11:19:08.008-0700)

ye if this is a permanent thing.. pls put it in the Wiki. It is very disappointing.

### Comment 7: migrated (2020-04-04T15:11:43.014-0700)

Just lost the best shulker box I had, thanks mojang, really cool. Btw, I know this isn't completely a bug, but still, your game is already full of unsolved bugs.

### Comment 8: markderickson (2020-09-17T07:35:31.437-0700)

Hi! I'd like to request ownership of this report.

### Comment 9: Avoma (2021-02-05T11:56:29.920-0800)

Can confirm in 21w05b.

### Comment 10: Avoma (2021-03-14T06:28:17.833-0700)

Can confirm in 21w10a. Video attached.

### Comment 11: Avoma (2021-04-30T05:48:34.558-0700)

Can confirm in 21w17a.

### Comment 12: Avoma (2021-06-18T01:37:31.270-0700)

Can confirm in 1.17.

### Comment 13: ampolive (2021-06-27T14:51:34.417-0700)

Can confirm in 1.17.1 Pre-release 1.

### Comment 14: migrated (2021-06-27T19:04:13.383-0700)

caused by the fix for MC-123155

### Comment 15: Avoma (2021-07-15T06:37:41.893-0700)

Can confirm in 1.17.1.

### Comment 16: Avoma (2021-08-17T04:50:55.576-0700)

Relates to MCPE-52483.

### Comment 17: migrated (2021-08-29T09:24:02.570-0700)

Why is this a bug? It is so people can't trap the end, by removing the platform and letting you fall in the void, or by soffocating you, intentional or not intentional. It also allowed for farming obsidian this way, which is used by many players. In my opinion this should be intentional game design. (If you want to fix it you could only generate the platform and remove the blocks once, when they enter.)

### Comment 18: migrated (2021-08-29T17:42:08.104-0700)

This is an intended feature. Not a bug. The solution is to not use the obsidian platform as an area to put your stuff.

### Comment 19: ampolive (2021-08-29T17:50:32.248-0700)

Newer players might not know this. Also this has an assigned Mojang Priority, so it is considered a bug.

### Comment 20: migrated (2021-08-30T00:18:07.319-0700)

Also, where is the source of this not being a bug?

### Comment 21: migrated (2021-08-30T00:41:43.105-0700)

I can see how this is a way of preventing "spawn killing", by breaking the platform, or filling its space up. However, it makes more sense to only set the obsidian blocks if there's air, and only set air anywhere on the platform, if there's no air on the platform (and if there is, to move the player to it).

### Comment 22: Avoma (2021-10-04T02:09:37.003-0700)

I am able to confirm this behavior in 21w39a. Here are some extra details regarding this problem.
The Bug:
The end obsidian platform resets every time an entity goes through the end portal, which can cause blocks to be deleted.
Steps to Reproduce:
- Enter the end by using an end portal.

- Place some blocks on top of and around the obsidian platform that you spawn on.

- Take note of the blocks that you've just placed.

- Run the "/kill" command.

- Enter the end once again by using an end portal and notice how some blocks that you previously placed have been deleted.

Observed Behavior:
The end obsidian platform resets every time an entity goes through the end portal, which can cause blocks to be deleted.
Expected Behavior:
The end obsidian platform would not reset every time an entity goes through the end portal, which wouldn't cause blocks to be deleted.

### Comment 23: migrated (2021-12-06T13:14:42.097-0800)

This horrible behavior.  I've been playing for years and didn't know this, and having a couple shulker boxes of stuff that took hours to create vanish without warning is a bug, esp. when there is no cause to clear the blocks...the platform had plenty of space to spawn players.  The fact that this was opened 9 years ago means "Normal" priority is to ignore it.

### Comment 24: migrated (2022-02-01T22:44:25.868-0800)

I just lost 3 SO MANY hours of work in mining and enchanting to this bug. How has this not been addressed? This is absolutely ridiculous.

### Comment 25: MacchuPicchu (2022-05-30T11:58:12.592-0700)

Present in 1.19-pre4.

### Comment 26: MacchuPicchu (2022-06-01T07:46:24.442-0700)

Present in 1.19-pre5.

### Comment 27: MacchuPicchu (2022-06-02T13:10:54.651-0700)

Present in 1.19-rc1.

### Comment 28: MacchuPicchu (2022-06-16T06:01:22.264-0700)

Present in 22w24a.

### Comment 29: migrated (2022-07-22T16:15:44.540-0700)

this is intended because the end has a fixed spawnpoint and you would suffocate if the obsidian platform and 2 3 by 3 layers above it wouldnt reset. i would rather be happy about a basicly infinite obsidian farm because of that.

### Comment 30: migrated (2022-07-22T17:18:34.339-0700)

Is it intended that when I set a shulker box full of high tier items down and another player comes through and it vanishes?  That's a bug.  clear the space around the head of the incoming player if you must and regenerate the obsidian, but not the whole platform.

### Comment 31: migrated (2022-07-22T21:59:26.092-0700)

It also doesn't need to do that every time; as long as it can find a place with block below feet and air at head, it shouldn't regenerate; if there's none, it only needs to fill those 2 blocks, not destroying everything.

### Comment 32: migrated (2022-08-24T11:28:24.154-0700)

I think the blocks should drop as if mined by a player instead of being deleted

### Comment 33: Avoma (2022-08-31T11:01:38.238-0700)

, this game mechanic isn't working as intended as per the assinged "Mojang Priority" on this ticket. In other words, Mojang Studios have recognized this to be a valid problem.

### Comment 34: Brain81505 (2023-01-18T06:25:10.865-0800)

Can confirm in 23w03a

### Comment 35: Brain81505 (2023-01-24T23:21:56.986-0800)

Can confirm in 23w04a

### Comment 36: Brain81505 (2023-02-01T08:04:47.509-0800)

Can confirm in 23w05a

### Comment 37: Brain81505 (2023-02-11T07:31:37.937-0800)

Can confirm in 23w06a

### Comment 38: numeritos (2024-05-29T07:11:26.727-0700)

Can reproduce in 1.21 Pre-1
EDIT: According to Kingbodgz' tweet (https://x.com/kingbdogz/status/1795823127362154962) this cannot be reproduced in 1.21 Pre-1

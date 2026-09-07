# MC-65040: Entities become invisible under certain conditions

**Mojira URL:** [https://bugs.mojang.com/browse/MC-65040](https://bugs.mojang.com/browse/MC-65040)

## Report details

- **Mojira categories:** Entities
- **Project:** MC
- **Issue key:** MC-65040
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2014-08-01T23:43:09.666-0700
- **Updated:** 2025-04-29T12:19:24.843-0700
- **Resolution date:** 2023-09-19T20:16:17.823-0700
- **Affects versions:** Minecraft 14w31a; Minecraft 14w34b; Minecraft 1.8-pre1; Minecraft 1.8-pre2; Minecraft 1.8-pre3; Minecraft 1.8; Minecraft 1.8.1-pre1; Minecraft 1.8.1-pre2; Minecraft 1.8.1-pre5; Minecraft 1.8.1; Minecraft 1.8.2-pre1; Minecraft 1.8.2-pre4; Minecraft 1.8.2-pre6; Minecraft 1.8.2; Minecraft 1.8.3; Minecraft 1.8.4; Minecraft 1.8.6; Minecraft 1.8.8; Minecraft 15w32a; Minecraft 15w32b; Minecraft 15w33b; Minecraft 15w33c; Minecraft 15w34a; Minecraft 15w36c; Minecraft 15w36d; Minecraft 15w37a; Minecraft 15w45a; Minecraft 15w46a; Minecraft 15w47a; Minecraft 1.8.9; Minecraft 15w50a; Minecraft 16w04a; Minecraft 16w05b; Minecraft 1.9 Pre-Release 1; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.4; Minecraft 1.10; Minecraft 1.10.2; Minecraft 1.11; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w13a; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 1.13-pre3; Minecraft 1.13-pre5; Minecraft 1.13-pre7; Minecraft 1.13; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w43a; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w46a; Minecraft 18w47a; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w07a; Minecraft 19w08a; Minecraft 19w08b
- **Fix versions:** Minecraft 15w38b; Minecraft 15w39a; Minecraft 15w40a
- **Labels:** entity; invisible; mojang_internal_1
- **Watchers:** 1
- **Attachments:** 7
- **Attachment filenames:** 2014-10-08_21.19.16.png; 2015-10-18_16-11-46.mp4; crash-2014-08-08_21.52.12-client.txt; crash-2014-08-19_18.04.44-client.txt; crash-2015-10-12_22.42.07-client.txt; Invisible Item Drops.rar; output_aXzsOs.gif
- **Issue links:** Relates:inward:MC-73227:Maps in item frames sometimes disappear/delete semi-permanently | Duplicate:inward:MC-49763:Teleporting another player to you has them invisible | Duplicate:inward:MC-63889:Item frames and Items in items frames randomly disappearing | Duplicate:inward:MC-64358:Paintings and Item Frames disappear. | Duplicate:inward:MC-66522:Item Frames and signs turning invisible | Duplicate:inward:MC-66683:Entities in always loaded chunks become invisible when player leaves and returns | Duplicate:inward:MC-66849:Armour stands despawn when the chunk unloads | Duplicate:inward:MC-67264:VBOs problem | Duplicate:inward:MC-68173:dogs/wolves despawn after a few seconds and never respawn | Duplicate:inward:MC-68181:Armor stand disappeared, but was viewable after logging out/in | Duplicate:inward:MC-68300:Mobs and leads sometimes do not render | Duplicate:inward:MC-68351:mob eggs don't spawn mobs at all | Duplicate:inward:MC-68421:Item Frames Disappearing When Chunks Unload | Duplicate:inward:MC-68697:Invisible Creepers | Duplicate:inward:MC-69305:Random entities become invisible until you re-enter the world | Duplicate:inward:MC-69501:Item Frames Unload Themselves | Duplicate:inward:MC-69782:item frames disappear when you go out of the chunk | Duplicate:inward:MC-69800:Item frames disappear when players go too far away | Duplicate:inward:MC-70152:Rabbits disappearing (ghost rabbits) | Duplicate:inward:MC-70383:Passive Mobs turn invisible | Duplicate:inward:MC-70390:Hostile and Nonhostile Mobs are Invisible | Duplicate:inward:MC-70444:invisible spiders | Duplicate:inward:MC-70479:Armor stand issue | Duplicate:inward:MC-70500:item frames disappear after loading then unloading it's chunk. In my singleplayer. | Duplicate:inward:MC-70696:Armour Stands Despawned | Duplicate:inward:MC-70819:endermen damadge | Duplicate:inward:MC-70836:Teleporting away and back to a location will turn every entity invisible to you | Duplicate:inward:MC-70903:Paintings dissapear | Duplicate:inward:MC-70941:Killed by invisible mob | Duplicate:inward:MC-70948:Invisible Witch | Duplicate:inward:MC-71055:Villager Problem | Duplicate:inward:MC-71467:The mystery of the disappearing Armor Stands | Duplicate:inward:MC-71517:Armor Stand Disappaerance | Duplicate:inward:MC-71551:Disappearing Chickens | Duplicate:inward:MC-71572:Invisible Mobs in the Nether | Duplicate:inward:MC-71606:Invisible monster in Nether (even with spectator mode) | Duplicate:inward:MC-71626:Item Frames despawn when leaving chunk | Duplicate:inward:MC-72096:Mobs vanishing when unloading chunks and returning, | Duplicate:inward:MC-72104:Armor stand disappeared | Duplicate:inward:MC-72275:Chicken's going invisible/underground inside fence. | Duplicate:inward:MC-72348:Items/entities disappear and reappear later | Duplicate:inward:MC-72414:Invisible skeletons. | Duplicate:inward:MC-72664:Partial Despawning of Entities | Duplicate:inward:MC-72706:/summoned Mobs are Sometimes Invisible When Hitting ctrl (Mac) | Duplicate:inward:MC-72756:Armor Stands Disappear When Placed | Duplicate:inward:MC-72782:Things disappearing and appear | Duplicate:inward:MC-72802:Invisible Mobs | Duplicate:inward:MC-72922:Invisible Players in Dedicated Servers (Mini Games Server) | Duplicate:inward:MC-72959:Invisible Entities | Duplicate:inward:MC-73125:Armor Stands despawn and respawn ever 3 or 4 minecraft days | Duplicate:inward:MC-73184:Disappearing Entities | Duplicate:inward:MC-73376:Players sometimes invisible. | Duplicate:inward:MC-73445:invisible item frames | Duplicate:inward:MC-73587:Diseppearance of Item Frames | Duplicate:inward:MC-73702:Invisible/disappearing Wolfs | Duplicate:inward:MC-74163:Item Frame and Armor Stand Bug | Duplicate:inward:MC-74442:Item Frames Vanish | Duplicate:inward:MC-74516:Invisible Entities | Duplicate:inward:MC-74612:Invisible livestock in pens | Duplicate:inward:MC-74746:Disappearing item frames upon chunk reloads | Duplicate:inward:MC-74960:When I started a new world on November 30, I started out normal. Eventually, I made an armor stand, and put my armor on it (of course). After a couple times of taking it off to go mining, I came back and saw that it was missing. | Duplicate:inward:MC-75118:Horse Disappears when in the pen you place it in. Log back off and on and it is standing in the place you put it again | Duplicate:inward:MC-75505:Potato disappeared from item frame | Duplicate:inward:MC-75538:Painting/Armor Stands, Item frames despawning when I fly a certain distance away from them. | Duplicate:inward:MC-76028:Item Frames' Random Disappearances | Duplicate:inward:MC-76087:Anmials are invisable sometimes when leaving and reentering the chunk | Duplicate:inward:MC-76432:Horses Vanish when far away | Duplicate:inward:MC-76718:Armour Stands Dissappear | Duplicate:inward:MC-76861:armor stand and item frames disapear | Duplicate:inward:MC-76912:Mobs and entities turn Invisible and Invincible after going away from it in an unloaded chunk | Duplicate:inward:MC-77069:Items frame glitch | Duplicate:inward:MC-77083:I placed down some armor stands in a building. I went to get supplies. When I got back some of the stand were gone. | Duplicate:inward:MC-77086:item frames & armour stands disappear  in 1.8+ | Duplicate:inward:MC-77456:Entities in spawn chunks disappear when: they enter lazy chunks then get loaded again | Duplicate:inward:MC-77698:Item Frames STILL disappearing | Duplicate:inward:MC-77853:Invisible Skeleton | Duplicate:inward:MC-77894:Entitys Invisible | Duplicate:inward:MC-77895:Paintings & ItemFrames dissapear for no reason | Duplicate:inward:MC-78029:A bar for an armour disappears if to go away far he her | Duplicate:inward:MC-78301:Mobs and item frames becoming invisible | Duplicate:inward:MC-78760:Entity Disaperance | Duplicate:inward:MC-79014:Mobs and Entities disappear and turn Invisible and Invincible after going away from it over 300 Blocks | Duplicate:inward:MC-79086:All my villagers have vanished | Duplicate:inward:MC-79183:Ender Dragon Disappearing at random points, so you cannot see it when it is flying, and then reappearing only when it is right next to you | Duplicate:inward:MC-79421:tile entites (armorstands, paintings, name-tagged mobs, itemframes) turn invisible and indistructable randomly | Duplicate:inward:MC-79644:item frames and armor stands dissapear in all of my worlds | Duplicate:inward:MC-79855:Entities don't appear when you respawn near them | Duplicate:inward:MC-79985:Mobs (Passive and Hostile Dissapering until Death) | Duplicate:inward:MC-80089:Blazes with NoAI get invisible upon chunk reloading | Duplicate:inward:MC-80285:Pigs and chickens hit box there but they do not spawn | Duplicate:inward:MC-80682:Horses become invisible randomly. | Duplicate:inward:MC-81207:Item Frame Disappearance | Duplicate:inward:MC-81235:Invisible Mobs | Duplicate:inward:MC-81269:armor stand bug | Duplicate:inward:MC-81583:[BUG]Mobs becomming invisible for no reason | Duplicate:inward:MC-81664:Invisible Zombie | Duplicate:inward:MC-82301:Invisible Entity | Duplicate:inward:MC-82362:Item frames, armor stands, minecarts and boats dissapearing | Duplicate:inward:MC-82442:Broken?!? | Duplicate:inward:MC-82475:Armour stand disappears, reappears on game restart. | Duplicate:inward:MC-82788:disappearing wall of maps | Duplicate:inward:MC-83815:friendly mobs disappear after respawning the ender dragon | Duplicate:inward:MC-84037:Mobs become invisible at a certain hight | Duplicate:inward:MC-84090:When you unload chunks with item frames in it, the item frames will dissapear, and there is a small chance that they will stay. | Duplicate:inward:MC-84522:Iron golem | Duplicate:inward:MC-84667:Disappearing Mobs | Duplicate:inward:MC-84940:Relogging on a server in 15w31c makes entities dissapear that then reappear after another relog | Duplicate:inward:MC-84975:Maps disappearing & Missing items | Duplicate:inward:MC-85148:After placing an Item Frame, if you teleport away using a command block and teleport back, the item frame is invisible and the only way to get rid of it is to mine the block it's on | Duplicate:inward:MC-85199:Item Frame disappearing | Duplicate:inward:MC-85240:Animals are despawning on Multiplayer | Duplicate:inward:MC-85311:Armor stands/Item frames Disappear | Duplicate:inward:MC-85403:Villager not shown | Duplicate:inward:MC-85538:Vanishing Armor Stands | Duplicate:inward:MC-85693:Item Frames | Duplicate:inward:MC-85765:Invisible Shulker: Completely invis and still shoots | Duplicate:inward:MC-85930:Items Frames becoming Invisible. | Duplicate:inward:MC-86048:Entities are disappearing again | Duplicate:inward:MC-86096:A Shulker is invisible. | Duplicate:inward:MC-86103:Friendly Animals and sword Disappeared | Duplicate:inward:MC-86126:Minecraft invisible mobs | Duplicate:inward:MC-86225:item frame with clock disappears | Duplicate:inward:MC-86462:Villagers Disappear At Night | Duplicate:inward:MC-86491:Entitys Disappearing and Reappearing! | Duplicate:inward:MC-86566:EnderCrystals disapear | Duplicate:inward:MC-86757:Item frames disappear randomly | Duplicate:inward:MC-87079:Villagers keep disappearing when I leave a chunk. I then leave it again and come back and they reappear | Duplicate:inward:MC-87189:Item frames disappear and reappear | Duplicate:inward:MC-87520:Block entities not visible | Duplicate:inward:MC-87960:Chest Minecart dissappear randomly | Duplicate:inward:MC-88081:Single Player - Entities Disappear Eg: item Frame, Minecart | Duplicate:inward:MC-88146:Item frame disappears | Duplicate:inward:MC-88488:An invisible zombie? | Duplicate:inward:MC-88503:invisible skeleton | Duplicate:inward:MC-89007:Item Frames are disappearing from blocks, after death | Duplicate:inward:MC-89097:Entities Disapear and attack | Duplicate:inward:MC-89761:Invisible overworld enemies kill players around nether portal | Duplicate:inward:MC-89872:Item Frame Disapper? | Duplicate:inward:MC-90850:Mobs teleported to unloaded chunks go invisible (and more) | Duplicate:inward:MC-91154:Animals visually disappear, return after restart | Duplicate:inward:MC-91847:Blocks not being placeable ( Per world ???) | Duplicate:inward:MC-92219:Entitys randomly disappearing(possibly dieing) | Duplicate:inward:MC-92279:Igloo's Pre-spawned Mobs Don't Exist for a Time | Duplicate:inward:MC-92858:Players disappear | Duplicate:inward:MC-93299:Map in item frame vanish... | Duplicate:inward:MC-93828:Hopper minecarts | Duplicate:inward:MC-94075:invisible spiders and silverfish. | Duplicate:inward:MC-95451:Chickens despawning when penned in a 15x15 area | Duplicate:inward:MC-95700:Item Frames Despawning at Random in Realms (Unknown if Single Player) | Duplicate:inward:MC-97010:Invisible players after teleport bug | Duplicate:inward:MC-97444:End portal and Elytra Wings issue | Duplicate:inward:MC-98303:Invisible players | Duplicate:inward:MC-99610:Invisibility bug after respawn | Duplicate:inward:MC-100942:Going to bed causes horses to visually disappear | Duplicate:inward:MC-101398:horses disappearing | Duplicate:inward:MC-101434:Horse problems when getting off it | Duplicate:inward:MC-105197:Horse invisible | Duplicate:inward:MC-105554:Invisible Husk Zombies | Duplicate:inward:MC-106766:Hopper minecarts running into invisible blocks | Duplicate:inward:MC-108668:villagers desapear after a period of time | Duplicate:inward:MC-110556:My Dogs are disappearing, and reappearing? | Duplicate:inward:MC-110582:All items disappear after death | Duplicate:inward:MC-110967:Item Frame/ ALL entities Disappearing randomly | Duplicate:inward:MC-114029:Armor Stands & Item Frames Dissappearing/Despawning | Duplicate:inward:MC-114627:Item frames disappear/become invisible. | Duplicate:inward:MC-116541:Hopper Minecart disappearing off track | Duplicate:inward:MC-116594:Villagers disappearing | Duplicate:inward:MC-116820:Villagers gone | Duplicate:inward:MC-116936:EDIT : INVISIBLE ENTITY Can't place blocs in precise location | Duplicate:inward:MC-117504:ghost animals | Duplicate:inward:MC-117874:minecart stops moving on specific spot | Duplicate:inward:MC-118219:Villagers despawn on chunk unload even when named | Duplicate:inward:MC-118222:Players vanish upon entering the portal taking you to the outer end islands | Duplicate:inward:MC-118535:Horses Disappearing | Duplicate:inward:MC-118641:Animals | Duplicate:inward:MC-119108:Items placed on a chunk border has a chance to disappear on chunk load | Duplicate:inward:MC-119114:3 Minecarts disappeared | Duplicate:inward:MC-119401:Horses disappearing after riding for a while | Duplicate:inward:MC-119506:invisible entity on minecart rail facing east | Duplicate:inward:MC-120152:Dissappearing tamed Wolves | Duplicate:inward:MC-120285:The horse disappears when it is dismounted | Duplicate:inward:MC-120383:Sometimes when I save and quit while I am riding a horse, then when I load up my world again, the horse is gone | Duplicate:inward:MC-120660:I logged in and all my itemframes were gone. Music overlaping | Duplicate:inward:MC-123439:Disappearing Villagers | Duplicate:inward:MC-124071:Map within item frame rendered invisible in the End | Duplicate:inward:MC-126381:Invisible mobs | Duplicate:inward:MC-128286:Named Villagers Disappearing/Despawning | Duplicate:inward:MC-129133:Sand or Desert Temples Cause Horses To Despawn | Duplicate:inward:MC-129534:Villagers phase out of existance, May reappear after enough world/chunk reloads | Duplicate:inward:MC-131785:Igloo spawns basement without villagers | Duplicate:inward:MC-132321:dolphins are invisivle in frozen ocean | Duplicate:inward:MC-132550:Villagers despawning | Duplicate:inward:MC-132972:Villager disappears randomly | Duplicate:inward:MC-133171:Some animals are summoned invisible | Duplicate:inward:MC-133278:Mobs are spawned on server-side, but not visible on client-side upon creating a new world. | Duplicate:inward:MC-134263:Invisible Sheep | Duplicate:inward:MC-135165:Horse dissapearing | Duplicate:inward:MC-135187:Invisible drowned /shipwreck inside ruins | Duplicate:inward:MC-135337:Invisible Husks | Duplicate:inward:MC-135694:Horses disappearing after un-mounting | Duplicate:inward:MC-135998:Villagers dissappear after going through a portal. | Duplicate:inward:MC-138160:Minecrats Disappearing in the new snapshot | Duplicate:inward:MC-138351:Certain mobs/items become invisible at random & cat issues | Duplicate:inward:MC-138479:Ghosting Passive mobs | Duplicate:inward:MC-138891:Armorstands aren't visible when teleporting to unloaded chunks | Duplicate:inward:MC-138937:Turtle problem | Duplicate:inward:MC-139032:Some entities randomly turn invisible | Duplicate:inward:MC-139059:Villagers and blocks disappeared | Duplicate:inward:MC-139601:Entity positions of client and server are out of sync | Duplicate:inward:MC-139715:Mobs invisible after teleporting | Duplicate:inward:MC-139733:Invisible mobs | Duplicate:inward:MC-139962:dissapearing mobs | Duplicate:inward:MC-140715:mobs are invisible | Duplicate:inward:MC-141421:Animals "invisible" and "visible" | Duplicate:inward:MC-141629:Animals Appear as Shadows Only | Duplicate:inward:MC-141816:Horses disappear when mounting off of them. | Duplicate:inward:MC-142148:Disappearing blocks after placing | Duplicate:inward:MC-142179:Issue similar to MC-142164 Invisible item frame / objects in frame / villagers, on world load | Duplicate:inward:MC-142824:Item frames despawning after visit to End | Duplicate:inward:MC-142830:Disappearing and Reappearing Minecarts | Duplicate:inward:MC-143123:Players become invisible to other players after traveling between Nether and Overworld | Duplicate:inward:MC-143589:Zombie Villager did not generate (may be inconsistent?). | Duplicate:inward:MC-144545:Inactive Zombie and invisible Archer in survival mode | Duplicate:inward:MC-144940:NPCs despawning | Duplicate:inward:MC-147655:Invisible mobs with no hitbox | Duplicate:inward:MC-147906:Chest Minecart disappearing | Duplicate:inward:MC-151182:Mobs dissapear ~80 blocks away then reappear when getting closer | Duplicate:inward:MC-155728:Horse Dissapears | Duplicate:inward:MC-2306:Other players invisible after /tp @a x,y,z | Relates:outward:MC-913:Semi-Invisible Entities | Relates:inward:MC-70979:Invisible Players/Players missing from tab list | Relates:inward:MC-74044:When in spectator mode, then in creative, tamed wolves disappear? | Relates:inward:MC-80298:Clients ignore Packets if there is not at least a tick between them ( 'Invisibile Entities' ) | Relates:inward:MC-91388:Chicken jockeys spawning without the zombie / invisible zombie | Relates:inward:MC-92073:End crystals not spawning in the end

## Description

18w43a - This issue has now gotten worse in 18w43a, appears to happen a lot more frequently
 This report only covers totally invisible mobs. (No distortions or partially invisible). Entities seem to become invisible in several ways in 1.8. In this report one of the ways are described. If any of these things listed below applies to what you are seeing, this is probably the right place, if not then you should probably look in the "related to" list below for the bug you are seeing:
- It is affected by draw distance.

- It happens only in or close to always loaded chunks (Spawn chunks or chunks loaded by chunkloaders or portals)

- It affects most entities, but not items just laying on the ground.
(Any the above alone is enough)

The reason that the other related bugs are not covered here is that they are not reproduced in the same way and they don't overlap much from a testing point of view, so it would be confusing to mix them together. However some of the other bugs around are probably heavily related to this one so in case of a fix, they should probably all be looked through. (Things turning invisible)
 Note: Due to recent merge with MC-66683 and also that I got to take over this report, the description here does not yet cover everything. It also needs some cleaning up. This however will be fixed soon. Until then most of the important parts are copied in here, but be sure to have a look at that report if you need extra info. Just make sure to post comments here to get everything in the same place.
General info
- Mobs and most other entities become invisible, but will still make sounds and can in some cases be interacted with.

- The issue covered here is only about mobs becoming totally invisible under certain conditions. It does not cover distorted or partially invisible mobs.

Conditions for it to occur
- The entity needs to be loaded in the world while still be out of render distance and can never get unloaded, between the time you leave the area until you come back, for this to occur.

- It happens using lower render distance settings (2-5) with it being easier to reproduce the lower the render distance is set to.

- Happens in constantly loaded chunks. (Either spawn chunks or chunks kept loaded by chunkloaders)

Affected entities
Most entities are affected by this including:
- Any creature or mob

- XP orbs (invisible but I can still pick them up)

- Empty and filled item frames

- Boats and any type of minecart

- Armor stand

However it seems, from the tests done so far, that items on the ground does not become invisible.
Reproduce
This issue is easy to reproduce and is still present in the current release (1.8).
Here is a video of this being reproduced
To reproduce this, follow these simple steps (originally described in MC-66683):
- Spawn a new world, preferably superflat so that it is easier to see, and at the exact point you spawn, place an armor stand. Record those coordinates. Set your render distance to smallest (2). (Further testing shows that render distance 2 to 5 all cause this issue if the player moves 100 blocks away and back)

- Travel exactly 100 blocks in any direction, and remember those coordinates. Place another armor stand there.

- Return exactly 100 blocks back in the direction of the first armor stand to find that it is gone.

- Teleport to the armor stand(s) (for example: /tp @e[name=Bob] or /tp @e[type=ArmorStand,c=-1]) to see that the armor stands are indeed still present but completely invisible. (Also teleport to item frames/paintings to see that they are present but completely invisible.)

- Travel exactly 100 blocks back to the second armor stand to find that it too is gone.

- Teleport to the armor stand(s) (for example: /tp @e[name=Bob] or /tp @e[type=ArmorStand,c=-1]) to see that the armor stands are indeed still present but completely invisible. (Also teleport to item frames/paintings to see that they are present but completely invisible.)

- Exit out of the world and enter it again and the armor stands/item frames/paintings reappear.

- (Optional) Test with traveling more than 100 blocks from spawn, placing armor stands every 100 blocks. You may find that upon returning to the first armor stand, it is still visible, but then repeating step 1 to 4 causes it to disappear again.

Further Testing:
- Create chunk loaders and spread them in any way you like. Make sure you make entity processing chunks by surrounding a chunk with 2 layers of chunks.

- Repeat the very first test's procedures, placing the armor stands/paintings/item frames inside the entity processing chunks.

Further Notes: I tested this with putting one armor stand at the exact point I spawned in a new world. Then I moved 100 blocks away and placed another and kept doing this. At some point, if I move too far out then fly back to spawn, the original ones are visible still. However, if I continue and follow the test procedures again and move only 100 blocks out, they disappear again.
More notes and further testing (copied from MC-66683)
Mobs are also disappearing when the player moves away from them, but the distance the player must move from them is different. From my tests I found them to be disappearing upon moving approximately 60 blocks away and coming back to them. It seems also to only occur in always loaded chunks, but of the lazy chunk variety.
To test this:
- Create a new world, superflat is preferred to see what is occuring. Set your render distance to 2.

- /summon <mob> ~ ~ ~ {NoAI:1b}

- Move exactly 50 blocks straight in any direction.

- /summon <mob> ~ ~ ~ {NoAI:1b}

- Move 60 blocks further in the same direction.

- /summon <mob> ~ ~ ~ {NoAI:1b}

- Move 60 blocks back in the opposite direction to return to second mob. /tp @e[type=<mob>,r=10] to see that it is indeed still there but invisible.

- Move 60 blocks in the original direction to find that third mob is still there.

- Move 60 blocks back in the opposite direction to find mob is still invisible. Continue 50 more blocks to first mob to find that it is still there.

- Exiting and entering the world will make invisible mob visible again. Note: dropped items do not seem to have this problem.

## Comments (99)

### Comment 1: migrated (2014-08-01T23:43:09.666-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: qmagnet (2014-08-02T05:18:33.054-0700)

Wow this bug is getting worse. Likely relates to MC-62166, or a duplicate and mobs should be added to that description.
Note: F3 + A will reload the chunks without having to leave the world file.  Temp fix for now.

### Comment 3: migrated (2014-08-02T15:55:49.288-0700)

I tried doing F3 + A when the mobs became invisible, and the chunks did reload, but the mobs did not reappear, which suggests that this issue is not closely related to that issue.

### Comment 4: qmagnet (2014-08-02T17:10:23.784-0700)

If you reload Minecraft, does the bug reoccur?

### Comment 5: migrated (2014-08-02T17:13:29.850-0700)

The mobs become visible again, but not permanently. The mobs will eventually become invisible again after leaving the area and returning

### Comment 6: kumasasa (2014-08-09T00:29:53.335-0700)

Graphics driver issue, see MC-913

### Comment 7: migrated (2014-08-09T00:40:04.446-0700)

This is not the same issue. Entites (including item frames and armor stands) are occasionally rendered (or rather, not rendered) completely invisible, not semi-invisible.

### Comment 8: kumasasa (2014-08-09T00:48:01.431-0700)

Please force a crash by pressing F3 + C for 10 seconds while in-game and attach the crash report ([minecraft/crash-reports/crash-<DATE>-client.txt|http://hopper.minecraft.net/help/finding-minecraft-data-folder]) here.

### Comment 9: kumasasa (2014-08-09T01:16:06.248-0700)

Reopened.

### Comment 10: migrated (2014-08-18T09:04:51.070-0700)

Steps to reproduce (bug happens in 80% of test cases for me) :
1. Create superflat world.
2. Optionally create a holding chamber and put a hostile mob or two in there,
3. Toggle F3+B so you see entity hitboxes
4. Fill your hotbar with items and switch to survival
5. /kill yourself and respawn
6. Many of the items you dropped are now invisible, as are the mobs. The hitbox from f3+b is not present, suggesting that the server isn't even sending the entity to the client.
7. Reload world. Entities now visible again.
Seems to depend on where respawn point is, as whenever I change spawnpoint the problem goes away.

### Comment 11: migrated (2014-08-19T09:04:10.283-0700)

I can confirm this in 14w34b
100% able to reproduce this in a single player superflat world when I put lots of cows in a 2x2 area, then unload/load the chunks again.
Restarting the game fixes it until you unload again.
Note: F3+A does not fix it for me.

### Comment 12: migrated (2014-08-19T09:13:09.803-0700)

Added crash log from F3 + C
crash-2014-08-19_18.04.44-client.txt

### Comment 13: migrated (2014-08-19T11:14:45.041-0700)

I Have now done some massive testing here and think that I have figured out ALOT more. (Still 14w34b)
- Occurs for most entities.

- Probably has something to do with render distance

- Occurs on render distances 5 and below.

- Only occurs if you go 5 chunks or below away from the target while still getting it out of render distance.

- The entity gets visible again if you get further away than 5 chunks and come back again (no matter what render distance you have)

My testing:
Reproduced around 50 times in a row with ONE sheep in a 3x4 fence encasing (just to know where it was). Killing it off in between.
Just had render distance to 2 (to make it easy to unload/load), flew out and in again, and it was invisible.
Killing it with sword is not possible. Killing it with splash potion of harming works and it drops loot.
Also tested with the following enteties getting the same results:
- XP orbs (invissible but I can still pick them up)

- Empty item frames

- Item frames with items in them

- Boats

- Minecarts with nothing below

- Minecarts with rail below

- Minecart with chest (and items in the chest)

- Chicken

- villager

- Armor stand

- creeper

- Skeleton

- Zombie Pigman

- Horse

Enteties that did NOT dissapear when unloading chunks:
- Items on the ground

Things that does not affect it that I tried while I was testing:
- Placing a armorstand on a slimeblock on top of a sticky piston, then make it invisible by unloading and loading chunks again. After that trying to make it visible by shooting it up in to the air. (Did not work)

- Changing from render distance 2 to 3 or 4 do nothing

- Use VBOs: on/off does not change anything.

Things that DO affect it when changed:
- Setting render distance to 6 or above will remove this totally. (Due to that you can not unload it and still be within 5 chunks)

- When setting render distance to 5 you can only reproduce this EXACTLY on the chunk border 5 chunks away.

- Moving further away than 5 chunks will reset all invisibility of the entities.

To sum it up.
Put down any entity (except regular items on the ground) and walk out of render distance, while still staying within 5 chunks of the target will make it invisible.
Moving further away than 5 chunks or quiting the game will make it visible again.
Setting render distance to > 5 will not result in invisible entities.

### Comment 14: migrated (2014-08-19T17:59:45.071-0700)

I made a more detailed post about this bug on my blog to not clutter up this thread to much: http://minecraft.cyoor.se/?p=57

### Comment 15: migrated (2014-08-20T03:25:50.158-0700)

I have a feeling it is related to MC-64161.

### Comment 16: lapppy (2014-08-22T23:17:36.346-0700)

Confirmed in 1.8-pre1. Very gamebreaking in my opinion.

### Comment 17: Sonicwave (2014-08-25T18:46:52.103-0700)

I have not experienced this with mobs but instead with the player's skin viewed from 3rd person.

### Comment 18: migrated (2014-08-25T19:01:55.992-0700)

: Are you are talking about third person view of your own avatar or looking at another player?
In case you are talking about a third person view of yourself, I see no way that you could get far enough away from yourself that you could unload your player. (Unless you do it some other way).
I think you should report that as another bug if it is yourself you are talking about, and maybe link to this one as maybe being related instead. This is based on what you can read in previous posts where I tested it.
However if it is some other player you are talking about, or that you have found some way to unload your own player, then it probably is the same bug, and more details would help. (Dont make a new bugreport if this is the case)

### Comment 19: migrated (2014-08-25T19:36:57.012-0700)

This probably is not the same issue, and I don't think the same unloading rules apply to the players because the player is not saved in chunks and can't be unloaded.

### Comment 20: Sonicwave (2014-08-26T16:11:31.568-0700)

@ Pierre Walden: 3rd person view of myself in Single Player.

### Comment 21: migrated (2014-08-26T17:12:07.056-0700)

: No, I don't think so either, but if it has something to do with something else than the entities just getting unloaded (in the normal way we think of it), then knowing if it had some effect on seeing other players aswell could have been a clue to something.
: I think you should look for other posts about what you are describing and if you cant find anyone matching, I think you should make a new report on that. But It would still be interesting if you could do some testing following what I did and see what happens.
Also I have some questions for anyone reading this:
1.) What graphics card and driver do you have? The reason that I am asking about this is that both me and the original poster got quite similar graphics cards (not identical). I just want to eliminate this as a cause.
2.) Have anyone ever seen this in multiplayer or only singleplayer?
3.) Could anyone try to reproduce what I described in my post, but on another computer and make sure that it is not just my setup that produces those exact results?
4.) Could someone do the same tests as I did, but on a server (read previous posts). On that server it would be interesting to see what happens with different view ranges on server/client. Test the ranges around 2-6 on view range. (Both on client and server)
Please if someone could test and post their results (any info), it would be intresting.
I would do this myself, but since I did my testing (that I wrote about before) I have not had so much time. So I haven't been able to go back and test it in a multiplayer world.
(For details on my testing, read my previous posts)

### Comment 22: Sonicwave (2014-08-31T03:24:24.155-0700)

Confirmed in 1.8-pre3.

### Comment 23: migrated (2014-08-31T08:57:26.437-0700)

I have the feeling this issue is often mixed up with MC-67608, which describes similiar things.

### Comment 24: migrated (2014-08-31T18:52:17.123-0700)

To continue my previous testing (Done some more testing):
- I have reproduced it in 1.8-pre3 with my previous way of testing.

- It seems that I am only able to reproduce this within the spawn chunks. (I am not 100% sure about this, but it seems like it)

- It does not have anything to do with the computer setup. (reproduced on several different computers with many different graphics cards and different java versions)

(I still have not tested on a server/client setup)

### Comment 25: migrated (2014-09-01T23:08:44.495-0700)

MC-68102 says that the mob distortion is caused by not having the lastest Java version.

### Comment 26: migrated (2014-09-02T05:51:10.839-0700)

Yes, and this bug has nothing to do with what Java version you have. I intentionally tested this, using both a computer with an older java and a computer with the latest java 7 (since I read somewhere that minecraft does not support java 8, I have not tested that)
I do not think that this bug has much to do with the mob distortion bug at all, and I have not even once get distorted mobs or mobs with body parts missing (and I have reproduced this bug around 500 times during the testing).
So yeah.. I don't have a clue of why the "distorted Mobs / body parts of mobs missing" is even in the title on this bug.

### Comment 27: migrated (2014-09-05T07:31:15.962-0700)

What are the forced entities under the crash report?

### Comment 28: migrated (2014-09-05T15:54:49.070-0700)

Confirmed. Definately. I was fighting mobs in my survival world at night, and there were no mobs near me. I'm walking, and I suddenly hear a creeper hissing sound. I look next to me and see an explosion out of nowhere, followed by a second creeper actually killing me. I've seen it with skeletons too. Please confirm, why is this still unconfirmed?

### Comment 29: kumasasa (2014-09-12T06:20:24.131-0700)

A possible cause for this is MC-66683

### Comment 30: migrated (2014-09-12T09:27:05.095-0700)

:
I would say that that one is a duplicate of this one.
If you have read my previous posts in this thread, you can see that NONE of the bugs set as duplicates to this one have anything to do with this bug. We have said that several times here if you read it all.
Also the change you made in the title from "Invisible Mobs" to "Invisible Mobs / body parts of mobs missing"  on 24/Aug/14 didnt make any sense (as we also have pointed out here before)
To be honest it seems like the changes you have made here have only dragged the description of the bugreport away from what it initially was a report for. The confusion you have here (that the rest of us doesn't have) is totally on you, since its you that have put things as duplicates that aren't duplicates, and also changed the title of the bugreport to something that the report is not related to.
It is totally clear what this bug is as I have described previously here both in posts in this bugreport, and in my blogpost (that I linked in a previous post here). It is 100% reproducible and I have gone in to details of how to do it. The bug you linked t as a possible cause is not just a "possible cause", it is 100% a duplicate of this one.
As  wrote 06/Sep/14, the bug MC-67608 should probably be reopened because it is NOT a duplicate of this one. Neither are any of the other bugs that you have put as duplicates here.
What you should do is:
1.) Revert back to the original title of the bugreport "Invisible Mobs" or change it to "Mobs become invisible when chunk gets out if render distance while still beeing loaded" (or something like that)
2.) Remove all the faulty duplicates that have just been put in here faulty to just die because they are not related.
3.) Set that thread you found as a duplicate of this one, since it the exact same bug.
Also, as someone said at some point 50% are duplicates on this board, so I sugest that you dont put more things as duplicates when they are not..
Sorry if I seem irritated here, but it is hard to reach anywhere when no one reads what is written.
Spending time reporting bugs kind of seems pointless when the conversation goes like this:
reporter: Bug is "A"
more people: Confirmed..
MOD: Oh.. Bug is "B", then it must be duplicated by all other "B".
Everyone else: No... Bug is "A" and is not related to "B" at all.
MOD: Ok I will change the title so that it says that the bug is "B".
Everyone else: Why? It is not "B".
Mod: It seems that all these other bugs are duplicates of B, lets close them.
Reporter of bug B: Why have you marked "B" as duplicate of "A"? They are not related.
MOD: No response
Everyone: We have now done a detailed analysis of "A", and it is still not related to "B", could you remove it?
Time passes.....
Mod: Oh I might have found a possible cause for this. LINK TO duplicate of "A"
Everyone else: Sigh... Well that is what this bug have been about all along.

### Comment 31: kumasasa (2014-09-12T13:35:30.127-0700)

@ et al.: Sorry for causing trouble here, things fixed. I made you the reporter of this ticket (Sorry ), so you can edit the summary and description.
To improve direct feedback to the mods there is a new subreddit at http://www.reddit.com/r/Mojira/

### Comment 32: migrated (2014-09-12T13:47:13.475-0700)

Thank you . I was already thinking that there was something weird going on between MC-66683,  and MC-67608, but it's fixed now. Important is that this issue is not related to the Java version, but MC-67608 probably is.

### Comment 33: migrated (2014-09-13T01:15:48.079-0700)

@ Thank you for clearing everything up, and I am sorry for maybe being a bit to harsh in my previous post. I got a bit tired and the frustration just boiled over.  I know that you mods are doing the best you can.
Regarding the issue.. I don't have that much time today, but I will try to as soon as possible make the bug description to contain all the vital information and details to make the bug report as clear as possible as soon as I can.
In the meanwhile: For everyone that got details on this or tests that you have done that I have not already written about, please post them here, and I will add those details to the summary when I update it.

### Comment 34: onnowhere (2014-09-13T09:08:42.248-0700)

Feel free to link to my MC-66683 report for it's tests and videos and explanations, or copy any info from there into here if you wish to.

### Comment 35: migrated (2014-09-13T13:05:34.022-0700)

The title and description of this bug need to be changed to include everything from MC-66683.

### Comment 36: migrated (2014-09-16T00:50:28.652-0700)

: I have for now copied a lot of the info from your report in to the description here and pointed out that the MC-66683 report have some important information. (I hope that you are ok with that?)
I guess that the two reports here have evolved independent of each other, and in both reports it seems that we have come a long way to figure this one out totally. This is good in a way I guess, since it shows how clear this bug is. But it also makes a lot of info spread over the two reports. I will try to go through everything in detail eventually to get it all in here eventually.
As soon as MCP is updated I will have a look at the code, but until then I have some more tests I would like to do.
Since you seem to be investing some time in to testing this, would you be interested in doing some of that testing together?
If so, feel free to contact me on mcblog[at]cyoor.se
: For now I have updated this report with the most important info from the other report. I will update this more soon to include all the testing that I have done. But since I have quite a lot to do atm, and most of the info is available in this thread or the other, I started by just making sure that the post important parts are noted here. More will have to come later.
While it makes things easier to get things done and will help a lot with the update of our testing, I did not expect to be set as the reporter of this ticket. I usually don't post tickets on my own when I don't have time to keep them up to date, but since I am invested in this one and I feel that I have tested it a lot already I will make sure that I wont let anyone down.
If anyone have comments on things that needs to be changed or made more clear, make sure to post them here and I will update with those details.

### Comment 37: migrated (2014-09-25T23:38:09.563-0700)

I think I am experiencing the same bug (unable to see mobs in game but can hear/get hurt by them), but I also can't seem to see other players in multiplayer, or my own character's skins in the inventory window. Does this help at all, or is it more likely something different?

### Comment 38: migrated (2014-09-27T00:43:17.192-0700)

: We have experienced the "invisible players" issue, that you describe, on our server as well, but we have not done any controlled tests yet to determine if it is caused by the same bug as this one. It might be, so if you have the possibility to do some more testing to give more info or maybe reproduce the invisible players thing, feel free to post it here.
If we find that it is the same issue, I will include it in the description, otherwise I guess that we know that it is a separate bug, and should be treated as such.
Things that you can test if you have the time is to do the same test as shown in the description, but instead you put players where you would have put the mobs/itemframes and so on. Go on to do the rest of the testing and see if it have the same results.
Also do one test where one player stands still and another player just runs off like 200 blocks and then back and see if it persists (Just as a control)
Regarding your own character's skin in the inventory, that is probably something else.

### Comment 39: Sonicwave (2014-09-29T20:01:09.775-0700)

Not sure if this has been mentioned already but their hitbox seems to disappear too (I attacked an invisible Villager and instead destroyed the block behind it).

### Comment 40: Sonicwave (2014-10-08T21:16:27.290-0700)

Also it seems that dying often causes dropped items to turn invisible (even if you are only a few blocks away). I did not find "die", "death" or "dying' with Ctrl+F so I assume that no one's stated it yet (though it has been reported several times.

### Comment 41: migrated (2014-10-08T21:37:07.043-0700)

^Yes, I first experienced this issue intermittently when dying and respawning....some of my items would be invisible but still collectible. F3+b shows no hitbox so my most logical guess is that the server is not sending the entity to the client to render.

### Comment 42: migrated (2014-10-09T04:39:13.694-0700)

: Items on the ground is the only type not showing the behavior when trying to reproduce this bug in the way we have done it so far.
It might however still be the same bug or something related. All info is useful. So if you could come up with a way to step by step reproduce this with items, I will test and see if it might in fact is the same bug but affected differently.

### Comment 43: migrated (2014-10-09T12:48:30.050-0700)

Is MC-67952 related to this?
Note: It's not a duplicate because MC-67952 also describes a flickering texture

### Comment 44: kumasasa (2014-10-09T15:26:17.077-0700)

IMO MC-67952 is about showing items and items as flat sprites being 0 pixels wide when looked at from straight above

### Comment 45: migrated (2014-10-09T15:31:56.539-0700)

:
Probably not, since this has to do with draw distance and loaded chunks. The way that bug is reproduced is totally different, so I do not think that they have much in common (except for the invisible part).

### Comment 46: marcono1234 (2014-10-12T05:38:45.933-0700)

Confirmed for
- 1.8 for items after death Sorry for no way to reproduce, here you go:

How to reproduce:
Die with items in your inventory in the spawn chunks (also with keepInventory false)

### Comment 47: migrated (2014-10-12T09:13:57.839-0700)

@
As I said to  before: Could you write down a way to step by step reproduce this with items, since items are not behaving the same way under other conditions. What you are experiencing might be another bug (or maybe the same). Either way, it is important to be able to reproduce and to check.
Until a way to reproduce items becoming invisible have been shown, I will not add it to the description.
So please.. I say it again: Write a step by step way to reproduce this with items.

### Comment 48: migrated (2014-10-12T13:38:59.153-0700)

this happened to me as I was experimenting with mobs and half slabs, after respawning for the nth time, at least two of the remaining skeletons turned invisible and both proceeded to attack and kill me.  now i had the render distance at 6 and the setup was just within viewing distance from spawn and in my astonishment i took numerous screenshots of which I selected 1 per second to insert into this gif.

### Comment 49: Sonicwave (2014-10-12T20:57:35.755-0700)

To reproduce items invisible on ground after dying:
1) Create a superflat world (preferably w/o grass so you can see items better)
2) Create a 1x1 platform above the ground
3) Set your spawn point (/spawnpoint) several blocks away from the platform
4) Give yourself some items, stand on the platform and do /kill
5) If items show up, kill yourself again until they do disappear.
6) When items disappear, type /entitydata @e (you will see that they exist but are not visible and may/may not be able to be picked up).
Teleporting away and back fixes the issue.

### Comment 50: migrated (2014-10-13T11:14:54.653-0700)

: I tried your method, but could not reproduce the problem. (Tried around 50 times to be sure, then I tried some other parameters, but with no results.)
Could you help me a bit? Specifically, could you clear up the following:
- How far above the ground do you have the platform / block?

- How far exactly is "several blocks away"?

- What render distance do you use, and does the render distance affect this?

- Can you reproduce the same thing at another location away from spawn, but instead use a bed?

Also.. Just to make sure: Have you checked so that it is not  ?

### Comment 51: migrated (2014-10-13T11:28:48.270-0700)

: It was a bit hard to tell what was going on from your gif.
You said that you were experimenting with halfslabs when this happend. Did you have anything below?
I could see a head in some of the pictures, are you sure that it is not  that you are experiencing? I dont know, but skeletons might be able to shoot you while still seem to be below the ground (and thus be invisible to you).
If not, could you describe a bit more what was going on?

### Comment 52: Sonicwave (2014-10-13T13:22:51.593-0700)

: Attached the world (newly generated). Just now it happened on the 3rd try on 11 render distance (though last time it happened on 4). When the items disappear, type

```/testfor @e[r=20]```
 and you will see that the item is within the radius, but invisible.
EDIT: It works also if you sleep in a bed elsewhere and /kill yourself 10 blocks away from the bed. There does not need to be a platform.
Also it seems that the world compressed into a RAR not a zip, I don't know if this will cause problems (but if it does you can also use the world in MC-68403).

### Comment 53: migrated (2014-10-14T05:42:14.721-0700)

: Yes I can confirm the items disappearing now. That is not the same bug as this one. The bugs are reproduced in different ways, they are not affecting the same items, render distance does not seem to affect the bug you have discovered and there are a lot of other differences... So not the same bug. I think that MC-68403 is the one you are experiencing though, so that one being a duplicate of this one is wrong.
If some mod sees this, please remove MC-68403 duplicating this one. They may at best be related.

### Comment 54: kumasasa (2014-10-14T05:45:40.287-0700)

If some mod sees this, please remove MC-68403 duplicating this one
Done & reopened MC-68403

### Comment 55: Sonicwave (2014-10-14T20:00:46.888-0700)

Thanks for the clarification. In that case MC-66136, MC-68504, MC-70949, and possibly MC-68693, MC-68086, MC-72620, MC-72865 and MC-71487 (they describe other entities, not just items) are duplicates of that issue and not this one.

### Comment 56: migrated (2014-10-15T03:38:56.439-0700)

: Thanks
:
I read through all of those reports and I agree in some cases, but it is quite hard to say in other cases. (Those cases probably dont matter, since the info on those reports are so thin). Anyway.. This is what I think regarding those that you posted:
The ones that is dupe of MC-68403:
MC-66136
MC-68504
MC-70949
Not enough info, but probably this one:
MC-68086
Not enough info, but probably MC-68403:
MC-72865
Not enough info (Could still be either one):
MC-68693
MC-72620
MC-71487

### Comment 57: kumasasa (2014-10-15T11:08:52.145-0700)

@: Yes, most of the other tickets have very little information, I resolved all "death" tickets to MC-68403

### Comment 58: onnowhere (2014-10-15T16:30:15.364-0700)

Still in 1.8.1 pre-1

### Comment 59: migrated (2014-10-16T04:15:40.443-0700)

: Yeah that sounds reasonable. Thanks.

### Comment 60: migrated (2014-11-09T17:08:31.304-0800)

: Sorry for not responding sooner to your question but I am certain that it is not related to #MC-119 as I placed the mobs there myself.  I put a bunch of skeletons in a hole 1 block deep with a half-slab roof and attempted to see how many of the skeletons I could coax into killing each other without dieing too often.  I tried similar experiments prior to that with other kinds of hostile mobs but the skeletons were the only ones that could still harm the player and stay in their hole.  I would upload the annotated world file but the computer it is on is currently in the repair shop for a damaged motherboard.  However, if and when I get the world file back in one piece, I will attach it to this issue report either under its original file-name, "Note Block Magic", or as "Mob Experiments" and hopefully clear up some confusion.

### Comment 61: onnowhere (2014-11-19T08:16:19.370-0800)

Still in 1.8.1-pre 5

### Comment 62: Sonicwave (2014-11-30T16:57:03.247-0800)

Still in 1.8.1.

### Comment 63: migrated (2014-12-17T14:57:03.134-0800)

I am having the same issue running official "release 1.8.1" singleplayer with no mods. It is opened up as a LAN game.
We are using itemframes for our storage chest area; as a result, we have 55+ itemframes up with items in each them.
Well before they started disappearing...
Also, before I forget:
Java 7 Update 67 (build 1.7.0_67-b01)
Windows 7 Enterprise 64bit SP1 (Legit)
AMD FX(tm)-8120
NVIDIA GeForce GTX560Ti
16GB RAM

### Comment 64: migrated (2014-12-29T05:14:55.263-0800)

Still in 1.8.2-pre1. I experienced it while playing a challenge map.

### Comment 65: migrated (2014-12-29T05:27:46.374-0800)

No wait, i'm not seem to experience this on 1.8.2-pre1 on the challenge map i'm playing, but yes on 1.8.1.

### Comment 66: Sonicwave (2014-12-29T15:44:21.077-0800)

Confirmed for 1.8.2-pre1.

### Comment 67: migrated (2015-01-30T21:11:13.303-0800)

Can confirm for 1.8.2-pre3

### Comment 68: TheTamedWolf (2015-01-31T15:34:59.686-0800)

This happened to me in 1.8.2pre6
Sometimes f3+A to reload the chunks beings the mobs back but it doesn't seem to work for things like item frames. Unless, can someone see if I am doing this right? (I noticed if you aren't EXTREMELY accurate with the commands, the mob or item will summon but it eventually disappears.)
This one works but only disappears (goes invisible) when I open to LAN.
summon ItemFrame -90 72 481 {Invulnerable:1,Facing:3b,ItemRotation:1b,Item:{id:blaze_rod}}
These disappear all the time when the chunk unloads.
summon ItemFrame -90 72 481 {Invulnerable:1,Facing:3b}
Note: The above disappears regardless if i put an item in it or not; invulnerable or not.
EDIT: This report is about item frames too right?

### Comment 69: migrated (2015-02-21T03:30:05.979-0800)

This still happening in 1.8.3, please fix that bug, is so annoying in Skyblock worlds.

### Comment 70: TheTamedWolf (2015-02-21T09:11:48.878-0800)

@kumasasa
It seems to only happen in the spawn chunks. For me anyway, I noticed that as long as I don't build my towns and such in the spawn chunks, the people and other entities don't disappear, including item frames!

### Comment 71: migrated (2015-03-19T16:33:52.220-0700)

Happens at any location for me, with both the view distance, and the getting killed methods, with or without using a bed. Occurs most often with mobs.
Yields — "Signature is missing from textures payload"
1.8.3

### Comment 72: migrated (2015-03-20T21:25:21.356-0700)

I just hit the horse teleport bug , it seems like the two would be related?
After teleporting a mob 100 blocks (assuming it's probably 80 like I saw with the horse), I see this.
F3+A did not reload the mob for me, I had to relog or move around a bit to get it to appear.
Render Distance at 32 chunks.

### Comment 73: migrated (2015-03-24T20:47:55.252-0700)

I found a simple fix for this
I have a potato battery (sarcasm) for a computer so I frequently deal with this bug because I only render 2-4 chunks normally.
What I found is that if I traveled a few chunks away, then went back to the same location, having it reload the chunk the bug was in, the entities would become visible again.
Hope this helps

### Comment 74: migrated (2015-04-11T07:05:23.687-0700)

@Quinn Coral
That's more similar to MC-45067, you should probably mention it there.

### Comment 75: onnowhere (2015-04-27T16:07:35.315-0700)

Still in 1.8.4

### Comment 76: migrated (2015-05-03T12:16:15.928-0700)

My issue (MC-74044) is not a duplicate of this post. Whoever decided to call it a duplicate is wrong and very sorry indeed.

### Comment 77: migrated (2015-05-05T04:02:40.006-0700)

The entities affected by this bug, still make particle effects (Blazes) and even if they have no hitbox, you cannot place blocks if the entity is in your way

### Comment 78: onnowhere (2015-05-12T21:53:43.888-0700)

I noticed today that it can occur in render distances up to even 8 chunks, and maybe more if condition is right..

### Comment 79: kumasasa (2015-05-15T05:12:25.502-0700)

MC-80298 is a possible cause for this issue.

### Comment 80: EarlyReflections (2015-08-13T10:59:58.640-0700)

I'm experiencing the same issue on my 15w33b server where almost all my villagers disappear (become ghosts) from my villager farm. I haven't found a way to reproduce it but it seems to be related to chunks loading/unloading. Server's render distance is set to 10 chunks. Only solution is to restart the server, several times a day.

### Comment 81: migrated (2015-08-16T09:53:26.223-0700)

Confirmed for 15w33c.

### Comment 82: migrated (2015-08-18T12:02:24.560-0700)

Sorry for the bump, but this is important. This bug has been here for quite a while but it is still unassigned.

### Comment 83: migrated (2015-08-20T09:01:01.661-0700)

I experience this even with render distance of 32 chunks, in 15w34a.  I only noticed it for the first time, however, in 15w32a.  I have lots of item frames, so this gives me the impression that something recent might have changed to affect large render distances, whereas this wasn't a problem before for such render distances.  (If that even makes sense.)

### Comment 84: migrated (2015-09-05T14:04:40.958-0700)

Confirmed for 15w36d. Armor stands turn invisible, and executing a command or using testfor proves their existence. I went to the nether a few times, and some in one chunk were invisible, while others in a different chunk were still there. Ughghghg.
Edit0: All chunks are spawn chunks.

### Comment 85: migrated (2015-09-14T08:20:39.810-0700)

Issue persists in 15w37a, single player
I have several armor stands that are executing a glowing effect to all players in a selected radius. Occasionally they will disappear and the execute command will no longer function.  Exiting and reloading the world will make them pop back up. I have seen villagers disappear as well, but I haven't tested on them as extensively as I have on armor stands.
Issue seems entirely random and is not associated with persistent chunks.

### Comment 86: EarlyReflections (2015-09-14T13:56:47.150-0700)

This issue is a puzzle to reproduce. It does seem to be related to chunks loading/unloading but when I try to reproduce the problem it doesn't manifest itself.
In 15w37 however, it's worse than ever. Whenever I log onto my server, ALL my farms are "empty". No cows, no sheeps, no chickens, no villagers, no minecarts, no armor stands. I have to teleport far away (or go to the nether), wait 30 seconds then come back to make them reappear. Using /testfor @e when close to the invisible entities results in a "that entity cannot be found" error.
My iron golem farm isn't producing anything for more than 75% of the time, since most of the times villagers are gone (invisible villagers don't register in villages).
It's weird to see that this issue is more than a year old and nothing is being done on such a showstopper. However, I haven't seen this problem very much until the 1.9 snapshots. In 1.8 it seemed to happen but very rarely and on very few entities. In the 1.9 snapshots it's "always" occuring. My iron farm is almost never producing anything, my villager trading station is pretty much empty all the time.
Please have someone look into this, as it's become very annoying and is disabling every single automatic farm (relying on entities), making the game almost unplayable and useless. I understand it wasn't such of an issue before as it rarely happened. But now the problem is present all the time and has become a huge issue.

### Comment 87: migrated (2015-09-14T14:21:56.250-0700)

if you make a world in 1.8.8, then open in snap, world is fine
EDIT: World becomes corrupt after, even, mobs without hotboxes and invisible any way

### Comment 88: migrated (2015-09-14T16:29:11.400-0700)

@Early Reflections abd other recent commenters:
This issue is only about entities being invisible clientside/not being sent to the client. In all cases they are still there serverside, can still attack you, be identified by testfor, etc.
No doubt your issue is also severe, but I think there's another ticket that better suits it (permanent disappearances)
Unless there's some weird case where it disappears both client and serverside, then reappears on login. Then that'd be really weird 0.o

### Comment 89: EarlyReflections (2015-09-15T09:28:15.026-0700)

@Vincent Lee:
Well, it seems it's really weird then! I wouldn't classify it as a "permanent disappearance" because they do reappear on chunk unloading/reloading, but more as a "total disabling and disappearing" of them, both server-side and client-side.
Invisible farmers don't farm, invisible hopper-minecarts don't run and don't collect anything, invisible animals have no hitboxes and cannot be heard/moved/fed/killed, invisible chickens don't lay eggs, invisible baby entities never grow up.
If this was only client-side, all of the above would be false. They would just be invisible, but still do their work.
I will try to post a video showing this before tomorrow.

### Comment 90: EarlyReflections (2015-09-16T00:35:21.151-0700)

Here's a video showing the problem: https://youtu.be/0mfzklwtNBc

### Comment 91: onnowhere (2015-09-18T06:45:05.041-0700)

THANK YOU SEAAAAAAAAAAAAAAAAAAAAAAAARRRRRGEEEEEEEEEEEEEE :DDDDDDDDDDDDDDDDDDDDDD

### Comment 92: migrated (2015-09-18T16:02:06.092-0700)

This definitely isnt fixed in 15w38b, Windows 7 sp1 x64, java 8 update 60 x64, a6-4400m cpu/ amd 7520g integrated graphics.

### Comment 93: migrated (2015-09-18T16:03:16.381-0700)

That's why it says Future Version.

### Comment 94: migrated (2015-09-18T16:27:07.878-0700)

Why is 15w38b listed as one of the fixed versions then? or does it mean itll be fixed in the release after 15w38b?

### Comment 95: migrated (2015-09-18T16:27:44.770-0700)

They tried a fix, didn't work. Now they did 3 fixes.

### Comment 96: EarlyReflections (2015-09-19T02:16:48.366-0700)

The current fix in 15w38b did the trick for my case. None of the issues I had ever occured again. Entities simply became "invalid" entities server-side, I guess. Thanks a ton for this!
On the other hand, since the fix, console spams a lot of "Tried to add entity X with pending removal and duplicate UUID xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx" errors. But it's basically a non-issue at this point!

### Comment 97: kumasasa (2015-09-19T02:57:39.574-0700)

: This is MC-88922

### Comment 98: SeargeDP (2015-09-28T07:51:34.767-0700)

Fixed again (for the 3rd time, fixing a 4th bug in addition to the 3 bugs I already found last time), hopefully it's now solved completely.

### Comment 99: Irbis (2015-10-12T12:46:39.949-0700)

Abandon your hope, Searge, because in 15w41b there is still invisible mob bug. =P
To reproduce:
set render distance to minimum (2 chunks)
type:

```/summon Pig ~ ~ ~2 {NoAI:1}
/tp @e[type=Pig] ~ ~ ~20
/tp @p ~ ~ ~20```
You should be next to pig, but there is no spoon... I mean there is no pig. You can't see it and do not collide with it, but also you can't place blocks, where the pig is.
It can happen far from spawn chunks (1000x, -2000z)

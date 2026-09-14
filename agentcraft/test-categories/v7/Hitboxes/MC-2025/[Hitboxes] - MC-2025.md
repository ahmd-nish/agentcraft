# MC-2025: Mobs going out of fenced areas/suffocate in blocks when loading chunks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-2025](https://bugs.mojang.com/browse/MC-2025)

## Report details

- **Mojira categories:** Entities; Hitboxes
- **Project:** MC
- **Issue key:** MC-2025
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-11-02T18:05:08.771-0700
- **Updated:** 2025-04-26T02:31:21.189-0700
- **Resolution date:** 2024-12-31T18:36:42.751-0800
- **Affects versions:** Minecraft 1.4.2; Minecraft 1.4.4; Minecraft 1.4.5; Snapshot 12w50b; Minecraft 1.4.6; Minecraft 1.4.7; Snapshot 13w01b; Snapshot 13w04a; Snapshot 13w06a; Snapshot 13w07a; Snapshot 13w09c; Snapshot 13w10a; Snapshot 13w10b; Minecraft 1.5; Snapshot 13w11a; Minecraft 1.5.1; Snapshot 13w16b; Minecraft 1.5.2; Snapshot 13w17a; Snapshot 13w18c; Snapshot 13w19a; Snapshot 13w21a; Snapshot 13w21b; Snapshot 13w23b; Snapshot 13w24a; Snapshot 13w24b; Snapshot 13w25a; Snapshot 13w25b; Snapshot 13w25c; Snapshot 13w26a; Minecraft 1.6; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.6.4; Minecraft 13w36a; Minecraft 13w42b; Minecraft 13w43a; Minecraft 1.7; Minecraft 1.7.1; Minecraft 1.7.2; Minecraft 1.7.3; Minecraft 1.7.4; Minecraft 14w02b; Minecraft 14w02c; Minecraft 14w08a; Minecraft 1.7.5; Minecraft 14w11b; Minecraft 1.7.6-pre1; Minecraft 1.7.9; Minecraft 14w18b; Minecraft 14w21b; Minecraft 14w25b; Minecraft 14w26c; Minecraft 1.7.10; Minecraft 14w27b; Minecraft 14w28b; Minecraft 14w34b; Minecraft 14w34d; Minecraft 1.8-pre2; Minecraft 1.8; Minecraft 1.8.3; Minecraft 1.8.4; Minecraft 1.8.7; Minecraft 1.8.8; Minecraft 15w32c; Minecraft 15w34d; Minecraft 15w38b; Minecraft 1.8.9; Minecraft 16w02a; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.2; Minecraft 16w15b; Minecraft 1.10; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w39a; Minecraft 16w39b; Minecraft 16w39c; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w42a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 1.12 Pre-Release 5; Minecraft 1.12 Pre-Release 6; Minecraft 1.12; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 1.13-pre8; Minecraft 1.14.2; 1.14.4; 20w12a; 20w17a; 20w22a; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w29a; 1.16.2 Release Candidate 1; 1.16.2; 1.16.4; 20w49a; 20w51a; 21w03a; 21w05a; 21w19a; 1.17; 1.17.1; 1.18; 1.18.1; 22w03a; 1.18.2; 1.19; 1.19.1 Pre-release 2; 1.19.1 Pre-release 3; 1.19.3; 23w04a; 1.20.1; 1.21; 1.21.3; 1.21.4
- **Fix versions:** Minecraft 15w45a; Minecraft 17w47a
- **Area:** Platform
- **Labels:** animal; area; chunk; cobblestone_wall; fence; mob; outside
- **Watchers:** 1
- **Attachments:** 30
- **Attachment filenames:** 1.6.2 (1).png; 2013-03-08_15.14.39.png; 2013-03-08_15.31.41.png; 2013-03-08_15.35.12.png; 2013-03-21_13.03.03.png; 2013-03-21_13.03.05.png; 2013-03-21_13.06.37.png; 2013-03-22_12.31.40.png; 2013-03-22_12.31.49.png; 2013-03-23_09.29.12.png; 2013-03-23_09.29.30.png; 2013-04-23_11.20.23.png; 2013-05-06_23.11.35_2.png; 2013-05-06_23.11.35.png; 2013-05-06_23.11.36.png; 2013-05-06_23.11.54.png; 2013-05-06_23.11.59.png; 2013-05-06_23.13.31.png; 2013-05-06_23.13.33.png; 2013-05-06_23.13.44.png; 2013-05-06_23.18.13.png; 2013-06-16_01.20.35.png; 2013-06-16_01.27.43.png; 2013-06-16_01.46.40.png; 2013-07-06_01.17.46.png; 2025 Bug Still Present 1.6.2.zip; BugStillPresent.png; chickenfences.jpg; Mob Escape Testing.zip; Screenshot.jpg
- **Issue links:** Relates:outward:MC-280290:Downscaled mobs can phase through walls and suffocate upon chunk reload | Relates:inward:MC-10:Mobs temporarily glitch out of fenced areas / into blocks | Relates:outward:MC-129994:Pufferfish can go through glass panes by puffing | Duplicate:inward:MC-80366:Mobs Suffocating When Loading World | Duplicate:inward:MC-248319:Cows excaping through fences. | Duplicate:inward:MC-245068:Mobs Phasing Through Fences | Duplicate:inward:MC-251765:Animals Phasing Through Fences | Duplicate:inward:MC-238849:Fence does not hold chickens | Duplicate:inward:MC-231679:Cows can clip through fence | Duplicate:inward:MC-229763:Mobs push themselves into blocks | Duplicate:inward:MC-214083:Animals glitching through fences | Duplicate:inward:MC-213672:Mooshrooms overcrowded in a single block cow crusher teleport instead of dying | Duplicate:inward:MC-158982:Mobs in minecart disappearing / dying | Duplicate:inward:MC-198738:mobs glitching through walls | Duplicate:inward:MC-18883:Horses suffocating when loading a new world | Duplicate:inward:MC-15694:Zombies go through walls | Duplicate:inward:MC-195205:Mobs Going through Walls | Duplicate:inward:MC-180829:Chicken Mob Glitch | Duplicate:inward:MC-26858:Animals get stuck in fence corners and chicken pass through fences. | Duplicate:inward:MC-29098:problems with animals and pens | Duplicate:inward:MC-86266:Hit-boxes with mobs/fences | Duplicate:inward:MC-155944:farm mobs are able to jump over fences | Relates:inward:MC-50821:Cats and dogs teleporting into transparent-solid blocks (redstone_bloc, glowstone, TNT), causing them to suffocate | Duplicate:inward:MC-136810:Dolphins in glass aquariums sometimes fall out of the bottom and die also they disappear from tank | Duplicate:inward:MC-27173:Horse Suffocation | Duplicate:inward:MC-120499:Animals can walk through fence and wall | Duplicate:inward:MC-118669:Relogging causes mobs between fence hitboxes to glitch through blocks | Duplicate:inward:MC-10422:Fencis bug | Duplicate:inward:MC-11252:Farm animals actually phasing through fences/glass panes--not just old visual glitch | Duplicate:inward:MC-12011:Chickens being pushed by water will pass thorugh a fence when logging out then logging back in. | Duplicate:inward:MC-19311:Animals able to escape fenced areas | Duplicate:inward:MC-33394:Sheep, and possible other mobs, still glitch through fences | Duplicate:inward:MC-41181:Animals appear outside the fences when you open the world | Duplicate:inward:MC-49747:chickens escape through fences | Duplicate:inward:MC-36308:My animals still escape their pens, even when I use leads to keep them in. | Duplicate:inward:MC-117521:Villagers glitch into blocks and die when I come through from the Nether | Duplicate:inward:MC-5369:Animals Leaving Fenced-In Areas | Duplicate:inward:MC-11203:13w10b Baby animals spawn outside of fenced in areas when world is loaded | Duplicate:inward:MC-19528:Zombie Pigman Clipping through one block space with door next to it. | Duplicate:inward:MC-115146:Villager Pushed Through Walls | Duplicate:inward:MC-28187:Animals Escaping Pens. | Duplicate:inward:MC-42006:Animals go Through Fences | Relates:inward:MC-77196:Villagers glitching through glass - reproducable | Duplicate:inward:MC-112471:Pigs, Cows, and Fences | Duplicate:inward:MC-112353:Beug wooden barrier animals glitch | Duplicate:inward:MC-109467:Villagers stuck in blocks and die 1.10.2 | Relates:outward:MC-73302:Block collision box issues (mobs glitch through blocks and more) | Duplicate:inward:MC-107232:Mobs can push each other into blocks on world load | Duplicate:inward:MC-85654:Entities get pushed into and through walls when relogging | Duplicate:inward:MC-105436:Animals walking through fences | Duplicate:inward:MC-105720:mobs clipping into walls and suffocating | Duplicate:inward:MC-105710:Fences 'Leaky' for animals in 1.10.2 for PCs | Duplicate:inward:MC-104745:Enities in small boxes | Duplicate:inward:MC-89231:Villagers teleporting | Duplicate:inward:MC-103007:Glitch | Duplicate:inward:MC-101046:animals go to walls | Duplicate:inward:MC-81473:Phasing Horses | Duplicate:inward:MC-97270:Skeletal (for me) horses phase through fences and some blocks. | Duplicate:inward:MC-95895:Passive Mobs glitch through cobblestone walls | Duplicate:inward:MC-94112:Entities fall through or walk through solid blocks | Duplicate:inward:MC-93015:Mobs glitching out from fences when reloading world | Duplicate:inward:MC-89867:animal glitching trough fences or walls | Duplicate:inward:MC-88983:Animals bugging through fences in multitude compared to 1.8 and prior versions | Duplicate:inward:MC-88923:Animals | Duplicate:inward:MC-88903:Cocoabeans and animals phasing trough walls | Duplicate:inward:MC-54552:Escaped Animals | Duplicate:inward:MC-41928:Animals are escaping thier pens. | Duplicate:inward:MC-40220:Animals going through fences | Duplicate:inward:MC-38181:Horses can pass through walls | Duplicate:inward:MC-36347:Mobs Escaping Pens | Duplicate:inward:MC-33316:Iron golem disappeared | Duplicate:inward:MC-32794:Animals still escape from fences at 1.6.4 | Duplicate:inward:MC-30683:Animals Escaping | Duplicate:inward:MC-29214:Baby horses still go through walls and die | Duplicate:inward:MC-27144:Mobs escape fenced ereas | Duplicate:inward:MC-26989:Chickens "jumping" fences | Duplicate:inward:MC-25966:Animals Still Escaping | Duplicate:inward:MC-24282:Villagers getting hurt when entering the game | Duplicate:inward:MC-21065:Mobs glitching! | Duplicate:inward:MC-20052:Baby Cows | Duplicate:inward:MC-19025:Animals escape from fences. | Duplicate:inward:MC-18732:Horses attached to leads clip through fences | Duplicate:inward:MC-18392:Animals Going Through Fences | Duplicate:inward:MC-17691:Sheep glitch through fences | Duplicate:inward:MC-17173:Mobs passing through fences | Duplicate:inward:MC-15169:Chickens get out of fenced areas | Duplicate:inward:MC-14741:baby mobs (cows, pigs) will go trough blocks wenn they are in one by one holes(solid blocks) | Duplicate:inward:MC-14453:cows cliping suffocating or even going trough blocks when logging in and out | Duplicate:inward:MC-13570:Mobs die/escape upon reloading world | Duplicate:inward:MC-12841:Animals escape pens made of wooden fences | Duplicate:inward:MC-12732:Animals not bound by fences | Duplicate:inward:MC-12564:Animals Warping Out Of Fenced Areas | Duplicate:inward:MC-12562:Mob Glitching | Duplicate:inward:MC-12348:Mobs escaping through fences | Duplicate:inward:MC-12260:bug mobs when they are in enclosure | Duplicate:inward:MC-12221:Animals escaping through the walls ! | Duplicate:inward:MC-12176:Baby animalss will escape fence boundaries upon logging out, then logging back in. | Duplicate:inward:MC-12114:Animals escaping in a completely fenced in area | Duplicate:inward:MC-11971:Animals frequently getting through fences in 1.5 update | Duplicate:inward:MC-11621:Mobs are glitching out of their cages upon reloading chunks | Duplicate:inward:MC-11455:Mobs glitch through or into blocks on log in | Duplicate:inward:MC-9777:Failing Fences | Duplicate:inward:MC-8707:Mobs go through fences on world load | Duplicate:inward:MC-4707:Mobs glitch through floor/walls on chunk loading | Duplicate:inward:MC-52279:Animals glitch out of corner fences. | Duplicate:inward:MC-20487:Baby cows walk through fences.. | Duplicate:inward:MC-16833:Cows escaping from fence enclosed area | Duplicate:inward:MC-11774:Baby animals seem to be able to escape fences and fence gates when a chunck is unloaded | Duplicate:inward:MC-86988:Animals glitching into fences/blocks on server restart | Duplicate:inward:MC-85762:Animals escape their pens apon world reload | Duplicate:inward:MC-85717:Spawned villagers are escaping from stone wall shops.. ? | Duplicate:inward:MC-85550:Mobs glitch into solid blocks and suffocate upon loading chunks | Duplicate:inward:MC-82262:Sheep leave their pens when I leave the chunk they are in | Duplicate:inward:MC-28709:The animals are still escaping their pens. | Duplicate:inward:MC-27135:Mob glichting through blocks (not fence glitch) | Duplicate:inward:MC-19860:Baby animal mobs escape fence pens. | Duplicate:inward:MC-18881:Baby mobs glitch through any type of block upon re-log | Duplicate:inward:MC-17228:Horses Going through walls and fence gates. | Duplicate:inward:MC-17138:Animals in enclosed spaces die | Duplicate:inward:MC-16925:Fences aren't holding in cows, chickens, pigs, and sheep. | Duplicate:inward:MC-14954:Animals escape from pens made of fences | Duplicate:inward:MC-11009:Mobs glitching through fences | Duplicate:inward:MC-10311:animals are getting out of fenced areas | Duplicate:inward:MC-9988:Animals can pass through fences. | Duplicate:inward:MC-9483:Animals in pens randomlly walk into walls and suffocate | Duplicate:inward:MC-2037:Black Sheep glitching through walls | Duplicate:inward:MC-26179:Mobs (Animals) passing through[glitching] fences | Duplicate:inward:MC-35309:Mob Glitching Through Fences Bug | Duplicate:inward:MC-7392:Animals escaping with no way to escape | Duplicate:inward:MC-10231:Extreme Animal Glitches | Duplicate:inward:MC-11950:animals escaping | Duplicate:inward:MC-12645:Pigs can walk through fences | Duplicate:inward:MC-12837:Animals are escaping, and mobs are attacking by walking cleanly through fences. | Duplicate:inward:MC-14866:small animals escape the fences | Duplicate:inward:MC-18515:Chickens move through cobblestone house in village generated map | Duplicate:inward:MC-26699:I think the "animals escaping pens fix" was missed for sheep | Duplicate:inward:MC-32129:Mobs get out of fences | Duplicate:inward:MC-78431:Pigs escaping fenced in areas with 1 gate that was closed in Minecraft Realms. | Duplicate:inward:MC-76227:Mobs escape fences | Duplicate:inward:MC-78014:Cow glitches through fences and glass | Duplicate:inward:MC-77955:Mobs Leaving Fence | Duplicate:inward:MC-74678:Animals Escaping from fenced enclosures | Duplicate:inward:MC-73943:Animals escaping fences area | Duplicate:inward:MC-72600:Fences and carpet | Duplicate:inward:MC-73140:Suffocating animals | Duplicate:inward:MC-72062:Wither skeletons glitching through walls bug. | Duplicate:inward:MC-70942:Animals can escape fenced areas | Duplicate:inward:MC-70834:Chickens glitched right out of glass pen | Duplicate:inward:MC-70299:Sometimes animals escape fences. | Duplicate:inward:MC-70265:mobs glitching | Duplicate:inward:MC-70140:Bunnies | Duplicate:inward:MC-70012:Cows and sheep moving through fences in 1.8-pre2 | Duplicate:inward:MC-69252:Horse Randomly Dying | Duplicate:inward:MC-68237:Animals go outside the fencing when chunk is loaded | Duplicate:inward:MC-67529:Farm animals glitching into/through fences | Duplicate:inward:MC-66011:Animals teleport through fences | Duplicate:inward:MC-64548:Cows Dying Next to Fences. | Duplicate:inward:MC-64375:Mobs escape pens | Duplicate:inward:MC-64467:Animals can jump the fences when I open the world | Duplicate:inward:MC-63736:Upon Loading Horses in a small fenced area will clip though fence | Duplicate:inward:MC-63749:World Loading Mobs | Duplicate:inward:MC-61767:Rabbits Going through glass | Duplicate:inward:MC-60614:Sound of villager being hurt upon entering world | Duplicate:inward:MC-59779:Animals Suffocate in Fence when loading in Map | Duplicate:inward:MC-59637:Animals going trough fences | Duplicate:inward:MC-58738:Animals getting out of fenced in area. | Duplicate:inward:MC-56426:Certain Mobs Escaped Pens made of fences during an update from 1.7 to 14w21b | Duplicate:inward:MC-55688:cows,sheep&pigs are missing from fenced in areals,when fences even three high&less then 19 blocks sq. | Duplicate:inward:MC-54779:Passive Mobs escape their pens | Duplicate:inward:MC-53292:all animals keep escaping and entering closed pens | Duplicate:inward:MC-53119:animals get through fences | Duplicate:inward:MC-51727:Animals can go through stone walls | Duplicate:inward:MC-49699:Villagers walk into walls and suffocate themselves for no reason. | Duplicate:inward:MC-49862:Chickens escaping fence | Duplicate:inward:MC-49837:Chickens getting through fences | Duplicate:inward:MC-48176:Baby Cow Bug | Duplicate:inward:MC-47833:Animals phase through blocks | Duplicate:inward:MC-46219:Chickens Phasing Through Walls | Duplicate:inward:MC-45434:Animals escaping fenced areas in 14w03b | Duplicate:inward:MC-42465:Sheep escape | Duplicate:inward:MC-42314:Bug | Duplicate:inward:MC-42048:Baby Villagers escaping through Iron bars | Duplicate:inward:MC-41997:Fence Glitching | Duplicate:inward:MC-41710:animals keep walking through cobblestone walls | Duplicate:inward:MC-19955:Baby Cows Everywhere! | Duplicate:inward:MC-38726:Animals Escaping Their Pens When Disconnecting | Duplicate:inward:MC-38156:Animal glitch | Duplicate:inward:MC-33427:Villagers (mobs in general) escape fences if crowded. | Duplicate:inward:MC-32946:Animals *STILL* escaping pins and some are stuck in the corner... i didn't see horses this time | Duplicate:inward:MC-29769:Horse suffocating bug is back | Duplicate:inward:MC-29283:If you relog on multiplayer the animals sometimes escape pens. (currently ive only had escaped sheep) | Duplicate:inward:MC-28588:my animals keep going through the fences | Duplicate:inward:MC-28218:Animals and Pens - Bug NOT fixed! | Duplicate:inward:MC-27561:Animals Escape Pens | Duplicate:inward:MC-26928:Animals escaping from pens | Duplicate:inward:MC-17508:Animals walk through fencing being used as pens. | Duplicate:inward:MC-19916:Animals | Duplicate:inward:MC-17650:Sometimes pig can go trought closed door | Duplicate:inward:MC-17380:Mobs seem to escape upon relog in SMP when ompressed into small spaces and covered by transparent blocks (glass) | Duplicate:inward:MC-17095:Baby Animal's Glitch through Transparent Blocks (Fence, Iron bars, etc) upon Relog in SSP and SMP | Duplicate:inward:MC-16675:Baby animals seem to walk through fences when loading the game | Duplicate:inward:MC-15856:Cows jump appear to have jumped over fences | Duplicate:inward:MC-15470:Animals getting trough fences and cobblestone walls | Duplicate:inward:MC-15317:Chicken's can walk right through fence's | Duplicate:inward:MC-15217:Animals glitching through single layer blocks | Duplicate:inward:MC-14335:horses glitch threw 2 high fence | Duplicate:inward:MC-13504:Chickens, pigs and cows are going trough blocks | Duplicate:inward:MC-13117:Fences | Duplicate:inward:MC-12822:baby sheep can jump over fences | Duplicate:inward:MC-12428:Farming mobs escape after disconnect and reconnect. | Duplicate:inward:MC-12297:Animals leave the farm / | Duplicate:inward:MC-12227:Pigs evade from fences and cobblestone walls | Duplicate:inward:MC-12018:Wierd fence issues | Duplicate:inward:MC-11386:Chicken Clipping issue | Duplicate:inward:MC-9525:Baby Animals Glitch Through Blocks (Cows and Pigs) | Duplicate:inward:MC-9476:fences | Duplicate:inward:MC-9894:Animals Chunk Bug | Duplicate:inward:MC-9753:Death of livestock | Duplicate:inward:MC-5401:Animals dying through suffocation. | Duplicate:inward:MC-11052:My chickens teleport over fence or stuck in it, when I close game and re-enter it. | Duplicate:inward:MC-11022:Stacked baby animals/villagers glitch through walls upon relogging | Duplicate:inward:MC-10894:Mobs escaping Fenced off enclosures. | Duplicate:inward:MC-10725:The animals leave the farm | Duplicate:inward:MC-9926:Animals walk through fences | Duplicate:inward:MC-9503:Animals can get through fences | Duplicate:inward:MC-6653:Sheep and cows can jump over fences | Duplicate:inward:MC-5230:Cows walking through fences. | Duplicate:inward:MC-5187:Cows have an odd tendency to glitch through cobblestone walls. World originally made in 1.3.2. | Duplicate:inward:MC-3753:Mobs can get out of a fence | Relates:inward:MCPE-1982:Mobs can escape enclosures and sometimes suffocate through walls.

## Description

The bug
Mobs can intersect with blocks, which are right next to the mobs, when the chunk they are in was previously saved and is now loaded. This can cause the mobs to suffocate and die or to escape enclosed areas.
Reasons
This is a list of all (possibly) reasons which can cause this bug. These reasons do not exclude each other.
Bounding box precision loss
Caused by floating point inaccuracies, first described in this comment.
Explanation of bug and fix (Worth reading!)
Mobs moving in unloaded chunks
See 's comment but might not happen, see this comment.
Baby mobs growing up
This is definitely one reason, see this comment and MC-103313.

## Comments (100)

### Comment 1: migrated (2012-11-02T18:05:08.771-0700)

This comment contained multiple image attachments (30), please login to view the attachments.

### Comment 2: migrated (2012-11-15T07:20:46.913-0800)

Seconding this.  Quit the world with 13 cows and MANY chickens in pens; come back to 8 cows and 5 chickens in pens.  The cows were dispersed around the place, I herded 3 back in... but I don't know what happened to the chickens.  In 1.4.2 on a server where their pens bordered on walls I'd sometimes see the animals' drops (and one or more animals missing) when their chunk re-entered memory, and playing 1.4.4 it looks like the issue still isn't solved.

### Comment 3: migrated (2012-11-21T15:20:24.492-0800)

I can confirm that this happens though only with pigs and chickens in my case. It seems to occur whenever the chunks are loaded because a similar phenomenon occurs when traveling around and coming back. Also, looking at the reports that this "duplicates", I have to say that this appears to be a similar problem.
As for the cause, I think it is due to animals butting up against cobblestone walls and wooden fences. When they're reloaded either at the start of the game session or being back in the area, the animals appear on the other side of the fence since animals right against fences appear to be inside them. The game mistakes the animals for being outside when they were inside.

### Comment 4: migrated (2012-11-22T01:50:41.683-0800)

Voted. This is a very annoying bug and it affects a lot of things (all walking mobs for sure). For example an iron golem farm. Iron golems or villagers can be found out of enclosed areas. When all villagers escape, the iron golem farm will be ruined. So you always have to use workarounds.

### Comment 5: migrated (2012-11-22T03:10:46.057-0800)

Voted, I also realized that I can kill chicken that appear to be outside the fence when they are actually inside. The drop appears at the correct location (inside). I also find eggs outside of the fence.

### Comment 6: migrated (2012-11-23T10:07:27.226-0800)

Breeding systems with minecarts also don't work because the animals are not. Cows are near the cart but not in the cart, they will also 'teleport' vertically if the cart was on a second floor of a barn e.g.

### Comment 7: migrated (2012-11-23T13:42:44.778-0800)

This bug is still present in 1.4.5.
It seems that the mobs can escape through all sort of blocks that do not cover the full block space, like fences, doors or glass panes.
I think the problem is, like Nicholas Williams already mentioned, that the mobs are running "into" the fences and when the chunk is unloaded and later reloaded the game can not say for sure from which side of the fence the mob was coming. So in some cases the game guesses wrong and the mob escapes.
Maybe the game just compares the integer values of the mob position with the positon of the fence block, without the fractional digits.

### Comment 8: migrated (2012-11-24T10:34:43.708-0800)

I believe it occurs with full blocks too. I travel a lot with ender pearls which most of the time land on chunks that have just loaded. Today I witnessed one sheep inside blocks of dirt taking damage and it died.

### Comment 9: migrated (2012-11-25T05:24:09.755-0800)

Issue in 4 pics.

### Comment 10: migrated (2012-11-28T01:37:24.873-0800)

Voted for this very annoying bug. I've got a animal farm with cows, sheeps, chickens and pigs. All of these animal types - but mostly sheeps - appear outside the fence - and they should have enough place inside the fence. And to bring them back is not that easy and very annoying. The animals does not only look like outside and "teleport" back, once I'm near them, they ARE outside and walk away from the farm if I don't have an eye on them.
Please keep an eye on this issue. I hope this is solved very soon..

### Comment 11: migrated (2012-11-29T13:23:43.811-0800)

Yeah, this is exactly the issue, animals are REALLY outside. When they just seem to be outside whereas they don't is another issue ( I assume).
Hope also it will be solved ... So keep on voting for this issue in order to make it popular  !

### Comment 12: migrated (2012-12-05T03:33:06.552-0800)

I have this problem, but with solid stone walls. Stupid cows crows up my chicken farm, and kill my chickens.

### Comment 13: migrated (2012-12-09T05:23:02.866-0800)

The same thing has happened to me aswell. I went to the nether and when I came back, some cows were running around free from their enclosures.

### Comment 14: migrated (2012-12-25T16:17:26.080-0800)

Confirmed in 1.4.6.

### Comment 15: migrated (2012-12-30T09:15:16.892-0800)

The animals often still look inside the fence (not the block) when the chunk is loaded, but they can then walk right out.

### Comment 16: bugi74 (2013-01-13T07:18:40.678-0800)

I have also witnessed couple pigs dying inside stone wall after reloading... probably having the same root cause as for the slipping through. (And also have had my share of farm animals going AWOL.)
Note, e.g. boats can be at slightly different position after reloading; if they were right against the beach when leaving the area/world, they can be just a bit more towards the beach and start "floating".
I'd imagine this could be some sort of glitch between using double's for entity positions while the area is loaded, but some different data format when storing the positions. The difference between exact values of stored vs. running system may cause tiny shifts in position, moving the entity "into" next block and causing the symptoms described.
(EDIT: alas, this was not the case, it seems. Entity position are also stored as doubles.)

### Comment 17: migrated (2013-01-24T22:36:26.942-0800)

So far I have only seen my sheep escape from the north side of the enclosure. Building a fugly wall up against the northern fence (not replacing it) seems to have successfully worked around the issue for me. Is that consistent with other people's experiences?

### Comment 18: migrated (2013-01-25T09:30:16.849-0800)

I really only see it to the west.

### Comment 19: migrated (2013-02-05T21:42:46.290-0800)

Animals escape to the north. If you want to have an example, look at the screenshots with sheeps. That is exactly where they escape.

### Comment 20: migrated (2013-02-06T04:15:43.910-0800)

I can imagine that it varies setup-to-setup.

### Comment 21: migrated (2013-02-07T14:01:17.997-0800)

I have a similar problem with a crowded underground chicken bunker - if you step just outside, logout, then log back in, you can hear chickens squawking lots and on reentry there are a number of corpses & feathers along the walls. No particular side is favoured.

### Comment 22: migrated (2013-02-07T16:27:11.020-0800)

Since 1.4.x, I noticed that animals have the ability to wander inside solid blocks. To reproduce, dig a 3x3x3 hole and place a cow inside and push it. The cow will go inside the block and turn black when he reach the middle point. When you release him, he gets out of the block slowly (spring effect). If another animal push hard, it can even make the animal suffocate or die. The reason I say that they escape to the north is because of multiple witnessing of this bug. I built a reserve bin that is divided in cells. All animals are problematic for me. When they are in a fenced farm, they wander randomly, but when they reach the west limit of the farm, they push, push, push to the north and that is where death or escape occurs (I always see the animal in a specific bin, if I close the bin, I see pieces of meat in from of the cell. If it is a fence or solid block, the animal pass right thru. Go figure. If you have a thick wall, the animal suffocate and die. Of course, if you have an over-crowded farm, they may escape everywhere. I think the best way to fix this bug is to completely prevent animals from passing thru block and fences by reducing the penetration distance of animals of exactly one block (except for chickens, since they are smaller) or increase the spring effect to surpass any other pushing effects from animals, players and mobs when the penetration reach a gap of around half a block (still half of a block too much but better than a full block). The facet of the block should be the penetration limit, that's my opinion. Do you guys remember old versions of Minecraft? Everything was perfect in term of physical collisions. Now, it is very berserk.
I am sick and tired of hunting down those escaping animals. I am making engineering devices to trap and bring the animals back in the farm, it is spacious, noisy and ugly looking. The best fix I found is to build a reserve bin all around the farm but I am having difficulties to bring the animals back in without adding catatonic piston and water noises. Please, if someone finds a way to circumvent this annoying bug, could you post your ideas? Thanks.

### Comment 23: migrated (2013-02-09T14:57:27.314-0800)

This is still an issue in Snapshot 13w06a. Has anyone tested if hostile mobs can "penetrate" walls/fences?

### Comment 24: migrated (2013-02-09T15:29:22.116-0800)

To my experience, I never saw a mob (zombie, skelly, creeper, spider) penetrate a wall/fence except for a small glitch MC-2713. The skeleton will visually seem to be passing thru a solid wall and he will wander around but he is still trapped. He can't hit you or vice versa - he is like a ghost. After a few seconds (probably a chunk update) the mob freeze and slide directly where he is supposed to be. It happen when you stack hundred of skellies in a 1x1 hole in single player.

### Comment 25: migrated (2013-02-13T03:51:48.775-0800)

It was working ok for me until Snapshot 13w06a, now the animals keep "escaping".

### Comment 26: migrated (2013-02-15T07:24:46.012-0800)

I can confirm, it's a very annoying bug that I wish would be fixed.

### Comment 27: migrated (2013-02-15T15:40:26.731-0800)

Yesterday I noticed that zombies from (panda's / panda4994) mob spawn switch had escaped from their 2x1 enclosure.

### Comment 28: migrated (2013-02-17T04:04:54.021-0800)

I can confirm, it's still an issue in 13w06a.
It also happens to Cobble Stone Walls.
Please fix this. It's imo one of the most annoying bugs

### Comment 29: migrated (2013-02-18T06:11:20.743-0800)

confirmed for 13w07a

### Comment 30: migrated (2013-02-22T10:38:21.106-0800)

I can confirm this is an issue for solid enclosures as well as fenced enclosures as of 13w07a.
I created a 2-block high glass enclosure at my farm for my chickens, since they kept getting stuck inside fence blocks (MC-4661), and kept killing themselves when I didn't use transparent blocks (MC-9568).
On reloading the chunks chickens were still able to escape, even though they had to displace themselves by a full terrain block from their former positions.

### Comment 31: migrated (2013-02-28T12:20:23.352-0800)

I am also having this issue. So far it has only been with pigs, both adult and baby. The cows have remained in their fences.

### Comment 32: migrated (2013-02-28T15:17:43.492-0800)

I hope this gets fixed!

### Comment 33: migrated (2013-02-28T20:24:48.195-0800)

I actually wasn't having this problem at all until I updated to 13w09a/b (from 13w04), now, nearly every baby animal I get winds up suffocating to death when I log out and back in, unless they wound up being spawned completely outside the enclosure.
The worst expression of this however is that creepers are glitching out of my mob trap, located nearly dead center of my base. I haven't had one blow up and take out hours of work, yet, but it's only matter of time at this point.

### Comment 34: migrated (2013-03-02T11:59:25.450-0800)

I'm having this same problem in 13w09c. (Single player, survival) In my underground pens, the babies, or even sometimes the adults, will glitch into the wall and suffocate. In my above ground fence pens, they escape when leaving and returning.

### Comment 35: migrated (2013-03-02T14:25:48.053-0800)

I'am having the same problem, been testing it in creative, They will escape all fences except gates, and seem to escape the stone fences very easily even if you are standing or idling near by and not changing which chunks are loaded.
I posted a bigger more precise post in another thread (MC-9476)

### Comment 36: migrated (2013-03-02T14:48:27.753-0800)

I have moved back to 13w04 because I had the villager I had been trying to breed grow up and get killed when another villager kid pushed him into wall SIX times. I did not log off and back on. I did not load or unload the chunk. I am standing 10-20 blocks away watching this villager spawn, waiting for him to grow up, then staring helplessly as another brat runs by and pushes him into a wall and he twitches to death.
Obviously this was something intended to counteract some kind of player abuse because less than half an hour after stepping back to the older snapshot, no sudden death syndrome, and i finally have several of the villager type I was trying to get. There has got to be a better way than whatever the team was trying to do that caused this.

### Comment 37: migrated (2013-03-05T15:30:17.399-0800)

Still a problem in 13w10a.

### Comment 38: migrated (2013-03-05T19:39:55.373-0800)

seeing it on 13w09 and 13w10.  Mostly my chickens are escaping.  Oddly somehow a cow escaped, but I ended up with an extra cow.  This is in an underground fortress so it wasn't just a cow wandering in.  I always keep 8 cows and 6 chickens, so works with small numbers of animals as well.

### Comment 39: migrated (2013-03-06T04:58:15.740-0800)

I can confirm this for 13w10b.

### Comment 40: shufboyardee (2013-03-07T07:47:46.083-0800)

Still in 1.5.

### Comment 41: migrated (2013-03-08T11:22:43.647-0800)

This still has not been fixed. I have tested this on the 1.5 Pre-release. This has always been an issue and seriously need to be fixed. Not only visually but they really do on occasion go through not only fences but blocks in general.

### Comment 42: migrated (2013-03-08T12:22:13.171-0800)

They can only escape through transparent blocks: steps, fences, "walls", glass.  They will not escape through solid blocks.  Animals which are standing very close to / inside these types of blocks may suffocate en masse when the world/chunk is loaded.  (MC 1.5)
(Even with an enclosure of all solid blocks, and plenty of room to move, they will sometimes push each other into the wall and suffocate. Also, network latency can cause them to appear to "slide" out of their enclosure, then pop back in when the connection catches up. These are probably separate issues.)

### Comment 43: migrated (2013-03-08T12:39:18.262-0800)

Again Negative. I have posted picture. You can also test. Its cause when entities are half way through a wall and a chunk loads. This causes them to go to the other side. A permanent fix would be to make object solid. At the moment objects are not solid. Entities can pass through blocks. Call it what you want its bad scripting. Included in the first image is a temporary fix.

### Comment 44: migrated (2013-03-08T12:41:19.326-0800)

This shows the current issue and a fix. I belive if mobs where to freeze for a moment till after the chunk is loaded it would fix this issue.

### Comment 45: migrated (2013-03-08T12:42:03.408-0800)

This is an example of before leaving the chunk or exiting the game.

### Comment 46: migrated (2013-03-08T12:44:31.287-0800)

This is after leaving the chunk and when it is reloaded the entited go through the wall. This is because they are already partially through the wall. That is the main issue. Not only visually but in actuality. A solid object script wize would prevent this. Blocks in general are scripted wrong, verified by looking at the code and scripting a mod to fix the issue. Both solutions work.

### Comment 47: migrated (2013-03-08T13:15:52.153-0800)

Nathan Gorzelanczyk: My testing was done in SMP with a reasonable number of mobs in the enclosure (the average use case).  I re-tested in Creative mode, and you are correct: if enough animals are in the enclosure that they are intersecting the walls (as in screenshot-2.jpg), reloading a chunk will indeed cause some of them to appear on the other side – regardless of the enclosure material.  Also, packing in a ridiculous amount of mobs will also cause the visual "sliding" (MC-11086), even in single-player where lag can't be the cause.

### Comment 48: migrated (2013-03-08T13:26:32.477-0800)

I just hope this issue is resolved. I have posted this in numerous locations over the span of minecraft, without any resolution. I appreciate the advanced response and you verifying what I am witnessing. It truly means a lot. As I have seen this issue not only in Single player mode but on numerous servers I run. A lot of accusations of grief when in reality it is simply a glitch. An again I really hope that a solution is made and sooner than latter as I have been waiting for a patch for this since 1.0 when minecraft was young!

### Comment 49: migrated (2013-03-08T14:46:24.860-0800)

I really hope this issue gets fixed because it can be super annoying when it comes to animal farming

### Comment 50: migrated (2013-03-08T14:50:20.567-0800)

i can confirm this, what i did is use water to trap them into place.

### Comment 51: migrated (2013-03-08T18:54:11.307-0800)

David and Nathan, This is not only a chunk loading issue so long as no chunks can load or unload while you are right there working or idling.
I have tested it numerous times and they will escape while idling in the vicinity.  It is not the visual sliding issue that I'm talking about.  I have a creative world where I have been testing it and my single player map is what brought me to test it because while I was sheering sheep they were escaping from closed pens.
I have all 6 fence types (cobble, mossy cobble, nether brick, gates, and wooden) set up with a 3*4 space inside and 6 sheep of a specified color in each.  There is a small flat of land around and a small trap that encircles the spit of land to trap the escaping sheep to verify they are escaping and not dieing.
Sheep have escaped in less than 10 minutes while idling directly next to the pens.  The only pen that does not loose sheep is the fence gate.  I have been testing it on and off in each shapshot for a minimum of 1 hour per snapshot.  Some drastically longer.  For instance 1.5 has been running for over 3 hours today.  Wooden fences lost 2 of 6, gates 0 of 6, nether 3 of 6, mossy 4 of 6 and cobble 2 of 6.

### Comment 52: migrated (2013-03-09T03:48:57.210-0800)

Chickens (didn't test other mobs) seem to like getting stuck in the corners of fences. As more get stuck they are pushed around to adjacent blocks, in this case the surrounding fences over a period of time. See screenshot above.
I've also caught the suffocation in solid blocks on video. I have yet to render it (it was part of a lets play), but if that is needed I'll post the link once its up.

### Comment 53: migrated (2013-03-09T06:23:50.884-0800)

This bug returned when the corner fence hitbox was corrected ([MC-2666]), so maybe it has something to do wiyh that.

### Comment 54: migrated (2013-03-09T09:49:04.160-0800)

You might be correct Stefan with the hitboxes and it may not be limited to fences/walls. Here is a simple test for the suffocation:
1.Create a room say 6x6x2 of cobble/stone blocks (not the walls).
2.Spawn a fair amount of chickens/babies. Say 10.
3.Sit a watch (from above) for a few minutes as they tend to group in corners or along the wall.
4.Notice that some are nearly half way into the blocks (clipping).
5.Close the map.
6.Load the map.
7.X amount of chickens suffocate or rarely escape the block wall.
I tested this with sheep, creepers and zombies. The creepers are less likely to suffocate than the zombies. Creepers are slender compared to zombies as zombies extend their arms. Baby sheep are as likely to die as chickens and chickens/baby animals are smaller and or longer.
So it seems to me this is more of a collision issue with the game knowing where a mob is (or the mob model itself) than specifically the hitboxes of fences/walls. It could even be a client/server issue as both SSP and SMP use a server now. Like the server saying "the mob is here", but the client is saying "ok they are in the wall now".
This bug, whatever the cause, is more noticable to us since fences/walls are smaller (and transparent) than a standard block and the mobs can pass through them without suffocating (most of the time) when the chuck loads. I think there is a decimal number off in the code some where.

### Comment 55: migrated (2013-03-10T04:38:47.965-0700)

I can confirm animals escape through wood fence in 1.5 pre-release.  I have yet to see any animals escape from cobblestone fence.

### Comment 56: migrated (2013-03-11T07:43:22.434-0700)

They can escape through cobble fence as well. The ones that are visually out of the box, become out of the box when the chunk is unloaded and then reloaded. The simplest method to reproduce this issue is to spawn a lot of them in a box, exit the game and reload a few times. This is the not just an issue with lots of spawns, but is simplest to reproduces this way. Please get your friends to vote this up!

### Comment 57: migrated (2013-03-11T08:16:08.639-0700)

Confirming. This has been happening for some time.
Building a good looking (fences only) farm is impossible now, because after some time all the animals are outside the fence or if blocks are used animals just die off.

### Comment 58: migrated (2013-03-11T08:30:45.273-0700)

Similar issues
 Going downward through solid blocks, causing suffocation, death of entries, and entities escaping
 Going forward through solid blocks, causing suffocation, death of entries, and entities escaping
Final Comment.

### Comment 59: migrated (2013-03-11T08:51:22.876-0700)

The only patch that I can figure at the moment.
Making mobs solid.
Therefor making mobs stack like blocks.
The underlying issue is mobs are not solid objects and therefor many can occupancy the same space.
A possible solution would be to make only animals solid and keep mobs the same as they are.
The reason I have not uploaded a patch is this would entirely change game play.

### Comment 60: migrated (2013-03-11T08:58:19.896-0700)

i agree with nathan here, the root of the bugs are probably the same but i have not checked the code. and yes the mods can be very thick headed.

### Comment 61: migrated (2013-03-12T15:24:48.040-0700)

My observation is that when baby animals grow up their hit box changes and they can then phase/glitch out of the fenced in area.

### Comment 62: migrated (2013-03-12T15:25:57.405-0700)

That happened to me a lot of times before, I hope that bug is fixed too before 1.5.1 comes out.

### Comment 63: migrated (2013-03-12T21:47:36.861-0700)

think I found a work around for this.  I dig down one block and then have all the edges fenced. since starting this configuration have notlost any further mobs
just to be more clear the fence in down one block from the surrounding area.

### Comment 64: migrated (2013-03-13T04:44:40.306-0700)

Also observed animals and villagers escaping enclosures made of fence, or suffocating in solid walls when pushed against the wall by water, when growing from baby to adult.  Leaving the area was not necessary, this happens even when the chunk is loaded and stays loaded.  Seen on 1.5pre.

### Comment 65: migrated (2013-03-13T12:18:53.034-0700)

Why this are not fixed in 1.5 ?

### Comment 66: migrated (2013-03-13T12:20:16.458-0700)

Can't understand this as well..

### Comment 67: migrated (2013-03-14T11:32:33.981-0700)

Animals exhibiting this behavior after maturing and going through/suffocating in walls upon loading chunks confirmed in 1.5.

### Comment 68: migrated (2013-03-15T13:59:59.496-0700)

this was NEVER a problem for me until starting to use 1.5?
 what gives?

### Comment 69: migrated (2013-03-15T14:20:22.107-0700)

You might just be very lucky.

### Comment 70: migrated (2013-03-15T14:27:11.839-0700)

Yeah….no chance of that.

### Comment 71: migrated (2013-03-15T14:30:06.908-0700)

It's got a lot worse for me since 1.5:  my crowded pens of chickens are having regular escapes (walls of wooden fence, fence gates, and cobblestone).

### Comment 72: migrated (2013-03-16T07:40:52.611-0700)

dig one down in a square then put water in the corners so the the water flows into the middle, your animals will get stuck in the water. put a fence around it (one block above the water). they will not escape, plus you can put a hopper in the middle so that you can get the eggs in case of chickens.

### Comment 73: migrated (2013-03-17T17:17:26.271-0700)

I have had the same problem in 1.5! Mojang please fix

### Comment 74: migrated (2013-03-18T02:06:47.983-0700)

Mojang has to fix this...

### Comment 75: migrated (2013-03-18T02:13:21.777-0700)

The problem in 1.5 is probably caused by changes in corner fences - details to follow:
I had a few crowded pens with animals of different kinds. In 1.4.3 it was working fine, but after upgrade to 1.5 following things happened:
- Chickens started to leave its pen and overran my wheat and pumpkin farms (so this were real escapes, not glitching through the wall)

- Pigs did the same (altough they did not have farms to ruin in the neighbourhood)

- A wolf entered sheep pen and killed at least one animal.

I noticed that it happened especially when I left the area and came back shortly thereafter. Im not sure if the distance was enough to chunks get unloaded, or just animals dissappeared and were reloaded.
I also found a workaround: When I replaced all corner fences with 2-high 1x1 wooden plank walls animals ceased to leave. Hence my note that the problem is with just corner fences in 1.5.

### Comment 76: migrated (2013-03-18T08:23:16.458-0700)

+1.5 minecraft

### Comment 77: migrated (2013-03-19T11:37:11.274-0700)

Still in the PRE-1.5.1.
Why?

### Comment 78: migrated (2013-03-19T11:45:40.854-0700)

Because the developers haven't found a convenient way to fix this issue yet. I think that should be pretty obvious.

### Comment 79: migrated (2013-03-19T12:54:44.969-0700)

why isnt it assigned yet?

### Comment 80: migrated (2013-03-19T14:32:14.859-0700)

In 1.5, I built an egg farm, and chickens are regularly being washed down the collection hole, despite that being covered by a top-slab.  I don't think it's just chicks, either, I find a lot of adult chickens too.  I suspect that to be another manifestation of this same bug.  Ironically, I built the egg farm to deal with the chickens escaping from my fenced pen....  It's good to hear the problem with that really is worse in 1.5, I wasn't just imagining things.  Also, I don't think it was explicitly mentioned above, but the most common form of this from prior versions was when baby animals pushed their "parents" into the fences/walls.

### Comment 81: migrated (2013-03-19T19:00:04.427-0700)

Yes...

### Comment 82: migrated (2013-03-19T20:06:12.380-0700)

This could be easily fixed, use a full block hitbox on movement of animals/mobs. its an easy quick dirty fix that would make many people happy enough.

### Comment 83: migrated (2013-03-20T08:20:31.621-0700)

You want baby chickens to have a block-sized hitbox?

### Comment 84: migrated (2013-03-20T09:00:29.161-0700)

no.

### Comment 85: migrated (2013-03-20T09:50:11.480-0700)

@C.J. Wijtmans ... I wish it was that easy! Its a little more complicated than that... lol
It has nothing to do with the hit box as this is completely different,
If the hit box spoke correctly to the blocks this would not be an issue,
Think of it this way, sand falls on block and stops right....
Well entities when chunks are loaded stop within a block... Not before a block, when they are inside it.
One issue
However when a chunk is loaded no blocks are there... so they for a moment can go farther inside the block.
When the game reads where they are within the block they are pushed toward that side, meaning they can escape.
Another issue
is because they read a block when they are inside it, a slight lag issue can cause the math to go bad and
they could be again, closer to the other side, so they are pushed to the wrong side.
It's the way that the physics and blocks are interpreted by each other that causes this bug.
It's very similar to the way entities can stack in the same spot, think mob grinder,
instead of like in real life where they would pile up.
Hope this helps in the understanding of the issue at hand.

### Comment 86: migrated (2013-03-20T11:01:41.516-0700)

So what exactly is your suggestion again?

### Comment 87: migrated (2013-03-20T11:11:00.570-0700)

Setting to private to temporarely stop the spam.

### Comment 88: migrated (2013-03-20T12:10:05.673-0700)

Thanks @Nathan.  I appreciated your explanations, even though the mods considered them spam and removed them.  Your comment about slower computers having more lag, and therefore seeing more of this issue—particularly in 1.5 which is a bit slower—made a lot of sense.  My FPS is around 20, so lots of escapes 8-(

### Comment 89: migrated (2013-03-20T13:54:36.610-0700)

Confirmed happening mainly with "baby mobs."  Adults are out mainly because they were babies that have "grown."
Confirmed happens when leaving an area and then returning.  That is to say, leaving the allotted distance within the game that the mobs are no longer active and returning. (essentially the same as disconnecting and reconnecting.)
Confirmed happens when breeding, disconnecting and reconnecting.

### Comment 90: migrated (2013-03-20T17:40:38.427-0700)

tbh i cant see how hard it can be to do this. for example an AI should have a vector called moveTo. which holds the coords where it wants to move to. During filling this moveTo vector it should detect hitboxes on its path, if it detects an obstacle it should put moveTo at the obstacle, which would resolve many bugs regarding AI movement. The CPU intensitvity should be OK and can be throttled down by making less moveTo modifications if CPU intensitivity is detected.

### Comment 91: migrated (2013-03-21T05:50:43.769-0700)

1.5.1 Update does not fix this.  Still mainly baby mobs.

### Comment 92: migrated (2013-03-21T10:39:08.448-0700)

I added some images of villagers which have managed to become trapped inside walls. This is roughly the third or fourth time it has happened; fortunately the villagers themselves are Invulnerable and thus do not suffocate.
Ignore the spawner and custom textures; it's an adventure map, but everything is vanilla. Note the slab floor; this may be related.

### Comment 93: migrated (2013-03-21T14:55:51.305-0700)

I'm not sure what you did, but after watching so many of them die for hours, I know villagers are not invulnerable to suffocation.

### Comment 94: migrated (2013-03-21T20:05:10.791-0700)

I edited the villagers to be Invulnerable for the purposes of the adventure map - they can't be harmed by anything. That's a vanilla feature and has no bearing on them phasing through solid walls.

### Comment 95: migrated (2013-03-21T20:49:06.135-0700)

Confirmed happening with me in 1.5.1. This happens with my separately caged animals. I had cows in one pen, pigs in another, and sheep in a third. I come back later (did not breed any) and some of each of the animals are in each other's pens. There is a natural diffusion at work.

### Comment 96: migrated (2013-03-22T09:06:05.902-0700)

Started the game just now and the baby cow was out of my pin... Thought this would be fix in 1.5.1... Just put up two pictures showing my animals getting stuck on the corners of my fences...

### Comment 97: migrated (2013-03-23T01:11:39.205-0700)

Used to keep over 128+ chickens penned in a small area with none escaping in 1.4.7
In 1.5.1 my surrounding terrain is being overrun by escapees! I've had to discontinue my animal farming so far as having a farm on top a sheer side of a cliff makes for difficult work removing chickens on the wrong side of a fence.

### Comment 98: migrated (2013-03-23T05:49:57.082-0700)

Just thinking... In 1.2 I had no problems with escaping animals. In 1.4.2 they started to escape through fences to the north - placing double fence on this side was sufficient to keep them inside. But now in 1.5.1 they escape literally everywhere! It's really annoying ang getting worse :/ I would be sooo happy to have it fixed...

### Comment 99: migrated (2013-03-23T07:26:44.602-0700)

This always keeps on happening on my world so it is very annoying.

### Comment 100: migrated (2013-03-23T07:31:13.594-0700)

Added a screenshot. I put sheep in the area, reloaded the world 2 times and the baby sheep glitches into the fence and gets out.

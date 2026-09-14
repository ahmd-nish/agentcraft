# MC-14826: Leads in unloaded chunks break, become invisible or connect to an invisible target far away

**Mojira URL:** [https://bugs.mojang.com/browse/MC-14826](https://bugs.mojang.com/browse/MC-14826)

## Report details

- **Mojira categories:** Entities
- **Project:** MC
- **Issue key:** MC-14826
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2013-04-27T18:18:49.259-0700
- **Updated:** 2026-03-20T11:55:03.610-0700
- **Resolution date:** 2023-12-20T18:15:00.173-0800
- **Affects versions:** Snapshot 13w17a; Snapshot 13w19a; Snapshot 13w21b; Snapshot 13w22a; Snapshot 13w23a; Snapshot 13w23b; Snapshot 13w24a; Snapshot 13w24b; Snapshot 13w25a; Snapshot 13w25b; Snapshot 13w25c; Snapshot 13w26a; Minecraft 1.6; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.6.4; Minecraft 13w36b; Minecraft 13w37a; Minecraft 13w37b; Minecraft 1.7.2; Minecraft 1.7.4; Minecraft 14w02c; Minecraft 14w03b; Minecraft 14w04a; Minecraft 14w04b; Minecraft 14w05a; Minecraft 14w07a; Minecraft 1.7.5; Minecraft 14w11b; Minecraft 1.7.9; Minecraft 14w20b; Minecraft 14w21a; Minecraft 14w21b; Minecraft 14w25a; Minecraft 14w25b; Minecraft 1.7.10; Minecraft 14w28b; Minecraft 14w31a; Minecraft 14w32d; Minecraft 14w34d; Minecraft 1.8-pre1; Minecraft 1.8-pre3; Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.2-pre1; Minecraft 1.8.2-pre2; Minecraft 1.8.2-pre3; Minecraft 1.8.2-pre4; Minecraft 1.8.2-pre5; Minecraft 1.8.2-pre6; Minecraft 1.8.2-pre7; Minecraft 1.8.2; Minecraft 1.8.3; Minecraft 1.8.8; Minecraft 1.8.9; Minecraft 16w04a; Minecraft 16w05a; Minecraft 16w05b; Minecraft 16w06a; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.2; Minecraft 1.9.4; Minecraft 16w20a; Minecraft 1.10; Minecraft 1.10.2; Minecraft 16w32a; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w38a; Minecraft 16w39a; Minecraft 16w39b; Minecraft 16w39c; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w42a; Minecraft 16w43a; Minecraft 1.11; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w13b; Minecraft 1.12 Pre-Release 7; Minecraft 1.12; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2; Minecraft 18w03b; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre5; Minecraft 1.13-pre8; Minecraft 1.13; Minecraft 18w30b; Minecraft 18w31a; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w07a; Minecraft 19w13b; Minecraft 1.14.1; 1.14.4; 19w41a; 19w45b
- **Fix versions:** Minecraft 15w31b; 1.15 Pre-release 1
- **Labels:** fence; horse; lead; leash_knot
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** 2013-06-08_07.54.44.png; 2016-01-23_16.57.54.png; 2016-01-23_17.54.13.png; 2016-01-23_17.56.36.png; 2018-10-31_21.47.52.png; invisible-invulnerable-lead.mp4
- **Issue links:** Duplicate:inward:MC-96024:Leads in unloaded chunks break, become invisible or connect to an invisible target far away | Duplicate:inward:MC-14304:Leashes on fenceposts are invisible when re-logging | Duplicate:inward:MC-14765:Horses brake leads | Duplicate:inward:MC-15585:Lead disconnecting | Duplicate:inward:MC-15628:Randomly Disappearing Leads | Duplicate:inward:MC-15901:Leads become Invisible when Reloading world | Duplicate:inward:MC-16088:leads on amimals may appear to despawn | Duplicate:inward:MC-16266:Invisible Lead / Leash after restarting Launcher | Duplicate:inward:MC-16766:Lead vanishes "after a while" or if you are to far away ( can'T tell what cause it exactly ) | Duplicate:inward:MC-16892:leads break off mobs you are holding when you exit minecraft | Duplicate:inward:MC-19588:Leads that are hanging Mobs are glitchy and do not appear on fences in SMP | Duplicate:inward:MC-19925:Leads breaks when loading the world | Duplicate:inward:MC-20032:Leads becoming invisible, and attached fence post must be broken to collect invisible lead. | Duplicate:inward:MC-20189:Horses don't actually exist after closing and reopening minecraft | Duplicate:inward:MC-20484:Leads keep breaking for no reason. | Duplicate:inward:MC-21608:Leads do not function and break when loaded | Duplicate:inward:MC-22060:Horse appears unattatched to leash. | Duplicate:inward:MC-22495:Leads disappear when you go and come back from the dimension | Duplicate:inward:MC-22982:Leaving a survival world and when you come back, the leads tied to your mobs sometimes dissapear. | Duplicate:inward:MC-22986:Invisible lead | Duplicate:inward:MC-23394:Leads Disappearing After A Short Time Offline A Server. | Duplicate:inward:MC-23748:Horses disconnects from leads | Duplicate:inward:MC-23951:horses come off leads | Duplicate:inward:MC-25261:lead bug | Duplicate:inward:MC-25318:leads not visible after exiting the nether | Duplicate:inward:MC-25498:When a chunk containing a lead is unloaded, the lead breaks. | Duplicate:inward:MC-26324:Horses Unleash Themselves | Duplicate:inward:MC-26556:The horses are unleashed when we close and re-open the world or server. | Duplicate:inward:MC-26620:If I hook a animal to a fence pole. Using a lead, than I die the lead will then be in lnvisible but still there.These makes it hard to tell if it is hooked up or not, please fix. | Duplicate:inward:MC-26685:Leads Disappearing When Mobs are Tied Up | Duplicate:inward:MC-26838:Leads break themselves after awhile | Duplicate:inward:MC-27013:Ropes keep breaking when you return to a horse or donkey that's been tied to a post. | Duplicate:inward:MC-27020:Ropes randomly will come off of a horse or donkey and drop when they are tied up for long periods of time or when they get stuck when being led on horseback or on foot. | Duplicate:inward:MC-27302:Leads break after a while | Duplicate:inward:MC-28027:Iron Golem Rope Multiplayer Invisible | Duplicate:inward:MC-28155:Leads on fences disapear when you go to far away | Duplicate:inward:MC-28197:Lead breaks when reloading chunks | Duplicate:inward:MC-29045:Invisible leads | Duplicate:inward:MC-30631:Lashes on the ground instead of on fence | Duplicate:inward:MC-32795:Invisible leads | Duplicate:inward:MC-33533:Leads despawn if chunks despawn | Duplicate:inward:MC-38748:Leads not staying attached to pole | Duplicate:inward:MC-38823:Leashes break on chunk load | Duplicate:inward:MC-41355:dissappearing leads | Duplicate:inward:MC-44756:The lead doesn't work. | Duplicate:inward:MC-44920:Horses detach from lead when chunk un-loads | Duplicate:inward:MC-45623:Leads Breaking | Duplicate:inward:MC-45681:Leads Disconnect on Restart | Duplicate:inward:MC-47173:Invisible leads | Duplicate:inward:MC-47235:Leads going invisible | Duplicate:inward:MC-48520:Leads disappearing/glitchy/bugged | Duplicate:inward:MC-50164:Leads Breaking | Duplicate:inward:MC-51433:Lead Falls To Ground When Chuck Is Unloaded | Duplicate:inward:MC-51505:leads not shown on fence | Duplicate:inward:MC-52560:Lead becomes disconnected from horses after period of time | Duplicate:inward:MC-54233:Leashes of the leashed mobs are gone after several hours | Duplicate:inward:MC-54785:Leashes Failing to break when reloading world | Duplicate:inward:MC-59679:Lead/leash breaks. | Duplicate:inward:MC-59809:Leashes break when the chunk is unloaded | Duplicate:inward:MC-60732:Leads won't keep hold of mobs when chunks are reloaded | Duplicate:inward:MC-61285:lead's in use are invisible on world start. | Duplicate:inward:MC-62404:animal lead bug | Duplicate:inward:MC-64428:When Chunk Unloads Leads release Animals | Duplicate:inward:MC-65397:bug lead | Duplicate:inward:MC-65489:Broken Leads | Duplicate:inward:MC-66419:Leads Break randomly when leaving chunks | Duplicate:inward:MC-68659:Lasso not holding Horse to fence post | Duplicate:inward:MC-69193:leads dissapear | Duplicate:inward:MC-70260:Lead pops off fence | Duplicate:inward:MC-70282:Leads on animals tied to fence posts break after unloading a chunk | Duplicate:inward:MC-72950:Structures below ground level don't render at certain angles | Duplicate:inward:MC-72953:Horse coming off lead? | Duplicate:inward:MC-74656:Lead removes from fence post | Duplicate:inward:MC-76477:The leads of invisible horses connected to fences will dissapear when reloading game. | Duplicate:inward:MC-76636:Leads Despawn if you leave. | Duplicate:inward:MC-79786:Leads on cat/dogs thats attached to fence post breaks away when player goes away | Duplicate:inward:MC-81712:Invisible lead on tied up horse in SMP | Duplicate:inward:MC-85284:When you lead a mob, then restart the world, the mob will break the lead | Duplicate:inward:MC-86535:Horse/lead bug | Duplicate:inward:MC-95312:When Iput a lead on a horse  and tie it to a fence and go out of the chunk and back the lead dissapears but the horse is still attached | Duplicate:inward:MC-96919:In the Minecraft 1.9 snapshots, leads tied around fence posts and animals, sometimes glitch out, causing them to stretched towards, coordinates 0 0 0. | Duplicate:inward:MC-98937:Horse attached to nothing | Duplicate:inward:MC-99944:Go too far, horse lead detach from fence | Duplicate:inward:MC-100464:Leads Disappear in 1.9 | Duplicate:inward:MC-101755:Lead glich when leaveing the chunck | Duplicate:inward:MC-102230:Leads become invisible after entering the nether | Duplicate:inward:MC-102497:When A Chunk De-Renders And Re-renders With Leads, They De-Render | Duplicate:inward:MC-103102:Horse & Donkey Lead Glitch in 1.9.4 | Duplicate:inward:MC-106482:disapeering leads | Duplicate:inward:MC-108892:Visual Bug with Leads | Duplicate:inward:MC-111160:Leads break constanty in multiplayer servers. | Duplicate:inward:MC-113782:Lead glitch | Duplicate:inward:MC-115328:Parrots break leash when loading chunk | Duplicate:inward:MC-115330:Leads don't show up | Duplicate:inward:MC-117179:Leash graphic glitch | Duplicate:inward:MC-117606:Lead bug | Duplicate:inward:MC-119550:Beug lead for animals | Duplicate:inward:MC-134157:Leads disappearing when you go too far | Duplicate:inward:MC-136500:hello i have find a Bug in the game | Duplicate:inward:MC-138613:cats escape when on a lead and fence. | Duplicate:inward:MC-139301:Texture Glitch (Accidentally put 18w45a) | Duplicate:inward:MC-142245:Leads on llamas break/despawn upon reopening game. | Duplicate:inward:MC-142889:Leash gets invisible after chunk / world reload | Duplicate:inward:MC-143199:The lead tied to the fence display is wrong | Duplicate:inward:MC-144483:Lead connected to an entity & fence goes invisible when player goes far away. | Duplicate:inward:MC-145371:Leads disappear when loging out and back in | Duplicate:inward:MC-145599:Lead completely glitched out when strapping a mob to a pole | Duplicate:inward:MC-146999:When you quit the game then rejoin it the leads disappear | Duplicate:inward:MC-150767:Leads acting weird MC 1.14 | Duplicate:inward:MC-150852:Lead graphic does not render correctly | Duplicate:inward:MC-152179:Leads Visually Disappear | Duplicate:inward:MC-152206:traveling trader lead not connected | Duplicate:inward:MC-152254:traveling trader leads go invisible | Duplicate:inward:MC-154619:Lead that was attached llama to fence disappears | Duplicate:inward:MC-155005:Invisible leads | Duplicate:inward:MC-155908:The Invisible Lead | Duplicate:inward:MC-157071:Lead texture disappear | Duplicate:inward:MC-157219:Invisible leads | Duplicate:inward:MC-157476:When loading or reloading into existing world leads dissappear from fence post and mob entity. | Duplicate:inward:MC-158230:Leads tying animals to fence disappear | Duplicate:inward:MC-158282:Leaded foxes leads disappear when they sleep. | Duplicate:inward:MC-158678:When I log back into my world all of the leads on fence posts disappear | Duplicate:inward:MC-160505:Horse rope disappears | Duplicate:inward:MC-160548:Lead becomes invisible! | Duplicate:inward:MC-161335:Multiple bugs involving leads/leashes and dropped item visibility | Duplicate:inward:MC-161694:When mobs attach to fences with leads, the leads disappear | Duplicate:inward:MC-162625:Disappearing leads when going to the nether | Duplicate:inward:MC-162900:Disappearing and breaking lead ropes | Duplicate:inward:MC-163199:Leads connecting mobs and fences disapear | Duplicate:inward:MC-163711:Leads disappearing | Duplicate:inward:MC-163907:leash doesnt appear when the llamas are leashed to the wandering trader when it spawns | Duplicate:inward:MC-164422:leads attached to mobs deleted on save and exit | Duplicate:inward:MC-165050:Leads not showing after logging out and logging back in . | Relates:outward:MC-14004:Leads become invisible after death | Relates:inward:MC-105979:Held lead breaks on save reload | Relates:inward:MC-160306:Leads held by a player disappear completely after leaving and rejoining a world | Relates:inward:MCPE-157182:Leads in unloaded chunks break upon re-entering chunk

## Description

Since I was given the ticket to this issue, I decided to make some changes to make this report a bit more informative. For full information, see . I'm just going to sum it up shortly in this report.
The bug
If you connect any animals to a lead, then place the lead on a fence, then go far away from them (Until they become unloaded), then go back, there is going to be most of the times one of these issues occurring:
- The lead will simply break and drop as an item on the ground.

- The lead will become invisible, sometimes unloading and reloading will fix this issue, sometimes not. If this occurrence happens, the client will think the animal isn't actually leashed, and you can right click it to leash it, however due to this being only client side, you cannot place the lead on a fence.

- The leads will glitch out and connect to an invisible target far away (See pictures). Following the lead for a bit of time will fix this, or, in some cases, make occurrence #1 happen.

I have yet to find a way to, using command blocks, leash the animals back. I'm not exactly sure how the leashing part works technically. It seems like there are two tags for every mob that are related to leads, but all they do is place a lead on the specified location, not connect the animal to it.
Code analysis
Code analysis by  can be found in this comment.

## Comments (100)

### Comment 1: migrated (2013-04-27T18:18:49.259-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: kumasasa (2013-04-28T00:11:38.904-0700)

Cannot reproduce.

### Comment 3: migrated (2013-05-10T11:28:25.759-0700)

Unable to reproduce.

### Comment 4: migrated (2013-05-12T15:02:12.749-0700)

I saw this in one of VintageBeef's recent episodes as well.

### Comment 5: migrated (2013-05-15T04:33:14.805-0700)

It still happens. just look at bdoubleOs latest episode in 13w19a  http://www.youtube.com/watch?v=h-0J61KbLns

### Comment 6: migrated (2013-05-17T22:37:30.974-0700)

This is happening on my server when it is rebooted, running 13w19a.

### Comment 7: kumasasa (2013-05-18T00:33:05.450-0700)

Reopened.

### Comment 8: kumasasa (2013-05-19T19:25:14.051-0700)

Confirmed.

### Comment 9: migrated (2013-06-07T10:48:16.064-0700)

Also affects 13w23a.

### Comment 10: kumasasa (2013-06-07T23:24:57.377-0700)

In the screenshot all horses are attached but only the two saddled ones show the lead

### Comment 11: migrated (2013-06-20T09:45:41.336-0700)

still in 25c!
I hope they fix this before the official release next week

### Comment 12: migrated (2013-06-25T16:14:46.158-0700)

Still in 1.6 pre-release

### Comment 13: migrated (2013-06-27T01:57:06.055-0700)

Confirmed in multi-player. Pre-release 1.6 (downloaded yesterday). When the server restarted ALL leads were broken and laying on the floor.

### Comment 14: Ezekiel (2013-06-29T13:47:14.134-0700)

Is this still a concern in the current Minecraft version? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 15: migrated (2013-07-02T11:05:22.224-0700)

it seems that if a baby horse is on a lead for to long they start taking damage and die?

### Comment 16: migrated (2013-07-02T15:16:07.953-0700)

You might be seeing MC-13632.

### Comment 17: migrated (2013-07-03T19:15:12.719-0700)

this bug is extremely annoying. have the same problem. sometimes the lead is just invisible, sometimes it lays on the ground and the animals walk freely around. sometimes this happens when i go far away and leave the chunk and come back. sometimes it happens when i rejoin the smp. you have to play a little longer, because sometimes it just works as it should. i dont know what exactly trigger this bug, but it happens on my smp way too often. and this is on release 1.6.1

### Comment 18: migrated (2013-07-08T14:25:24.646-0700)

bug is still present in 1.6.2

### Comment 19: migrated (2013-07-08T17:56:06.999-0700)

got the bug in 1.6.2 too. However I didn't recognize it in 1.6.1, but that might be by luck.

### Comment 20: migrated (2013-07-11T14:04:55.040-0700)

I saw this on the SMP server I administrate after restarting the server app in both 1.6.1 and 1.6.2. (Win7 based server)
A gamer on the server has also seen this happen in 1.6.2

### Comment 21: migrated (2013-07-12T04:56:18.916-0700)

It is certainly in 1.6.2. We have a scheduled reboot daily, and are now considering not doing the reboot. 25% of everyone's horses go missing each time.

### Comment 22: migrated (2013-07-19T08:04:12.363-0700)

This is currently happening to me also. The leads in my instance are not invisible but can be found lying on the ground around the posts after traveling away from the chunk in question and then returning to it. Oddly, it does not happen in ALL instances, only sometimes.

### Comment 23: migrated (2013-07-19T16:58:30.638-0700)

This happens to me, except they don't act like they are on a lead. I will tie up my horse, donkey, and mule, leave for a while, return and the leads are gone and the 3 mobs are freely walking around.

### Comment 24: migrated (2013-07-21T17:16:24.633-0700)

I did some testing today. My Horse was standing in chunk A while the fence was in chunk B. Because chunk A was loaded before chunk B, the lead drops itself on the floor.
Current fix -> Try to leave horse and fence in the same chunk.... I hope, that it will work for a while.
Edit: Nope, my fix doesn't work

### Comment 25: macks2008 (2013-07-22T17:48:26.317-0700)

Based on the above comments, there seems to be at least two different (but closely related) bugs that are being confused. One with leashes breaking inexplicably (mob drops a lead item and is able to wander; leash no longer appears to be on the mob; seems to happen whenever the server (minecraft's internal server or the smp server, whatever is doing the non-graphics processing.) is restarted), and one with leashes and their knots disappearing (selection box included) but the mobs still acting like they are leashed, which seems to happen when the client is restarted (again, it can be SSP or SMP).
The bug's are probably the same oversight (occurring when the leash is unloaded on either the server or client), but appearing to be different do to the differences in what the two do.

### Comment 26: migrated (2013-07-25T19:13:12.666-0700)

Okay now they are disappearing when I am right next to them. I tied up my horse, donkey, and mule, did some smelting/crafting/buildings, and despite being less than 35 blocks away from them the entire time, the leads broke. However, this time they dropped as items, although they still broke for an unknown reason.

### Comment 27: migrated (2013-07-27T15:10:20.135-0700)

My god this is so annoying. A few days ago I had 12 leads, now I am down to 3, because they keep breaking and then the items despawn. Can they fix this in 1.7, or maybe like 1.6.3???

### Comment 28: migrated (2013-07-28T09:45:24.383-0700)

I have the same problem when I go to the nether and back. nothing else, just the nether. In survival.

### Comment 29: migrated (2013-08-11T14:38:39.830-0700)

It seems as if the lead is only visually gone; the mob acts as if it is still attached (tested with a tamed horse).
However, if you punch the fence, it destroys the fence instead. The lead drops, but after a small delay.

### Comment 30: migrated (2013-08-24T22:16:12.389-0700)

This is an annoying problem. I can't ride my horse anymore because, even though I removed the fence, it stands still.

### Comment 31: migrated (2013-08-26T12:15:16.455-0700)

The problem is not just a visual one. There may be two bugs here:
1. The leads disappear from the fence post to the mob when I log out and then back in to my server, but
2. The leads actually break and appear on the ground as an item when I leave the area and come back (perhaps on chunk reload?).
This is extremely annoying as it has cost me several mobs. Furthermore, I can't rely on just bringing fence and leads when I go exploring. I have to encase my horse in walls because I just can't rely on the to leads keep my horse there.

### Comment 32: migrated (2013-09-03T11:02:00.219-0700)

I can verify this - just encountered it the other day. Had a horse leashed to a post in a desert village. Did some errands, came back to hear my horse running into a cactus (that was out of reach of his leashed limit). I went to the spot where it was and the lead was nowhere to be seen and my horse completely un-tethered. (Not a case of an invisible lead!)

### Comment 33: migrated (2013-09-10T22:48:43.367-0700)

I've seen issue two myself once. I'm not sure whether I had gone to the nether, a long way away, or just logged in/out.
Could this be a similar issue to mobs escaping from fences MC-2025? Say the horse and fence are in two different chunks and the horse is at the maximum range of the leash when the chunk unloads.
- The chunk with the horse loads.

- The horse starts moving.

- The chunk with the fence loads, leash is connected up to the horse. (The horse moves again and code detects the) leash is too long, leash breaks. Sometimes this will not drop a leash at all (a chance based thing?).

This could also happen with the horse and fence in the same chunk, if the leash is loaded later.

### Comment 34: migrated (2013-09-11T03:44:23.838-0700)

Confirming it is easily able to be reproduced most of the time by going far enough away for the chunk to unload. Note that this for the lead actually breaking, not the invisible lead problem. I am unsure as to why the breaking problem is being closed as duplicates.
Been getting this since 1.6.1. I thought it was a SMP issue but it have been happening extremely often in my current SSP world as well (1.6.2).

### Comment 35: migrated (2013-09-11T06:36:06.915-0700)

Confirmed, still a problem on my server running 1.6.2.  Everyone has to build stables for their horses, or the leads break and they wander away.

### Comment 36: migrated (2013-09-12T10:58:52.231-0700)

@Joey F - They are being closed as duplicates because they are duplicates of this ticket. 1000 "Hey the leads don't work" doesn't help us, only one ticket with appropriate information is necessary.
@ArmEagle - I doubt this is anything related to mobs escaping fences. If anything it would be closer related to an old bug (pre-JIRA) where minecarts would derail if they moved into an unloaded chunk. I SUSPECT that when the leashed mob's chunk is loaded but the fencepost is not, that the leash determines it's not connected to anything instead of waiting for the chunk to load before checking.

### Comment 37: migrated (2013-09-13T04:38:07.698-0700)

Confirmed for 13w37a in SMP. Three horses next to each other all dropped their leashes when restarting the server.

### Comment 38: migrated (2013-09-13T16:13:27.042-0700)

Confirmed in 13w37a. When leaving the chunk, leads either are invisible until the fence is broken or leads are not there at all and the horses are walking around.

### Comment 39: migrated (2013-09-26T07:00:56.769-0700)

I will confirm if this behavior is still present in 13w38c later today.

### Comment 40: migrated (2013-10-25T21:17:42.086-0700)

Still present in 1.7.2.

### Comment 41: migrated (2013-10-30T11:26:22.686-0700)

This is happening to me a lot in 1.7.2. The leads DO NOT become invisible, they BREAK. Most of the time I find the items lying on the ground. However looks like the cause is the same, since it doesn't happen in loaded chunks.
I agree with Talven81 assumption.

### Comment 42: migrated (2013-10-31T08:51:36.000-0700)

Experiencing this issue as well with 1.7.2. Oddly enough, the lead that did break somehow not only broke, it simply vanished. It cannot have despawned, breaking should have caused it to fall into a system of water that I have leading into a hopper > chest and the lead simply did not end up in the chest. ie, somehow it simply vanished. Regardless, given the circumstances, I am inclined as well to suspect it being related to the (slow) loading of the chunk and the fence post(s) this lead was connected to.

### Comment 43: migrated (2013-10-31T23:46:41.915-0700)

This is happening to me and my friend as well.
For me, the lead broke and was completely gone. It did not even spawn as items. For my friend, the leash only became invisible. However, we were both in the same server (I was running the server) and our house were only a few blocks away from each other.
This is becoming annoying since the horse ran to our wheat farms, chicken farms, cow farms and so forth farms and then I have to hunt for the horse and make a new lead again.

### Comment 44: migrated (2013-11-26T09:33:30.690-0800)

It is not just leads that show this kind of behaviour; if I use a water / hopper containment for an egg farm instead of using leads, similar phenomena occur when reloading the chunk. Specifically, chickens will start falling through the hopper top and end up inside of it. Any eggs they lay subsequently are no longer caught by the hopper and simply fall to the side (if there is room).
A reasonably straightforward I can think of would be to simply ensure that the loading of (passive) animals/mobs occurs after everything else has been loaded. To ensure that any leads they are attached to, any trap they are contained in and so forth actually is present whenever they are in fact loaded.

### Comment 45: migrated (2013-11-27T03:16:08.098-0800)

I'm pretty sure that I found the source of the problem (and a solution) of vanishing leads.
It is related to the reading and writing of the NBT tag of the (leashed) entities.
When the entity is read from the NBT tag, the leash is not read directly, but the corresponding tag compound is first stored in a temporary variable (in MCP it's called field_110170_bx). Once the entity has its first update, this temporary variable is then used to attach the entity to another entity or to a leash knot, and the temporary variable is set to null.
The problem occurs when the entity is again written to an NBT tag before it had its first update, because it is not yet attached to something. But the writing method assumes that the lead has already been initialized, and therefore, no further information about the lead is stored. The next time, the entity is read from the tag, we have the information that it is leashed, but the information of where it is attached to has gone.
So, the problem can be solved by additionally checking on writing to the NBT tag, if the temporary tag compound variable for the leash (field_110170_bx) is not null. If this is the case, then the lead was not yet initialized, and it is necessary to store again the tag compound. I tried this and it worked.

### Comment 46: migrated (2013-11-28T02:23:14.736-0800)

I have to add, as already pointed out in earlier comments, there are actually two different bugs - one, where the leashes disappear completely, and one, where they disappear only visually. Both bugs have the same reason, but the solution that I suggested in my previous post only helps with the first one.
The second bug, where the leash is invisible, but the entities behave leashed, happens when the client does not know about the leash because it did not receive a corresponding packet from the server. This is because the server does not send a packet, if the tag for the leash was not yet read (i.e. the information is still only in the temporary variable field_110170_bx in the class EntityLiving).
This problem can be solved by sending a package at the end of the method that reads the leash tag, which is called func_110165_bF in class EntityLiving in MCP, analogously to the package that is sent when a leash is created in func_110162_b.
With this modification and the suggested modification in my previous comment, I could not observe any disappearing leashes.

### Comment 47: migrated (2014-01-25T21:55:14.441-0800)

2 months and no word. Is this going to be fixed? It happens all the time to me and makes leads pretty much useless as they can't be relied upon.

### Comment 48: migrated (2014-01-30T12:47:24.434-0800)

Still broken as of 14w05a.

### Comment 49: migrated (2014-03-09T22:42:19.261-0700)

Word of advice, never leave your animals on a lead, only use it to "lead" your animals to their pens/stables/enclosed areas. Won't be fixed anytime soon(over a year now). Deal with it in the meantime with my advice.

### Comment 50: migrated (2014-03-16T03:03:03.727-0700)

Confirmed for 14w11b

### Comment 51: migrated (2014-05-16T13:53:10.945-0700)

I regularly encounter both issues: invisible lead and breaking lead (breaking much more often).  Both problems occur when the chunk is unloaded and reloaded again.  Still a problem as of 1.7.9.

### Comment 52: migrated (2014-05-25T05:47:46.115-0700)

Confirmed for 14w21b.

### Comment 53: migrated (2014-06-18T02:14:22.388-0700)

I just discovered this in 1.7.9
Leads are nice for traveling, but if they keep breaking on fence posts then 50% of its functionality is wasted. Seems pretty high priority to me.

### Comment 54: migrated (2014-06-19T17:55:55.357-0700)

Confirmed for 14w25b.

### Comment 55: macks2008 (2014-06-30T19:15:43.142-0700)

perhaps the current implementation should just be scrapped and redone. Or maybe they're waiting until the rest of Minecraft works better for this sort of thing? Still, if this is not working, what is the point of having this part of the lead's functionality? It's a bunch of false security for your animal farm. Take it out until it works and leave people to use fenceposts like we did before this item came out.

### Comment 56: migrated (2014-07-07T06:41:17.221-0700)

What is so hard about fixing this? My horse keeps wandering off when I go caving and I have to craft new leads all the time.

### Comment 57: migrated (2014-07-07T12:15:38.262-0700)

Normally before, like I said, the leads would randomly break and be on the ground. I would tie up my animals, walk off, return, and the animals would be roaming freely and the leads would be items on the ground.
Around 10 minutes ago, I went to ride my horse and, just like this problem states, the horse acted like it was on a lead although the lead didn't seem to be present. I found out it was invisible, and in order to get the lead back I had to destroy the fence post it was on. So I've experienced both variants of this lead disappearance glitch, and both are annoying.

### Comment 58: migrated (2014-07-07T15:52:21.583-0700)

Hawk: Until the issue is fixed, you can simply keep your horses in a fenced-in pen.  You can jump a horse over a fencepost when you're riding, but a riderless horse can't jump a fencepost.  This isn't a fix, of course, but at least you can stop losing leads.

### Comment 59: migrated (2014-07-13T11:54:19.101-0700)

confirmed for 14w28b, affects all animals not only horses

### Comment 60: migrated (2014-07-16T10:25:42.158-0700)

I attached a 30s video showing an instance where a lead is invisible upon game start and doesn't even pop off when the fence it is tied to is destroyed.
After exiting and starting the game again, the lead appeared again (in mid-air where the fence once stood) and popped off into item form after a few seconds.

### Comment 61: migrated (2014-08-07T08:09:11.371-0700)

They did remove the rabbit teleporting in MC-64395.

### Comment 62: migrated (2014-08-23T09:54:10.763-0700)

I'm playing 1.8 pre-release 1 and the leads break on my horses when I travel far away. I have to fence them in. All the leads drop to the ground and no animals are missing.
I used to be able to rely on leads keeping animals in place when I was far away but now I need to obtain much more wood to create large enough pen for all the animals.
I like to keep horses and donkeys outside pens for easy access since I use them for traveling.
Not sure if it's related but animals that usually teleport to you, such as wolves and cats, are unable to keep up because the chunks behind you are unloaded and the animals aren't teleported out as a clean-up measure. Any animals following a player that are supposed to teleport to the player should be teleported before the chunk is unloaded. The animals also tend to get stuck in water very easily and won't teleport while in the water if you walk too far away. Animals that are stuck at path finding get the same issue. It probably has something to do with the threaded AI not restoring to teleportation fast enough.
Chunks scheduled for unloading should be checked for animals in follow-mode and make sure that the AI thread teleports them as a cleanup measure. The AI isn't very good at water and dense forests, which is something that I can live with as long as the intended teleportation works the way it should. I often have to run back to make sure that the animal is able to catch up. Walking slow doesn't help, since they easily get stuck in leaves or ponds.

### Comment 63: migrated (2014-08-23T10:23:20.935-0700)

@Tobias, the mobs swimming slow is covered by MC-48616 and seems to predate the threaded AI. There might be other tickets open regarding your teleportation concerns. Remember to vote on issues.

### Comment 64: migrated (2014-08-23T10:25:50.644-0700)

> Not sure if it's related but animals that usually teleport to you, such as wolves and cats,
> are unable to keep up
Teleporting being broken in 1.8-pre1 is .

### Comment 65: Niknokinater (2014-08-23T20:45:17.050-0700)

Same here. I leave for maybe a day (a forest or two away) and I come back and my leaded Horse is walking around and the lead (in item form) is floating on the ground, waiting for pickup.
EDIT: Forgot to mention; I am currently using 1.8 -Pre1.

### Comment 66: migrated (2014-08-24T23:15:06.028-0700)

I'm getting this every 3 minutes. Why? Because I have a command block teleporter to get between my two bases (about half a km apart). Every time I return to my village the lead has broken.

### Comment 67: migrated (2014-08-30T18:19:40.558-0700)

Using 1.8 pre-3  This seems to be related to chunks unloading and reloading. Simply walking away or flying away and returning will cause the lead to disconnect and eventually de-spawn.

### Comment 68: kumasasa (2014-08-30T18:31:58.148-0700)

@
This seems to be related to chunks unloading and reloading.
Therefore the summary of this ticket is
Lead break / disappear on game restart or chunk reload

### Comment 69: migrated (2014-09-07T10:11:12.269-0700)

affects the final 1.8 too

### Comment 70: migrated (2014-09-20T00:15:59.822-0700)

I get this same issue. Tying leads to posts for more then a minute is useless. I suspect the chunk loading causes the mob to temporarily "fall" more than 10 blocks from the lead triggering it to break. If you remember back when there were missing chunk bugs you'd often catch mobs "bouncing" up and down in the missing space. They keep falling and resetting their position until the blocks load. My guess is that's what happens and snaps the lead.

### Comment 71: migrated (2014-09-20T08:47:47.248-0700)

That's a very good theory. I tested in a creative world, by tying a horse to a fence at 0,0 and then teleporting it various distances away from the fence
/tp @e[type=EntityHorse,r=15] 0 ~ 9
/tp @e[type=EntityHorse,r=15] 0 ~ 10
With the prior command, the horse bounces back towards the fence, and then walks towards the fence.
With the latter command, the horse breaks free and walks towards the fence. A lead item appears 10 block away from the fence. The fence still has a knot until I reload the chunk (e.g. exit and rejoin the game).
Perhaps the falling entities don't bounce back towards the fence (like a mob hanging from a fence, which just bounces and accumulates fall damage)

### Comment 72: migrated (2014-12-06T13:07:05.046-0800)

It could be the leads themselves. They're loaded before the blocks are, like all other entities. In the split second before the blocks are loaded, the game thinks that the lead knot isn't attached to a fence, so it breaks the lead.
What could determine which explanation, this or the mobs falling, is correct, would be to see how long it takes the chunk containing the leashed mob to load. If the time is not enough for a mob to fall 10 blocks, then the lead itself is the problem.
If the mob falling is the cause, then this could be fixed by slowing the falling speed of all mobs when the chunks aren't fully loaded yet, like players (if that's possible to do with mobs).
If the lead is the cause, then something similar can be done: have the check for if the lead is attached to a fence wait until the chunk has finished loading (again, if that's possible).

### Comment 73: firebird7 (2015-02-21T08:40:30.540-0800)

Also in 1.8.3.
Fencing-in my horses now.

### Comment 74: migrated (2015-07-30T10:10:51.216-0700)

Still present 1.8.8.

### Comment 75: migrated (2015-07-30T11:58:45.869-0700)

It appears it is fixed in the latest snapshot, 15w31b.
Can't seem to break the lead without hands and arrows, so it must have been fixed.

### Comment 76: Ezekiel (2015-07-30T22:20:19.039-0700)

Resolved as fixed. If someone can reproduce it in the snapshots, please say so

### Comment 77: migrated (2015-08-17T17:44:56.487-0700)

Supposedly this still exists in 15w33c, according to MC-86535.

### Comment 78: migrated (2015-08-18T08:47:06.786-0700)

I said that THIS bug HAS been fixed in the snapshot. The bug I requested a fix for has gone unnoticed by the Mods since 1.6 and is STILL not fixed in the snapshot because they have been getting confused between the bug that I and countless other people have reported and this one so the posts related to mine have been incorrectly marked as duplicates of this bug. Please confirm my report.

### Comment 79: migrated (2015-08-23T03:50:34.720-0700)

kieran heilner is right. this bug here is about a lead which disappears visibly, but is still "there". his bugreport is about a lead which disconnects from horse and fence after reload chunk or restart. if last one can be reproduced in a new snapshot i guess it has another cause than the bug here and therefore is NOT A DUPLICATE of this.

### Comment 80: kumasasa (2015-10-14T23:14:37.315-0700)

@ and : Please confirm what I've understood from you:
In this ticket are two different issues mixed up:
- that leads are still connected to fence post and horse but visually invisible (fixed)

- that leads break, the item form is floating on the ground and the horse is running around (not fixed)

### Comment 81: migrated (2015-10-15T01:45:07.430-0700)

I'm trying to reproduce this bug (either one) and couldn't do it at first (after 10 or so tries with different things). After giving up and going about my game I just respawned near one and the first version of the bug (visual-only) is happening. The lead is visible, but trying to point to some point in the ground and wavering back and forth rapidly in a glitchy way. The horse IS still prevented from leaving the area by the lead. It looks like the lead is changing angles 20 times a second, maybe a max difference in angles of about 15 degrees.

### Comment 82: migrated (2015-10-15T10:54:47.234-0700)

i cannot confirm for the snapshots for version 1.9 (though i didn't played them yet), but the latest 1.8-version. leads clearly aren't connected to the horses and lying on the ground when i "get home". and this is clearly another bug than the one fixed. maybe it has the same cause and therefore could be fixed now, but, as i said, i cannot confirm for the snapshots as i haven't played them. maybe i can in a few days, but maybe someone else is quicker than me
to be clear,  : yes, you understood right. though the fixed/not fixed cannot be said (by me).

### Comment 83: migrated (2015-11-08T13:49:42.548-0800)

Apparently this ticket is actually two bugs. If you're still experiencing any of them, please create a new ticket and leave a comment with the ticket number here.

### Comment 84: migrated (2016-01-23T07:31:58.541-0800)

Still experiencing it.

### Comment 85: migrated (2016-01-30T06:01:16.079-0800)

I seriously hope this will get more attention. It says it's fixed, but it's actually not and no one bothers to do something about it.

### Comment 86: migrated (2016-01-30T08:47:31.879-0800)

Is any part of  that is not covered in  still an issue?

### Comment 87: migrated (2016-02-01T07:11:50.533-0800)

What's not covered in  that is here?

### Comment 88: migrated (2016-02-01T12:38:45.276-0800)

Fine, reopening this ticket, resolving  to this ticket and making you the reporter of this ticket.

### Comment 89: migrated (2016-02-02T08:45:50.896-0800)

Thanks.

### Comment 90: migrated (2016-02-02T22:50:57.908-0800)

This happens to me constantly on my 1.8.9 server. Anything I tie up (horses, cows, sheep) breaks the lead and just gets away before I even notice most of the time. I remember this vaguely being an issue on 1.7, but it's gotten a lot worse now. Back then I generally only had the issue with the lead turning invisible, now they always break. Leads are pretty much useless for me.
This, combined with , means that I cannot store animals or mobs in any fashion. They die or escape within a few hours of gameplay.

### Comment 91: migrated (2016-02-05T01:39:27.254-0800)

Hey, just asking @Grum; Does "Far Future Version - 1.10" mean it's going to be fixed but probably not in the very soon snapshots or does it literally mean it's going to be fixed in 1.10?

### Comment 92: migrated (2016-02-05T12:00:44.215-0800)

If they're doing it the same as with "Far Future version - 1.9?" during the 1.8 snapshots, it just means "not now".

### Comment 93: migrated (2016-02-05T14:16:30.724-0800)

Not now, as in not in the current version of the snapshots, or just not the soon snapshots?

### Comment 94: migrated (2016-02-06T11:00:24.514-0800)

"Most likely not in any snapshot before the next major release."

### Comment 95: migrated (2016-02-06T11:43:45.332-0800)

Well that's just great. I'm gonna have to wait another year until this high priority bug is fixed.

### Comment 96: md_5 (2016-02-27T20:34:09.181-0800)

Not quite the same bug, but it appears that at least on 1.9-pre4 if you travel far away from the entity then come back, the leash will be invisible and require a relog to be seen.

### Comment 97: migrated (2016-03-04T00:41:25.777-0800)

It is the same bug. See occurrence #2.

### Comment 98: migrated (2016-04-02T10:11:27.738-0700)

Still problematic in 1.9 single player, nothing will stay tied up. The lead always breaks.

### Comment 99: migrated (2016-04-02T10:33:35.146-0700)

1.9 is already listed, and outdates

### Comment 100: migrated (2016-05-20T02:59:49.461-0700)

Occurring 3 is still present in 1.9.4 (Leads connect to an invisible target far away after reentering chunks)
Two more accurate facts to occurring 3:
The lead will always visually connect to x=0,z=0 but it has no physical effect.
And the Entity only needs to be unloaded for the client while it can still be loaded through the spawn chunks.

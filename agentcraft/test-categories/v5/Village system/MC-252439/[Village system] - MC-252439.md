# MC-252439: Cured Villager trades are not refreshing

**Mojira URL:** [https://bugs.mojang.com/browse/MC-252439](https://bugs.mojang.com/browse/MC-252439)

## Report details

- **Mojira categories:** Village system
- **Project:** MC
- **Issue key:** MC-252439
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2022-06-03T10:30:17.854-0700
- **Updated:** 2025-05-29T09:09:57.427-0700
- **Resolution date:** 2023-10-16T04:37:16.353-0700
- **Affects versions:** 1.19 Release Candidate 2; 1.19
- **Fix versions:** 22w24a
- **Watchers:** 2
- **Attachments:** 7
- **Attachment filenames:** 2022-06-04_10.00.32.png; 2022-06-30_22.05.09.png; 2022-07-22_20.58.01.png; 2022-07-22_20.58.49.png; 2022-07-22_20.58.49-1.png; MC-252439_JE.png; villagers be weird.zip
- **Issue links:** Relates:inward:MC-252686:Villagers do not reclaim their workstation after being cured | Duplicate:inward:MC-252136:Villager Trades not restocking after renaming with a name tag | Duplicate:inward:MC-252198:villagers will not restock | Duplicate:inward:MC-252530:Villager cannot regain job site after curing. | Duplicate:inward:MC-252559:Villagers refuse to take job sites properly (but lock them) | Duplicate:inward:MC-252808:Villagers won't restock | Duplicate:inward:MC-252857:Villagers won't restock after being cured | Duplicate:inward:MC-252861:Villagers refuse to restock after being cured, and was traded with previously. | Duplicate:inward:MC-252887:villagers are broken in 1.19 | Duplicate:inward:MC-252971:Villager unable to refill after cured from zombie villager | Duplicate:inward:MC-252998:Villagers will not restock trades after curing them | Duplicate:inward:MC-253069:Villagers will not restock | Duplicate:inward:MC-253074:Villagers won't restock after being turned to zombie | Duplicate:inward:MC-253174:Post-zombified Villagers refuse to work at their station | Duplicate:inward:MC-253279:Cured Villagers don't save their workstation | Duplicate:inward:MC-253316:villager restock not working after curing from zombie villager | Duplicate:inward:MC-253515:Cured villagers won't restock | Duplicate:inward:MC-253694:Cured villagers and work stations | Duplicate:inward:MC-253701:This was said to be a resolved bug , but the issue persists , Villagers will not restock their trades after their cured from being a zombie villager. | Duplicate:inward:MC-253737:Villager wont reset trades after curing | Duplicate:inward:MC-253751:Farmer no longer reset trades after being cured | Duplicate:inward:MC-253904:Villagers aren't restocking their trades | Duplicate:inward:MC-253934:Villagers will not restock after curing | Duplicate:inward:MC-254058:Farmer stations in a villager trading hall are not re-stocking their inventories | Duplicate:inward:MC-254064:Cured Villagers Not Restocking | Duplicate:inward:MC-254203:Villagers not resocking or leveling up | Duplicate:inward:MC-254413:Villagers won't restock after being cured | Duplicate:inward:MC-254555:Cured Villagers Unable too Restock (Game Breaking) | Duplicate:inward:MC-254591:Villagers are really buggy | Duplicate:inward:MC-254598:Villagers are out of stock and cannot be recovered | Duplicate:inward:REALMS-10345:Villager not restocking

## Description

Steps to reproduce:
PART I:
First I spawned in a Villager, made hima cozy little ... house, and put a lectern in front of him, which resulted in the following Brain data:

```
{memories: {"minecraft:last_worked_at_poi": {value: 2305L}, "minecraft:job_site": {value: {pos: [I; -232, 128, 110], dimension: "minecraft:overworld"}}}}
```
then I traded with him and waited around a bit for him to do his work routine which resulted in the following:

```
{memories: {"minecraft:last_worked_at_poi": {value: 19582L}, "minecraft:job_site": {value: {pos: [I; -232, 128, 110], dimension: "minecraft:overworld"}}}
```
then a zombie "snuck" in to my little "house" (totally on accident), and I converted the poor fella into a villager again after he was inevitably munched on by the zombie.
and I do understand that that must have messed with his Brain quite a bit, but he lost all information in there resulting in the following

```
{memories: {}}
```
so he lost his job_site and all other valuable information, but I decided to just give him a new lectern (so he had two for the moment), which he cheerfully accepted by emitting green particles, a check on the data of him did reveal that there was nothing in Brain still (no change to above)
I then tried breaking and placing the workstation a couple times, which was acknowledged by green particles every time, but still his Brain showed signs of his previous affliction, and would not register the job_site again.
I also waited for a couple ingame days, sleeping through some nights, not sleeping through others without any luck of him realizing he's standing right infront of a suitable workstation.
I then tried placing other workstations, namely a composter and a grindstone, which was greeted by the same green particles emitted before.
This behaviour is not only frustrating but also it doesn't make much sense to me, that the villager would act this way.
PART II:
I then proceeded to add all other possible workstations, which were ALL acknowledged by our Librarian friend.
Guessing they would all be locked to the Librarian now I added two more villagers, without profession so he wouldn't be too lonely, and as I expected they weren't able to pick any of the 14 job sites available to them now (2 lecterns and 1 of each other type)
only after breaking and replacing the composter for example was one of the professionless villagers able to pick it up as his own.
Possibly useful information:
The workstations in Part 1 were always adjecent to the villager on foot level, so there should be no issue with pathfinding.
The Villager always stood on the same block for the entire process of Part 1.

## Comments (27)

### Comment 1: migrated (2022-06-03T10:30:17.854-0700)

This comment contained multiple image attachments (7), please login to view the attachments.

### Comment 2: migrated (2022-06-03T10:38:47.788-0700)

Could you elaborate on what exactly you mean with update/refreshing trades

### Comment 3: migrated (2022-06-03T11:25:19.621-0700)

maxing out an item purchase (ex wheat) will stay maxed out..can never buy it again

### Comment 4: migrated (2022-06-03T15:13:39.464-0700)

The villager needs to restock at their workstation, that's not an instant thing. Give it time and the villager will restock.

### Comment 5: migrated (2022-06-03T15:37:42.939-0700)

yes im well aware of that..hence the bug report

### Comment 6: MMK21 (2022-06-03T22:21:29.448-0700)

This may be a duplicate of MC-252136

### Comment 7: migrated (2022-06-04T03:23:45.638-0700)

I did test an upgraded world. At this point nametags didn't matter. The re-cured villagers would not restock.

### Comment 8: markderickson (2022-06-04T04:02:04.637-0700)

or , could either of you please attach a screenshot or a video of this issue? Based on 's comment here, I'd expect a similar resolution if this is not present on this report.

### Comment 9: migrated (2022-06-04T07:02:55.112-0700)

this issue was present in pre3* and i commented on someone elses complaint about this

### Comment 10: Moesh (2022-06-08T00:15:19.173-0700)

Can you please attach a world? If it is too big, please use OneDrive or Google Drive to share.

### Comment 11: apple502j (2022-06-08T02:16:07.197-0700)

MC-252559 contains a complete reproduction step. It seems like cured villagers lose all brain data from that report.

### Comment 12: Moesh (2022-06-08T05:50:21.633-0700)

Thanks, updated the description

### Comment 13: migrated (2022-06-08T06:21:52.457-0700)

Removing and re-placing the work benches fixes this for some but not all of my villagers. I'm not sure why.

### Comment 14: migrated (2022-06-08T07:37:22.249-0700)

I just added my world file, which I used to experiment with the villagers when I opened my bug report MC-252559, maybe it can help out understanding the underlying issue (villagers be weird.zip)

### Comment 15: MMK21 (2022-06-10T08:47:47.726-0700)

Relates to MC-252136 and MC-251670
(Possibly clones MC-251670)

### Comment 16: migrated (2022-06-14T08:56:28.673-0700)

Still having this issue, how do i resolve it? causing a bit of a headache for my players...

### Comment 17: MMK21 (2022-06-14T11:42:33.605-0700)

@OcraM The fix version stated at the top of the issue is "Future Version - 1.19+", which means that Mojang has fixed the bug, but the fix has not been included in any released version yet.

### Comment 18: migrated (2022-06-14T12:04:06.708-0700)

Thank you for the info @MMK21

### Comment 19: migrated (2022-06-14T22:13:40.179-0700)

So how do I fix this? Do I have to wait for like 1.19.2??

### Comment 20: MMK21 (2022-06-15T00:20:22.917-0700)

The fix will most likely be shipped with a patch version (1.19.1), but there's no way of knowing if/when that version will release.

### Comment 21: migrated (2022-06-30T19:06:50.165-0700)

This bug seems to still exist in minecraft server version 1.19.1 Pre-release 2.
For context, I started seeing this happen in the 1.19 release.
I updated the server to hopefully fix them,
Does this not fix existing villagers with the bug?
I waited 3 in game days of restocking to confirm that they didn't refresh,
Update: This was fixed upon breaking the workstation. For anyone experiencing this, breaking the workstation should allow the bug fix to work.

### Comment 22: migrated (2022-07-05T15:44:04.276-0700)

still bugged for me villagers will restock before zombifiy but not after being cured

### Comment 23: ampolive (2022-07-05T17:51:19.581-0700)

This was fixed in 22w24a, which was released after 1.19. This fix will be available once you update to 1.19.1.

### Comment 24: migrated (2022-07-12T11:13:27.007-0700)

Hello, is this now open? And getting fixed?
Bc im right now playing on 1.19. server and its still not working.
Cured 4 Villagers a couple of times. Now they don't restock their trades

Edit: ah got it from the comment above: its fixed after 1.19

### Comment 25: migrated (2022-07-22T12:09:07.550-0700)

For anyone looking to fix this in 1.19, here is a suggestion: I placed down a bunch of bells around the affected villagers (used the `/data get entity ...` command to make sure they recognized it). They all recognized the bells, after this I could just break & replace the workstation and they would restock their trades. I think placing down the bells somehow updated their memories and they accepted workstations again? With some villagers it went easier than with others: some instantly restocked, others only did so after I switched dimensions / unloaded & reloaded them or broke & replaced their workstation multiple times, but this fix didn't take me more than 10 minutes or something.

### Comment 26: migrated (2022-08-23T21:18:08.801-0700)

So it will work if i now update my world from 1.19 to 1.19.2?

### Comment 27: migrated (2022-08-24T05:46:19.852-0700)

It got fixed in 22w24a. And after this, 1.19.1 was released where it obviously was included.
So yes. It works again in every version after 22w24a.
BTW u can already get a hint for that answer in earlier Comments:
Comment from ampolive

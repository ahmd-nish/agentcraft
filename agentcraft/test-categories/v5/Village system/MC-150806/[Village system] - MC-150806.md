# MC-150806: Multiple villagers are attached to the same profession block

**Mojira URL:** [https://bugs.mojang.com/browse/MC-150806](https://bugs.mojang.com/browse/MC-150806)

## Report details

- **Mojira categories:** Village system
- **Project:** MC
- **Issue key:** MC-150806
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2019-05-04T12:55:35.772-0700
- **Updated:** 2025-04-30T05:18:53.678-0700
- **Resolution date:** 2023-03-08T12:51:23.267-0800
- **Affects versions:** Minecraft 1.14; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3 Pre-Release 3; 1.14.4; 1.15 Pre-release 6; 1.15; 1.15.1; 1.15.2; 20w06a; 20w13b; 20w15a; 20w16a; 20w17a; 20w18a; 20w19a
- **Fix versions:** 20w22a
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Duplicate:inward:MC-150503:Two villagers have the same job site | Duplicate:inward:MC-151030:Armorer, Weaponsmith, Toolsmith | Duplicate:inward:MC-151209:Several villagers can get a profession from one profession block. | Duplicate:inward:MC-152087:Villagers are claiming already claimed workstations | Duplicate:inward:MC-152253:Multiple villagers claim the same job site block | Duplicate:inward:MC-152399:Villagers are taking professions already owned by another villager | Duplicate:inward:MC-152761:Placing job blocks prioritize transforming default villagers over relinking with existing professions | Duplicate:inward:MC-152950:Multiple villagers claim the same station | Duplicate:inward:MC-153114:Unemployed Villagers take over claimed job blocks | Duplicate:inward:MC-153302:Job Stations forget which villager owns it. | Duplicate:inward:MC-153336:Villagers with established professions stealing others' professions after removing their workplace. | Duplicate:inward:MC-153403:Villagers are losing their workstation/ stealing others | Duplicate:inward:MC-153673:Multiple villagers claiming the same work station. | Duplicate:inward:MC-153778:Villager overtaking other villagers' workstations | Duplicate:inward:MC-153877:Villagers, that had a profession before, claim a different Job Site that has been claimed already | Duplicate:inward:MC-154424:Villagers Forget Job Sites Randomly | Duplicate:inward:MC-154490:Villagers linking to same jobsite block | Duplicate:inward:MC-154806:Jobless Villagers "steal" workstations from apprentice+ villagers | Duplicate:inward:MC-155839:villagers occupy their jobs | Duplicate:inward:MC-156104:Multiple Villagers Claim The Same Workstations | Duplicate:inward:MC-156167:Villagers randomly leaves/steal workstations, unemploying the original villagers. | Duplicate:inward:MC-157459:Villager claim eachother's workstations | Duplicate:inward:MC-157503:Villagers will randomly lose/shuffle around workstations | Duplicate:inward:MC-157556:Villagers are sharing workstations, when the workstation is removed, the villagers remain as it was. I am on a server and re-logging does not help this issue. As shown in the picture, there is only 2 work stations. | Duplicate:inward:MC-157576:Villagers taking over workstations of other villagers | Duplicate:inward:MC-157998:Villagers assigned to workstations lose their workstations to unassigned villagers within vicinity | Duplicate:inward:MC-158572:Two Villagers Will Take the Same Jobsite | Duplicate:inward:MC-158639:one composter two farmers | Duplicate:inward:MC-159675:Villagers with XP in a profession do not get prioritized when a new workstation of their craft is placed | Duplicate:inward:MC-159704:Villagers become librarians even though the lectern is already being used by another librarian | Duplicate:inward:MC-160509:Villager gets profession for already occupied profession block | Duplicate:inward:MC-161070:New villagers stealing job blocks | Duplicate:inward:MC-161462:Villagers Take the profesion of a block used already by another villager and sometimes get stuck in their profesions. | Duplicate:inward:MC-162168:A villager not traded with not changing jobs even after connected job site is destroyed, multiple villagers connected to one job site | Duplicate:inward:MC-162747:Villager are not detecting used job site | Duplicate:inward:MC-162830:Point of interest bug | Duplicate:inward:MC-163621:Unemployed villagers randomly decide to steal an employed villager's workstation. | Duplicate:inward:MC-164780:Villager workstation AI | Duplicate:inward:MC-164842:Villagers don`t follow daily schedule | Duplicate:inward:MC-168155:Villagers taking an already taken profession block | Duplicate:inward:MC-168968:no-one else have found it before | Duplicate:inward:MC-169638:unemployed villagers can take jobs from job blocks that have been already claimed by another villager | Duplicate:inward:MC-171900:Many villager have same job but there is only one block of work | Duplicate:inward:MC-172535:Villager Leaves workbench and wont return | Duplicate:inward:MC-176300:Villagers becoming linked to the same job block | Duplicate:inward:MC-176663:Villager with profession loses jobsite block to unemployed villager | Duplicate:inward:MC-178526:Villager work stations not working right | Duplicate:inward:MC-178839:Multiple Villagers binding to the same station or switching stations after traded and bound to a station | Duplicate:inward:MC-179246:Villagers work on taken workstations | Duplicate:inward:MC-179597:Two villagers use the same worktable | Duplicate:inward:MC-179756:villagers linking to claimed work stations | Duplicate:inward:MC-182198:Villagers Switching Profession Blocks | Duplicate:inward:MC-182407:Villager problems | Duplicate:inward:MC-183341:Villagers claiming already-claimed work stations | Duplicate:inward:MC-183802:Villagers acting weird with their workstations | Duplicate:inward:MC-187083:Villagers professions not working correctly | Duplicate:inward:MC-190686:Villager claims workstation that's already claimed (old bug thats back in 1.15.2) | Relates:outward:MC-164233:"Skilled" villagers without job site do not get precedence over unemployed villagers | Cloners:inward:MC-248783:Multiple villagers on one job block

## Description

The bug
I am trying to build a trading hall on my world and I notice that jobless villagers entering the area are automatically taking certain jobs when there aren't associated work blocks for them to attach to. When I run the /data get entity  [ID] Brain command, the newly entering villagers are attaching to blocks that are already claimed by other villagers. Breaking that block and rechecking doesn't change the associated block.
How to reproduce
From  in this comment
- Have an enclosure with a couple of villagers in

- Place one jobsite block of any type

- Trade with the villager who aquired the job to lock it in outside working house (2000-9000 tick) quickly break the jobsite block and replace it with the same type and observe a new villager have aquired a profession and both the locked in and new villager will show they have claimed the same jobsite.

→  When the time of the day reaches 2000, both will begin to work at the same jobsite. Logging out and back in to the game wont change this.

## Comments (42)

### Comment 1: migrated (2019-06-15T14:36:09.852-0700)

Can confirm this also happens on Minecraft 1.14.3 Pre-Release 3 if anyone is interested.

### Comment 2: migrated (2019-07-06T05:37:15.091-0700)

I'm very interested, Mr. Villa-Lobos. Thank you. The pathfinding updates seem to have made this happen less often, but it is still occuring.

### Comment 3: XqVDLZZt (2019-07-07T10:00:11.745-0700)

I have found that it is easy to cause two villagers to claim the same job site block by rapidly breaking and placing it (can take several tries — noticed when I was trying to get librarians with specific enchanted books). However, when this is the case, they will both lose their jobs if the block is broken again.
Sometimes it can even cause more than two villagers to claim the same block — I managed to get three.

### Comment 4: migrated (2019-07-25T20:42:45.180-0700)

I think that there are two related problems that cause (at least some of) these issues:
1) Villagers randomly disconnect from their workstations
2) Villagers that have had their trades locked (by having at least one completed trade) do not automatically try to connect with a workstation (or, possibly, do not try to connect to a workstation until after unemployed villagers have done so, but when locked villagers have lost their workstations I've never seen one automatically reconnect to one, regardless of how many or what types of other villagers and/or workstations are or are not nearby).
These two problems together mean that villagers will lose their workstations and those workstations will be picked up by a different villager, leaving the original villager unassigned and unable to renew its trades.

### Comment 5: dscheJ-Ouh (2019-07-28T18:57:44.453-0700)

sigh
Still happens in 1.14.4…

### Comment 6: migrated (2019-07-28T21:04:47.148-0700)

I would like to mention this is still a problem in 1.14.4. It seems that unemployed villagers have first dibs on workstations which messes things up when you're moving a workstation with unemployed villagers present.

### Comment 7: migrated (2019-08-08T10:39:40.322-0700)

This would explain why I cant get any villagers to trade after the first few ones. I guess I need to have workstations up before they grow up so they can immediately claim a workstation not claimed by any other villager. I noticed that only the first few villagers will trade with me, all others just shake head all the time although they have workstations already present.

### Comment 8: migrated (2019-08-20T12:49:11.015-0700)

This still happens in 1.14.4; I have a small village with 3 composters, a brewing stand, and a stone-cutter, but after some mining, I came back to find that I had an extra farmer and an extra mason. The original farmer and mason, who where the only villagers I had leveled up, had been disconnected from their blocks (the jobless villages "stole" them) so the could not refresh their trades. neither of the other farmers, nor the priest, none of whom had been leveled at all, had their workstations stolen. it would seem that only villages who have been leveled up are susceptible to having their workstation stolen.

### Comment 9: migrated (2019-08-24T09:13:34.443-0700)

A possible fix could be, that each block that is workable by a villager has a "claimed" attribute, perhaps linking to the villager UUID or a boolean. If the block is claimed, no other villager seeking for a job is assigned. The claimed attribute is removed if the assigned villager (coordinates of workplace are also saved in a tag) is killed (remove tag from workplace coordinates block) or the pathfinding fails. For possible concurrency problems a semaphor might be used instead.
Furthermore, this could also be enhanced by the system I proposed in MC-159675, but this might cause concurrency problems aswell.

### Comment 10: migrated (2019-08-27T13:05:06.349-0700)

Here is a very simple way to reproduce the bug (1.14.4) : Make a container for 2 or more villagers (you can make it out of glass so you can see the profession of the villagers), then put down a work station which is 10 or more blocks away from the containers, and break and replace the work station quickly several times until you see that all of the villagers become whatever the profession is. At the end you can leave the workstation placed down, then release the villagers, and they will all go and work at that work station. This is related to the possible bug that novice villagers won't immediately lose their profession if a work station placed more than 8 or 9 blocks away is broken.

### Comment 11: migrated (2019-10-08T10:57:11.221-0700)

This is still happening in the latest Snapshot. I've been playing q new world and managing villagers its been hard.

### Comment 12: migrated (2019-12-07T06:15:11.432-0800)

still happening in 1.15 pre6

### Comment 13: migrated (2020-01-04T18:12:58.998-0800)

At first, I had this problem in a creative world, but not in my survival world. Then recently the problem started happening in the survival world too. I don't know why it has only recently started happening in the survival world but it's been causing a lot of problems in my trading hall.

### Comment 14: Justerfrog (2020-02-08T11:14:18.763-0800)

I discovered this glitch on my own in 1.15.2, and i have some new info about it
this seems to only happen when the villagers are meeting.
it seems to be fixed in 20W06A.

### Comment 15: migrated (2020-02-10T04:56:22.859-0800)

The problem mainly comes in how the villagers prioritise what blocks to sync up with. It seems to be based on the order in which the villagers, and the blocks, are added to the village. Every so often the village jumbled this data up, causing them all to reset.

The whole villager sync portion just needs to be changed, making villagers check for beds and profession blocks based on how close they are to them, once synced he stays synced as long as he can still reach the bed and block... if he can't, he then scans again for the closest unclaimed bed and block he can get to, and will sync with those.

Also, profession blocks need to be able to be turned off, so they can be used as decoration without messing up villagers.

### Comment 16: Justerfrog (2020-02-10T13:09:33.378-0800)

my experience makes it look more like the breaking the site block makes the villagers forget about the job site but not change profession, but when you place it back it remembers it but a new one claims it.

### Comment 17: migrated (2020-02-11T23:40:31.014-0800)

Affects 20w06a.

### Comment 18: migrated (2020-02-12T04:10:38.405-0800)

Possibly related to MC-166980 beecause bees seem to beehave similar with beehives: bees can stay attached to a beehive they can't use anymore (potentially by breaking and replacing or just over time) and then get stuck wandering to the north-west and refuse to get into another beehive until the original one is broken. See this comment: https://bugs.mojang.com/browse/MC-166980?focusedCommentId=632081&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-632081
Villagers who lost their workstation also tend to wander to the edge of the village (many also accumulate in the north-west corner, but not all and it might be a coincidence), and combined with  that makes them glitch through walls surrounding the village and then can't get back in, this makes it quite difficult to work with villagers (and bees).

### Comment 19: migrated (2020-02-12T18:14:04.317-0800)

I just had this happen. I have 2 villagers in stalls in the same chunk with their workstations (composter) in front of them. I have a villager opposite of them that had a lectern as a workstation. However, the villager was stationed just outside of the chunk, but the worksite location was 1 block in front of the villager, on the inside border of the chunk (so, 3 workstations in 1 chunk). When I broke the lectern and went to place it again, I saw the villager became a farmer (composter was 11 blocks away). Note - the other 2 villagers were already farmers and traded with. The former librarian has not been traded with. As a result, I seem to have to wait up to 3 Minecraft days before the villager loses its' profession.

Also, I've noticed the villagers wandering to the edge of the village problem. The first village I tried to "secure" by removing beds and work-stations, the villagers moved to the opposite side of the village from where I had put all of the beds and workstations in.
To comment on an above quote - I think it may have something to do with locked trading villagers not having priority, so the game loops through a collection of loaded villagers that is sorted by un-traded villagers, then villagers that are trade-locked. A bit more testing, and it seems to happen when the intended villager (the librarian in this case) looks at their lectern for a long time (not the nodding). A short time after that, breaking/placing the lectern back will cause the villager to select the wrong workstation.

A few work-arounds -
1 - Seal off the offending villager and place a work-station in front of another unaffected villager. It seems to reset the occupation of the job thief. (Work fraud and wage theft seems rampant in these villages... I mean, it's been 10 years before their economy changed. )
2 - Completely wall in the villager you're trying to assign a job to. That way, they shouldn't path-find to a new workstation.

### Comment 20: migrated (2020-02-12T19:00:03.156-0800)

Have had this issue since at least 1.14.2, still experiencing the bug as of SS20w06a

### Comment 21: LaserSlime (2020-03-18T11:45:31.044-0700)

Please fix it´s so annoying

### Comment 22: migrated (2020-03-28T13:02:10.318-0700)

Still present in 20w13b.

### Comment 23: migrated (2020-03-31T01:50:10.569-0700)

Don't know if it's the same bug or a different one, but the same happens with beds. My villagers keep having one too many babies than there are beds - leading me to the conclusion that one of the beds must have been claimed by two villagers. One of them is unable to sleep.

### Comment 24: migrated (2020-03-31T04:30:57.073-0700)

I have the same problem on my server. Two villagers can take one work station, when first villager inside trapdoors, and second is sitting in the boat.

### Comment 25: migrated (2020-04-11T19:52:41.371-0700)

It's still present in 20w15a.

### Comment 26: migrated (2020-04-11T23:56:28.200-0700)

1.15.2  Same thing still happening in naturally occurring villages. As villagers multiply, more than one villager will take on a profession, even though there is only one related workstation. The result is that some villagers do not replenish their trades. Example: Newly discovered village had only two workstations, both composters. I crafted and placed one loom, and one villager took on the profession of shepherd. After trading with this villager for several days, a second shepherd suddenly appeared and started hanging out around the loom. The original shepherd, who used to hang out near the loom, was found on the other side of the village. Breaking the loom and replacing it in the same place does not cause the loom to be associated with the first shepherd again.  This problem is extremely annoying in villages with multiple farms and multiple farmers. You end up with many farmers with locked trades because they don't replenish their trades.

### Comment 27: Johnibur (2020-04-12T06:46:40.797-0700)

Are you testing with new villagers on each version?

### Comment 28: migrated (2020-04-15T11:28:42.645-0700)

still present in 20w16a
I think it might be related to MC-164233 where a skilled villager don't get precedence over a jobless villager in picking a new jobsite.
I have found that this bug with multiple villagers attached to the same jobsite is more prevalent when the villagers have been skilled than if their trades have not been locked in.
Edit: A way to reproduce this:
1) Have an enclosure with a couple of villagers in
2) place one jobsite block of any type
3) trade with the villager who aquired the job to lock it in
4) outside working house (2000-9000 tick) quickly break the jobsite block and replace it with the same type and observe a new villager have aquired a profession and both the locked in and new villager will show they have claimed the same jobsite. When the time of the day reached 2000, both will begin to work at the same jobsite. Logging out and back in to the game wont change this.

### Comment 29: migrated (2020-04-24T05:56:39.586-0700)

still present in 20w17a

### Comment 30: migrated (2020-04-28T15:18:37.332-0700)

It seems logical to assume that this could be resolved by something where villagers of higher tiers can kick lower tier villagers off of their jobsites.

### Comment 31: migrated (2020-04-28T21:47:58.907-0700)

Can confirm, present in 20w17a.

### Comment 32: migrated (2020-04-29T14:19:59.538-0700)

still present in 20w18a

### Comment 33: migrated (2020-04-29T14:21:29.129-0700)

Also I would imagine this relates to MC-164233

### Comment 34: migrated (2020-04-30T06:41:51.708-0700)

Since this is now "In Progress" it might be a good idea to look at this bug also, which I think might be related also. Cured villagers can work at wrong jobsite. MC-177505

### Comment 35: migrated (2020-05-05T13:37:04.378-0700)

Additionally villagers are able to pathfind to workstations that are inaccessible to them; on the other side of a wall for example. I believe this adds to this bug. Villagers should only be able to link to a workstation they can properly pathfind to.

### Comment 36: migrated (2020-05-07T07:37:22.754-0700)

still present in 20w19a

### Comment 37: migrated (2020-05-20T07:16:35.677-0700)

I have the same issue although in a regular village. I put down two smithing tables and traded with both toolsmiths that appeared until they were both master level. Then a new villager appeared as an apprentice toolsmith. This new apprentice toolsmith will on occasion keep the master level toolsmiths from renewing their trades at the workstation which is why this is an issue for me.

### Comment 38: migrated (2020-05-20T08:19:44.409-0700)

Still present in 20w20b

### Comment 39: migrated (2020-06-20T18:54:51.812-0700)

Still occurs in 1.16 RC1
I have exactly 1 brewing stand and two clerics standing next to it.

### Comment 40: migrated (2020-12-25T15:46:03.400-0800)

I agree with Scott Caton's comment.
I am also still seeing this in my village in 1.16.4. I place a job site block, a villager claims it, and I will level that villager up all the way to Master. Then, I will come back later and find a Novice villager working at that job site block, and the Master will be wandering around. I guide the Master back to their original job site block (by breaking and replacing it), and yet I will still see a Novice working at the job site block when I come back later.

### Comment 41: migrated (2021-03-31T12:33:19.708-0700)

Still present 1.16.5

### Comment 42: migrated (2023-03-08T12:51:23.267-0800)

Still present 1.19.3

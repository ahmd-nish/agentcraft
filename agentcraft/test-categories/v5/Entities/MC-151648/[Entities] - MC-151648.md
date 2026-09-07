# MC-151648: Non-player entities cannot travel through unlinked nether portals

**Mojira URL:** [https://bugs.mojang.com/browse/MC-151648](https://bugs.mojang.com/browse/MC-151648)

## Report details

- **Mojira categories:** Entities
- **Project:** MC
- **Issue key:** MC-151648
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2019-05-12T11:16:59.980-0700
- **Updated:** 2025-04-26T07:59:55.492-0700
- **Resolution date:** 2024-12-19T17:26:37.271-0800
- **Affects versions:** Minecraft 1.14; Minecraft 1.14.1 Pre-Release 2; Minecraft 1.14.1; 1.14.4; 1.15; 1.15.1; 1.15.2; 20w07a; 20w08a; 20w10a; 20w13b; 20w16a; 20w17a; 20w20a; 1.16 Pre-release 7; 1.16 Release Candidate 1; 1.16; 1.16.3 Release Candidate 1; 1.16.3; 21w06a; 1.17.1; 1.18; 1.20.1; 1.20.3 Pre-Release 2
- **Fix versions:** 24w21a
- **Area:** Platform
- **Labels:** nether_portal
- **Watchers:** 1
- **Attachments:** 5
- **Attachment filenames:** 2019-05-12_20.16.11.png; 2019-05-12_20.16.19.png; 2019-05-12_20.19.57.png; Minecraft pigmen bug 1.14.1.mp4; Minecraft pigmen bug 1.14.1 Pre Release 2.mp4
- **Issue links:** Relates:outward:MC-278942:Mobs are able to create new portals from those that are unlinked in both the nether and the overworld | Duplicate:inward:MC-264207:Mobs not passing through nether portals on nether side back into overworld | Duplicate:inward:MC-264037:Some mobs can't teleport in portal like ghast or strider | Duplicate:inward:MC-150011:Villager not going through Nether Portal | Duplicate:inward:MC-199884:Entities Deciding Not to Use Portals | Duplicate:inward:MC-102754:Mobs don't use nether portals when there is no portal in the nether | Duplicate:inward:MC-183856:Ghast portal issues | Duplicate:inward:MC-168192:Panda's can't go through nether portals | Duplicate:inward:MC-174332:My dog can't leave the Nether | Duplicate:inward:MC-172868:Tamed Cats wont go through Nether portal. | Duplicate:inward:MC-171760:Entities can't go through portals on the nether roof | Duplicate:inward:MC-169785:villagers sometimes can't go through nether portals | Duplicate:inward:MC-149847:Certain villagers refuse to go to the nether | Duplicate:inward:MC-158170:Horse Will Not Go Through the Nether Portal | Duplicate:inward:MC-159106:Horse Cannot Go Through Nether Portal | Duplicate:inward:MC-159774:Villagers Not Going Through Nether Portals | Duplicate:inward:MC-158146:Dismounting a horse inside a portal sometimes does not cause it to go through | Duplicate:inward:MC-158998:Villagers won't go through portal | Duplicate:inward:MC-159058:Entities not going through Nether portal after going in a boat that was destoyed inside the portal in Minecraft Server 1.14.4 version | Duplicate:inward:MC-161369:I can't get ghasts through nether portals | Duplicate:inward:MC-157866:Foxes and cats not going through nether portals? | Duplicate:inward:MC-152451:Some horses unable to use Nether portals even if cooldown timer is at 0 | Duplicate:inward:REALMS-1847:Entities cannot exit the Nether

## Description

The bug
Non player entities cannot travel through portals if it's not generated on both sides.
How to reproduce (from )
- Create a new world and create an unlit portal frame.
- If in an existing world, create an unlit portal somewhere far from any existing portals in both the nether and the overworld.

- Put a boat in the portal frame

- Check the boat's PortalCooldown tag by typing

/data get entity @e[type=minecraft:boat,limit=1] PortalCooldown
, note the tag is at 0
- Light the portal
 →  Observe that the boat is not teleported but PortalCooldown is now at 300.

Original Description
Basically my bug is that sometimes pig-men come through the nether portal, to the overworld. Issue is that I cannot seem to push them back into the nether, by physically pushing them into the portal whilst it's lit. Not sure if it's changed that the pig-men need to stay there longer (in the portal) to transport. I had one there for around 8 seconds, but didn't get transported.
Note: I haven't gone to the nether, so idk if it's registered a new world for the nether, or if I'll have to go there myself to generate it to then go back and push him back in. I'll check that and update on if that resolved the issue, and then if this even is a bug.
Update: After going to the nether, and back to try pushing him back in again, the issue is still the same. The pig-man won't be transported back through the portal.
Restarting game didn't resolve it either. As can be seen on the video attatchment.
Issue still remains in the newest version of Minecraft (1.14.1)
However I've found out if the pigman goes into the portal on his own, he will be teleported, but if I try pushing him in he will not teleport.

## Comments (26)

### Comment 1: migrated (2019-05-12T11:16:59.980-0700)

This comment contained multiple image attachments (5), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2019-05-12T11:20:38.521-0700)

Did the zombie pigman leave the portal before you tried to push it back in?

### Comment 3: migrated (2019-05-12T11:22:31.765-0700)

Yes, I waited till he left to make sure. And then tried pushing him back in, but it didn't work.

### Comment 4: [Mod] violine1101 (2019-10-01T09:21:59.694-0700)

Entities need to wait 300 ticks until they can teleport through a portal again. If they enter a portal before that cooldown has counted down to 0, the counter is reset to 300 every tick they're in the portal. I'm not sure whether that's what this issue is about.

### Comment 5: migrated (2019-12-06T07:03:14.054-0800)

I'm having this same issue. trying to move a couple dozen villagers and 2 out of three will not go through on the Nether side, been working on this for two days. Every once in a whole I'll try and to push them through again and they just stand in the portal.
Also, I had one Villager go through and then come back and then he wouldn't go through again, so I had to set him aside as well.

### Comment 6: FaRo1 (2019-12-06T07:37:05.230-0800)

In which version? Also, there's a cooldown after going through a portal, you need to wait for a few seconds before that entity can go through a portal again.

### Comment 7: migrated (2020-01-01T17:58:54.478-0800)

I'm having the same issue with some villagers in 1.15.1 at the moment. I think it's related to the `Dimension` nbt tag. It seems to usually be -1 for entities in the nether, but these villagers which were bred in the nether have Dimension=0, which would seem to imply that they think they're in the overworld. New villagers fresh from a spawn egg have Dimension=-1, and are able to go through the same portal as normal.

### Comment 8: Jeuv (2020-03-05T02:00:14.552-0800)

After some testing in 1.15.2 and 20w10a, I found out that if an non-player entity tries to travel through a portal when there isn't one on the other side, its Dimension tag gets changed, but it doesn't actually get teleported. This then means that that entity can never travel through a portal again, as its Dimension tag does not match the current dimension. You can reproduce this fairly easily.
Reproduction steps:
1. Create an unlit portal somewhere where far from any existing portals, both in the nether and the overworld.
2. Put a boat in the portal frame
3. Check the boat's Dimension tag by typing

```/data get entity @e[type=minecraft:boat,limit=1]```
4. Light the portal
5. Observe that the boat does not get teleported
6. Check the boat's Dimension tag again
-> Observe that the boat's Dimension tag changed, without it changing dimensions.

### Comment 9: ryu3025 (2020-03-29T15:04:28.420-0700)

I did what Jeuv said, only with a cow. The problem still exists in 20w13b.

### Comment 10: migrated (2020-03-30T13:04:49.286-0700)

im getting the same problem with a villager who wandered into a portal. my version in 1.15.2, and i checked his dimension tags and it says overworld yet he is still in the nether :/ chunks are loaded on both sides, the overworld side being the spawn chunks. i have let him out of the portal for a few seconds, and held him in the portal, but nothing.

hope this gets resolved

### Comment 11: ryu3025 (2020-04-22T14:57:09.364-0700)

The bug is in 20w17a.

### Comment 12: ryu3025 (2020-06-10T14:46:22.024-0700)

I think the bug is fixed in 1.16 Pre-Release 3. Is anyone else not having a problem with this bug?
EDIT: I wasn't sure before, but I tested in survival and everything thing is still working. I think this bug is resolved.

### Comment 13: [Mod] violine1101 (2020-06-16T15:02:53.166-0700)

I'm still able to reproduce in 1.16-pre7.

### Comment 14: ryu3025 (2020-06-17T13:37:44.990-0700)

There must be something different between my testing and your testing, because I'm not having this problem in 1.16-pre7. I just tested in 1.16-pre8 and I'm not having a problem there either. This is how I'm testing it:
- build nether portal

- use a lead on a cow and walk around the portal to lure it in and out of the portal

- the cow has portalcooldown data but no dimension data

- attach the cow's lead to a fence pull then walk into the nether and out to generate a portal on the other side

- lead the cow back into the portal and it teleports into the nether

- return to the nether to where the cow is

- the cow still has portalcooldown data but no dimension data

### Comment 15: Jeuv (2020-06-18T05:20:47.294-0700)

Still in pre-8, this makes getting the advancement Uneasy Alliance really hard.
Edit: I can confirm that mobs that lost their Dimension tag can still go through a portal now, so at least that part is fixed.

### Comment 16: numeritos (2020-06-20T16:26:31.605-0700)

Affects 1.16-rc1

### Comment 17: ryu3025 (2020-06-21T08:41:57.808-0700)

I don't believe this is an issue anymore.
This main problem this issue was causing was that entities would get permanently stuck in the overworld, but in pre-8 (I haven't tried 1.16-rc1) the dimension tag doesn't get set or used, so entities aren't getting stuck in the overworld.
Entities still aren't teleporting if there isn't a Nether Portal on the other side, but should they? If an entity teleported into the Nether without a portal on the other side, it would weird for a player traveling in the Nether, to eventually find an overworld entity without a portal. The teleported entity would have to generate the matching portal and nether chunks when it goes in and the player that pushed it in would probably have to wait in a loading screen even though they aren't teleporting themselves.

### Comment 18: migrated (2021-02-16T11:48:44.601-0800)

Confirmed for 21w06a

### Comment 19: migrated (2021-04-11T12:09:42.564-0700)

I found that if there is a wall behind the nether portal in the dimension you are trying to get the horse to travel to, the horse won't go through as the horse is 2 blocks fat so needs space around the portal to go through.

### Comment 20: ampolive (2021-07-23T07:20:41.613-0700)

Can confirm in 1.17.1.

### Comment 21: migrated (2022-07-04T15:40:48.133-0700)

Would this bug cover Captain Sparklez's struggles to get the Uneasy Alliance Advancement in 1.19? If so, how does 1.19 get added to the Affected Versions list?
This video from here https://youtu.be/grcfZ-s5arg?t=4363 until about 1:20:00 shows his first few attempts with Ghasts and portals. And this one https://youtu.be/J22zYtTjxsQ?t=3480 shows the ghast actually flying through a lit portal at timestamp 58:35 with no affect.

### Comment 22: migrated (2023-07-05T07:36:27.428-0700)

In 1.20.1 this bug appeared again.

### Comment 23: migrated (2023-08-06T10:11:20.338-0700)

Still doesn't work

### Comment 24: [Mod] Jingy (2023-11-26T18:06:29.871-0800)

Can confirm in 1.20.3 Pre-Release 2

### Comment 25: migrated (2024-02-20T18:35:30.210-0800)

Wanted to add something to this and see if I could get any help. My portals are linked on XYZ cords within .50 of a block (the division doesn't always give a whole number) and I am trying to get a zombie to go through the portal and it just keeps walking through the lit portal. I have visited both sides and even set up an area around the nether side that is lit and flat. The only thing that could be causing issues is that the portal is on the nether roof but the Y levels for the overworld-nether portal are the same. I am not sure what to do.

Went into creative and everything worked fine. There are some portals that are within 200 blocks on my server that i had the problem with so maybe that is it.

### Comment 26: [Mod] GoldenHelmet (2024-03-02T11:12:28.208-0800)

Intended behavior based on the resolution of MCPE-166172.

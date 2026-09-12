# MC-181190: The discount for curing a villager is multiplied if the villager is reinfected and cured again

**Mojira URL:** [https://bugs.mojang.com/browse/MC-181190](https://bugs.mojang.com/browse/MC-181190)

## Report details

- **Mojira categories:** Village system
- **Project:** MC
- **Issue key:** MC-181190
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-04-27T20:21:54.373-0700
- **Updated:** 2026-04-02T23:43:06.589-0700
- **Resolution date:** 2024-08-07T17:52:35.356-0700
- **Affects versions:** 1.15.2; 20w17a; 20w18a; 20w19a; 20w21a; 20w22a; 1.16 Pre-release 1; 1.16 Pre-release 2; 1.16 Pre-release 5; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.2; 1.16.3; 1.16.4 Release Candidate 1; 1.16.4; 20w46a; 20w49a; 20w51a; 1.16.5; 21w08b; 21w10a; 21w15a; 21w16a; 21w17a; 21w18a; 21w20a; 1.17 Pre-release 3; 1.17 Release Candidate 1; 1.17; 1.17.1; 21w38a; 21w39a; 1.18; 1.18.1; 1.18.2; 22w19a; 1.19 Pre-release 2; 1.19.1 Release Candidate 2; 1.19.2; 1.19.3; 1.19.4 Release Candidate 2; 1.19.4; 1.20 Release Candidate 1; 1.20
- **Fix versions:** 23w31a
- **Area:** Gameplay
- **Votes:** 0
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** Screen Shot 2020-04-27 at 8.11.16 PM.png
- **Issue links:** Relates:outward:MC-186647:Villager price changes are extremely inconsistent, and completely break in combination with hero of the village | Duplicate:inward:MC-230794:Villager Trading Gives More Loot Than Taken | Relates:inward:MC-268017:Re-curing fully discounted villagers resets/doesn't change discounts on that villager

## Description

When curing a zombie villager, infecting it, and curing it again, the resulting villager has stacked discounts. This exploit makes hero of the village useless (and also allows the fix of MC-153334 to be surpassed with enough curing), as you can just cure villagers multiple times to get the best deals. It also makes no sense, doesn't the villager already owe you its life?

## Comments (27)

### Comment 1: migrated (2020-04-27T20:21:54.373-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2020-04-27T21:16:59.345-0700)

Its intentional. Not a bug.

### Comment 3: MMK21 (2020-05-25T00:14:48.317-0700)

WAI

### Comment 4: migrated (2020-05-27T02:04:28.059-0700)

When you cure a zombie villager it creates a Minor Positive Gossip and a Major Positive Gossip. The Major one with a strength value of 20. This can be stacked a total of 5 times giving a value of 100. So the curing is capped at 5 times maximum, all extra curings wont add to this. This is even explained in the wiki. I think it is intentional. Also it takes quite the work to cure the same villager multiple times so is not super unbalanced.

### Comment 5: migrated (2020-05-27T03:22:42.009-0700)

Not WAI, can be exploited

### Comment 6: migrated (2020-07-03T16:30:27.769-0700)

Plenty of WAI things can be exploited, doesn't mean its a bug

### Comment 7: migrated (2020-07-31T01:08:46.522-0700)

I don’t see how it can be intentional to multiply Emeralds absurdly high while it also destroys completely the purpose of the Hero of the Village effect, another side thing is that Mojang addressed last time the Librarian Bookshelves Trade, so what’s the point of the price increase when you can still achieve the same unwanted final result (Gain Emeralds with no resources gathering) I know I’m not Mojang to decide if this WAI or not but from a logical and balanced point of view this is way too broken and easy to exploit (Yes it’s not hard to have a dedicated Zombie ready to infect 5 times a Villager)
Hopefully they discuss carefully this topic once they take a moment to address this inconsistency.

### Comment 8: migrated (2020-10-10T20:11:29.466-0700)

I think a decent compromise would be to have the the hard game setting make zombies convert villagers to zombie villagers only, say, 15-20% of the time. That would make it a large investment to have a villager cured 5 times. As a bonus, it would also encourage getting spawned zombie villagers to get player villagers (rather than breeding them), as that would ensure at least the ability to cure at least one time. If the player wants to try for additional cure times, they would be subject to the 80-85% chance the zombie would actually kill the villager. Perhaps some buff to the conversion percentage if the player does it with some environment build, similar to how conversion is sped up slightly bar iron bars or beds.
I agree it's not a bug, but could be changed for a better gameplay experience.

### Comment 9: FivesBlue (2021-01-22T00:40:11.217-0800)

I've been thinking about this, and perhaps the best fix would be to manually introduce a floor price for each trade. Using the farmer as an example, trades like the cake trade wouldn't be affected at all, trades like the golden carrot and glistening melon trade could be reduced to a minimum of say 1-2 emeralds after maybe 3 conversions. Trades like the melon and pumpkin trades could be reduced to a minimum of 1-2 melons/pumpkins each as well after the maximum 5 conversions, and trades like the Wheat/Carrot/Potato/Beetroot trades could be reduced to a minimum of 5-10 wheat/carrot/potato/beetroot after the maximum 5 conversions. I think this keeps the current game mechanic without the same level of exploit as before

### Comment 10: migrated (2021-02-11T06:37:39.962-0800)

I've learned from running a Paper server that fixing this "exploit" so cure discounts do not stack at all (and existing stacked discounts get removed) leads to player disappointment and frustration.  Hearing my player's frustration when I switched from Spiggot to Paper was not fun for me as a server admin.
Because of this, I have disabled Paper's exploit fixes in my server settings.
Players put a lot of effort into designing and building Villager trading halls with inventive redstone systems to make use of zombie cure discount stacking. There is a growing city on my server centered on one such Villager trading hall. This city likely would not exist if players on the server had not been interested in the discount stacking mechanic and collaborated to make use of it.
I feel this is an issue where emergent gameplay and what is more fun for players needs to be taken into consideration.  Removing discount stacking completely would ruin a game mechanic that players have made entire builds around.

### Comment 11: migrated (2021-03-07T17:32:32.904-0800)

literally it's a part of the game and it still is relatively difficult to work with villagers with this feature. yall look past the fact that you can start a world on skyblock and do so much but when it comes to cheaper villager prices somehow that's too far? smh. I literally put all I have into massive trading areas and this was a feature known since 1.14 but it hasn't been removed which means it's obviously intentional. and considering so many people have gotten invested in trading hall-based setups when making a base I think it's a bit cruel to remove that now.

### Comment 12: ampolive (2021-06-30T15:28:23.210-0700)

This is unquestionably a bug, because it already has a Mojang Priority assigned. This causes exploits such as trading loops allowing players to get virtually unlimited amounts of emeralds.

### Comment 13: ampolive (2021-09-03T15:48:07.434-0700)

Can confirm in 1.17.1.

### Comment 14: Machine Maker (2021-12-29T10:46:55.583-0800)

Still an issue in 1.18.1

### Comment 15: migrated (2023-07-27T14:16:53.419-0700)

Hasn't this been in the game since pre 1.14? Shouldn't this be considered a bug in 1.14 as well? Is the whole reason this is being fixed is because mojang is turning the game into more of a grindy game than a relaxing game? Is it because of hero of the village? Hasn't this been confirmed as a feature at one point? Again, hasn't this been in the game since discounts, curing, and trading were added in 1.3.1? (I'm not actually sure when the ability to cure was added, but I'm fairly certain it came with trading and villagers as well)
Edit: Besides, how does this make hero of the village useless? It gives barely any discount to trades on villagers that haven't been cured, and they throw items at you that aren't useful. To me, its already been useless this whole time, even without cured villagers. To make it useful, they don't have to drop rare items, but for example theres a mod that makes hero of the village useful with and without curing villagers, just by giving them better items to give you, and example being toolsmiths giving you lava buckets. Its not really rare, but it can be annoying enough to get that being able to have it thrown at you just for killing a few pillagers and illagers is good enough.
Edit 2: Removing this is like not adding vertical slabs. I've heard that the reason for not adding it is that it would "inhibit creativity." How exactly would it do that? I've got tons of build ideas that I just can't build without scaling it up so each block is actually made of 8 blocks. People have been creative and made many structures just to use this feature. With mods that had vertical slabs, people have made many more structures than is possible without it. (Although personally, I'd like 1/8 block things rather than vertical slabs, because it would allow you to make vertical slabs, very small pillars, or pillars that are just off the normal blocks, or vertical stairs.)
I just don't know why we can't have cool bugs and consider them features anymore.
I think a good compromise could be that, as someone else said, have floor prices and make it take multiple conversions for things to happen. The best trades could take 10-20 conversions to get it down to 1 emerald, and also if the villager gets turned back into a zombie say, a minute after it was converted back into a villager? That is obvious exploitation of a feature. Go ahead and make them revoke a "conversion point" or two, if not all of them. Making players wait and do whatever they want in the meantime without forcing them to grind for hours for something (think netherite in 1.20, it will take hours, possibly days just to get a full set, and to lose it all? I dislike how grindy minecraft has become, considering I used to play it to relax. It still takes forever to mine diamonds as well considering how long it takes to break deepslate and how much rarer they are since 1.17. (1.18? didn't create a new world until then) and how now you have to make a mine on a different y-level for each specific ore to get the best rates rather than just one. Instead of making players do what they want, they've been forced to grind so they can do what they want.) Making players wait without grinding feels like a good compromise.
Also, I've never heard anyone refer to this as a bug until today when I saw this.

### Comment 16: migrated (2023-07-27T16:07:45.335-0700)

Hasn't this been confirmed as a feature at one point?
No, not by Mojang, and anyone else who says otherwise is making things up.
Just because it got in with the version that added discounts, doesn't mean it was supposed to stack with the existing discount for curing. (Trading and zombification existed WAAAY before 1.14 (1.3 and 1.4 respectively.))
The whole problem here is game-balace and that's being adressed.
Not responding to anything else you wrote as that has no relation to this issue. For discussions go to reddit, for feature/change requests, go to feedback.minecraft.net.

### Comment 17: migrated (2023-07-27T20:48:17.429-0700)

This was not a bug, why are we changing this. After so long with so many players using this mechanic once they get to the stage where they understand villagers. This is very poor judgement call by Mojang.

### Comment 18: [Mod] LateLag (2023-07-27T21:18:48.329-0700)

The report has had an assigned employee and priority as far back as 2020, it was a very clear bug.

### Comment 19: ampolive (2023-07-28T14:09:09.666-0700)

This is a bug tracker, not a discussion forum. For feedback on the resolution of this bug, head to the Feedback website. Any further comments complaining about the resolution of this bug or containing feedback will be removed.

### Comment 20: rumickon (2023-08-07T04:04:28.945-0700)

Finally fixed. Thank you.

### Comment 21: migrated (2023-08-09T08:00:40.118-0700)

Not a bug. No need to fix.

### Comment 22: migrated (2023-08-09T08:07:26.383-0700)

Mojang's actions say otherwise. Just because you like(d) it, doesn't mean it's by design.

### Comment 23: migrated (2023-08-09T22:14:48.260-0700)

You nerfed villagers without fixing xp issue (pickaxe that cost 19xp now costs 39)

### Comment 24: migrated (2023-08-09T23:19:23.308-0700)

Read the mod comment below; for feedback go to feedback.minecraft.net; additionally, this fix is separate from trade changes.

### Comment 25: migrated (2024-05-27T23:41:25.488-0700)

Could they perhaps bring this back as a feature?

### Comment 26: migrated (2024-08-07T17:52:35.356-0700)

Change it to "reopened"

### Comment 27: Ash ford (2026-01-03T13:15:32.292-0800)

I also believe it should be brought back as a feature.

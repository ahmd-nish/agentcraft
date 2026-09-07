# MC-107529: Marker:1b Armor Stands render themself and their equipment dark if inside solid blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-107529](https://bugs.mojang.com/browse/MC-107529)

## Report details

- **Mojira categories:** Commands; Hitboxes; Lighting
- **Project:** MC
- **Issue key:** MC-107529
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2016-09-28T10:13:02.393-0700
- **Updated:** 2025-04-29T20:38:22.548-0700
- **Resolution date:** 2021-12-19T12:01:06.873-0800
- **Affects versions:** Minecraft 1.10.2; Minecraft 16w38a; Minecraft 16w39a; Minecraft 16w39b; Minecraft 16w39c; Minecraft 16w40a; Minecraft 16w41a; Minecraft 16w42a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w14a; Minecraft 17w15a; Minecraft 17w16a; Minecraft 17w16b; Minecraft 17w17a; Minecraft 17w17b; Minecraft 17w18a; Minecraft 17w18b; Minecraft 1.12 Pre-Release 1; Minecraft 1.12 Pre-Release 2; Minecraft 1.12 Pre-Release 3; Minecraft 1.12 Pre-Release 6; Minecraft 1.12 Pre-Release 7; Minecraft 1.12; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45b; Minecraft 17w46a; Minecraft 17w47a; Minecraft 17w47b; Minecraft 17w48a; Minecraft 17w49a; Minecraft 17w49b; Minecraft 17w50a; Minecraft 18w01a; Minecraft 18w03b; Minecraft 18w05a; Minecraft 18w16a; Minecraft 18w22a; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre8; Minecraft 1.13; Minecraft 18w31a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w45a; Minecraft 18w46a; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03b; Minecraft 19w03c; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w12b; Minecraft 19w13b; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2 Pre-Release 3; Minecraft 1.14.3; 1.15.1; 1.15.2 Pre-Release 1; 1.15.2; 20w06a; 20w09a; 20w12a; 20w13a; 20w13b; 20w14a; 20w17a; 20w19a; 1.16 Pre-release 5; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w28a; 1.16.2 Pre-release 1
- **Fix versions:** 1.16.2 Pre-release 3
- **Labels:** armor_stand; marker
- **Watchers:** 1
- **Attachments:** 8
- **Attachment filenames:** 1.png; 17w49b-2.png; 2.png; 2016-09-28_18.35.36.png; 2016-09-28_18.43.30.png; 2016-09-28_19.02.12.png; 3.png; QuickFixAttempt_pollitoyeye.png
- **Issue links:** Cloners:inward:MC-197260:Armor Stand renders itself and armor dark if its head is in a solid block

## Description

Despite the fact that Armor Stands got Marker:1, they are rendering black because part of their hitbox (the top) is inside a solid block.
Steps to reproduce
1. Place a commandblock
2. Stack 3 solid blocks on top of the CommandBlock, e.g. smoothstone
3. Insert the following command into the CommandBlock and trigger it:

```
/summon armor_stand ~ ~2 ~ {CustomNameVisible:1b,Glowing:1b,ShowArms:1b,Marker:1b,Invisible:0b,NoBasePlate:0b,HandItems:[{id:"minecraft:lapis_block",Count:1b},{id:"minecraft:lapis_ore",Count:1b}],ArmorItems:[{id:"minecraft:iron_boots",Count:1b},{id:"minecraft:iron_leggings",Count:1b},{id:"minecraft:chainmail_chestplate",Count:1b},{id:"minecraft:player_head",Count:1b,tag:{SkullOwner:{Id:"994924dc-8404-4af4-a58b-678426ee0095",Properties:{textures:[{Value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYzBmZmE0OWIxYWQ3ZmNmZDJhNWUxYTU4YzMxZjFkM2I5OTYwMDZjMTAzODBhNTQ0MTlkZmFmM2ZiNzc4MzdjZiJ9fX0="}]}}}}],CustomName:"{\"text\":\"Meri\",\"color\":\"dark_blue\",\"bold\":\"true\",\"italic\":\"true\"}"}
```
4. teleport the Armor Stand gradually down, e.g. with:

```
/execute as @e[type=armor_stand] at @s run tp @s ~ ~-0.1 ~
```
At some point you'll see that the Armor Stand including its equipment goes dark.
As AS are used a lot not only outside, but also inside of blocks, and using transparent blocks instead to circumvent the AS incl. their rendered equipment going dark is not always a possible option, it'd be desirable for mapmakers to have Marker:1-AS rendering themself and their equipment "dark" fixed, while keeping the other needed fixes for AS that already were made or that are currently in the making.
But, as already pointed out, it'd be very good for mapmakers if Marker:1 would not render AS/their equipment dark if stuck inside a solid block, as more options would then be possible for us.

## Comments (39)

### Comment 1: migrated (2016-09-28T10:13:02.393-0700)

This comment contained multiple image attachments (8), please login to view the attachments.

### Comment 2: NeunEinser (2016-09-29T16:12:30.300-0700)

(MCP v9.30 names)
Hello,
first of all this does not only apply for ArmorStands, but also for pretty much every other entity. The reason why this is the case, is because net.minecraft.entity.Entity.getBrightnessForRender(float) only looks for the brightness level of the block at the entity's eye height.
A possible fix would be to actually look at every block the Entity is (partially) in. In this example it is going to set the entity's brightness to the light level of the brightest block the entity is touching. This means, if the entity is partially inside of a block (brightness 0), it is still going to find other blocks that are brighter and will choose the brightest one.
net.minecraft.entity.Entity.getBrightnessForRender(float)

```public int getBrightnessForRender(float partialTicks)
{
    BlockPos.MutableBlockPos blockpos$mutableblockpos = new BlockPos.MutableBlockPos(MathHelper.floor_double(this.posX), 0, MathHelper.floor_double(this.posZ));

    if (this.worldObj.isBlockLoaded(blockpos$mutableblockpos))
    {
    	int light = 0;
    	AxisAlignedBB boundingBox = this.getRenderBoundingBox();

    	for (double x = boundingBox.minX; Math.floor(x) <= Math.floor(boundingBox.maxX); x++)
    	{
    		for (double y = boundingBox.minY; Math.floor(y) <= Math.floor(boundingBox.maxY); y++)
    		{
    			for (double z = boundingBox.minZ; Math.floor(z) <= Math.floor(boundingBox.maxZ); z++)
    			{
    				blockpos$mutableblockpos.set(MathHelper.floor_double(x), MathHelper.floor_double(y), MathHelper.floor_double(z));
    				light = Math.max(light, this.worldObj.getCombinedLight(blockpos$mutableblockpos, 0));
            		}
        	}
    	}
        return light;
    }
    else
    {
        return 0;
    }
}```
NOTE: In 1.10, this is NOT going to fix marker-AS as they have no hitbox in this version. But since they actually do have a hitbox in 1.11 snapshots, it is very likely that this fix will also work for marker-AS in the snapshots, but I do not have any way of testing that.
This might cause some lag, especially if many big mobs like giants or enderdragons are around but with my quick and limited testing, it seems to be okay.
Also, even for none-marker-ArmorStands the hitbox is not quite big enough to cover the entire armor stand + equipment and it is still the case that it goes black at some point. But it is a lot better than it was before.
Edit:
If it is considered too laggy, especially for giants/enderdragons, you could stop searching as soon as you find a block with a light level bigger than 0.
net.minecraft.entity.Entity.getBrightnessForRender(float)

```public int getBrightnessForRender(float partialTicks)
{
	BlockPos.MutableBlockPos blockpos$mutableblockpos = new BlockPos.MutableBlockPos(MathHelper.floor_double(this.posX), 0, MathHelper.floor_double(this.posZ));

	if (this.worldObj.isBlockLoaded(blockpos$mutableblockpos))
	{
		AxisAlignedBB boundingBox = this.getRenderBoundingBox();
		int light;

		for (double y = boundingBox.maxY; Math.floor(y) >= Math.floor(boundingBox.minY); y--)
		{
			for (double x = boundingBox.minX; Math.floor(x) <= Math.floor(boundingBox.maxX); x++)
			{

				for (double z = boundingBox.minZ; Math.floor(z) <= Math.floor(boundingBox.maxZ); z++)
				{
					blockpos$mutableblockpos.set(MathHelper.floor_double(x), MathHelper.floor_double(y), MathHelper.floor_double(z));
					light = this.worldObj.getCombinedLight(blockpos$mutableblockpos, 0);
					if (light > 0) {
						return light;
					}
				}
			}
		}
	}
	return 0;
}```
To make it behave more like current behavior, I start in this case with the highest y value of the bounding box. to be closer to the eye height at the beginning.

### Comment 3: NeunEinser (2016-09-30T03:04:01.655-0700)

I added another variation of the fix which decreases the amount of lag caused by it.

### Comment 4: migrated (2016-09-30T11:50:39.713-0700)

Thank you very much  }=)

### Comment 5: NeunEinser (2016-11-03T10:33:27.348-0700)

The hitbox got changed back to the 1.10 behavior. This means, that once again the lightning of the armor stand's base is the relevant one and my suggested fix would not work for marker AS anymore, but it still would make it better for everything but marker-AS. I think however the link in the description to my fix should be removed since it is not relevant for this issue any longer.

### Comment 6: migrated (2016-11-14T10:17:06.644-0800)

In 1.11, this also affects marker:1 armor stands, so creations using makers holding blocks for "micro blocks" are pretty much useless.
This is a HUGE Issue for map makers.

### Comment 7: migrated (2017-01-10T16:57:34.025-0800)

I am on PC, using 1.11.2.
I am having the same issue with my vending machine. The stands and the items it holds are black. It seems to fix it's self when i place a glowstone first or any block that lights up (only when it is lit up).

### Comment 8: migrated (2017-08-18T01:57:11.463-0700)

Are there any plans on fixing this?

### Comment 9: migrated (2017-08-18T03:31:25.422-0700)

No idea if it's that easy to fix, as you may conclude from my post, there was a short time during snapshots where it was temporarily fixed due to a different fix/addition, but it caused other, more severe problems for map-/contraption makers, and those were more important to be fixed, so this bug here occurred again as a result.

### Comment 10: migrated (2017-09-16T12:30:48.233-0700)

Why is this critical bug fixed for so long? We have been waiting for a year. The developer of the "Vehicles" plugin was offended because of this bug and does not update its plugin.

### Comment 11: migrated (2017-09-16T12:41:02.127-0700)

As you may infer from the screenshots and my comment just right above yours, this bug was actually temporarily fixed, at least nearly, but it caused another bug which was way more severe, so it had to be reverted.
I'd also love this to be fixed asap, but it doesn't seem to be that easy, without affecting it negatively for mapmakers in other areas.

### Comment 12: onnowhere (2017-12-06T22:21:22.724-0800)

This is an incredibly important issue that affects my project. I've been working on a project that used to rely on seamless double slabs not making marker armor stands go dark pre-1.13. However, in 1.13, this is no longer the case. I have been working on this project since 1.9 in the hopes that it can provide help to map makers come with all the data pack, recipe customization etc. possible in 1.13, however, just due to this bug, it can't be completed. In my case personally, fixing this bug would save an entire project.

### Comment 13: NeunEinser (2017-12-07T01:19:18.212-0800)

would it be possible for you to use a different block like upside down stairs that use a different model? Or even an 8 high snow layer? It would be very sad if your project would fail because of a minor change like that.

### Comment 14: migrated (2017-12-07T09:51:22.452-0800)

I can confirm that this happens even for pistons now, which was not the case before.
Given the current situation, I would not like anyone to try to fix it for pistons specifically, but strictly for armor stands.
 I don't know your project, but can you not do it with another block, or, like  already wrote, with a model/via resource pack? Given the fact that even pistons render Marker-true-AS dark now, I don't know if it would do it similarly for stairs or snow layers though, so how about a glass block which got the texture of being opaque, but the specs of being transparent?
 See pic, transparent blocks shouldn't affect Marker-true-AS.

### Comment 15: onnowhere (2017-12-07T17:15:33.926-0800)

My project relies on not replacing common blocks used by players in creative/survival and mimicking different solid blocks like stone or wood based, so I can't. I relied on seamless double slabs as they were less commonly used and there were multiple types to use to mimic actual blocks (stone based, wood based, etc.)

### Comment 16: migrated (2017-12-07T20:54:11.962-0800)

Too bad you can't use giant mushroom blocks, it'd be 160 to chose from.
But they are sadly not transparent, the AS also gets dark inside them.
(It's ~6am for me and I got to go asap, so check your Twitter DM sometime this day, I'll try to get back to you there during 2 business appointments/lunch break, at latest around 8pm Germany time.)

### Comment 17: migrated (2018-01-17T11:28:50.881-0800)

We entered in 2018 and an important issue opened in 2016 that was caused by the programmers isn't even fixed yet.
I see bug fixes every update that are totally less relevant than this one.
31 persons voted for this issue and the only response we got was "use another blocks with resourcepacks".
Armorstands were also introduced to evade resourcepacks and allow good vanilla creations.
What's the point of them if you suggest us to use resourcepacks?
As a programmer I'm totally sure fixing this won't take more than a day as other devs even pointed how to fix this.
Seeing how this issue gets marked as still happening every snapshot is just sad.

### Comment 18: migrated (2018-01-17T11:43:04.589-0800)

I agree that it's an annoying thing for mapmakers, but I know for some reason (I already asked) that it isn't as easy to fix as one may think.
I also assume they have some other priorities currently on top, and there are not many Devs for Java, given the code base you sadly can't just hire anybody for it.
The way we use some things which are in Minecraft is not always as they may have been intended in the beginning, and it seems close to impossible to have all mapmaker tools updated to a state where they "should be", considering the small Dev team, other bugs having to be fixed and new things to be implemented.
All I can ask for is still patience, if we are lucky we may get a complete rewrite or new addition as replacement at some point, I'll keep an eye on it and related issues for mapmakers, and continue to ask for replacements or similar.

### Comment 19: migrated (2018-01-17T11:56:07.223-0800)

I have to disagree with you. Making entities with a tag rendering no shadows is not something difficult.
It is as simple as modifying the current tag to work like that or adding a new tag "NoShadow" that removes entity shadows.
You can't sell something that probably implies an if -> return as a work of titanic magnitudes.
I can accept the fact that they won't just fix it because they don't even remember this issue or they are with other things they "consider more important".
But please, don't threat the most important part of the community (Map Makers) as if they were stupid.

### Comment 20: migrated (2018-01-17T12:11:11.168-0800)

I will rephrase it.
I didn't want to say it that bluntly to not give the wrong impression, but to make it very clear to you so you'd hopefully reconsider your slightly hostile attitude:
I asked one of the Java developers directly, on November 24th 2017, regarding this very bugpost, so you can disagree with me now however you want, but feel very much invited to provide a code fix which doesn't break other things (see my other comments/remarks here from the time when it was fixed for a little while, but broke other, more serious, things) though, they said so publicly that they very much appreciate that.
The "don't treat the most important part of the community" remark was absolutely unnecessary by the way, I don't know if you meant the Devs with that or myself, but with both you'd be mistaken with what you stated as a fact, not even as an assumption.
If you want to discuss or just vent your anger, please go to the Mojira-Reddit.

### Comment 21: migrated (2018-01-18T03:48:01.206-0800)

As you asked I did it. It took 10m.
Haven't tested it yet but if this is not the solution it's something really near from this.
Put this on EntityArmorStand.class. (Names mapped from Forge 1.12.2)

```@Override
    @SideOnly(Side.CLIENT)
    public int getBrightnessForRender(){
    	if(hasMarker()){
    		return 15728880;
    	}
    	return super.getBrightnessForRender();
    }```
If you actually want the armorstand to render darker depending of the blocks light it would be as easy as changing the inside of the if and taking in consideration external block lights.
As it's overriding a super class method and only gets called for marker armorstands this breaks nothing. Even a new tag could be added just for this as mentioned. NoShadow for example.

### Comment 22: migrated (2018-01-18T13:04:20.818-0800)

Hello, thank you very much for your QuickFix(attempt), I tested it, and although you said "If you actually want the armorstand to render darker depending of the blocks light" it's not what you did, although you also added "it would be as easy as changing the inside of the if and taking in consideration external block lights."
So why didn't you do it rightaway when you knew that the ingame result would never be considered "WaI" by Mojang?

To just provide a 10-minutes-QuickFix to "prove a point" that it should be doable for Mojang to fix this bug in a short amount of time, but then yet again push the responsibility for a proper fix to Mojang, is not really helpful or would validate what you said, quite the opposite.
It's quite obvious that Mojang currently prefers to work rather on the code structure (see 1.13 snapshots), not on "quick fixes".
That's why I wrote to you: "if we are lucky we may get a complete rewrite or new addition as replacement at some point".
I rather have a proper fix than a hotfix for this type of issue.
I currently don't have the time to reply to you today in detail, I should also better open a Redditpost for that as the mods don't like the bugtracker to be used as discussion forum, but I know Panda4994 has been working on explaining the whole bugfix-situation to the community since longer, so I'll ask him instead, as he also knows the current state of the code way better than I do.
He's busy working on another video at the moment, but knowing him, he'll surely be so kind to reply to you as soon as possible, possibly in a Redditpost or whatever he may find suited, which he'd then link here for you, I just can't promise you when that would be due to his real life and also the video he's working on.

### Comment 23: NeunEinser (2018-06-23T08:06:40.009-0700)

Can confirm for 1.13-pre3.
Command in step 4 needs to be changed for 1.13:

```/execute as @e[type=armor_stand] at @s run tp @s ~ ~-0.1 ~```
 (besides the execute at, it should be ~-0.1 to teleport downwards)

### Comment 24: Panda4994 (2018-06-27T11:53:40.500-0700)

Confirmed for 1.13pre4.

### Comment 25: Panda4994 (2018-07-04T11:10:39.739-0700)

Confirmed for 1.13-pre6.

### Comment 26: Panda4994 (2018-07-13T14:50:24.897-0700)

Confirmed for 1.13-pre8.

### Comment 27: Panda4994 (2018-07-20T08:57:49.572-0700)

Confirmed for 1.13.

### Comment 28: migrated (2018-08-01T20:21:38.062-0700)

Confirmed for 18w31a.

### Comment 29: migrated (2018-10-09T10:01:13.185-0700)

Confirmed for 1.13.1.

### Comment 30: migrated (2018-10-20T07:56:46.541-0700)

Confirmed for 1.13.2-pre2

### Comment 31: bill96012 (2019-12-17T09:13:41.823-0800)

Confirmed for 1.15.1

### Comment 32: migrated (2020-06-17T22:39:14.551-0700)

You can use {Fire:10000s,Marker:1b} as a workaround. But it might not work perfectly since Marker sometimes doesn't render which is why I am here

### Comment 33: migrated (2020-06-18T07:53:26.825-0700)

What you mean is probably , if you want to follow that specific bug

### Comment 34: migrated (2020-08-07T02:02:33.557-0700)

Confirmed fixed for me in pre-3, thank you so very much!! 💙💙💙

### Comment 35: onnowhere (2020-08-07T02:15:57.252-0700)

Thanks Meri for the original report, finally fixed

### Comment 36: migrated (2020-08-12T12:50:48.893-0700)

It is not fixed.
It goes dark or light depending of where it's placed.
What I am riding in the picutres is made of moving armorstands so it is a good way to test it, you can notice the problem in the wheels.
It should always look like the first picture.

### Comment 37: migrated (2020-08-12T13:22:10.514-0700)

Does MC-160917 describe your issue?
Edit: I just noticed there's also  now.

### Comment 38: migrated (2020-11-06T08:28:38.989-0800)

This bug is present in 1.16.4.

### Comment 39: Sniper1.1 (2021-12-19T12:01:06.873-0800)

This seems to be somewhat broken in 1.18.1. I’m trying to make use of armor stands for map detailing but they go dark when the head space is in a block even if they have {Marker:1}. It seem marker armor stands can have a block in their feet and be fine, but not their head. This also applies to small armor stands. I would really like markers to not go dark please.

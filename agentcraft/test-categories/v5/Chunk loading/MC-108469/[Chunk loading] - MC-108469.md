# MC-108469: Chunk-wise entity lists often don't get updated correctly (Entities disappear)

**Mojira URL:** [https://bugs.mojang.com/browse/MC-108469](https://bugs.mojang.com/browse/MC-108469)

## Report details

- **Mojira categories:** Chunk loading; Entities
- **Project:** MC
- **Issue key:** MC-108469
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2016-10-08T13:00:11.943-0700
- **Updated:** 2025-04-29T10:54:47.163-0700
- **Resolution date:** 2024-01-29T13:33:00.464-0800
- **Affects versions:** Minecraft 1.10.2; Minecraft 16w40a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 1.11.2; Minecraft 1.12; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 17w50a; Minecraft 18w20a; Minecraft 18w20b; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre8; Minecraft 1.13; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03c; Minecraft 19w04a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w08b; Minecraft 19w11b; Minecraft 19w12b; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 1; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3 Pre-Release 3; Minecraft 1.14.3 Pre-Release 4; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 2; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; 1.14.4; 19w36a; 19w37a; 19w40a; 19w41a; 1.15 Pre-release 1; 1.15.1; 1.15.2 Pre-Release 1
- **Fix versions:** 20w45a
- **Labels:** chunk; entity; unloaded-chunks
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Relates:outward:MC-89667:Position based selector arguments fail finding entity if it has been moved to a different chunk in the same tick | Duplicate:inward:MC-129685:/tp command doesn't handle entity tp properly | Duplicate:inward:MC-143173:If an entity is teleported to an unloaded chunk, upon leaving then reloading the game the entity no longer exists | Duplicate:inward:MC-153381:/teleport does not update chunk positions of entities | Relates:inward:MC-125824:Unexpected behavior with same-tick entity teleportation and summoning over multiple chunks

## Description

The bug
In many cases when entities are moved into another chunk they are not added to the new chunks entity lists rightaway.
Instead they get added when the entity receives the next update tick. Until that happens the entity will not be found by some searches that use the chunk-wise lists.
In some cases (like in lazy chunks) it can even happen that the entity is not ticked and doesn't get added to the new list at all. Upon unloading the world the entity will not get saved in the correct chunk and be deleted upon the next reload.
Two cases where this bug can happen are teleport commands and pistons. It's likely that there are more cases though.
How to reproduce
- Create a superflat world.

-

```
/setworldspawn 0 0 0
```

-

```
/tp 1000 100 0
```

- Reload the world to make sure only the right chunks are loaded.

-

```
/summon minecraft:armor_stand 0 100 0 {NoGravity:1,Tags:["MC-108469"]}
```

-

```
/tp @e[tag=MC-108469,x=0,y=100,z=0,distance=..10] 200 100 0
```
Notice that the target position is still a loaded chunk, just not one in which entities get ticked.

- If you now unload and reload the world the armour stand will be gone only leaving the following messages in the launcher:

```
[INFO] 01:58:46.893 Preparing spawn area: 0%
[WARN] 01:58:46.919 Wrong location! (12, 0) should be (0, 0), avm['Armor Stand'/22, l='19w46b', x=200.50, y=100.00, z=0.50]
[INFO] 01:58:46.960 Changing view distance to 31, from 10
```

Alternatively to reloading the world, the error can be shown using these commands. They are not able to find the entity.

```
/say @e[tag=MC-108469]
```

```
/say @e[tag=MC-108469,x=200,y=100,z=0,distance=..100]
```
In contrast this one does find the entity:

```
/say @e[tag=MC-108469,x=200,y=100,z=0,distance=..1000]
```
Given the position of the armorstand all of the above commands should be able to find it, however, since it is not constantly updated across different entity lists, only the third one will find it (as off 1.15pre1).
Also note that the behaviour of these commands is highly dependant on performance decisions of entity selectors and might not behave the same under all conditions.
This issue affects survival (pistons) as well as creative/map making (teleport commands).
Another way this issue shows is when trying to teleport an entity twice in the same tick through several chunks, using selectors that make use of the chunk entity lists. The second selector will then not be able to find the entity.
Code analysis
Code analysis and suggested fix by  can be found here and there. Additional minor optimization here.

## Comments (32)

### Comment 1: [Mod] Neko (2016-10-08T13:25:39.013-0700)

Does  describe your issue?

### Comment 2: Panda4994 (2016-10-08T13:30:03.010-0700)

It's likely to be related, but  is describing a wide set of issues for players, not for entities in general.
I think that many issues in  might be caused by the client/server communication, while this issue purely lies on the server side.

### Comment 3: migrated (2016-10-29T07:36:56.631-0700)

The occasional disappearance of moving entities after chunk unloading probably also is related to that. Also sometimes moving entities get duplicated after chunks get unloaded/loaded

### Comment 4: SunCat (2016-11-23T22:02:25.805-0800)

Relates to MC-89667

### Comment 5: migrated (2018-01-04T17:16:42.618-0800)

This bug is related to the way the entity's are processed. The entity code in World.java on line 1957: "updateEntityWithOptionalForce" causes this issue.
This is because entity's that are suddenly moved into a new chunk that is not loaded never get added to the unloaded chunk they have entered. They are removed from the list of entity's that are added to chunks and they stay in memory until the chunks around the entity are loaded to make it entity process. Then the entity is added to the chunk it is in. Because all data is stored per chunk basis it means that if entity's do not belong to any chunk they simply get unloaded along with the world without being saved to disk. This can happen to entity's that are moving faster then 32 blocks per game tick and other rare instances when pistons push entity's.
Detailed code explanation.
In World.java line 1959 in updateEntityWithOptionalForce this if check can be found

```if (!(entityIn instanceof EntityPlayer))
        {
            int i = MathHelper.floor(entityIn.posX);
            int j = MathHelper.floor(entityIn.posZ);
            int k = 32;

            if (forceUpdate && !this.isAreaLoaded(i - 32, 0, j - 32, i + 32, 0, j + 32, true))
            {
                return;
            }
        }```
This code allows for entity's to be skipped if there is a chunk within a 5x5 area around that is not loaded. The term entity processing is used to describe this.
Later in the same function at line 1987 the entity gets updated at the line "entityIn.onUpdate();" and it might have been moved at this point.

```if (forceUpdate && entityIn.addedToChunk)
        {
            ++entityIn.ticksExisted;

            if (entityIn.isRiding())
            {
                entityIn.updateRidden();
            }
            else
            {
                entityIn.onUpdate();
            }
        }```
If the entity moves into a new chunk the entity gets removed from the old chunk and added to the next chunk it enters. This happens at line 2022.

```if (!entityIn.addedToChunk || entityIn.chunkCoordX != l || entityIn.chunkCoordY != i1 || entityIn.chunkCoordZ != j1)
        {
            if (entityIn.addedToChunk && this.isChunkLoaded(entityIn.chunkCoordX, entityIn.chunkCoordZ, true))
            {
                this.getChunkFromChunkCoords(entityIn.chunkCoordX, entityIn.chunkCoordZ).removeEntityAtIndex(entityIn, entityIn.chunkCoordY);
            }

            if (!entityIn.setPositionNonDirty() && !this.isChunkLoaded(l, j1, true))
            {
                entityIn.addedToChunk = false;
            }
            else
            {
                this.getChunkFromChunkCoords(l, j1).addEntity(entityIn);
            }
        }```
This is where the bug shows up. at line 2039 an if check is done on the entity to make sure that the chunk the entity have moved into is loaded. If the entity have moved into a unloaded chunk it simply gets a boolean check "addedToChunk" as false without being added to the chunk it has entered and at the same time a few lines above it gets removed from the old chunk it was in.
At this point the entity gets stuck in memory as it dosen't have a 5x5 loaded chunk area around itself to become processing while it is not saved to any chunk and not able to get saved to disk. The exception to this is when the entity is teleported as in goes through portals or teleported by other means. This rare instance the "setPositionNonDirty" is set to true and the entity is added to the chunk it has entered. But this only happens when entity's are moved via teleportation.
This is probably not as intended because the entity can only be saved to disk and unloaded from memory if the player loads the area where the entity is in again and makes the entity become entity processing. Only then does the entity notice that it doesn't belong to any chunk and adds itself to the chunk it is in. The entity's that are moved into unloaded chunks can cause corruption and other issues when the world is shut down without being properly saved to disk. Mobs can be lost because of this. If entity's are not allowed to get saved to disk they also cause lag as they clog the memory by being added to list of loaded entity's without being able to get removed.
Suggested fix
As entity's can only be saved to disk and removed from memory when they are added to a particular chunk. It is suggested to simply add all entity's to the chunk they enter by removing the if check and explicitly add them to said chunk they enter. The only reason this check must have been done would have been to save some additional memory space prior to the "save-all chunks" every 900 game ticks. This must have been here to prevent chunks from becoming loaded prematurely. With the added 900 game tick "save-all chunks" added to the game makes this particular issue a non issue. Entity's can simply be added to chunks they enter and temporarily load the chunk to get saved to it. Later they can get unloaded and removed from memory while being saved to disk.
This code suggestion can simply be done to fix this bug.

```if (!entityIn.addedToChunk || entityIn.chunkCoordX != l || entityIn.chunkCoordY != i1 || entityIn.chunkCoordZ != j1)
        {
            if (entityIn.addedToChunk && this.isChunkLoaded(entityIn.chunkCoordX, entityIn.chunkCoordZ, true))
            {
                this.getChunkFromChunkCoords(entityIn.chunkCoordX, entityIn.chunkCoordZ).removeEntityAtIndex(entityIn, entityIn.chunkCoordY);
            }

            // if (!entityIn.setPositionNonDirty() && !this.isChunkLoaded(l, j1, true))
            // {
            //    entityIn.addedToChunk = false;
            // }
            // else
            // {
                this.getChunkFromChunkCoords(l, j1).addEntity(entityIn);
            // }
        }```
It is not harmful to the game to add an entity to an unloaded chunk. What will happen is that the chunk it is temporarily loaded and later unloaded by the 900 game tick "save-all chunk unloading" cycle. This suggested fix however dosesn't fix the issue that piston causes to entity's that are moved into the next chunk. The fix to make sure entity's get properly saved to disk when pushed by pistons needs a more complex fix that haven't been looked into. Most likely will need a better entity movement check done by pistons.

### Comment 6: migrated (2018-01-06T15:27:30.574-0800)

Bug can be seen here by EDDxample.
https://www.youtube.com/watch?v=xuFLfSI43bI
To fix this bug fully as the code suggestion above was only for entity's that move themself into unloaded chunks. The issue with pistons is that pistons can also move entity's without sending an update on the entity. To fix that pistons need to notify the entity to send an update to the entity that is being moved.
Simply adding "world.updateEntityWithOptionalForce(entity, false);" to line 209 in class TileEntityPiston.java in the function "moveCollidedEntities" in addition to the fix suggested above.
Some entity's need to be fully updated to save there correct position and therefore move back to the old position before the piston move. An extra entity update would fix this but as the entity is clearly in an unloaded area it makes no sense to do so in this instance. This happens to Minecarts for example. This last noted bug is to minor and trivial as the entity is there but in the wrong position. Most other entity's are reloaded in the correct position including armorstands.

```private void moveCollidedEntities(float p_184322_1_)
    {
        EnumFacing enumfacing = this.extending ? this.pistonFacing : this.pistonFacing.getOpposite();
        double d0 = (double)(p_184322_1_ - this.progress);
        List<AxisAlignedBB> list = Lists.<AxisAlignedBB>newArrayList();
        this.func_190606_j().addCollisionBoxToList(this.world, BlockPos.ORIGIN, new AxisAlignedBB(BlockPos.ORIGIN), list, (Entity)null, true);

        if (!list.isEmpty())
        {
            AxisAlignedBB axisalignedbb = this.func_190607_a(this.func_191515_a(list));
            List<Entity> list1 = this.world.getEntitiesWithinAABBExcludingEntity((Entity)null, this.func_190610_a(axisalignedbb, enumfacing, d0).union(axisalignedbb));

            if (!list1.isEmpty())
            {
                boolean flag = this.pistonState.getBlock() == Blocks.SLIME_BLOCK;

                for (int i = 0; i < list1.size(); ++i)
                {
                    Entity entity = list1.get(i);

                    if (entity.getPushReaction() != EnumPushReaction.IGNORE)
                    {
                        if (flag)
                        {
                            switch (enumfacing.getAxis())
                            {
                                case X:
                                    entity.motionX = (double)enumfacing.getFrontOffsetX();
                                    break;

                                case Y:
                                    entity.motionY = (double)enumfacing.getFrontOffsetY();
                                    break;

                                case Z:
                                    entity.motionZ = (double)enumfacing.getFrontOffsetZ();
                            }
                        }

                        double d1 = 0.0D;

                        for (int j = 0; j < list.size(); ++j)
                        {
                            AxisAlignedBB axisalignedbb1 = this.func_190610_a(this.func_190607_a(list.get(j)), enumfacing, d0);
                            AxisAlignedBB axisalignedbb2 = entity.getEntityBoundingBox();

                            if (axisalignedbb1.intersectsWith(axisalignedbb2))
                            {
                                d1 = Math.max(d1, this.func_190612_a(axisalignedbb1, enumfacing, axisalignedbb2));

                                if (d1 >= d0)
                                {
                                    break;
                                }
                            }
                        }

                        if (d1 > 0.0D)
                        {
                            d1 = Math.min(d1, d0) + 0.01D;
                            field_190613_i.set(enumfacing);
                            entity.moveEntity(MoverType.PISTON, d1 * (double)enumfacing.getFrontOffsetX(), d1 * (double)enumfacing.getFrontOffsetY(), d1 * (double)enumfacing.getFrontOffsetZ());
                            field_190613_i.set(null);

                            if (!this.extending && this.shouldHeadBeRendered)
                            {
                                this.func_190605_a(entity, enumfacing, d0);
                            }

                            // Add this update to the entity's that are being pushed.
                            world.updateEntityWithOptionalForce(entity, false);
                        }
                    }
                }
            }
        }
    }```

### Comment 7: migrated (2018-01-08T11:02:49.115-0800)

While looking into the function "updateEntityWithOptionalForce" it might be worth noting a small optimization where the if boolean "forceUpdate" can be moved into the upper if check to improve entity optimization sightly.
From this

```if (!(entityIn instanceof EntityPlayer))
        {
            int i = MathHelper.floor(entityIn.posX);
            int j = MathHelper.floor(entityIn.posZ);
            int k = 32;

            if (forceUpdate && !this.isAreaLoaded(i - 32, 0, j - 32, i + 32, 0, j + 32, true))
            {
                return;
            }
        }```
To this

```if (forceUpdate && !(entityIn instanceof EntityPlayer))
        {
            int i = MathHelper.floor(entityIn.posX);
            int j = MathHelper.floor(entityIn.posZ);
            int k = 32;

            if (!this.isAreaLoaded(i - 32, 0, j - 32, i + 32, 0, j + 32, true))
            {
                return;
            }
        }```
The boolean can be done a few lines up as it is unnecessary to enter the upper if check when its going to skip the 2nd if check anyway.

### Comment 8: marcono1234 (2018-01-09T12:53:53.063-0800)

Would it make sense to rather directly update the chunk entity lists as soon as the position of an entity changes? Otherwise MC-89667 would remain unfixed and require a different solution.

### Comment 9: migrated (2018-05-15T23:11:24.544-0700)

if your having issues with /tp command go into the code and apply this fix needs an if statement around it though.
https://bugs.mojang.com/browse/MC-129685?focusedCommentId=452773&page=com.atlassian.jira.plugin.system.issuetabpanels:comment-tabpanel#comment-452773
I looked at your code and that code should be cleaned up there but, spawning the entity into the world has nothing to do with the /tp command issue the issue is the chunk isn't loaded and the entity ins't added to the chunk so it never saves.
Yes forceUpdate is a bit buggy based on what I seen the area isn't loaded and force update is true yet it still returns there is probably a reason for this though entities if the chunks are not loaded shouldn't be allowed to update depending on intent of coder and method. The proper solution is to load the chunk first if not loaded and add the entity to that chunk
I haven't debugged this enough perhaps it occurs in loaded chunks to but, the player keeps the chunks loaded and the entity isn't added to the chunk but, still saves. I don't know maybe it does add it to the chunk if it's loaded need more debugging.

### Comment 10: migrated (2018-05-15T23:26:10.240-0700)

"Would it make sense to rather directly update the chunk entity lists as soon as the position of an entity changes? Otherwise MC-89667 would remain unfixed and require a different solution."
Yes editing all the entity.setLocation/positions if chunk detected has been changed it would make sense to remove the entity from that chunk and add it to the new one. This would be more of a proper fix for everything. Then the entity selectors from the other issue mentioned here should work as well if not they should be able to easily wip up a fix
Could have sworn they made this bug fix a long time ago like in beta guess they must have reverted their code since jeb took over

### Comment 11: migrated (2018-05-15T23:52:37.698-0700)

Thanks for your input, just one thing:
All your edits get sent to us watchers into their emails, so each time you change anything in your post, we get notified via email, which is a bit too much if there's loads of edits
So far I (and all the others) have gotten 9 notifications from you on this bugpost, in the past 40 minutes.
I usually pre-write comments and let it sit for a few minutes or longer, think about it, to make sure I won't have to add or delete too much off it again, or if so, only once; but that's just a suggestion for you, maybe you didn't know about the notification thing

### Comment 12: Panda4994 (2018-05-16T11:52:09.325-0700)

This is a bit offtopic, but when editing this post, the links in it got removed.
It happens in Visual mode.
Reddit post.

### Comment 13: migrated (2018-05-16T13:53:35.973-0700)

interesting fact the entity never gets added to the chunk in the same tick even if the chunk is loaded so here is my fix for all the related issues for the new /tp doTeleport() Command:
https://gist.github.com/jredfox/86630098b66b6f43978c8e103fd4db02
You might ask well why provide chunk? If it's loaded it gets from cached if it's unloaded it helps fix the issue and regardless the entity isn't added to the chunk so the rest of the code forces it to do so.
I am going to say player transportation is also not handled correctly from world server chunk map if player loads to new chunks but, I don't know really how to fix it so I am going to let mojang make a EntityPlayer patch during the doTeleport() since updating the next tick isn't how it should be handled. It's unkown to me if player chunk map is for all players in all dimensions or just one dimension? That's why I am letting mojang fix the patch for players I fixed the regular entities though.
Note this doesn't support cross dimensional teleport if you want that you can take a look at CMDDim "/tpdim" for evil notch lib as it fully supports it. I can't take all the credit brandon's core order to do what helped out alot and fixed it up a bit. Note it's still wip for regular entities since I disagree with brandon's core on a couple hard coded things.

### Comment 14: migrated (2018-05-23T05:51:00.192-0700)

If they apply the fix above they should also fix the detection for wrong entity location since if an entity enters a new chunk at a certain location it will freak out and kill the entire mob stack saying wrong entity location. I am getting around to this by saying it's better that the vanilla bug of the mob not being there till next tick is better then the entire mob stack randomly dying when entering a new chunk.

### Comment 15: Panda4994 (2018-06-05T15:52:52.500-0700)

It's currently (1.13pre1) hard to confirm because the positioned commands fail to find the entity every time.
I also tried this with no success:

```execute positioned 0 100 0 run tp @e[tag=MC-108469,distance=10] 100 100 0```
There might be another bug here or I might just not see through the new command system.
So the way to reproduce needs fixing.

### Comment 16: Skylinerw (2018-06-05T16:10:44.096-0700)

With distance=10 you'll be looking for an entity that is only exactly 10 blocks away from the position, rather than anywhere between the position and 10 blocks. You'll have to specify a range, which uses ".." as the separator:

```execute positioned 0 100 0 run tp @e[tag=MC-108469,distance=..10] 100 0```
(where x..y would mean "between x and y", while no value in either position would mean absolute minimum/maximum).

### Comment 17: Panda4994 (2018-06-05T16:21:52.017-0700)

Thank you Mr. W
I already suspected that it was just some change I didn't know yet.
The commands in the post are updated to the new system now.

### Comment 18: migrated (2018-06-08T07:02:36.194-0700)

Things make so much more sense now.
I always assumed that this was MC-119971 alone.  But instead, there is an ugly interaction between these two bugs.  MC-119971 is the situation where a chunk is reloaded while it is in the midst of being zlib compressed before being saved to disk.  During that time, the chunk is not listed anywhere that the main thread can know about, so an old version gets loaded.  This results in deletions and duplications at chunk boundaries (blocks and entities being pushed by pistons, item deletion and duplication in hoppers).
But seeing , things make so much more sense.  I've seen it many times where a minecart gets inexplicably stuck at some point along a track, even on a powered rail.  I eventually found that if you break the block beneath the rail that seems to have an invisible boundary, another minecart will materialize and fall into the hole.
It seems like MC-119971 (fix available) is responsible for making the duplicate, while  is responsible for making the invisible one.

### Comment 19: migrated (2018-10-12T19:31:56.229-0700)

To add an alternative fix – I realized a patch I added in https://bugs.mojang.com/browse/MC-136995 requires a field CraftBukkit added, to retain if the entity is in the world or not, which I used to fix this bug in Paper:

```protected void onEntityAdded(Entity entityIn)
    {
        for (int i = 0; i < this.eventListeners.size(); ++i)
        {
            ((IWorldEventListener)this.eventListeners.get(i)).onEntityAdded(entityIn);
        }
        entityIn.valid = true;
    }

    protected void onEntityRemoved(Entity entityIn)
    {
        for (int i = 0; i < this.eventListeners.size(); ++i)
        {
            ((IWorldEventListener)this.eventListeners.get(i)).onEntityRemoved(entityIn);
        }
        entityIn.valid = false;
    }```
Then this code only needs a very minor change:

```if (!entityIn.valid && !entityIn.setPositionNonDirty() && !this.isChunkLoaded(l, j1, true)) // add valid check at start
            {
                entityIn.addedToChunk = false;
            }
            else
            {
                this.getChunkFromChunkCoords(l, j1).addEntity(entityIn); // If added to the world, it will always be added to the chunk
            }```

### Comment 20: migrated (2018-10-12T19:33:13.652-0700)

The downside to Xcom's fix is that dimension teleporting will trigger chunk loads to an unnecessary chunk as it first updates the position of the entity before snapshotting it to copy into the new dimension, and that would trigger the chunk to load.
however, the entity being removed from the world before its moved would set valid=false and then not load the chunk with my supplied version.

### Comment 21: migrated (2018-10-12T19:53:45.194-0700)

MC-98153 was already fixed in 13 though. The bug where entity's would pingpong using portals.

### Comment 22: migrated (2019-01-24T13:05:24.893-0800)

Confirmed for 19w04a, took me ages to figure out it was this bug that caused my system to fail

### Comment 23: Panda4994 (2019-03-24T02:28:23.437-0700)

The steps to reproduce only partially work in 19w12b due to MC-146470.
/say @e[tag=MC-108469]
This command will not be able to detect the entity now, but the warning message after reloading the world persists, and I was still able to delete the entity.
Since MC-146470 is likely to be fixed soon, I will not change the description.

### Comment 24: FaRo1 (2019-06-03T09:23:01.153-0700)

I cannot reproduce the second half of step 7, as  said, but also not step 8. But the armour stand is actually gone after all these steps. Are there new reliable reproduction steps for the commands part?

### Comment 25: Panda4994 (2019-11-22T17:18:55.472-0800)

I added new commands, however the entity selector based reproduction should be taken with a grain of salt, as it's highly dependant how entity selectors are optimized. So it might change between versions or even be affected by things like how many entities are loaded etc.
The warning on reloading has been consistently there and likely will keep working and thus should be the preferred reproduction.

### Comment 26: FaRo1 (2019-11-23T05:29:34.399-0800)

I can reproduce it with those commands in 1.15-pre1.

### Comment 27: pulpetti (2020-07-06T13:01:01.223-0700)

I can't seem to reproduce this in 1.16

### Comment 28: FaRo1 (2020-07-07T03:23:32.428-0700)

I also can't reproduce it in 20w27a. The armour stand is not loaded anymore after step 6, there is no warning in the log and none of the given commands find it, "/say @e" doesn't, either. When you teleport to it, it's still there. This also does not break the common commands trick to modify "Pos" of an entity and teleport a player to it.
Seems good to me!

### Comment 29: boq (2020-07-07T04:02:17.928-0700)

We did changes to improve situation, but it's probably not enough to fix that issue.
In 1.16 we've extended chunk handling to also work for entities in "border" chunks (as opposed to just "entity ticking"), since that's part of bug could be reproduced without commands (for example, with piston in block ticking border pushing entity over chunk boundary). However, I have no idea if that fixes issues with longer teleports to areas completely outside of loaded chunks.

### Comment 30: FaRo1 (2020-07-07T04:23:32.729-0700)

Would that mean that this bug cannot occur without (command) teleports or NBT changes anymore? That would at least check this off my "critical issues" list, because you can't just randomly lose entities in your Survival world anymore.
To be considered/tested: Portals, respawning, ender pearls, chorus fruit (incl. foxes), anti-cheat, endermen, shulkers, pets, minecarts (snapping to rails) and dragon eggs all have/cause some kind of instantaneous motion that might be considered "teleporting" in the context of this bug or might not.

### Comment 31: boq (2020-07-07T04:54:43.552-0700)

This bug could not be triggered by move that happened inside entity tick, which covers most of the categories (even things like being pushed by fluid). Only "external" moves (like pistons, because it happens during block tick or commands) caused that.

### Comment 32: migrated (2024-01-29T13:33:00.464-0800)

Since I am playing a long term world with version 1.16.5 my question is if this bug still affects this world in pure survival mode? Reading the history here, it looks like this is no longer the case since 1.16. Are there still constellations in pure survival mode where the bug still has an effect in 1.16.5? Unfortunately, the last comment from 07.07.2020 (Bartosz Bok) did not answer this very clearly for me.

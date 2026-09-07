# MC-170010: Sky-lightmaps not properly initialized

**Mojira URL:** [https://bugs.mojang.com/browse/MC-170010](https://bugs.mojang.com/browse/MC-170010)

## Report details

- **Mojira categories:** Lighting
- **Project:** MC
- **Issue key:** MC-170010
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-01-17T14:09:48.176-0800
- **Updated:** 2025-04-30T04:47:42.450-0700
- **Resolution date:** 2023-04-19T07:53:07.604-0700
- **Affects versions:** 1.15.1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w20b; 20w21a; 1.16.2; 21w08b; 1.17.1
- **Fix versions:** 23w16a
- **Labels:** mojang_internal_1
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2020-01-17_20.47.54.png; 2020-01-17_21.36.36.png; Lighting Bug 2.zip
- **Issue links:** Relates:outward:MC-148580:Server lighting still broken in 1.14 pre-4 | Relates:inward:MC-169498:Empty top subchunks don't update skylight in some cases

## Description

This is a direct continuation of MC-148580. I post it as a new report since the old one already contains several similar bugs and I don't want it to digress too much, given that it's already closed for quite a while now.
The issue remains the same, namely that the topmost lightmap is not correctly initialized to a light value of 15, but rather to a value of 0.
net.minecraft.world.chunk.light.SkyLightStorage.java

```
protected ChunkNibbleArray createLightArray(long pos) {
    ChunkNibbleArray chunkNibbleArray = (ChunkNibbleArray)this.lightArraysToAdd.get(pos);
    if (chunkNibbleArray != null) {
        return chunkNibbleArray;
    } else {
        long l = ChunkSectionPos.offset(pos, Direction.UP);
        int i = ((SkyLightStorage.Data)this.lightArrays).topArraySectionY.get(ChunkSectionPos.withZeroZ(pos));
        if (i != ((SkyLightStorage.Data)this.lightArrays).defaultTopArraySectionY && ChunkSectionPos.getY(l) < i) {
            ChunkNibbleArray chunkNibbleArray2;
            while((chunkNibbleArray2 = this.getLightArray(l, true)) == null) {
                l = ChunkSectionPos.offset(l, Direction.UP);
            }

            return new ChunkNibbleArray((new ColumnChunkNibbleArray(chunkNibbleArray2, 0)).asByteArray());
        } else {
            return new ChunkNibbleArray();
        }
    }
}
```
The lightmap will then be registered for relighting inside onLightArrayCreated(...) and finally be relighted in updateLightArrays(...). There are however some problems with this initialization code:
- If the subchunk is non-empty, light is only propagated from above, but not from the sides. There are cases where this is not sufficient. However, this issue is completely shadowed by the next one.

- The initialization is completely skipped if another lightmap is added above it.

I attached a world producing wrong lighting using this second problem. Since I lag the lighting engine to spawn mutible blocks at once before the lighting engine can react, the provided world might not reliably work on some systems, but at least it does reliably work on mine. Would be nice if someone can confirm this on their system.
The setup is as follows:
- We have some subchunk that does not have a lightmap and no lightmap above, but all its 4 neighbors do have one.

- Schedule a bunch of lightmap creations and light updates to lag the lighting engine, so we can spawn several blocks at once before the lighting engine can react to it. (This is similar to , but a fix for it will not help here.)

- Spawn a stone platform in the beforementioned subchunk.

- Now this subchunk will get a lightmap, which gets scheduled for initialization. However, afterwards the subchunk above it will get a lightmap as well, canceling the initialization again.
 In the end, the lightmap of the subchunk containing the stone platform will remain uninitialized.

- Since all its neighbors already had lightmaps, the initialization code does not spread light form there to the subchunk containing the stone platform, so light contributions from the side are missing.
 This is also the reason for the first problem I mentioned above regarding the initialization code. wouldn't it be shadowed by the second one.

- Since block updates schedule light checks not only for the affected blocks but also for all 6 neighbors, we do get a contribution from the blocks directly below the stone platform, but not from any other blocks.

- This produces the following image

There is another bug caused by the initialization code, namely MC-169498. The problem here is that upon removing a lightmap, the new topmost lightmap is scheduled for reinitialization. In case the corresponding subchunk is empty, initialization then sets the whole lightmap to 15 and spreads light to its neighbors. In the setup described in the bug, as soon as the stone block is broken, this will cause the subchunk it was in to be set to a lightvalue of 15. Note that also  plays a role here as it causes lightmaps to be removed before the block removal is properly processed; however, that doesn't really matter for the solution discussed below.
As always, the problem with this is that this initialization changes light values without informing everyone about it; in this case, the subchunk containing the sandstone blocks is not marked dirty and hence not rerendered. As can be seen, the lighting is actually correctly at a value of 15, but the subchunk is not rerendered and hence still shows the value of 14.

My suggested solution is the same as for MC-148580: Don't change light values by creating lightmaps, but initialize them to the exact values that would have been returned before. As no light values change, you don't have to inform anyone about any changes and you don't have to schedule any additional light and darkness propagations in order to compensate for changed values.
Concretely, this means to initialize topmost skylightmaps of already lighted  chunks with a value of 15 and not doing anything else. For not yet lighted chunks, simply initialize the lightmap with 0, as is currently done, and also do nothing else in this case (except potentially some actions required for initial lighting, see below).
This will get rid off both issues and in fact allows to remove some now obsolete code, reducing code complexity by quite a bit.

As far as I understand it, the current lightmap initialization code basically handles the initial skylight. So, let's look into that in more detail and see that my suggested solution doesn't interfere with this. In fact, it will allow to simplify and optimize the code a bit. In the following, I will assume MC-170012 to be fixed.
Starting with some definition, let's call all subchunks of a given chunk that do not have a lightmap above them (or associated directly to them) the empty region, and all subchunks that do not have a block above (or inside) them the pseudo-empty region; so the empty-region is that part of the pseudo-empty region that does not have associated lightmaps above (or directly associated to) them.
Before a chunk is lighted, it does not receive any direct skylight, ie. the empty region is completely dark.
The invariant we want to prove is:
- Before a chunk is lighted, it properly receives and propagates all skylight contributions from its neighbors, but its pseudo-empty region might be opaque to skylight. More precisely, the interior of every subchunk in the pseudo-empty region is transparent to skylight, but its faces (except the top face) might be opaque, whereas the top face is also transparent.

- Once a chunk is lighted, its pseudo-empty region is now properly transparent and has a skylight value of 15. All skylight is properly propagated to neighbors (except to their pseudo-empty regions which might be opaque).

During initial lighting, the topmost lightmap gets scheduled for initialization inside
net.minecraft.world.chunk.light.SkyLightStorage.java

```
protected void setLightEnabled(long l, boolean bl) {
    this.updateAll();
    if (bl && this.lightEnabled.add(l)) {
        int i = ((SkyLightStorage.Data)this.lightArrays).topArraySectionY.get(l);
        if (i != ((SkyLightStorage.Data)this.lightArrays).defaultTopArraySectionY) {
            long m = ChunkSectionPos.asLong(ChunkSectionPos.getX(l), i - 1, ChunkSectionPos.getZ(l));
            this.method_20810(m);
            this.checkForUpdates();
        }
    } else if (!bl) {
        this.lightEnabled.remove(l);
    }
}
```
The initialization then basically pushes skylight from above to the topmost lightmap and then propagates it, using some optimization in case the subchunk is empty as mentioned before (but that's not relevant here).
Now let's prove the invariant inductively.
- Since not yet lighted chunks do not receive direct skylight, skylight can only exist in a 3x3 neighborhood around lighted chunks. Assuming MC-170012 has been fixed, all relevant lightmaps have been created in that region. Hence, all skylight updates will be properly propagated, except for the case when they get stuck at the boundary to the empty region because of missing lightmaps. This case is however in accordance with our inductive hypothesis, so this is not a problem.

- When a chunk gets lighted, it already receives all contributions from neigbor chunks. The only remaining defects are that it does not yet receive direct skylight and the pseudo-empty region might be opaque. The beforementioned initialization code will now propagate direct skylight to the topmost blocks of the topmost lightmap, which will then propagate and light up the whole pseudo-empty region, setting it to a value of 15 and hence making it transparent to skylight.
 Hence, the chunk itself receives all skylight contributions after it has been lighted.

- The initialization code also pushes skylight from lightmaps in the pseudo-empty region, and more generally from everywhere except the empty region, to all neighbor chunks. We need to show that all lightmaps in the non-pseudo-empty region of a neighbor chunk properly receive their contributions, ie. that no lightmap in the non-pseudo-empty-region of a neighbor chunk is adjacent to the empty region of the chunk that is currently being lighted. However, this is clear, since a subchunk in the non-pseudo-empty region has a block above it by definition. This causes a lightmap to be created in the chunk that is currently being lighted that is above the lightmap in question, ie. the lightmap in question might be adjacent to the pseudo-empty region of the chunk that is currently being lighted, but not to the empty region, which is what we wanted to show.

Note that this argument never used the complicated initialization logic for lightmaps of already lighted chunks. All the relevant logic is carried out by the initialization code as scheduled by setLightEnabled(...). Hence, it is safe to simply initialize topmost lightmaps in already lighted chunks with a skylight value of 15, without causing any interference with the initial lighting code.

There might in fact be a missing point in the above argument, namely in case the pseudo-empty region of not yet lighted chunks can change over time. This would cause bugs already in the current version of the code and would need a fix independ of my suggested fix for the issue described here. I'm not familiar enough with the worldgen code to say whether or not this event is possible. For completeness, I will describe the issue more precisely and show that the current code would not deal with it.
Suppose we have a chunk that has a lighted neighbor, so it is sufficiently far through worldgen to have reached the pre_ligth stage (and hence probably shouldn't receive any worldgen block updates; but as I said, I am not sure about this) but is not yet lighted itself (and hence probably shouldn't receive any block changes caused by actual game ticks). Now suppose it is possible for this chunk to receive block updates, in particular, we may spawn a stone platform in the empty region. Now, the subchunk containing the stone platform and all subchunks below are pushed to the non-pseudo-empty region. This breaks our invariant because they must no longer be opaque.
The current initialization code manages to push in light from the side in case a new lightmap is spawned in the respective neighbor chunks. However, if the neighbor chunk already had a lightmap, the initialization code won't do anything and we are missing contributions from all sides. As the stone platform blocks light from above and there is no mechanism that will eventually push in light from the sides, this will indeed result in a presistent lighting error.
Fixing this is rather easy: When a subchunk in a pre_light ed but not yet light ed chunk turns non-empty, we need to pull in skylight from all sides for this subchunk and all subchunks below that were previously in the pseudo-empty region. Note that we actually don't need to pull in light from the top faces, as these were already transparent before, but we do need to pull in light from all bottom faces, which might have been opaque before.
As you can see, this fix is independent of lightmap initialization for already lighted chunks.
As I said, I can't say whether this is relevant or not.

I hope that my suggested fix is now sufficiently convincing
Finally, let's discuss some simplifications and optimizations that are now possible:
Since the (current) lightmap initialization code now solely deals with initial skylight, we can now properly move it to the rest of the initialization code, where it belongs, instead of being scattered around.
As lightmap initialization now indeed no longer changes any light values, we can remove those parts of the code that compensated for changes in light values. Concretely, that is the last part of updateLightArrays(...) that currently spreads darkness to the previous topmost lightmap
net.minecraft.world.chunk.light.SkyLightStorage.java

```
this.pendingSkylightUpdates.clear();
if (!this.field_15816.isEmpty()) {
    var4 = this.field_15816.iterator();

    label90:
	while(true) {
	    do {
		    do {
				if (!var4.hasNext()) {
			    	break label90;
			    }

			    l = (Long)var4.next();
		    } while(!this.field_15820.remove(l));
	    } while(!this.hasLight(l));

	    for(ag = 0; ag < 16; ++ag) {
		    for(j = 0; j < 16; ++j) {
		        long ai = BlockPos.asLong(ChunkSectionPos.getWorldCoord(ChunkSectionPos.getX(l)) + ag, ChunkSectionPos.getWorldCoord(ChunkSectionPos.getY(l)) + 16 - 1, ChunkSectionPos.getWorldCoord(ChunkSectionPos.getZ(l)) + j);
			    lightProvider.updateLevel(Long.MAX_VALUE, ai, 15, false);
		    }
	    }
	}
 }
```

Also, there is no need to relight the new topmost lightmap after removing a lightmap (in fact, that doesn't even seem to be necessary with the current code).
Removing those two pieces of code should already simplify the code by quite a bit and hence improve maintainability.
Now, diving into some small optimizations that may squeeze out a bit of performance:
- The optimization that empty subchunks are directly set to 15 and light is then manually spread to all sides, instead of letting the lighting engine propagate the light from the top face, can be applied to all lightmaps in the pseudo-empty region upon initial lighting, not only to the topmost lightmap.

- Currently, the code pushes light from the pseudo-empty region from the chunk that is being lighted to the pseudo-empty region of all neighbors. In particular, in practice the topmost lightmaps are often on the same y-level. This causes light to be spread to a lightmap that will later be overridden with a value of 15 anyway. While this is not drastically bad, it is easy to optimize. Simply extend the above optimization to skip propagations from lightmaps in the pseudo-empty region to the pseudo-empty region of (not yet lighted) neighbor chunks. This optimization will not interfere with our invariant above, as it says that the pseudo-empty region of not yet lighted chunks can be opaque.
 Also, note that we can safely skip propagations to the pseudo-empty region of lighted neighbors, as they already have a skylight value of 15. In conclusion this means that we can skip propagations from the pseudo-empty region to the pseudo-empty region of all neighbors.

Summary
- Both described bugs can simply be solved by initializing topmost skylight maps of already lighted chunks to a value of 15 and not doing anything else. This doesn't interfere with the initial lighting code.

- Lightmap initialization not changing values allows to get rid off some code that is currently needed to compensate for these changes. Hence the proposed solution will reduce code complexity.

- There might be some bug with the current initial lighting code, depending on whether or not there can be block changes for chunks between pre_light and light stage. You can probably judge better than me whether this is a problem or not

- Restricting the current lightmap initialization code solely to initial lighting allows moving it to a more fitting place and allows for some easy optimizations.

Hope this is helpful
Best,
PhiPro

## Comments (9)

### Comment 1: migrated (2020-01-17T14:09:48.176-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: PhiPro (2020-01-17T21:59:58.156-0800)

It turns out that the interaction between initial lighting and skylight optimization introduces some subtleties I didn't really deal with; basically "Hence, all skylight updates will be properly propagated" isn't completely true due to the interaction between skylight optimization and the fact that some subchunks might be partially opaque to skylight.
I will update that discussion once I figured things out completely.

Nevertheless, this doesn't really affect the general theme of the solution: Initialize lightmaps to the exact values that would have been returned before adding it and only schedule additional propagations as needed to fullfill the desired invariant for initial lighting. Don't mix lightmap initialization with initial lighting code and compensate the change in values with a bunch of other checks. That will only complicate the code and has a high probability that some check is missing.
For the moment, I would suggest to simply keep that part of the initialization logic that spreads light to neighbors (in fact, independent of whether the subchunk is empty or not), but properly initialize lightmaps inside createLightArray(...) and remove those parts of the logic that reinitalize lightmaps and spread darkness.

In order to figure out the correct way to deal with the interaction between initial lighting and skylight optimization, it would be quite helpful to know whether the event of a block change inside a chunk between pre_ligth and light stage as described above is possible or not

### Comment 3: PhiPro (2020-01-18T16:46:22.082-0800)

After looking through the code some more, I feel like it is indeed possible that there are block changes inside chunks between the pre_light and light stage. In particular, ProtoChunk.setBlockState(...) contains the clause

```if (this.status.isAtLeast(ChunkStatus.FEATURES) && state != blockState && (state.getOpacity(this, pos) != blockState.getOpacity(this, pos) || state.getLuminance() != blockState.getLuminance() || state.hasSidedTransparency() || blockState.hasSidedTransparency())) {
    LightingProvider lightingProvider = this.getLightingProvider();
    lightingProvider.checkBlock(pos);
}```
suggesting the possibility of block changes in those stages.
For what it's worth, I could only come up with one simple implementation that trivially works correctly (which I will present below). Everything else I tried causes problems in one way or another. The basic problem is that the skylight optimization is only aplpicable away from any non-air blocks, but that the empty region behaves necessarily as if it were opaque. This makes the skylight optimization inapplicable near the empty region of any not yet lighted chunk, as we don't necessarily have enough lightmaps around. Hence many applications of it during initial lighting are in fact not correct; however, simply turning off this optimization would cause problems as well, as we have to deal with missing lightmaps around the empty region in some way.
I can also cook up examples that break the current vanilla code and produce persistent errors, as long as block changes in those chunks are not forbidden. I also suspect some more issues than I currently found...
So, in summary, I think it's not at all straightforward to come up with some solution (other than the one I present below) that works in all edge cases. The current solution definitely does not, although those situations don't arise in practice with high probability.
If block changes were forbidden, the situation would be much simpler. In that case, we wouldn't really care about what happens in the pseudo-empty region, as it will be completely filled with skylight later on, anyway. So in this case we could simply state in the invariant that the pseudo-empty region does whatever it wants (as long as light is correctly propagated to the outside, perhaps). But as soon as the pseudo-empty region is allowed to change and light can decrease, things are really easy to mess up. Keeping any invariant always seems to require some repair mechanism.

On another note, there is currently also a problem when removing the topmost lightmap of the pseudo-empty region: When removing such a lightmap, light values will be overridden with 0. The reason for this change in light values is that we model the empty region as opaque, but do not properly react to this change in opacity. The result from this is that we now produce ghost light, in case there was any outgoing light from this lightmap before its removal. If later on some skylight is decreased, the lighting engine won't be able to properly track this through the missing light map and will produce persistent errors. So, currently we also should counteract this situation by spreading darkness when removing such a lightmap. However, this is not needed in the solution below.
Also, there is currently some mechanism in the code that prevents lightmaps from being completely erased before the chunk finishes its initial lighting. Readding a previously removed lightmap will simply restore its old values. I'm not really sure what the idea behind this is. My guess is that it should prevent lightmaps from being deleted between loading the chunk from disk and registering its non-empty subchunks. The problem with this is that this mechanism is only turned off once the initial lighting is done. So, if we readd some lightmap during initial lighting, some stale values will be restored instead of creating and initializing a new one. It is again easy to cook up examples, where this stale lightvalues will cause persistent lighting errors. So, I would suggest here to disable this mechanism as soon as the non-empty subchunks have been registered and not only after initial lighting.

So, let's now discuss my proposed solution for initial skylight. It is conceptually quite easy and avoids all this discussion about inapplicable skylight optimization and actions required upon adding and removing lightmaps. Currently, the main problem is that the empty region behaves as if it was filled with stone, causing all kinds of problems around it. To overcome this issue, we can simply push up this misbehaving region high up into the sky.
Basically, I want to model initial skylight simply as if there was a stone platform high up above the world and then use the normal lighting code. This will solve all these nasty issues.
Concretely, this means that we should forceload a lightmap in the void above the world in the pre_light stage together with all the regular lightmaps (as far as I can tell, lightmaps can currently be created 1 subchunk below and above the world bounds already) and make it receive all light contributions from all sides, but no direct skylight from above. This perfectly simulates the situation that there was a stone platform just above this lightmap. Preventing direct skylight contribution is already implemented, so there isn't really much to do here. The chunk now behaves as any other ordinary chunk, simply with a stone platform directly above it. Hence, as for any other chunk, there are no special actions required upon adding or removing lightmaps and skylight optimizations are now perfectly fine.
Initial lighting now takes the form of removing this imaginary stone platform. Concretely, this means that we should set all lightmaps in the pseudo-empty region to a value of 15 and spread light to everything adjacent to the pseudo-empty region, as is currently almost done (currently we only spread light to neighbors below the topmost lightmap, but we should in fact spread light for every y-level in the (pseudo)-empty region). Afterwards  we can then simply remove the forceloaded lightmap.
While this approach might be slightly less optimal due to the additional lightmap, I don't think that the difference will be really noticeable. Given the fact that it avoids all kinds of light checks upon adding and removing lightmaps, it might even pay off performance-wise.
Basically, this is the same solution as already presented in the original report, with the only difference being this forceloaded lightmap high up in the sky that solves all the nasty issues. So this keeps all the benefits listed above, primarily it allows to simply solve the bug originally addressed in this report by simply initializing lightmaps with the previous values at the respective positions and not doing any other action upon lightmap addition or removal. It also moves all of the initial lighting code to one place, instead of being scattered around, making the coder easier to understand and maintain.
I would suggest to implement this solution, mainly for its simplicity and correctness.

It would be cool to hear your opinions on this. In particular, I would be interested in what your idea was for the current initial lighting code. Maybe we can come up with some fancy more optimal and actually correct solution together
Best,
PhiPro

### Comment 4: PhiPro (2020-05-15T10:59:00.269-0700)

While implementing this fix as a fabric mod, i noticed that MC-170012 should ideally be fixed first, as it makes the handling of the forced lightmaps, as mentioned in the previous comment, a bit easier. The problem is that upon initial lighting we need those forced lightmaps to be present for the neighbors, which is currently not so nice because of MC-170012. Alternatively, instead of fixing that issue first, you can also explicitly force these lightmaps on the neighbors, but I think this will be the more cumbersome way to do things.

### Comment 5: PhiPro (2020-05-20T16:18:00.454-0700)

As a reference, I have implemented my suggested solution as a fabric mod. The code can be found at https://github.com/PhiPro95/mc-fixes/tree/mc-170010. While doing so, I noticed a few things that are worth documenting here. Also note that the code really isn't that long or complicated, although the use of mixins vs. direct source control sometimes makes things look more complicated than they actually are.
Observe that this also solves  as explained there.

First, as already noted in the last comment, it is convenient to fix MC-170012 first. This is done in https://github.com/PhiPro95/mc-fixes/tree/mc-170012. In my implementation I introduced a new pre_light generation stage and mirrored the state of the current  light stage, i.e., it requires chunks in the features stage within a margin of 1. This is due to the fact that ProtoChunk does not properly handle lightmaps, as noted in the code. So I didn't want to introduce problems by promoting chunks too early and hence mirrored the current light stage. Whether or not this margin can be removed or if the missing lightmap handling in ProtoChunk is in fact a bug requires some knowledge about the worldgen code that I don't have. So that decision is up to you.
Edit: Looking a bit more into the worldgen code it indeed looks like the missing lightmap handling is a bug. Once the missing lightmap handling is added and the blockligth version of MC-170012, as noted in the comment there, is fixed, this margin is no longer needed. This is done in the most recent version of my implementation.

Second, it turns out that the current data retainment mechanism, as mentioned in the report and comment above, has some more far reaching problems than I thought. It not only overrides lightmaps in certain rare situations, as mentioned above, but it can in fact lead to loss of data in surprisingly common situations. I will link the bug report to that once it is created.
As a consequence, I would ignore this lightmap retainment code for the moment and simply leave it as it is. Simply write the code as if the issue with the lightmap retainment code was solved. This doesn't cause any regression compared to the current vanilla code, any potential problems already exist within the current code.
The retainment code can then be fixed later. In fact, it may be even convenient to solve this issue here first, so that newly created lightmaps are always trivial in the appropriate sense. This would at least slightly help for the solution I have in mind, but more on that in the report for the data retainment issue.

Third, it turns out that the current code hides some problems of  in some rare cases. For example, consider the following situation:
- Create a new redstone-ready world

- /fill 0 96 0 15 96 15 minecraft:stone

- /fill 0 96 0 15 96 15 minecraft:air

This will already trigger part 1 of , but this is hidden by the current lightmap initialization code. With my proposed fix, this is no longer the case and these steps will produce some dark spots on the ground. However, the current code only helps in some edge cases and it's easy to find situations where it doesn't help. For example, modify the steps above by placing a block above the platform, e.g., /setblock 7 255 7 minecraft:glass. This will suffice to trigger the issue with the current vanilla code as well. So, I would say that this little regression is a fair compromise, given that it solves the rather severe performance issue of .
Nevertheless, I have also implemented a fix for this part of , which can be found at https://github.com/PhiPro95/mc-fixes/tree/mc-169913. While fixing the whole issue described there requires a bit of work, as the multithreading code needs to be rewritten, the first part of the issue, which is what we observe here and which is also the most common and severe part of the issue, can be fixed rather easily. As explained there, we must simply reorder operations on the main thread as follows:
- Schedule creation of lightmaps as necessary

- Change the block in the chunk

- Schedule all relevant light updates

- Schedule removal of lightmaps as necessary

and the lighting engine must move the lightmap removal to the POST_UPDATE phase, whereas lightmap creation needs to stay in PRE_UPDATE. However, there is a small problem with this, namely that earlier removals of lightmaps can override later creations, as they are carried out in a later stage.
This is solved by my proposed solution for the complete problem by cancelling operations properly, but this requires the rewrite of the multithreading code. Fortunately, we can easily work around this issue by scheduling an additional lightmap creation into the POST_UPDATE phase. This will eliminate any overrides and make sure that the final configuration of lightmaps is now indeed correct. However, as noted in the bugreport, this will not eliminate the problem of lightmaps being removed and recreated, causing data loss. But this situation shouldn't be that common in practice.
In summary, this easy solution for part 1 of  greatly improves the situation over the current vanilla code and eliminates any regression introduced by eliminating code that currently shadows these issues.

I hope these inputs assist you in implementing a fix for the issue.
Best,
PhiPro

### Comment 6: PhiPro (2020-06-08T15:07:33.496-0700)

I found another small bug impacting initial skylighting. I post it here since the report already kindof derailed into a discussion about initial lighting. Let me know if I should open a new bug report.
ChunkSkyLightProvider.recalculateLevel(long id, long excludedId, int maxLevel) contains some logic to calculate contributions from neighbors that don't have an associated lightmap, namely it looks up the light value by inherting it from the next lightmap above, as usual.
net.minecraft.world.chunk-light.ChunkSkyLightProvider.java

```protected int recalculateLevel(long id, long excludedId, int maxLevel) {
   ...
   } else if (direction != Direction.DOWN) {
   for(m = BlockPos.removeChunkSectionLocalY(m); !((SkyLightStorage)this.lightStorage).hasLight(n) && !((SkyLightStorage)this.lightStorage).isAboveTopmostLightArray(n); m = BlockPos.add(m, 0, 16, 0)) {
      n = ChunkSectionPos.offset(n, Direction.UP);
   }

   ChunkNibbleArray chunkNibbleArray4 = ((SkyLightStorage)this.lightStorage).getLightArray(n, true);
   if (m != excludedId) {
      int p;
      if (chunkNibbleArray4 != null) {
         p = this.getPropagatedLevel(m, id, this.getCurrentLevelFromArray(chunkNibbleArray4, m));
      } else {
         p = ((SkyLightStorage)this.lightStorage).isLightEnabled(n) ? 0 : 15;
      }
       if (i > p) {
         i = p;
      }
       if (i == 0) {
         return i;
      }
   }
   ...
}```

The problem now occurs if there is no such lightmap, i.e., the neighbor block is directly exposed to skylight, in which case it uses p = ((SkyLightStorage)this.lightStorage).isLightEnabled( n) ? 0 : 15;.
However, 0 is the skylight value of the neighbor (note that light values are inverted inside the lighting engine) but p should contain the propagated value, as is the case when chunkNibbleArray4 != null. Hence this should not be 0 but 1, as this case only deals with horizontal propagations.
Or even better it should be this.getPropagatedLevel(m, id, ((SkyLightStorage)this.lightStorage).isLightEnabled( n) ? 0 : 15).
This issue basically only affects intial skylight, as it can only occur if the block in question is directly exposed to skylight, which means that it will be completely bright anyways. However, before initial lighting this conclusion does not hold true.
This bug then makes the lighting model depend on the empty region which cuases problems when the empty region changes, similar to issues discussed above.

### Comment 7: migrated (2020-06-30T11:56:13.215-0700)

This bug still present in 1.16.1 or not?

### Comment 8: pulpetti (2020-08-12T07:55:15.324-0700)

In 1.16.2

### Comment 9: ampolive (2021-07-13T16:47:14.452-0700)

Can confirm in 1.17.1.

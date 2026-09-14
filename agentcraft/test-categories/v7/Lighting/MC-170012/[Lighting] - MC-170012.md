# MC-170012: Lightmaps are missing for initial skylight

**Mojira URL:** [https://bugs.mojang.com/browse/MC-170012](https://bugs.mojang.com/browse/MC-170012)

## Report details

- **Mojira categories:** Lighting
- **Project:** MC
- **Issue key:** MC-170012
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2020-01-17T15:34:39.074-0800
- **Updated:** 2025-04-30T04:51:28.215-0700
- **Resolution date:** 2023-04-12T01:35:27.861-0700
- **Affects versions:** 1.15.1; 1.15.2 Pre-release 2; 1.15.2; 20w06a; 20w20b; 20w21a; 1.16.2; 1.16.4; 20w48a; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w37a; 21w40a; 1.18; 1.19 Pre-release 3
- **Fix versions:** 23w16a
- **Labels:** mojang_internal_1
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** 2020-01-18_00.26.19.png; 2021-06-26_19.53.43.png
- **Issue links:** Relates:inward:MC-196725:Lightmaps get lost upon unloading chunks | Relates:inward:MC-196614:Queued lightmaps are ignored for skylight propagation and initialization | Relates:outward:MC-196542:Small cleanup for skylight propagation code

## Description

Upon initial lighting of a chunk, skylight (and blocklight which doesn't matter here) is directly propagated to all neighbors. However, those neighbors might not have their lightmaps set up correctly, yet.
Non-empty subchunks are only registered during initial lighting
net.minecraft.world.ServerLightingProvider.java

```
public CompletableFuture<Chunk> light(Chunk chunk, boolean bl) {
    ChunkPos chunkPos = chunk.getPos();
    chunk.setLightOn(false);
    this.enqueue(chunkPos.x, chunkPos.z, ServerLightingProvider.Stage.PRE_UPDATE, Util.debugRunnable(() -> {
        ChunkSection[] chunkSections = chunk.getSectionArray();

        for(int i = 0; i < 16; ++i) {
            ChunkSection chunkSection = chunkSections[i];
            if (!ChunkSection.isEmpty(chunkSection)) {
                super.updateSectionStatus(ChunkSectionPos.from(chunkPos, i), false);
            }
        }
        ...
```
This means that during initial lighting, neighbor chunks might have not yet registered their non-empty subchunks and hence lightmaps might not have been setup yet correctly.
This can cause skylight updates to get stuck at missing lightmaps. When later on the missing lightmaps get created during initial lighting of the neighbor chunks, those lightmaps will be initialized by copying down the skylight values from the lightmap above it. Hence, if such a subchunk contains any blocks but did not have a lightmap associated to it, the lightmap will now be initialized to wrong values, making the subchunk erroneously bright.
As a concrete example, I will use "erase cached data" in order to force a relighting and hence simulate initial skylight on a well controlled geometry.
- Create a new redstone-ready world

- /tp 500 56 0

- /fill 496 80 0 511 95 15 minecraft:stone hollow

- /setblock 487 119 7 minecraft:stone

- /tp @s 0 56 0 270 0

- Optimize world -> erase cached data

- Fly 500 blocks in +x direction and fly inside the stone cube using spectator mode

Fortunately, this issue is quite easy to solve. Simply move the registration of non-empty subchunks outside of the initial lighting to some earlier stage. Concretely, add some pre_light stage to worldgen that registers all non-empty subchunks and require all neighbors to have passed this stage before running initial lighting for a chunk.

Best,
PhiPro

## Comments (15)

### Comment 1: migrated (2020-01-17T15:34:39.074-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: PhiPro (2020-06-08T14:16:21.985-0700)

There is also a related issue for blocklight. As mentioned in the discussion of  ProtoChunk.setBlockState(...) schedules light checks for chunks that have passed the features generation stage, suggesting that such block updates are indeed possible. Looking at the worldgen code also suggests that this is possible since the features generation stage has access to an 8 chunk radius.
The problem is now that such a block change could place a light source and the scheduled light check would then propagate the light too early. In contrast to the original report about skylight, lightmaps do exist for the neighbors, since they will be created due to the placed blocklight source (well, not quite due to the second issue below). However, the lighting engine treats chunks before the features stage as opaque, so the light propagation can get stuck at the chunk boundary nevertheless. So the end-result is similar to the original report, namely that light propagation can get stuck if carried out too early, i.e., before the neighbors are ready, altough the underlying cause is slightly different in this case.
Note that this version for blocklight cannot be as easily visualised by relighting the world using erase cached data as it relies on blocks being placed between the features and light generation stage.
The fix for this is again quite easy. Just let the lighting engine check if a chunk already has its initial lighting done, and otherwise ignore the luminance of a block for light calculations. This way, blocks don't emit light by themselves before the initial lighting and are properly turned on during initial lighting, similar to my proposed solution for initial skylight in .
Note that you cannot simply remove the light checks that cause the early propagation. Initial lighting spreads light too all neighbors, which are only guaranteed to be in pre_light stage at that point. Any block changes thereafter need to schedule light checks as otherwise you can have missing or ghost-contributions to those neighbors. When later on those neighbors are Initially lighted they will not be completely relighted but only add their own blocklight-sources. So, you need any lighting information to stay consistent after the pre_light stage and hence you need these light checks.
Also note that you should not fix this bug by not treating chunks before the features stage as opaque. Leaving in the early propagation of blocklight would then cause light propagations into chunks before the features stage and hence the above discussion would also apply to those, so you would need to schedule light checks before the features stage as well. However, for performance reasons this is not desired.

There is another issue related to block changes after the features stage. ProtoChunk only schedules light checks upon block changes (for chunks after the features stage). but it does not handle lightmap creation and removal. Concretely, it misses the calls to LightingView.updateSectionStatus(BlockPos pos, boolean status) that are present in WorldChunk and World. In view of  lightmap creation schould be scheduled before the block change and lightmap removal should be scheduled after the light checks.

Let me know if I should post these as separate bug reports.

### Comment 3: pulpetti (2020-08-12T08:22:26.096-0700)

In 1.16.2

### Comment 4: PhiPro (2020-09-03T03:32:35.437-0700)

There is another related issue regarding chunks before the light stage. Upon loading from disk, lightmaps are only loaded for chunks that were already lighted and discarded otherwise, although they are always saved to disk.
net.minecraft.world.ChunkSerializer.java

```public static ProtoChunk deserialize(...) {
    ...
    boolean bl = compoundTag.getBoolean("isLightOn");
    ...
    if (bl) {
        if (compoundTag2.contains("BlockLight", 7)) {
           lightingProvider.enqueueSectionData(LightType.BLOCK, ChunkSectionPos.from(pos, k), new ChunkNibbleArray(compoundTag2.getByteArray("BlockLight")), true);
        }

        if (bl2 && compoundTag2.contains("SkyLight", 7)) {
           lightingProvider.enqueueSectionData(LightType.SKY, ChunkSectionPos.from(pos, k), new ChunkNibbleArray(compoundTag2.getByteArray("SkyLight")), true);
        }
    }
    ...
}```

This basically erases any light propagations to chunks in pre_light stage when unloading them before the light stage and hence causes lighting glitches.

The Vanilla code currently uses this mechanism to erase cached data, which only removes the isLightOn field but not the lightmaps themselves.

### Comment 5: SunCat (2020-09-10T03:51:25.969-0700)

Please create a new ticket

### Comment 6: SunCat (2020-09-10T13:54:09.788-0700)

Actually both comments should have separate tickets

### Comment 7: PhiPro (2020-09-10T14:35:37.793-0700)

I posted the second comment as .
I would prefer to leave the first comment as is. It is more of a theoretical input and the glitches caused by it would be rather sporadic, so a reproducible setup is very hard to find. So I think for the moment it fits best here, as it falls under the general issue that pre_light (or features) and light stage aren't properly distinguished.
In case this report gets marked as fixed without fixing the comment, I will repost it as separate report.

### Comment 8: migrated (2020-12-01T04:55:40.393-0800)

In 1.16.3, 1.16.4 and 20w48a. Could reproduce the issue in all three of these versions.

### Comment 9: ampolive (2021-06-26T15:55:01.271-0700)

Can confirm in 1.17 and 1.17.1 Pre-release 1.

### Comment 10: ampolive (2021-06-30T09:51:46.547-0700)

Can confirm in 1.17.1 Pre-release 3.

### Comment 11: ampolive (2021-07-05T12:22:17.624-0700)

Can confirm in 1.17.1 Release Candidate 2.

### Comment 12: ampolive (2021-07-11T10:08:49.202-0700)

Can confirm in 1.17.1.

### Comment 13: ampolive (2021-09-17T08:01:14.413-0700)

Can confirm in 21w37a.

### Comment 14: ampolive (2021-10-10T08:38:58.772-0700)

Can confirm in 21w40a.

### Comment 15: ampolive (2021-12-06T05:24:42.013-0800)

The relevant code is in lightChunk(...) in net.minecraft.server.level.ThreadedLevelLightEngine.java using Mojang mappings.

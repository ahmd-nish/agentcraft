# MC-263340: Incorrect Protochunk#setStatus call on chunk generate

**Mojira URL:** [https://bugs.mojang.com/browse/MC-263340](https://bugs.mojang.com/browse/MC-263340)

## Report details

- **Mojira categories:** Chunk loading
- **Project:** MC
- **Issue key:** MC-263340
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2023-06-08T21:08:44.016-0700
- **Updated:** 2025-03-25T13:08:48.797-0700
- **Resolution date:** 2023-06-10T12:40:51.366-0700
- **Affects versions:** 1.20
- **Fix versions:** 1.20.1 Release Candidate 1
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 0

## Description

In 1.20, the ChunkStatus#generate method is implemented differently from in 1.19.4. It seems like there is a mistake with using the incorrect ChunkAccess when setting the status on a chunk being upgraded in the new implementation. While this is an issue with all chunk statuses, it's most relevant for the FULL status as it replaces the ChunkAccess when doing it's work.

Here is ChunkStatus#generate in 1.20:

```
public CompletableFuture<Either<ChunkAccess, ChunkHolder.ChunkLoadingFailure>> generate(Executor $$0, ServerLevel $$1, ChunkGenerator $$2, StructureTemplateManager $$3, ThreadedLevelLightEngine $$4, Function<ChunkAccess, CompletableFuture<Either<ChunkAccess, ChunkHolder.ChunkLoadingFailure>>> $$5, List<ChunkAccess> $$6) {
    ChunkAccess $$7 = $$6.get($$6.size() / 2);
    ProfiledDuration $$8 = JvmProfiler.INSTANCE.onChunkGenerate($$7.getPos(), $$1.dimension(), this.toString());
    return this.generationTask.doWork(this, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7).thenApply(($$2x) -> {
        if ($$7 instanceof ProtoChunk) {
            ProtoChunk $$3x = (ProtoChunk)$$7;
            if (!$$3x.getStatus().isOrAfter(this)) {
                $$3x.setStatus(this);
            }
        }

        if ($$8 != null) {
            $$8.finish();
        }

        return $$2x;
    });
}
```
We can see the $$7 ChunkAccess has it's status set, however we should be setting the status on the chunk wrapped by the result either $$2x (if present). This is because in the case of full chunks, doWork will replace the ChunkAccess, meaning the list retrieved before doing work, and the chunk gotten from it, are no longer up to date.

I noticed this issue when I saw that the visible chunk map in 1.20 contained non-imposter ProtoChunks that had a FULL status, which never happened in previous versions.

Switching the use of $$7/$$3x to $$2x with the following mixin resolved the issue:

```
@Mixin(ChunkStatus.class)
public class ChunkStatusMixin {
    @Shadow @Final private ChunkStatus.GenerationTask generationTask;

    /**
     * @author
     * @reason
     */
    @Overwrite
    public CompletableFuture<Either<ChunkAccess, ChunkHolder.ChunkLoadingFailure>> generate(Executor $$0, ServerLevel $$1, ChunkGenerator $$2, StructureTemplateManager $$3, ThreadedLevelLightEngine $$4, Function<ChunkAccess, CompletableFuture<Either<ChunkAccess, ChunkHolder.ChunkLoadingFailure>>> $$5, List<ChunkAccess> $$6) {
        ChunkAccess $$7 = $$6.get($$6.size() / 2);
        ProfiledDuration $$8 = JvmProfiler.INSTANCE.onChunkGenerate($$7.getPos(), $$1.dimension(), this.toString());
        return this.generationTask.doWork((ChunkStatus) (Object) this, $$0, $$1, $$2, $$3, $$4, $$5, $$6, $$7).thenApply(($$2x) -> {
            // Use result instead of chunk from list computed before doing work.
            $$2x.ifLeft(chunkAccess -> {
                if (chunkAccess instanceof ProtoChunk protoChunk) {
                    if (!protoChunk.getStatus().isOrAfter((ChunkStatus) (Object) this)) {
                        protoChunk.setStatus((ChunkStatus) (Object) this);
                    }
                }
            });

            if ($$8 != null) {
                $$8.finish();
            }

            return $$2x;
        });
    }
}
```

## Comments (4)

### Comment 1: gegy (2023-06-09T02:51:09.181-0700)

Hi! Thank you for making this report! I looked into this, and as far as I can tell, the only area this affects seems to be chunk saving - specifically, a chunk may be saved as a ProtoChunk with FULL status before actually getting upgraded to a LevelChunk. That's definitely not great, as entities can get lost and post-processing is missed. Other chunks never write into these misidentified chunks given the dependency order.
Are there any other ways that you are aware of that this issue manifests, besides the saving issue? Thanks again!

### Comment 2: migrated (2023-06-09T08:48:41.142-0700)

Does this bug affect new world generation, or only upgrading existing chunks?

### Comment 3: migrated (2023-06-10T12:08:37.971-0700)

idk how you got the code

### Comment 4: migrated (2023-06-10T12:40:51.366-0700)

By extracting it, putting it through a decompiler with the mojang mapping, and reading the result.

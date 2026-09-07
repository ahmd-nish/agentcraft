# MC-275445: Specifying the size of a target in post effect shaders fails

**Mojira URL:** [https://bugs.mojang.com/browse/MC-275445](https://bugs.mojang.com/browse/MC-275445)

## Report details

- **Mojira categories:** Rendering; Resource Packs
- **Project:** MC
- **Issue key:** MC-275445
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-08-16T11:12:48.106-0700
- **Updated:** 2025-04-26T16:15:06.838-0700
- **Resolution date:** 2024-09-02T01:16:55.886-0700
- **Affects versions:** 24w33a; 24w34a
- **Fix versions:** 24w36a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** deobf_latest.log; latest.log; MC-275445-resource-pack.zip

## Description

As of 24w33a, the "targets" field of post shaders is an object, instead of an array of objects/strings. It works correctly when the name of the target is mapped to an empty object. However having the object contain fields "width" and "height" fails to load the shader file.
Steps to Reproduce:
- Create a resource pack in version 24w34a (pack format 36)

- Copy the vanilla file assets/minecraft/post_effect/transparency.json

- In the "targets" field, write

```
{
        "final": {},
        "potato": {
            "width": 16, "height": 16
        }
}
```

- Load the resource pack with fabulous graphics

Observed Results:
The resource pack fails loading, and the game logs raise this error:
[^deobf_latest.log]

```
Failed to parse post chain at minecraft:post_effect/transparency.json
com.google.gson.JsonSyntaxException: Both alternatives read successfully, can not pick the correct one; first: (Left[b[]], {"width":16,"height":16}) second: (Right[a[width=16, height=16]], {"width":16,"height":16}) missed input: {"potato":{"width":16,"height":16}}
	at com.mojang.serialization.DataResult$Error.getOrThrow(DataResult.java:287)
	at ghx.b(SourceFile:145)
	at ghx.a(SourceFile:80)
	at ghx.b(SourceFile:36)
	at auz.a(SourceFile:11)
	at java.base/java.util.concurrent.CompletableFuture$AsyncSupply.run(CompletableFuture.java:1768)
	at java.base/java.util.concurrent.CompletableFuture$AsyncSupply.exec(CompletableFuture.java:1760)
	at java.base/java.util.concurrent.ForkJoinTask.doExec(ForkJoinTask.java:387)
	at java.base/java.util.concurrent.ForkJoinPool$WorkQueue.topLevelExec(ForkJoinPool.java:1312)
	at java.base/java.util.concurrent.ForkJoinPool.scan(ForkJoinPool.java:1843)
	at java.base/java.util.concurrent.ForkJoinPool.runWorker(ForkJoinPool.java:1808)
	at java.base/java.util.concurrent.ForkJoinWorkerThread.run(ForkJoinWorkerThread.java:188)
```
Expected Results:
Since this is the vanilla file, in which we specified an unused target (the same as the example from the article, the game should not output an error.
Notes:
From what I understood reading the output logs, it seems the json interpreter struggles with the new syntax...
Attachment
The joined zip file is a resource packs, for 24w34a.It modifies the

```
assets/minecraft/post_effect/transparency.json
```
, specifically adding a target in the post effect shader. I made sure to use the same syntax as in the snapshot article to demonstrate the bug.

## Comments (5)

### Comment 1: migrated (2024-08-16T11:12:48.106-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: [Mod] turbo (2024-08-18T10:31:22.012-0700)

We do not have enough information to reproduce this issue.
Please attach any needed commands, datapacks, resourcepacks, screenshots, videos, or worlds needed to help reproduce this issue.
Refer to the Bug Tracker Guidelines for more information about how to write helpful bug reports. Bug reports with insufficient information may be closed as Incomplete.
This issue is being temporarily resolved as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support (Technical Issues) – 📧 Microsoft Support (Account Issues)
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: JulienStudio (2024-08-18T13:08:14.031-0700)

Sorry for the inconvenience, I sent a zip file containing 2 resource packs, one that works in 1.21 and the bugged one for 24w33a. Tell me if you need anything else !

### Comment 4: Jarl-Penguin (2024-08-22T03:02:07.202-0700)

I could not reproduce this in 24w34a, is this still an issue?
This issue is being temporarily resolved as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support (Technical Issues) – 📧 Microsoft Support (Account Issues)
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 5: JulienStudio (2024-08-22T09:55:11.754-0700)

I updated the bug report to 24w34a.

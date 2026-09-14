# MC-251773: The --dev argument for the data generators no longer converts NBT to SNBT properly

**Mojira URL:** [https://bugs.mojang.com/browse/MC-251773](https://bugs.mojang.com/browse/MC-251773)

## Report details

- **Mojira categories:** Dedicated Server
- **Project:** MC
- **Issue key:** MC-251773
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-05-15T14:15:05.771-0700
- **Updated:** 2025-04-16T13:03:04.394-0700
- **Resolution date:** 2022-09-03T20:26:36.980-0700
- **Affects versions:** 22w19a
- **Fix versions:** 1.19 Pre-release 1
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** fat_tower_base.nbt
- **Issue links:** Blocks:outward:MC-131740:Re-running the data generator in the same folder causes previously generated -reports and- .snbt files to be deleted

## Description

Steps to reproduce:
- Download the below nbt file. (An end city structure template file.)

- Download the 22w19a server jar from this link.

- Put both of them in the same folder.

- Run the data generator using the below command:

```
java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --dev --input <path>
```
...where <path> is the folder in which you placed the nbt file.
You should see the following log:

```
Starting net.minecraft.data.Main
[16:09:26] [ServerMain/INFO]: Building unoptimized datafixer
[16:09:26] [ServerMain/INFO]: Starting provider: NBT to SNBT
[16:09:27] [ServerMain/INFO]: Converted fat_tower_base from NBT to SNBT
[16:09:27] [ServerMain/INFO]: NBT to SNBT finished after 49 ms
[16:09:27] [ServerMain/INFO]: All providers took: 50 ms
[16:09:27] [ServerMain/INFO]: Caching: total files: 1, old count: 0, new count: 1, removed stale: 1, written: 0
```
If you check the generated folder, nothing but the cache file will be there, instead of the snbt version of fat_tower_base and the cache.
The last line,

```
[16:09:27] [ServerMain/INFO]: Caching: total files: 1, old count: 0, new count: 1, removed stale: 1, written: 0
```
Did not exist before 1.19 snapshots, and I suspect that the

```
removed stale:
```
 portion has something to do with this.

## Comments (2)

### Comment 1: migrated (2022-05-15T14:15:05.771-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: tryashtar (2022-05-16T15:02:48.467-0700)

Confirmed, also this started in 22w15a; 22w14a works fine

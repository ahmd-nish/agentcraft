# MC-266968: /return executed within an advancement reward function globally discards all subsequent commands

**Mojira URL:** [https://bugs.mojang.com/browse/MC-266968](https://bugs.mojang.com/browse/MC-266968)

## Report details

- **Mojira categories:** Advancements; Commands; Data Packs
- **Project:** MC
- **Issue key:** MC-266968
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2023-11-24T00:11:08.943-0800
- **Updated:** 2025-03-07T21:35:42.279-0800
- **Resolution date:** 2023-11-28T05:13:12.237-0800
- **Affects versions:** 1.20.3 Pre-Release 2
- **Fix versions:** 1.20.3 Pre-Release 4
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** mc-266968.zip

## Description

The bug
When /return is executed within an advancement reward function, it will discard all subsequent commands globally, not just the local commands that the function has.
How to reproduce
- Install the data pack in Attachments

- Run

```
/function mc-266968:a
```

Results
The following table shows whether each message was expected to be printed or not, and whether it was actually printed or not.
Message
Expected
Actual

a-1
Yes
Yes

a-2
Yes
No

b-1
Yes
Yes

b-2
No
No

As the table suggests, say a-2 in mc-266968:a was not executed because it was discarded by return 0 in mc-266968:b.
Resources
data/mc-266968/functions/a.mcfunction

```
say a-1
advancement grant @s only mc-266968:b
say a-2
```
data/mc-266968/functions/b.mcfunction

```
advancement revoke @s only mc-266968:b
say b-1
return 0
say b-2
```
data/mc-266968/advancements/b.json

```
{
  "criteria": {
    "": {
      "trigger": "impossible"
    }
  },
  "rewards": {
    "function": "mc-266968:b"
  }
}
```
Code analysis
An advancement reward function is executed as an initial function, which has a frame with depth 0, regardless of the current depth. Because /return discards all command queue entries above the depth of the currently executed function, /return executed in an advancement reward function discards all entries, which have a depth >= 0.

## Comments (1)

### Comment 1: migrated (2023-11-24T00:11:08.943-0800)

This comment contained an image attachment, please login to view the attachment.

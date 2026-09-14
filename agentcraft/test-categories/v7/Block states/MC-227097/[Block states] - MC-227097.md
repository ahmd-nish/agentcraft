# MC-227097: End portals delete blocks that are inside of the portal

**Mojira URL:** [https://bugs.mojang.com/browse/MC-227097](https://bugs.mojang.com/browse/MC-227097)

## Report details

- **Mojira categories:** Block states
- **Project:** MC
- **Issue key:** MC-227097
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2021-06-01T15:50:58.471-0700
- **Updated:** 2025-04-26T13:26:19.567-0700
- **Resolution date:** 2025-01-15T08:45:33.921-0800
- **Affects versions:** 1.17 Pre-release 3; 1.17 Pre-release 4; 1.17 Pre-release 5; 1.17 Release Candidate 1; 1.17; 1.17.1 Pre-release 1; 1.17.1 Pre-release 2; 1.17.1 Release Candidate 1; 1.17.1; 21w37a; 21w38a; 1.18.1; 1.19.1 Pre-release 5; 1.19.1; 1.19.2; 1.19.3; 1.19.4 Pre-release 2; 1.21 Pre-Release 1
- **Fix versions:** 25w03a
- **Labels:** end-portal
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** End portal deletes blocks.mp4
- **Issue links:** Relates:outward:MC-273945:Unlike end portals, nether portals do not drop replaced blocks, which can result in major item loss

## Description

When you place blocks inside of an end portal, then light the portal, the blocks get deleted. They don't even drop anything, so the block is gone forever.
What I expected to happen was:
- The blocks will drop when the end portal opens

What actually happened was:
- The blocks get deleted and don't drop anything

Steps to reproduce:
- Build an end portal but don't put in the eyes

- Place blocks in the middle of the end portal

- Put in the eyes; the blocks will get deleted

- Go through the portal

Notice that the blocks got deleted, but they did not drop anything
Fix suggestions:
- Easy fix: Make it so the blocks drop when destroyed by the end portal

- Hard fix: Make it so the portal will not open until there is nothing in the way

## Comments (13)

### Comment 1: migrated (2021-06-01T15:50:58.471-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: migrated (2021-06-01T20:50:45.635-0700)

In the video it says in the command log doTilesDrops is set to false which means blocks will not drop itself. Therefor this is an intended game mechanic.

### Comment 3: migrated (2021-06-01T21:22:37.954-0700)

This is a invallid post for the reasons that Dylan Peterson says.

### Comment 4: migrated (2021-06-02T11:07:42.301-0700)

I meant to set it to true in the video, to prove that it is on, but I accidentally set it to false instead, and I didn't notice.
I have attached a new video, to not have the attached video contradict the bug report

### Comment 5: ampolive (2021-08-01T19:09:14.389-0700)

Can confirm.

### Comment 6: ampolive (2021-09-21T10:57:53.644-0700)

Can confirm in 21w37a.

### Comment 7: Avoma (2021-12-10T12:25:50.823-0800)

Can confirm in 1.18.1.

### Comment 8: [Mod] EVGENSYPERPRO (2022-06-11T11:21:24.118-0700)

Relates to MC-95910

### Comment 9: Avoma (2022-07-31T08:22:25.217-0700)

Can confirm in 1.19.1.

### Comment 10: Avoma (2022-10-05T11:57:17.208-0700)

Can confirm in 1.19.2.

### Comment 11: muzikbike (2024-05-31T03:18:03.190-0700)

Still affects 1.21 pre-release 1, despite this version fixing MC-902.

### Comment 12: muzikbike (2025-01-15T07:50:52.566-0800)

This appears to be fixed in 25w03a. Can someone verify that this is the fix version?

### Comment 13: muzikbike (2025-01-15T08:24:48.361-0800)

According to https://cdn.skye.lol/diffs/25w02a_to_25w03a.html this was indeed fixed in 3a.

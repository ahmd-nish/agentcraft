# MC-306328: Using golden dandelions to unlock aging forcibly removes persistence of baby animals

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306328](https://bugs.mojang.com/browse/MC-306328)

## Report details

- **Mojira categories:** Mob behaviour; Mob spawning
- **Project:** MC
- **Issue key:** MC-306328
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2026-02-11T10:05:03.677-0800
- **Updated:** 2026-03-13T01:41:55.496-0700
- **Resolution date:** 2026-03-13T01:41:55.432-0700
- **Affects versions:** 26.1 Snapshot 7; 26.1 Snapshot 9; 26.1 Snapshot 10
- **Fix versions:** 26.1 Pre-Release 2
- **Area:** Expansion A
- **Votes:** 2
- **Watchers:** 2
- **Attachments:** 1
- **Attachment filenames:** 2026-02-13 21-36-23.mp4

## Description

Using a Golden Dandelion on a baby animal that is age locked in order to remove the age lock will also remove its persistence, even if the animal should remain persistent due to other factors. (most notably, having a name tag applied to it)
This is caused by the method setAgeLocked in the AgeableMob class calling mob.setPersistenceRequired while only taking into account the age locking itself, and not other factors that should result in persistence.
Steps to reproduce:
- Spawn, summon, or encounter a baby animal

- Use the /data get entity command to verify that its AgeLocked value is 0b, and its PersistenceRequired value is also 0b

- Use a named Name Tag item to apply a name to the mob

- Use the /data get entity command to verify that its PersistenceRequired value has now become 1b, as expected, indicating the mob will no longer despawn

- Use a Golden Dandelion item to lock the baby’s aging

- Use the /data get entity command to verify that its AgeLocked value has now become 1b, as expected

- Use a second Golden Dandelion item to unlock the baby’s aging

Expected Result:
- Using the /data get entity command, you’ll see its AgeLocked value has returned to 0b as expected, and its PersistenceRequired value has remained 1b due to the baby having a name tag applied, preventing it from despawning

Actual Result:
- Using the /data get entity command, you’ll see its AgeLocked value has returned to 0b as expected, however its PersistenceRequired value has also become 0b, meaning the baby can despawn again despite still having a name tag applied

## Comments (6)

### Comment 1: kyleisNOTmyname (2026-02-13T18:44:19.324-0800)

Can confirm as of 26.1-snapshot-7.

It removes the PersistenceRequired when the golden dandelion is unapplied.
This includes special name tags like Toast, jeb_, Grumm and Dinnerbone.
I applied/removed it to/from a squid towards the end of this video and it caused the squid to despawn despite being named via a nametag.
The cows are showcasing the issue via the data get command.

### Comment 2: [MOD] Greymagic27 (2026-02-15T05:56:41.753-0800)

Thank you for your report!
We're tracking this issue in https://report.bugs.mojang.com/servicedesk/customer/portal/2/MC-306097 , so this ticket is being resolved and linked as a duplicate.
That ticket has already been resolved as Fixed. Please check the Fix Version/s field in that ticket to see in which version this behavior was or will be fixed.
If you haven't already, you might like to make use of the search feature to see if the issue has already been mentioned.
Quick Links:
📓 Bug Tracker Guidelines -- 💬 Community Support -- 📧 Mojang Support (Technical Issues) -- 📧 Microsoft Support (Account Issues) -- 📓 Project Summary -- ✍️ Feedback and Suggestions -- 📖 Game Wiki

### Comment 3: shnupbups100 (2026-02-15T09:06:44.641-0800)

This is a separate issue, brought upon by the ‘fix’ to that issue. NOT a duplicate. Please reopen.

### Comment 4: kyleisNOTmyname (2026-02-15T23:21:55.502-0800)

Can confirm that this is a separate issue.
MC-306097 is referring to mobs not being persistent after being given a golden dandelion, which was fixed, whereas this is stating that mobs that are persistent beforehand get their persistence removed upon giving them the dandelion for the second time.
This removes persistence from mobs that should still have it (such as a name tagged mob which was shown in  the video I attached.)

### Comment 5: kyleisNOTmyname (2026-02-17T18:42:47.583-0800)

Still an issue in 26.1-snapshot-8

### Comment 6: kyleisNOTmyname (2026-02-25T11:01:36.940-0800)

Still an issue in 26.1-snapshot-10

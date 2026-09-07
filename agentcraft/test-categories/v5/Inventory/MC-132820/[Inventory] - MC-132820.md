# MC-132820: Spawner isn't in the creative inventory

**Mojira URL:** [https://bugs.mojang.com/browse/MC-132820](https://bugs.mojang.com/browse/MC-132820)

## Report details

- **Mojira categories:** Inventory
- **Project:** MC
- **Issue key:** MC-132820
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2018-07-05T11:43:19.788-0700
- **Updated:** 2025-04-30T06:35:09.098-0700
- **Resolution date:** 2022-10-26T06:31:26.727-0700
- **Affects versions:** Minecraft 16w50a; Minecraft 1.13-pre6; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 5; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.2 Pre-release 2; 1.16.2 Pre-release 3; 1.16.2 Release Candidate 1; 1.16.2 Release Candidate 2; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 20w46a; 20w48a; 21w03a; 1.16.5; 21w07a; 21w08b; 21w14a; 21w15a; 1.17; 1.17.1; 21w39a; 21w42a; 1.18 Pre-release 1; 1.18.1; 1.18.2; 22w11a; 1.19; 1.19.1 Pre-release 1; 1.19.1 Release Candidate 1; 1.19.1 Pre-release 5; 1.19.2; 22w42a
- **Fix versions:** 22w43a
- **Game mode:** Creative
- **Labels:** creative-inventory-contents; vanilla-parity
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 2018-07-05_20.40.01.png; 2021-05-07_09.48.04.png; MC-132820.mp4; MC-132820.png

## Description

For a comprehensive list of other examples of issues with item positions in the Creative inventory, click here.
The bug
The spawner is completely absent from the Creative inventory for some reason. It would be expected it would be there, as it isn't a very technical block like barriers or command blocks which have been intentionally kept out of the Creative inventory.
This is also a parity issue, as the spawner does appear in Bedrock Edition's creative inventory. The fact that it exists in the Creative inventory in Bedrock Edition may be due to some behavioural differences; placed spawners are empty by default in Bedrock Edition, but spawn pigs in Java Edition, so it may be advisable to make Java Edition's behaviour match Bedrock Edition's.
How to reproduce
- Give yourself a spawner: /give @p minecraft:spawner

- Note the item name - this will be used for searching

- Open the Creative inventory

- Enter the Search tab

- Search for Spawner

- See no relevant results

## Comments (22)

### Comment 1: migrated (2018-07-05T11:43:19.788-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: Arisa Bot (2020-06-07T09:01:15.252-0700)

Thank you for your report!
We're tracking this issue as MC-918, so this ticket is being resolved and linked as a duplicate.
That ticket has already been resolved as working as intended, which means this is not considered a bug and won't be fixed. Please do not leave a comment on the linked ticket.
If you haven't already, you might like to make use of the search feature to see if the issue has already been mentioned.
Quick Links:
📓 Issue Guidelines – 💬 Community Support – 📧 Customer Support – ✍️ Feedback and Suggestions – 📖 Game Wiki
-- I am a bot. This action was performed automagically! Please report any issues in Discord or Reddit

### Comment 3: anthony cicinelli (2020-06-17T06:31:59.468-0700)

Confirmed for 1.16 Pre-Release 7

### Comment 4: anthony cicinelli (2020-06-21T08:05:13.415-0700)

Confirmed for 1.16 Release Candidate 1

### Comment 5: anthony cicinelli (2020-06-25T20:50:10.075-0700)

Confirmed for 1.16.1

### Comment 6: migrated (2021-02-19T12:19:48.397-0800)

Confirmed for 21w07a

### Comment 7: Avoma (2021-03-08T00:45:00.556-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 8: Avoma (2021-06-27T08:48:12.529-0700)

Can confirm in 1.17.

### Comment 9: ampolive (2021-07-29T04:46:48.692-0700)

Can confirm in 1.17.1.

### Comment 10: Tanuki_Bakero (2021-10-06T13:09:45.970-0700)

Confirmed with 21w39a

### Comment 11: Tanuki_Bakero (2021-10-21T11:00:47.828-0700)

Confirmed with 21w42a

### Comment 12: Tanuki_Bakero (2021-11-11T12:59:40.785-0800)

Confirmed with 1.18 Pre-release 1

### Comment 13: MMK21 (2021-12-11T05:41:22.897-0800)

Affects 1.18.1

### Comment 14: migrated (2022-03-20T06:20:47.047-0700)

Affects 22w11a

### Comment 15: Avoma (2022-03-23T08:19:50.745-0700)

Can confirm in 1.18.2.

### Comment 16: Tanuki_Bakero (2022-04-09T08:47:37.083-0700)

Confirmed with 22w14a

### Comment 17: Sniper1.1 (2022-04-09T10:09:54.096-0700)

I wonder if this as something to do with Java not having just an empty spawner block. It's default is pigs. This is unlike Bedrock, which can just be empty. This is a parity issue itself, but I wonder if maybe because it can't really be used for decoration like Bedrock, it just isn't in the inventory.

(also, I'd be surprised if this report stays open. any parity issue from pre 1.14 times seems to count as a "suggestion", not "bug".

### Comment 18: Avoma (2022-06-22T07:50:59.548-0700)

Can confirm in 1.19.

### Comment 19: Tanuki_Bakero (2022-06-27T13:16:56.800-0700)

Confirmed with 1.19.1 Release Candidate 1

### Comment 20: Avoma (2022-10-15T06:32:16.366-0700)

Can confirm in 1.19.2.

### Comment 21: migrated (2022-10-26T06:16:29.868-0700)

Fixed in 22w43a,according to the changelog.

### Comment 22: Avoma (2022-10-26T06:27:37.971-0700)

I can also confirm that this has been fixed in 22w43a.

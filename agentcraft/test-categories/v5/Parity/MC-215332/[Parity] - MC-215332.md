# MC-215332: Glow squids lack a baby variant

**Mojira URL:** [https://bugs.mojang.com/browse/MC-215332](https://bugs.mojang.com/browse/MC-215332)

## Report details

- **Mojira categories:** Parity
- **Project:** MC
- **Issue key:** MC-215332
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2021-02-13T02:09:32.464-0800
- **Updated:** 2025-04-26T12:34:57.258-0700
- **Resolution date:** 2024-08-17T16:36:26.338-0700
- **Affects versions:** 21w06a; 21w07a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 1.17 Pre-release 1; 1.17 Pre-release 3; 1.17 Release Candidate 1; 1.17; 1.17.1 Pre-release 1; 1.17.1 Release Candidate 1; 1.17.1 Release Candidate 2; 1.17.1; 21w37a; 21w38a; 21w39a; 21w40a; 21w41a; 21w42a; 21w43a; 21w44a; 1.18 Pre-release 1; 1.18 Pre-release 2; 1.18 Pre-release 4; 1.18 Pre-release 5; 1.18 Pre-release 8; 1.18 Release Candidate 1; 1.18 Release Candidate 3; 1.18 Release Candidate 4; 1.18; 1.18.1 Pre-release 1; 1.18.1 Release Candidate 1; 1.18.1 Release Candidate 2; 1.18.1; 22w03a; 22w05a; 22w06a; 1.18.2 Pre-release 2; 1.18.2 Pre-release 3; 1.18.2 Release Candidate 1; 1.18.2; 22w11a; 22w12a; 22w14a; 22w15a; 22w16b; 22w18a; 1.19 Pre-release 3; 1.19; 22w24a; 1.19.1 Pre-release 1; 1.19.1 Release Candidate 1; 1.19.1 Pre-release 2; 1.19.1 Pre-release 4; 1.19.1 Pre-release 5; 1.19.1 Pre-release 6; 1.19.1 Release Candidate 2; 1.19.1; 1.19.2; 22w42a; 22w44a; 22w45a; 22w46a; 1.19.3 Pre-release 2; 1.19.3 Pre-release 3; 1.19.3 Release Candidate 1; 1.19.3 Release Candidate 3; 1.19.3; 23w03a; 23w04a; 23w05a; 23w06a; 23w07a; 1.19.4 Pre-release 1; 1.19.4 Pre-release 2; 1.19.4 Pre-release 3; 1.19.4 Pre-release 4; 1.19.4 Release Candidate 1; 1.19.4 Release Candidate 2; 1.19.4 Release Candidate 3; 1.19.4; 23w12a; 23w13a; 23w14a; 23w16a; 23w17a; 23w18a; 1.20 Pre-release 1; 1.20 Pre-release 2; 1.20 Pre-release 4; 1.20 Pre-release 5; 1.20 Pre-release 6; 1.20 Pre-release 7; 1.20 Release Candidate 1; 1.20; 1.20.1 Release Candidate 1; 1.20.1; 23w31a; 23w32a; 23w33a; 23w35a; 1.20.2 Pre-release 1; 1.20.2 Pre-release 2; 1.20.2 Pre-Release 3; 1.20.2 Pre-Release 4; 1.20.2 Release Candidate 1; 1.20.2 Release Candidate 2; 1.20.2; 23w40a; 23w41a; 1.20.4
- **Fix versions:** 24w33a
- **Area:** Gameplay
- **Labels:** baby; glow_squid; mob-spawning; vanilla-parity
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** img (956).png; MC-215332.mp4; MC-215332.png
- **Issue links:** Relates:outward:MC-192081:Some aquatic mobs have no baby type

## Description

The Bug:
Parity issue: Baby glow squids exist in Bedrock Edition, but not in Java Edition.
Steps to Reproduce:
- Launch an instance of Java Edition, and attempt to summon a baby glow squid by using the following command.

```
/summon minecraft:glow_squid ~ ~ ~ {Age:-25000}
```
- Take note as to whether or not a baby or adult glow squid is summoned upon executing this command.

Observed Behavior:
Baby glow squids exist in Bedrock Edition, but not in Java Edition.
Expected Behavior:
Baby glow squids would exist in Java Edition, just like in Bedrock Edition.

## Comments (77)

### Comment 1: migrated (2021-02-13T02:09:32.464-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2021-02-13T02:24:29.795-0800)

Normal squids and dolphins may be considered a feature request, as only parity issues since Buzzy bees (J.E. 1.15 and B.E. 1.14.0) are considered valid unfortunately, so it'd be a good idea to remove them from this report

### Comment 3: migrated (2021-02-17T13:48:35.502-0800)

can confirm for 21w07a

### Comment 4: Avoma (2021-02-20T11:58:30.783-0800)

Here are some steps to reproduce this issue:
Steps to Reproduce:
- Attempt to summon a baby variant of both squids and glow squids, through using the following commands:

```/summon minecraft:squid ~ ~ ~ {Age:-25000}
/summon minecraft:glow_squid ~ ~ ~ {Age:-25000}```
→  Notice how the both of the squids aren't babies.

### Comment 5: Avoma (2021-02-26T05:28:10.136-0800)

Can confirm in 21w08b.

### Comment 6: migrated (2021-02-27T00:11:08.826-0800)

For consistency between aquatic mobs, it will be good idea to "fix" also 192081

### Comment 7: Avoma (2021-03-18T03:15:17.382-0700)

Can confirm in 21w11a.

### Comment 8: Tinsel (2021-03-31T20:33:20.494-0700)

In 21w13a

### Comment 9: Tinsel (2021-04-07T11:33:28.398-0700)

Also in 21w14a

### Comment 10: Avoma (2021-04-14T11:55:14.459-0700)

Can confirm in 21w15a.

### Comment 11: Avoma (2021-04-22T02:12:38.168-0700)

Can confirm in 21w16a.

### Comment 12: Tinsel (2021-04-28T10:14:33.874-0700)

Affects 21w17a

### Comment 13: Tinsel (2021-05-05T13:26:51.641-0700)

In 21w18a

### Comment 14: migrated (2021-05-12T09:22:47.431-0700)

can confirm for 21w19a

### Comment 15: migrated (2021-05-28T09:57:13.678-0700)

can confirm for 1.17 pre-release 1

### Comment 16: Tanuki_Bakero (2021-06-04T20:33:49.725-0700)

Confirmed with 1.17 Release Candidate 1

### Comment 17: Tinsel (2021-06-08T12:16:13.773-0700)

Affects 1.17

### Comment 18: Tanuki_Bakero (2021-06-21T00:41:17.412-0700)

Confirmed with 1.17.1 Pre-release 1

### Comment 19: Tanuki_Bakero (2021-07-01T12:44:05.979-0700)

Confirmed with 1.17.1 Release Candidate 1

### Comment 20: Tanuki_Bakero (2021-07-05T10:02:19.210-0700)

Confirmed with 1.17.1 Release Candidate 2

### Comment 21: migrated (2021-09-15T13:08:13.283-0700)

Affects 21w37a

### Comment 22: Tanuki_Bakero (2021-09-23T10:47:55.786-0700)

Confirmed with 21w38a

### Comment 23: Tanuki_Bakero (2021-10-03T06:56:35.020-0700)

Confirmed with 21w39a

### Comment 24: Tanuki_Bakero (2021-10-08T11:08:10.700-0700)

Confirmed with 21w40a

### Comment 25: Tanuki_Bakero (2021-10-13T20:04:00.747-0700)

Confirmed with 21w41a

### Comment 26: muzikbike (2021-10-15T18:39:09.772-0700)

No it isn't. This is a clear parity issue, and is valid due to it originating after 1.15.

### Comment 27: migrated (2021-10-19T14:46:48.894-0700)

It is still a valid parity issue. It's also already assigned, and given a priority saying exactly that it is NOT ok.

### Comment 28: Tanuki_Bakero (2021-10-21T10:52:26.860-0700)

Confirmed with 21w42a
@Connor Steppie
@Dhranios
Ignore Kai Maldonado and
Let's leave it alone.
Also, it seems that I deleted the comment because it became inconvenient.

### Comment 29: Tanuki_Bakero (2021-10-28T12:01:31.763-0700)

Confirmed with 21w43a

### Comment 30: Avoma (2021-10-30T02:51:14.060-0700)

I am able to confirm this behavior in 21w43a. Here are some extra details regarding this problem.
The Bug:
Parity issue: Baby glow squids exist in bedrock edition, but not in java edition.
Steps to Reproduce:
- Launch an instance of java edition, and attempt to summon a baby glow squid by using the following command.

```/summon minecraft:glow_squid ~ ~ ~ {Age:-25000}```
- Take note as to whether or not a baby or adult glow squid is summoned upon executing this command.

Observed Behavior:
Baby glow squids exist in bedrock edition, but not in java edition.
Expected Behavior:
Baby glow squids would exist in java edition, just like in bedrock edition.

### Comment 31: Tanuki_Bakero (2021-11-03T20:28:33.874-0700)

Confirmed with 21w44a

### Comment 32: Tinsel (2021-11-11T10:28:16.524-0800)

Still in 1.18 Pre-1

### Comment 33: Tanuki_Bakero (2021-11-16T12:59:42.188-0800)

Confirmed with 1.18 Pre-release 2

### Comment 34: Tanuki_Bakero (2021-11-17T13:49:35.238-0800)

Confirmed with 1.18 Pre-release 4

### Comment 35: Tanuki_Bakero (2021-11-19T14:44:35.959-0800)

Confirmed with 1.18 Pre-release 5

### Comment 36: Tanuki_Bakero (2021-11-24T19:24:39.917-0800)

Confirmed with 1.18 Pre-release 8

### Comment 37: Tanuki_Bakero (2021-11-25T12:31:00.260-0800)

Confirmed with 1.18 Release Candidate 1

### Comment 38: Tanuki_Bakero (2021-11-27T04:57:00.964-0800)

Confirmed with 1.18 Release Candidate 3

### Comment 39: Tanuki_Bakero (2021-11-29T12:29:05.549-0800)

Confirmed with 1.18 Release Candidate 4

### Comment 40: Tanuki_Bakero (2021-12-03T11:57:27.488-0800)

Confirmed with 1.18.1 Pre-release 1

### Comment 41: Tanuki_Bakero (2021-12-07T12:02:21.981-0800)

Confirmed with 1.18.1 Release Candidate 1

### Comment 42: Tanuki_Bakero (2021-12-09T19:42:24.493-0800)

Confirmed with 1.18.1 Release Candidate 2

### Comment 43: Tanuki_Bakero (2021-12-10T05:47:10.824-0800)

Confirmed with 1.18.1

### Comment 44: Tanuki_Bakero (2022-01-30T06:17:53.419-0800)

Confirmed with 22w03a
@Dhranios
Although there was a priority, there is also a pattern that has become "Works As Intended"(MC-200268), so it can not be said that "priority is attached = corrected".
By no means, I do not defend the person who posted the comment (deleted).

### Comment 45: Tinsel (2022-02-02T13:12:32.179-0800)

In 22w05a

### Comment 46: Tanuki_Bakero (2022-02-09T10:38:49.524-0800)

Confirmed with 22w06a

### Comment 47: Tanuki_Bakero (2022-02-21T16:48:09.774-0800)

Confirmed with 1.18.2 Pre-release 2

### Comment 48: Tanuki_Bakero (2022-02-23T11:26:27.397-0800)

Confirmed with 1.18.2 Pre-release 3

### Comment 49: Tanuki_Bakero (2022-02-25T11:18:58.044-0800)

Confirmed with 1.18.2 Release Candidate 1

### Comment 50: Tanuki_Bakero (2022-02-28T19:46:37.873-0800)

Confirmed with 1.18.2

### Comment 51: Tanuki_Bakero (2022-03-16T12:39:05.988-0700)

Confirmed with 22w11a

### Comment 52: Tanuki_Bakero (2022-03-26T06:37:34.092-0700)

Confirmed with 22w12a

### Comment 53: Tanuki_Bakero (2022-04-06T10:44:41.345-0700)

Confirmed with 22w14a

### Comment 54: migrated (2022-04-13T15:24:17.015-0700)

In 22w15a

### Comment 55: Tanuki_Bakero (2022-04-24T06:47:18.374-0700)

Confirmed with 22w16b

### Comment 56: Tanuki_Bakero (2022-05-28T08:33:45.248-0700)

Confirmed with 1.19 Pre-release 3

### Comment 57: Tanuki_Bakero (2022-06-08T05:58:14.360-0700)

Confirmed with 1.19

### Comment 58: Tanuki_Bakero (2022-06-16T09:47:23.241-0700)

Confirmed with 22w24a

### Comment 59: Tanuki_Bakero (2022-06-27T13:10:30.448-0700)

Confirmed with 1.19.1 Release Candidate 1

### Comment 60: Tanuki_Bakero (2022-07-03T12:59:27.221-0700)

Confirmed with 1.19.1 Pre-release 2

### Comment 61: Tanuki_Bakero (2022-07-11T14:29:27.082-0700)

Confirmed with 1.19.1 Pre-release 4

### Comment 62: Tanuki_Bakero (2022-07-15T13:41:23.106-0700)

Confirmed with 1.19.1 Pre-release 5

### Comment 63: Tanuki_Bakero (2022-07-20T12:18:38.703-0700)

Confirmed with 1.19.1 Pre-release 6

### Comment 64: Tanuki_Bakero (2022-07-23T15:52:10.102-0700)

Confirmed with 1.19.1 Release Candidate 2

### Comment 65: Tanuki_Bakero (2022-07-29T14:24:46.427-0700)

Confirmed with 1.19.1

### Comment 66: Tanuki_Bakero (2022-08-06T14:37:31.401-0700)

Confirmed with 1.19.2

### Comment 67: Tanuki_Bakero (2022-10-22T14:17:57.362-0700)

Confirmed with 22w42a

### Comment 68: Tanuki_Bakero (2022-11-02T11:05:11.828-0700)

Confirmed with 22w44a

### Comment 69: Tanuki_Bakero (2022-11-09T11:30:28.616-0800)

Confirmed with 22w45a

### Comment 70: Tanuki_Bakero (2022-11-17T08:20:57.261-0800)

Confirmed with 22w46a

### Comment 71: Tanuki_Bakero (2022-11-25T14:06:37.457-0800)

Confirmed with 1.19.3 Pre-release 2

### Comment 72: Tanuki_Bakero (2022-11-30T07:51:34.285-0800)

Confirmed with 1.19.3 Pre-release 3

### Comment 73: Tanuki_Bakero (2022-12-01T13:10:31.451-0800)

Confirmed with 1.19.3 Release Candidate 1

### Comment 74: Tanuki_Bakero (2022-12-06T14:04:26.421-0800)

Confirmed with 1.19.3 Release Candidate 3
Our current reporter has been inactive for over a year.
Therefore, would you please give me ownership of this ticket?
We will continue to update this ticket.

### Comment 75: ampolive (2022-12-07T06:52:59.948-0800)

Done.

### Comment 76: Tanuki_Bakero (2022-12-07T08:49:36.214-0800)

thank you.

### Comment 77: Tanuki_Bakero (2022-12-07T09:08:55.131-0800)

Description updated to 's comment. (Comment of 30/10/21 6:51 PM JST)

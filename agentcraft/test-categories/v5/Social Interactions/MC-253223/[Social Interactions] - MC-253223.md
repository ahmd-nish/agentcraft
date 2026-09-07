# MC-253223: A preposition is incorrectly used within the "gui.abuseReport.reason.terrorism_or_violent_extremism.description" string

**Mojira URL:** [https://bugs.mojang.com/browse/MC-253223](https://bugs.mojang.com/browse/MC-253223)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-253223
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-06-17T04:01:03.301-0700
- **Updated:** 2025-03-20T23:46:55.858-0700
- **Resolution date:** 2022-07-14T08:53:31.308-0700
- **Affects versions:** 22w24a; 1.19.1 Pre-release 1; 1.19.1 Pre-release 3
- **Fix versions:** 1.19.1 Pre-release 3; 1.19.1 Pre-release 5
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-253223.png; MC-253223 - 1.19.1-pre3.png; MC-253223 - Analysis.png

## Description

The Bug:
A preposition is incorrectly used within the "gui.abuseReport.reason.terrorism_or_violent_extremism.description" string.
This string is currently grammatically incorrect as the preposition within it, (that being the word "with"), doesn't contain a noun before it, therefore not making it clear who the given person is threatening these comments toward.
Below, I've constructed a table that states all of the necessary and relevant information regarding this issue.
Affected String:
Before reading the table, please note the following:
- Words colored in GREEN are correct.

- Words colored in RED are incorrect.

Translation Key
Current String
Expected String
String URL on Crowdin
gui.abuseReport.reason.terrorism_or_violent_extremism.description
Someone is talking about, promoting, or threatening with acts of terrorism or violent extremism for political, religious, ideological, or other reasons.
Someone is talking about, promoting, or threatening acts of terrorism or violent extremism for political, religious, ideological, or other reasons.
https://crowdin.com/translate/minecraft/10002/enus-engb#5297058
h3. Steps to Reproduce:
- Display this string by executing the command provided below.

```
/tellraw @s {"translate":"gui.abuseReport.reason.terrorism_or_violent_extremism.description"}
```
- Look closely at the usage of the preposition (that being the word "with") within this string.

- Take note as to whether or not a preposition is incorrectly used within the "gui.abuseReport.reason.terrorism_or_violent_extremism.description" string.

Observed Behavior:
A preposition is incorrectly used.
Expected Behavior:
Prepositions would be correctly used within this string.

## Comments (5)

### Comment 1: migrated (2022-06-17T04:01:03.301-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: [Mod] turbo (2022-06-17T04:02:36.271-0700)

Can confirm.

### Comment 3: Avoma (2022-06-23T10:46:14.342-0700)

This issue has been fixed in 1.19.1 Release Candidate 1.

### Comment 4: Avoma (2022-07-04T07:56:18.916-0700)

Just clarifying since this report has been assigned; this issue is not present in 1.19.1 Pre-release 2 as this string was changed in 1.19.1 Release Candidate 1, thus fixing this error.

### Comment 5: Avoma (2022-07-06T08:46:18.163-0700)

This issue has not been fixed in 1.19.1 Pre-release 3 and is still present therefore I'd like to request for this ticket to be reopened if that's okay.  For some bizarre reason, this problem was fixed in 1.19.1 Release Candidate 1, but has been reverted to its incorrect state in 1.19.1 Pre-release 3, thus making this an issue again.

# MC-264561: Some new strings introduced in 23w31a are missing articles

**Mojira URL:** [https://bugs.mojang.com/browse/MC-264561](https://bugs.mojang.com/browse/MC-264561)

## Report details

- **Mojira categories:** Internationalisation
- **Project:** MC
- **Issue key:** MC-264561
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-08-02T10:43:42.554-0700
- **Updated:** 2025-04-30T03:37:40.636-0700
- **Resolution date:** 2023-08-30T03:00:42.713-0700
- **Affects versions:** 1.20.1; 23w31a; 23w32a
- **Fix versions:** 23w35a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2023-08-10 16-24-22.mkv

## Description

The Bug:
Some new strings introduced in 23w31a are missing articles.
For a bit of context, there are three articles within the English language. These are "a", "an", and "the". Articles are used before nouns. Considering that articles are present throughout many other strings within the game, this introduces an inconsistency.
Affected Strings:
Before reading the table, please note the following:
- Words colored in GREEN are correct.

- Words colored in RED are incorrect.

Translation Key
Current String
Expected String
String URL on Crowdin
commands.random.error.range_too_large
Range of random value must be at most 2147483646
The range of the random value must be at most 2147483646
https://crowdin.com/translate/minecraft/10038/enus-engb#5346305
commands.random.error.range_too_small
Range of random value must be at least 2
The range of the random value must be at least 2
https://crowdin.com/translate/minecraft/10038/enus-engb#5346307
pack.dropRejected.message
Following entries were not valid packs and were not copied:  %s
The following entries were not valid packs and were not copied:  %s
https://crowdin.com/translate/minecraft/10038/enus-engb#5346369
symlink_warning.title.world
World folder contains symbolic links
The world folder contains symbolic links
https://crowdin.com/translate/minecraft/10038/enus-engb#5346381
h3. Steps to Reproduce:
- Display any of the affected strings as listed above by using the command provided below and replacing "XYZ" with the string's translation key.

```
/tellraw @s {"translate":"XYZ"}
```

- Observe if the string contains an article where appropriate.

- Take note as to whether or not some new strings introduced in 23w31a are missing articles.

Observed Behavior:
Articles are missing.
Expected Behavior:
Articles would be present.

## Comments (2)

### Comment 1: migrated (2023-08-02T10:43:42.554-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: AMGAMES04 (2023-08-10T07:25:14.385-0700)

Can confirm in 23w32a

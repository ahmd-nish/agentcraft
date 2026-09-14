# MC-264829: Text Filter on signs doesn't hide if fully filtered

**Mojira URL:** [https://bugs.mojang.com/browse/MC-264829](https://bugs.mojang.com/browse/MC-264829)

## Report details

- **Mojira categories:** Dedicated Server; Text
- **Project:** MC
- **Issue key:** MC-264829
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2023-08-13T10:40:32.747-0700
- **Updated:** 2025-04-10T14:59:16.476-0700
- **Resolution date:** 2024-01-31T15:58:41.814-0800
- **Affects versions:** 1.20.1
- **Fix versions:** 23w31a
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** image-2023-08-13-18-36-00-618.png; image-2023-08-13-18-36-54-159.png
- **Issue links:** Relates:inward:MC-268197:Text Filter on Written Book titles doesn't hide if fully hidden

## Description

if a player with the account text filter disabled* makes a sign with a line that gets fully filtered by the text-filter-config specified in server.properties (either since it exceeds hashes to drop, or the "hashed" key in the response doesn't exist), then the line is shown to players with the text filter enabled, even though the line should be fully hidden.
this is due to an empty component in the filtered_message defaulting to messages,
which while correct if the message is fully allowed, is incorrect if the whole line should be empty for users playing with the text filter
Reproduction
- have a webserver providing text-filtering. i have made https://textfilter-server.the456gamer.workers.dev/ as a demo, use https://textfilter-server.the456gamer.workers.dev/exampleconfig to copy the text-filtering-config**

- ensure the dedicated server is running, with the text-filter-config set to the right url, and hashes to drop being 0 (so every text would cause it to be empty)

- on an account with textfilter disabled,* place a sign with a line that gets filtered

- on an account with textfilter enabled, observe that the sign contains the line that should be filtered

tested with the following sign
123: filtered line
abc: unfiltered lin
semi-filtered line
with the filter:
if line contains "abc": never filter
if line contains "123": always fully filter
else: filter every character
placed on unfiltered client, viewed on filtered client
placed on filtered client, viewed on filtered client (what both should look like on filtered client)
*: this is needed as otherwise the filtered text will be placed into the messages: tag, not filtered_messages where the fallback exists
**: this logs the requests to discord, see root url for more info

## Comments (1)

### Comment 1: migrated (2023-08-13T10:40:32.747-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

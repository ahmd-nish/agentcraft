# MC-252987: Illegal character '\n' in text component clickEvent

**Mojira URL:** [https://bugs.mojang.com/browse/MC-252987](https://bugs.mojang.com/browse/MC-252987)

## Report details

- **Mojira categories:** Social Interactions
- **Project:** MC
- **Issue key:** MC-252987
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-06-13T10:39:48.251-0700
- **Updated:** 2025-03-08T11:10:36.244-0800
- **Resolution date:** 2022-06-29T06:56:23.213-0700
- **Affects versions:** 1.19; 22w24a
- **Fix versions:** 1.19.1 Release Candidate 1
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** Click me text.png; Illegal Chars Screen.png

## Description

If a run_command click event that has a new character ( \n ) causes the player to get kicked from the world and displays the `Illegal characters in chat` screen

Steps to Reproduce:
- Create a singleplayer world (make sure to enable cheats).

- Paste the following command into the chat. Then press enter.

```
/tellraw @s [{"text":"Click me!","clickEvent": {"action":"run_command","value": "/tellraw @s [{\"text\":\"Players:\n\"},{\"color\":\"gray\",\"selector\":\"@a\"}]"} }]
```

- Open chat and press `Click me!`

Observed Results:
- The world closes and displays the `Connection lost, Illegal characters in chat` screen after pressing the text.

- Removing the `\n` character from the run command event causes the command to run.

- Double escaping the new line character seems to fix it.

```
/tellraw @s [{"text":"Click me!","clickEvent": {"action":"run_command","value": "/tellraw @s [{\"text\":\"Players:\\n\"},{\"color\":\"gray\",\"selector\":\"@a\"}]"} }]
```

- Putting the new line character in the main tellraw command properly works.

```
/tellraw @s {"text":"Hello\nWorld"}
```

Expected Results:
- The click event properly runs the tellraw command and displays all active players.

## Comments (1)

### Comment 1: migrated (2022-06-13T10:39:48.251-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

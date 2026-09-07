# MC-203401: Double-tapping forward button to sprint cannot be disabled/reconfigured

**Mojira URL:** [https://bugs.mojang.com/browse/MC-203401](https://bugs.mojang.com/browse/MC-203401)

## Report details

- **Mojira categories:** Accessibility; Input
- **Project:** MC
- **Issue key:** MC-203401
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2020-11-02T16:51:55.502-0800
- **Updated:** 2025-07-25T06:18:09.282-0700
- **Resolution date:** 2025-07-25T06:18:09.214-0700
- **Affects versions:** 1.15.2; 1.16.2; 1.16.4; 20w46a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05b; 21w06a; 21w18a; 21w20a; 1.17 Pre-release 1; 1.19; 22w42a; 22w43a; 23w05a; 1.19.4 Pre-release 2; 1.19.4; 23w14a; 1.20.1; 1.20.4; 1.21.7
- **Fix versions:** 25w31a
- **Area:** Platform
- **Labels:** controls-not-configurable
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** 2020-11-03_00.48.41.png; 2020-11-03_00.49.15.png
- **Issue links:** Relates:inward:MC-147718:F1, F3, F3+[char] combos cannot be rebound | Relates:outward:MC-270985:"Pick block with NBT/components" key cannot be rebound | Relates:outward:MC-268283:Navigating the hotbar via the scroll wheel cannot be rebound | Relates:inward:MC-122645:Narrator hotkey cannot be customized or disabled | Duplicate:inward:MC-179496:Sprinting by double-pressing "Walk Forwards" (default "W" key) cannot be disabled | Duplicate:inward:MC-299291:Sprint activates on its own

## Description

The bug
Sprinting via double-tapping the "forward" button cannot be bound separately from the "forward" button itself. This means there is no way (outside of hunger) to not sprint when tapping the "forward" button in quick succession, which may be required for precise positioning.
This may be considered a feature request but for a control to be absent from configuration does not seem right.
How to reproduce
- Double-tap your usual forward button while grounded and the hunger bar is full if applicable

- Note that this causes sprinting

- Change the forward keybind to an unused key such as G

- Double-tap this new key and note that you still start sprinting, demonstrating that it follows the "forward" key

Expected behaviour
The double-tap-to-sprint behaviour would not follow the forward movement button.
Actual behaviour
This functionality is hardcoded to always be stuck with the move forward button. There exists no option to disable it, nor is it a different rebindable control that happens to share the move forward key's place by default.
How to fix
There are several ways in which this issue could be fixed:
- Preferable solution: There would be two different keybinds for sprint: one which defaults to LCONTROL, and a second that defaults to W. W is also the default forward key, so pressing W once would trigger normal walking whereas pressing it twice would activate sprinting and cause the player to move forward. If the sprint key and forward key do not share a keybind, the "new" sprint keybind would work identically to the normal sprint keybind. The "Random Patches" mod for 1.16.5 uses this behaviour.

- The "Controls" menu could contain a toggle which would determine whether pressing the forward key twice should activate sprinting, or not.

## Comments (11)

### Comment 1: migrated (2020-11-02T16:51:55.502-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: FivesBlue (2020-11-02T23:44:56.900-0800)

Double tapping whatever button you use for "forward" will always activate sprint when double-tapped. I don't believe this can be changed without modding the game. The button which activates sprint (without double tapping forward) can be changed in your key bind setting though.

### Comment 3: muzikbike (2020-11-03T06:46:33.760-0800)

....which is literally what I described within the ticket.

### Comment 4: Avoma (2021-01-08T08:08:15.170-0800)

Can confirm in 20w51a.

### Comment 5: Avoma (2021-02-05T08:12:30.742-0800)

Can confirm in 21w05b.

### Comment 6: Avoma (2021-02-13T09:35:58.888-0800)

Can confirm in 21w06a.

### Comment 7: migrated (2021-05-05T11:25:49.319-0700)

Affects 21w18a

### Comment 8: Brevort (2021-05-30T21:28:21.401-0700)

Also true for double-tapping space for flying. If you would like to include it here you may but it's up to you.

### Comment 9: muzikbike (2021-10-15T09:00:27.484-0700)

I plan on reporting this separately.

### Comment 10: migrated (2022-06-19T12:28:04.984-0700)

Affects 1.19

### Comment 11: muzikbike (2022-10-23T05:24:07.534-0700)

Flying has been reported under MC-256811.

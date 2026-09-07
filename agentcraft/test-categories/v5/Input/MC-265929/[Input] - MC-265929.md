# MC-265929: Ctrl+Backspacing a word with non-BMP characters in an edit box deletes additional characters

**Mojira URL:** [https://bugs.mojang.com/browse/MC-265929](https://bugs.mojang.com/browse/MC-265929)

## Report details

- **Mojira categories:** Input; UI
- **Project:** MC
- **Issue key:** MC-265929
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-10-19T01:37:21.968-0700
- **Updated:** 2025-03-20T22:16:29.021-0700
- **Resolution date:** 2023-11-23T07:49:41.499-0800
- **Affects versions:** 1.20.2; 23w42a; 23w44a
- **Fix versions:** 1.20.3 Pre-Release 1
- **Area:** Platform
- **Labels:** gui; gui-textbox
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** 2023-10-19_04-11-20.mov

## Description

Using Ctrl+Backspace to delete a word in an edit box results in additional characters being deleted if that word contains non-BMP characters.
Reproduction
- Open the screen to add a server

- Paste the string 𐑐 𐑑𐑑 𐑒𐑒𐑒 𐑓𐑓𐑓𐑓 𐑔𐑔𐑔𐑔𐑔 𐑕𐑕𐑕𐑕𐑕𐑕 𐑖𐑖𐑖𐑖𐑖𐑖𐑖 (consisting of Shavian characters) into the ‘Server Address’ box

- Make sure the cursor is at the end of the string

- Press Ctrl+Backspace repeatedly

Intended behavior: only one word is deleted at a time
Actual behavior: the preceding word is deleted as well
Code analysis
(Based on the 1.20.2 code, using Yarn version 1.20.2+build.1. Decompiled with Fabric’s fork of CFR, with some editing from me.)
TextFieldWidget#keyPressed calls TextFieldWidget#erase when it detects a Backspace or Delete press. erase, in turn, calls eraseWords or eraseCharacters depending on whether Ctrl is pressed.
eraseWords is implemented as follows:

```
public void eraseWords(int wordOffset) {
        if (this.text.isEmpty()) {
            return;
        }
        if (this.selectionEnd != this.selectionStart) {
            this.write("");
            return;
        }
        // The argument passed in is in code units, not code points!
        this.eraseCharacters(this.getWordSkipPosition(wordOffset) - this.selectionStart);
    }

    public void eraseCharacters(int characterOffset) {
        if (this.text.isEmpty()) {
            return;
        }
        if (this.selectionEnd != this.selectionStart) {
            this.write("");
            return;
        }
        int pos = this.getCursorPosWithOffset(characterOffset);
        int from = Math.min(pos, this.selectionStart);
        int to = Math.max(pos, this.selectionStart);
        if (from == to) {
            return;
        }
        String newText = new StringBuilder(this.text).delete(from, to).toString();
        if (!this.textPredicate.test(newText)) {
            return;
        }
        this.text = newText;
        this.setCursor(from, false);
    }

    private int getCursorPosWithOffset(int offset) {
        // Util.moveCursor traverses the string in code points, not code units!
        return Util.moveCursor(this.text, this.selectionStart, offset);
    }

    public int getWordSkipPosition(int wordOffset) {
        return this.getWordSkipPosition(wordOffset, this.getCursor());
    }

    private int getWordSkipPosition(int wordOffset, int cursorPosition) {
        return this.getWordSkipPosition(wordOffset, cursorPosition, true);
    }

    private int getWordSkipPosition(int wordOffset, int cursorPosition, boolean skipOverSpaces) {
        int pos = cursorPosition;
        boolean reverse = wordOffset < 0;
        int absOffset = Math.abs(wordOffset);
        for (int i = 0; i < absOffset; ++i) {
            if (reverse) {
                while (skipOverSpaces && pos > 0 && this.text.charAt(pos - 1) == ' ') {
                    --pos;
                }
                while (pos > 0 && this.text.charAt(pos - 1) != ' ') {
                    --pos;
                }
            } else {
                int len = this.text.length();
                if ((pos = this.text.indexOf(' ', pos)) == -1) {
                    pos = len;
                    continue;
                }
                while (skipOverSpaces && pos < len && this.text.charAt(pos) == ' ') {
                    ++pos;
                }
            }
        }
        return pos;
    }
```
That is:
- eraseWords calls getWordSkipPosition, which returns an index into the text in UTF-16 code units, then subtracts this by the current cursor position. This difference is the number of code units to be deleted, combined with the direction to delete the text in.

- This difference is passed to eraseCharacters, which computes the position to which the text should be erased using getCursorPosWithOffset, which uses Util.moveCursor internally.

- However, Util.moveCursor moves across a code point on iteration, so the offset it takes should be in code points.

This bug could be fixed by having eraseWords delete the part of the text in the range from this.selectionStart to this.getWordSkipPosition(wordOffset) (or vice versa) directly instead of calling eraseCharacters.

## Comments (1)

### Comment 1: migrated (2023-10-19T01:37:21.968-0700)

This comment contained an image attachment, please login to view the attachment.

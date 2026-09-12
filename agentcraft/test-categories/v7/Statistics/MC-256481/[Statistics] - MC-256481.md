# MC-256481: minecraft.used:minecraft.BOOK_TYPE doesn't increase when placing books onto chiseled bookshelves

**Mojira URL:** [https://bugs.mojang.com/browse/MC-256481](https://bugs.mojang.com/browse/MC-256481)

## Report details

- **Mojira categories:** Statistics
- **Project:** MC
- **Issue key:** MC-256481
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-10-19T06:45:40.595-0700
- **Updated:** 2025-10-06T08:09:04.557-0700
- **Resolution date:** 2022-11-21T06:19:45.639-0800
- **Affects versions:** 22w42a; 22w43a; 22w44a; 22w45a
- **Fix versions:** 1.19.3 Pre-release 1
- **Area:** Expansion A
- **Labels:** chiseled_bookshelf
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-256481.mp4; MC-256481.png
- **Issue links:** Relates:outward:MC-302587:“minecraft.used:minecraft.ITEM” doesn't increase when placing items onto shelves

## Description

The Bug:
minecraft.used:minecraft.BOOK_TYPE doesn't increase when placing books onto chiseled bookshelves.

Affected Scoreboard Objectives
minecraft.used:minecraft.book
minecraft.used:minecraft.writable_book
minecraft.used:minecraft.written_book
h3. Steps to Reproduce:
- Create a scoreboard objective for tracking the use of a writeable book and set it to display on the sidebar.

```
/scoreboard objectives add UseWritableBook minecraft.used:minecraft.writable_book
```

```
/scoreboard objectives setdisplay sidebar UseWritableBook
```
- Obtain a writable book, otherwise more commonly known as a book and quill, and place down a lectern along with a chiseled bookshelf.

- Place the writable book onto the lectern and take note of how the scoreboard increases.

- Place the writable book onto the chiseled bookshelf.

- Take note as to whether or not minecraft.used:minecraft.BOOK_TYPE increases when placing books onto chiseled bookshelves.

Observed Behavior:
The scoreboard doesn't increase.
Expected Behavior:
The scoreboard would increase.

## Comments (1)

### Comment 1: migrated (2022-10-19T06:45:40.595-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

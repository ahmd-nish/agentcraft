# MC-257178: Chiseled Bookshelf redstone behavior is inconsistent

**Mojira URL:** [https://bugs.mojang.com/browse/MC-257178](https://bugs.mojang.com/browse/MC-257178)

## Report details

- **Mojira categories:** Redstone
- **Project:** MC
- **Issue key:** MC-257178
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-11-03T07:27:20.533-0700
- **Updated:** 2025-04-30T04:48:32.005-0700
- **Resolution date:** 2023-04-18T00:47:17.256-0700
- **Affects versions:** 22w44a; 1.19.3
- **Fix versions:** 23w16a
- **Area:** Expansion A
- **Watchers:** 1
- **Attachments:** 0

## Description

Now that hoppers can interact with chiseled bookshelves in 22w44a, the redstone behavior no longer matches the intended behavior from the announcement.
Setup
- Place a chiseled bookshelf over a hopper. Set up a comparator to visually measure the signal strength from the bookshelf.

- Power the hopper.

- Fill all hopper slots with plain books, so it can take in only more plain books.

- Insert books into the bookshelf in the following order: Protection I enchanted book, plain book, plain book, Protection II enchanted book, Protection III enchanted book, Protection IV enchanted book.

- De-power the hopper. Observe comparator output as the two plain books are removed.

- Add two books-and-quills to the chiseled bookshelf, observing comparator output as this is done.

- Remove the books from the bookshelf.

Actual behavior
At step 5, the books are removed from slots 2 and 3. Comparator output indicates 6 after the first removal, then 5 and then 4 after the second. Block texture is no different from when slots 5 and 6 were empty.
At step 6, the books-and-quills are inserted into slots 2 and 3. Comparator output indicates 5 then 6.
At step 7, we get back the books in the following order: Prot IV, Prot III, Prot II, book-and-quill, book-and-quill, Prot I, confirming that the two books-and-quills were inserted into slots 2 and 3.
Expected behavior
There are several ways this could work to be consistent:
- The comparator output indicates slots 2 and 3 when slots 2 and 3 are the last interacted with, as it is currently defined. And ideally the block texture would visually indicate which slots are empty too.

- The hopper works more like "remove book from slot 2 then shift all books over" so the empty slots are always at the end. In that case the comparator output should have been 5 (not 6) after the first removal (since the last action was moving the book in slot 6 to slot 5), the output after the second removal should have immediately been 4 (not 5-then-4), and the order the books are retrieved in step 7 should reflect the books-and-quills having been inserted into slots 5 and 6.

- The hopper can only take from the last filled slot. Although IMO that would be much less useful behavior.

- Redefine the redstone behavior to indicate fullness, like other containers, instead of "last interacted slot". And still maybe adjust the texture to indicate which slots are empty.

## Comments (7)

### Comment 1: migrated (2022-11-03T07:29:24.406-0700)

I suppose also of note is that sometimes it will do the "shift all books over" thing, e.g. on a save-reload cycle. Just not consistently.

### Comment 2: migrated (2022-11-16T17:21:14.243-0800)

Behavior is more predictable in 22w46a. The one remaining oddity I've noticed is that a hopper failing to draw from a non-empty bookshelf will reset the signal to indicate the last-filled slot.
This appears to be because the hopper technically takes each book, finds it can't actually put it into the hopper's inventory, and then reinserts it back into the bookshelf. The "reinsert" step changes the bookshelf's last-interacted slot.

### Comment 3: ampolive (2022-11-16T17:27:56.699-0800)

Does MC-257622 describe your issue?

### Comment 4: migrated (2022-11-20T13:31:07.293-0800)

No, that is entirely unrelated.

### Comment 5: migrated (2022-12-01T00:44:06.649-0800)

Agree would see the interaction of hoppers with the chiseled bookshelf as a stack and not a queue, The books placed in the initial slots shouldn't change as things are pulled in/out. i.e. the last book placed in should be the first one out so order is maintained.

I still think it's odd that adding/removing from the same slot outputs the same signal. Since there's only 6 slots and 15 possible redstone signals, there's a lot of possibilities here. I still think it'd be interesting to have different strength signals for adding vs. removing from a slot. For instance 1-6 being added to that slot last, 7-12 removed from that slot last, or 1 & 2 being added/removed for slot 1, signal-strength 3 & 4 added/removed for slot 2, etc...

### Comment 6: Brain81505 (2023-02-18T05:41:45.044-0800)

Does this issue still occur in 1.19.3?

### Comment 7: migrated (2023-02-19T06:16:26.145-0800)

The situation does not seem to have changed from the behavior in 22w46a as described in #comment-1212161.

# MC-170659: Loss of precision in entity_scores conditions

**Mojira URL:** [https://bugs.mojang.com/browse/MC-170659](https://bugs.mojang.com/browse/MC-170659)

## Report details

- **Mojira categories:** Loot tables
- **Project:** MC
- **Issue key:** MC-170659
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2020-02-01T08:25:43.126-0800
- **Updated:** 2025-04-30T07:25:56.787-0700
- **Resolution date:** 2022-07-19T12:57:25.211-0700
- **Affects versions:** 1.15.2; 20w06a; 20w07a; 20w08a; 20w09a; 20w10a; 20w11a; 20w12a; 20w14a; 20w16a; 20w17a; 20w18a; 20w20b; 1.16 Pre-release 5; 1.16.1; 1.16.2 Pre-release 1; 1.16.2 Release Candidate 1; 1.16.2; 1.16.3; 1.16.4 Pre-release 1; 1.16.4; 20w45a; 20w46a
- **Fix versions:** 20w46a
- **Labels:** entity_scores
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** MC-170659 data pack.zip
- **Issue links:** Relates:inward:MC-254370:Loot condition "entity_scores" cannot check all possible scores | Relates:inward:MC-138426:Not all CustomModelData values can be checked by predicate, due to floating point imprecision

## Description

The bug
entity_scores conditions cannot express all possible ranges of ints because they use RandomValueBounds that its min and max are floats.
Actual score
Predicate
Condition passes?
Should this happen?
16777216
16777216
yes

16777216
16777217
yes

16777217
16777216
yes

16777217
16777217
yes

How to reproduce
-

```
/scoreboard objectives add _ dummy
```

-

```
/scoreboard players set @s _ 16777216
```

-

```
/execute if predicate _
```
 →  Test passed

-

```
/scoreboard players set @s _ 16777217
```

-

```
/execute if predicate _
```
 →  Test passed

-  data/minecraft/predicates/_.json

```
{
    "condition": "minecraft:entity_scores",
    "scores": {
        "_": 16777216
    },
    "entity": "this"
}
```

## Comments (7)

### Comment 1: migrated (2020-02-01T08:25:43.126-0800)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: SPGoding (2020-02-02T14:27:44.610-0800)

Attached a datapack which tests this automatically after loaded.

### Comment 3: migrated (2020-05-13T21:07:12.871-0700)

Confirmed in 20w20a.

### Comment 4: intsuc (2020-11-11T22:29:50.077-0800)

Fixed in 20w46a. The entity_scores condition now uses IntRange for scores.

### Comment 5: SPGoding (2020-11-14T13:34:35.054-0800)

Can confirm the fix.

### Comment 6: bill96012 (2022-07-19T01:15:48.979-0700)

I don't think it uses the int range, the entity_scores condition after this fix can even pass the score 16777216 in both conditions  16777216 and  16777217. (tested in 20w46a and 1.19.1-pre5)

### Comment 7: SPGoding (2022-07-19T12:53:11.556-0700)

Thanks for the info, ! Upon some testing,
In 20w45a
Actual score
Predicate
Condition passes?
Should this happen?
16777216
16777216
yes

16777216
16777217
yes

16777217
16777216
yes

16777217
16777217
yes

In 20w46a
Actual score
Predicate
Condition passes?
Should this happen?
16777216
16777216
yes

16777216
16777217
yes

16777217
16777216
no

16777217
16777217
no

The behavior has changed between the two versions, so I have created a new ticket  to track the new behaviors.

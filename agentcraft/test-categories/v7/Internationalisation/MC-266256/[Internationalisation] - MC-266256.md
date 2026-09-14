# MC-266256: Accessibility button in the Welcome screen still needs its own string

**Mojira URL:** [https://bugs.mojang.com/browse/MC-266256](https://bugs.mojang.com/browse/MC-266256)

## Report details

- **Mojira categories:** Internationalisation
- **Project:** MC
- **Issue key:** MC-266256
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2023-10-30T08:27:20.928-0700
- **Updated:** 2025-04-16T13:02:32.804-0700
- **Resolution date:** 2023-11-13T07:27:00.284-0800
- **Affects versions:** 1.20.2; 23w43b; 23w44a
- **Fix versions:** 23w45a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 6
- **Attachment filenames:** cy_gb + nl_nl + el_gr + sv_se + tl_ph.png; Options menu.png; String_Bug1.png; String_Bug2.png; String_Bug3.png; Welcome screen.png
- **Issue links:** Cloners:outward:MC-261119:Accessibility button in the Welcome screen needs its own string

## Description

The Bug:
This is a clone of MC-261119.
The Accessibility settings button on the Welcome screen uses the same string as the Accessibility settings button in the Options menu (options.accessibility), which causes issues in some languages where the text doesn't fit due to the icon.
To make it extra clear (considering the misunderstanding in MC-261119):
The button shown in
 and the button shown in
 both use the string options.accessibility. The request is to make these two buttons have separate strings, for example one strings options.accessibility and the another onboarding.accessibility.
Observed Behavior:
The current string used for the Accessibility settings button on the Welcome screen is the same as for the Accessibility settings button in the Options menu.
Expected Behavior:
To ensure the Accessibility settings button on the new Welcome screen fits properly in all languages, a separate string should be added. This would align with the approach taken for other settings, where separate strings are used for different elements (for example options.sounds and options.sounds.title).
Note:
The attached examples illustrate this need for a separate string. The current behavior can make it difficult for users with accessibility needs to read and access the button. Therefore, creating a separate string is important to ensure that the feature is accessibility-friendly.

## Comments (3)

### Comment 1: migrated (2023-10-30T08:27:20.928-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: kapla (2023-11-13T07:10:16.033-0800)

Bug still occurs on version 23w45a.
Attachments:
String_Bug1.png
String_Bug2.png
String_Bug3.png

### Comment 3: [Mod] turbo (2023-11-13T07:27:00.284-0800)

Translations are not applied directly in the fix version, but only in the next snapshot, as the string still needs to be translated. As you can see, there is a new string that has not yet been translated, which is an indicator that the bug has been fixed. Please wait until 23w46a.

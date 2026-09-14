# MC-47607: Barrier particles aren't shown if particles are set to minimal

**Mojira URL:** [https://bugs.mojang.com/browse/MC-47607](https://bugs.mojang.com/browse/MC-47607)

## Report details

- **Mojira categories:** Particles; Rendering
- **Project:** MC
- **Issue key:** MC-47607
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2014-02-06T10:15:01.270-0800
- **Updated:** 2025-05-29T09:21:20.713-0700
- **Resolution date:** 2023-09-27T05:39:37.820-0700
- **Affects versions:** Minecraft 14w06b; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08a; 21w08b; 21w10a; 21w11a; 21w13a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 1.17; 1.17.1; 21w40a; 21w41a; 21w42a; 1.18 Pre-release 1; 1.18; 1.18.1; 22w03a; 22w05a; 1.18.2 Release Candidate 1; 1.18.2; 22w16b; 22w17a; 1.19; 1.19.1; 1.19.2; 22w43a; 1.19.3; 1.19.4; 1.20; 1.20.1; 23w31a
- **Fix versions:** 23w40a
- **Labels:** barrier
- **Watchers:** 2
- **Attachments:** 3
- **Attachment filenames:** 2014-02-06_22.01.53.png; MC-47607.mp4; MC-47607.png
- **Issue links:** Relates:outward:MC-203704:Candles don't show flame animations when particles are set to "Minimal" | Duplicate:inward:MC-46735:Barriers should be visible when holding one in creative | Duplicate:inward:MC-48698:Can't see barrier block texture | Duplicate:inward:MC-48721:Barrier won't show up when selected in toolbar | Duplicate:inward:MC-49037:Barriers are Invisible in Creative | Duplicate:inward:MC-51139:When Barrier Item Is Held In Inventory, The Barrier Block Texture Doesn't Appear | Duplicate:inward:MC-51347:barrier bloc | Duplicate:inward:MC-52443:barriers ALWAYS invisible | Duplicate:inward:MC-54205:Barriers not seeable | Duplicate:inward:MC-55305:you don't see the red barrier block anymore | Duplicate:inward:MC-58860:Barrier particle not showing | Duplicate:inward:MC-62640:Barrier block isn't visible while holding one | Duplicate:inward:MC-64146:You cannot see placed barriers while holding a barrier in your hand In Creative Mode | Duplicate:inward:MC-67863:Barrier Particle doesn't show | Duplicate:inward:MC-69523:barrier only visible in creative mode when particles are set to 'All' | Duplicate:inward:MC-69557:Barrier Icon/particle (Inside the barrier blocks) does not show up when holding a barrier | Duplicate:inward:MC-70311:Barrier block not visible in creative | Duplicate:inward:MC-80663:Barriers not shown when holding themselves. | Duplicate:inward:MC-119396:Barrier texture not showing when barrier item is held | Duplicate:inward:MC-120971:Barriers won't show when holding the barrier item anymore! | Duplicate:inward:MC-122938:Barrier block particle | Duplicate:inward:MC-125180:Barrier invisible while holding barrier. | Duplicate:inward:MC-127453:Barrier block is invisible at all time | Duplicate:inward:MC-139166:Barrier block doesn't appear when holding barrier (nvm, works as intended) | Duplicate:inward:MC-162075:Barriers in creative mod. | Duplicate:inward:MC-165502:Barrier Error | Duplicate:inward:MC-177156:It's fixed! Particles was minimal | Duplicate:inward:MC-194020:Barrier set | Duplicate:inward:MC-194887:Barriers will remain hidden while holding a barrier block | Duplicate:inward:MC-212593:Buggy Barrier Blocks | Duplicate:inward:MC-212718:Barrier blocks don't show particles | Duplicate:inward:MC-241176:placed barrier not rendering as it is held | Duplicate:inward:MC-245389:Invisible Barriers | Duplicate:inward:MC-254223:Barrier can not show the texture

## Description

The Bug:
Barrier particles aren't shown if particles are set to minimal.
Steps to Reproduce:
- Set your particles to "minimal" in your video settings.

- Switch into creative mode and place down a barrier block.

- Take note as to whether or not barrier particles are shown if particles are set to minimal.

Observed Behavior:
Barrier particles aren't shown.
Expected Behavior:
Barrier particles would be shown.

## Comments (12)

### Comment 1: migrated (2014-02-06T10:15:01.270-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2014-02-06T10:19:37.749-0800)

Turn your particle settings up. You have them set to minimal.

### Comment 3: migrated (2014-02-06T10:22:21.342-0800)

Thanks problem resolved!

### Comment 4: migrated (2021-01-20T00:23:21.012-0800)

I'd like to request ownership, the original reporter hasn’t been active since April 2014, I will keep it updated.

### Comment 5: migrated (2021-04-10T10:02:20.400-0700)

Still affects 21w14a - The Barrier and Light inner block visual particles should bypass the particle settings when held, which would then display them even on the Minimal Particles setting & instantly fix this problem.

### Comment 6: Avoma (2021-06-26T04:22:14.417-0700)

Can confirm in 1.17.

### Comment 7: Avoma (2021-07-13T04:13:11.924-0700)

Can confirm in 1.17.1.

### Comment 8: migrated (2021-07-30T16:10:13.864-0700)

Yes, that's how particles work. This isn't a bug. It's quite literally how the game is designed. It is a particle, so if you set the game to see no particles, you won't see it.

### Comment 9: SlimySpeck (2021-08-24T17:40:42.460-0700)

The issue that looks similar to  because when particles are set to minimal

### Comment 10: Avoma (2021-10-11T03:00:48.680-0700)

Can confirm this behavior in 21w40a. Here are some extra details regarding this problem.
The Bug:
Barrier particles aren't shown if particles are set to minimal.
Steps to Reproduce:
- Set your particles to "minimal" in your video settings.

- Switch into creative mode and place down a barrier block.

- Take note as to whether or not you are able to see barrier particles.

Observed Behavior:
Barrier particles aren't shown if particles are set to minimal.
Expected Behavior:
Barrier particles would be shown if particles are set to minimal.

### Comment 11: Avoma (2021-10-18T00:41:01.346-0700)

Can confirm in 21w41a.

### Comment 12: pulpetti (2022-01-29T12:01:38.116-0800)

In 22w03a.

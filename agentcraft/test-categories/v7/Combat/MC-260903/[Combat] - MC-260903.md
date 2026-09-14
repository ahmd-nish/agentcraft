# MC-260903: Less recent attacker can be credited for kill

**Mojira URL:** [https://bugs.mojang.com/browse/MC-260903](https://bugs.mojang.com/browse/MC-260903)

## Report details

- **Mojira categories:** Combat; Text
- **Project:** MC
- **Issue key:** MC-260903
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2023-03-10T13:09:56.398-0800
- **Updated:** 2025-04-30T03:54:24.168-0700
- **Resolution date:** 2023-07-26T03:49:42.836-0700
- **Affects versions:** 1.19.4 Release Candidate 2; 1.19.4; 23w13a
- **Fix versions:** 1.20 Pre-release 3
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** player-test-scoreboard.gif; zombie-husk-test.gif
- **Issue links:** Relates:inward:MC-260761:Taking any damage before fatal fall damage removes the attacker credited for kill | Relates:inward:MC-264420:Dead mobs can no longer appear in extended death messages | Duplicate:inward:MC-261406:Previous attacker is credited for kill despite being overridden by new attacker | Duplicate:inward:MC-261587:playerkills Scoreboard objective and player killed entity advancement do not track correctly | Duplicate:inward:MC-261727:Incorrect player kill credit using /effect and /kill from command block after player gets attacked

## Description

The bug
A less recent attacker than the one that actually caused a player's death can be credited as the killer, appearing in death messages and affecting scoreboards and statistics as mentioned in this comment.
Steps to Reproduce
1) Take one hit from a zombie
2) Take one hit from a husk afterwards
3) Run /kill
Observed result
"Player didn't want to live in the same world as Zombie"
Expected result
"Player didn't want to live in the same world as Husk" since the Husk dealt the most recent damage to the player.

## Comments (6)

### Comment 1: migrated (2023-03-10T13:09:56.398-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: InQuognito (2023-03-29T10:27:48.910-0700)

hey Mojang, you marked my ticket as Duplicate when in fact, this bug runs much deeper than death messages. It affects scoreboards and advancements at their core; It doesn't look like it's the wrong attacker, it is the wrong attacker. This is game breaking for combat maps in 1.19.4. Here are some common examples of issues that can occur because of this:
- Monster Hunter achievement could be granted to the wrong player

- PvP maps where kills are tracked as the main determining factor for the winner

- Maps that run commands at a killer; for instance, a sword with a kill effect such as "Gives player strength I for 3 seconds on kill"

- Maps that take advantage of the new death message system

- Statistics that track player kill, both in survival and mapmaking alike

### Comment 3: ampolive (2023-03-29T10:49:31.670-0700)

Updated ticket with this information.

### Comment 4: InQuognito (2023-03-29T10:57:38.744-0700)

This issue is also identifiable in 1.19.3:
https://discord.com/channels/154777837382008833/1073164131026337812

### Comment 5: InQuognito (2023-03-29T11:00:10.233-0700)

Also, our team has extensively tested this bug and it isn’t just on /kill, it’s any death whatsoever. It also seems to be extremely consistent. It isn’t a chance to happen, this seems to happen every single time (within the 5 second memory limit for attackers)

### Comment 6: migrated (2023-04-30T11:30:58.789-0700)

I've run into the same issue. The first player to hit an other player seems to get the killcredit (till the killcredit cooldown is over) and if a new player hits the same player it doesn't overwrite the previous hitter. This issue only occurs when you use you leftclick/hit a player. When you hit someone with an arrow or with tnt that carries your UUID it does overwrite it properly and gives the last hitter the killcredit.

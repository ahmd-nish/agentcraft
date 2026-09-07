# MC-121048: When an entity dies, the combat tracker only records the killing blow

**Mojira URL:** [https://bugs.mojang.com/browse/MC-121048](https://bugs.mojang.com/browse/MC-121048)

## Report details

- **Mojira categories:** Combat
- **Project:** MC
- **Issue key:** MC-121048
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2017-10-08T06:53:21.574-0700
- **Updated:** 2025-04-30T05:04:37.843-0700
- **Resolution date:** 2023-03-26T13:21:03.368-0700
- **Affects versions:** Minecraft 1.12.2; Minecraft 1.13.2; 1.15.2; 20w09a; 20w10a; 20w11a; 20w12a; 20w14a; 20w15a; 20w16a; 20w17a; 20w21a; 1.16 Pre-release 2; 1.16 Pre-release 3; 1.16 Pre-release 4; 1.16 Pre-release 7; 1.16 Pre-release 8; 1.16 Release Candidate 1; 1.16; 1.16.1; 20w27a; 20w30a; 1.16.2; 1.16.3; 20w51a; 21w14a; 21w18a; 1.17 Release Candidate 1; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w37a; 21w42a; 21w43a; 1.18 Pre-release 4; 1.18.1; 1.18.2; 22w12a; 22w14a; 22w15a; 22w17a; 1.19 Pre-release 2; 1.19; 1.19.1 Pre-release 4; 1.19.1 Pre-release 6; 1.19.1; 1.19.2; 22w42a; 22w43a; 22w44a; 22w46a; 1.19.3 Pre-release 1; 1.19.3
- **Fix versions:** 23w03a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** MC-121048.mp4; MC-121048.png
- **Issue links:** Relates:inward:MC-189692:Dying by other means than mobs when knocked back by a bee sting does not mention the bee in the death message | Relates:inward:MC-197466:Some unused Death messages | Duplicate:inward:MC-173511:Death messages relating to specific kinds of fall damage ("doomed to fall") do not work | Duplicate:inward:MC-173646:Some death messages won't show | Duplicate:inward:MC-237248:When the player was fall from knocked by a mob/player, the death message do not mention the attacker | Relates:outward:MC-260437:Death message when falling from a high place whilst on fire is different from 1.19.3

## Description

Code analysis below uses 1.19's code, deobfuscated manually using the official obfuscation mappings for 1.19.
Living entities have a CombatTracker, which tracks the details of recent hits. When such an entity is damaged, the combat tracker's recordDamage method is called to record it.
recordDamage first calls recheckStatus, which resets the tracked data if certain conditions are met. It then adds the data for the damage currently being taken.
The issue here is that, when recordDamage is called for the killing blow, recheckStatus will clear the tracker due to the condition !this.mob.isAlive() being met. This is because isAlive checks that the entity's health is above 0.
Looking at the method LivingEntity#actuallyHurt shows the problem:

```
protected void actuallyHurt(DamageSource damageSrc, float amount) {
   if (!this.isInvulnerableTo(damageSrc)) {
      amount = this.getDamageAfterArmorAbsorb(damageSrc, amount);
      amount = this.getDamageAfterMagicAbsorb(damageSrc, amount);
      float f2 = amount;
      amount = Math.max(amount - this.getAbsorptionAmount(), 0.0F);
      this.setAbsorptionAmount(this.getAbsorptionAmount() - f2 - amount);
      float f = f2 - amount;
      if (f > 0.0F && f < 3.4028235E37F && damageSrc.getEntity() instanceof ServerPlayer) {
         ((ServerPlayer)damageSrc.getEntity()).awardStat(Stats.DAMAGE_DEALT_ABSORBED, Math.round(f * 10.0F));
      }
      if (f2 != 0.0F) {
         float f1 = this.getHealth();
         this.setHealth(f1 - f2);
         this.getCombatTracker().recordDamage(damageSrc, f1, f2);
         this.setAbsorptionAmount(this.getAbsorptionAmount() - amount);
         this.gameEvent(GameEvent.ENTITY_DAMAGE);
      }
   }
}
```
The health is updated before recordDamage is called, which makes the entity show up as dead and causes the combat data to be cleared.
Then, shortly afterwards, die is called for the just-killed entity. This checks getKillCredit to determine who to credit with the kill.
getKillCredit will first consult CombatTracker#getKiller which contains logic to go through the combat history and pick out the "best" attacker.
However this logic is currently irrelevant, as due to the above issue, the tracker will only contain an entry for the killing blow and nothing else.
The solution here is to change LivingEntity#actuallyHurt to call recordDamage first, followed by setHealth.
Fixing this bug will allow for the "doomed to fall" death messages to appear.

## Comments (8)

### Comment 1: migrated (2017-10-08T06:53:21.574-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: galaxy_2alex (2020-05-22T14:19:17.472-0700)

Does this still affect the latest versions of the game (Stable 1.15.2 / Snapshot 20w21a)? If so, please update this ticket accordingly. Should the original reported be inactive and no longer contribute to the bug tracker, the reporter of the ticket can be changed to an active user.
Quick Links:
📓 Issue Guidelines – 💬 Community Support – 📧 Customer Support – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: chumbanotz (2021-06-05T16:22:34.274-0700)

I can confirm that this is still an issue in 1.17 Release Candidate 1.

### Comment 4: Arisa Bot (2021-06-05T16:22:44.531-0700)

This report is currently missing crucial information. Please take a look at the other comments to find out what we are looking for.
If you added the required information and a moderator sees your comment, they will reopen and update the report. However, if you think your update to this report has been overlooked or you want to make sure that this report is reopened, you can contact the Mojira staff on Discord or Reddit.
-- I am a bot. This action was performed automatically! If you think it was incorrect, please notify us on Discord or Reddit

### Comment 5: [Mod] ManosSef (2022-07-08T12:44:05.089-0700)

Can confirm for 1.19.1 Pre-release 4. May I request ownership?

### Comment 6: Ray (2023-03-13T12:08:45.135-0700)

seems this is still not working correctly in 1.19.4 rc3? https://youtu.be/3mZguAFyUrQ

### Comment 7: ampolive (2023-03-14T10:06:12.760-0700)

That is .

### Comment 8: AnalogMC (2023-03-26T13:21:03.368-0700)

Not 100% sure if this is the one, but fixing this bug in 1.19.4 may have caused some havoc in totalKillCount scoreboards (and similar objectives). I've been using this objective to display custom kill messages, and sometimes they showed the wrong player credited for the kill, most likely the one to deal the most damage. It was all working in 1.19.2 and before.

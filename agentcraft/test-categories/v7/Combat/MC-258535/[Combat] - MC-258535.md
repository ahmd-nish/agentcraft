# MC-258535: End crystal and TNT explosions do same damage regardless of difficulty

**Mojira URL:** [https://bugs.mojang.com/browse/MC-258535](https://bugs.mojang.com/browse/MC-258535)

## Report details

- **Mojira categories:** Combat; Player
- **Project:** MC
- **Issue key:** MC-258535
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-12-15T07:57:58.190-0800
- **Updated:** 2026-02-03T16:46:56.502-0800
- **Resolution date:** 2023-03-14T12:19:35.962-0700
- **Affects versions:** 1.19.3; 23w04a
- **Fix versions:** 23w06a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 0
- **Issue links:** Relates:inward:MC-4708:Explosion deals no damage to the player in "Peaceful" difficulty | Duplicate:inward:MC-258817:1.19.3 protection causing ender crystal damage reduce more under hard mode | Duplicate:inward:MC-259072:End Crystals deal less damage on hard mode | Relates:outward:MC-258561:Endermen teleport away instead of taking damage from end crystal, TNT and wither skull explosions | Relates:inward:MC-260993:End crystals and TNT explosions do same damage regardless of difficulty for entities except players

## Description

The Bug:
End crystals do the same damage across difficulties in 1.19.3. This also applies to TNT explosions.
This is what the damage looks like when you stand in the middle of one:
1.19.2 and previous versions:
Peaceful: 0 hp / 0 full hearts
Easy: 43.5 hp/ 21.75 full hearts
Normal: 85 hp / 42.5 full hearts
Hard: 127.5 hp / 63.75 full hearts
1.19.3:
Peaceful: 85 hp / 42.5 full hearts
Easy: 85 hp / 42.5hp full hearts
Normal: 85 hp / 42.5 hp full hearts
Hard: 85 hp / 42.5 hp full hearts
Steps to reproduce:
- Set the difficulty to anything other than normal, such as hard, peaceful, or easy.

- Spawn an end crystal.

- Observe that the end crystal does the same damage as it would on normal difficulty.

Expected behavior:
The damage from an end crystal should do the same as on version 1.19.2 and before that.
Actual behavior:
The same damage that end crystals do on normal difficulty is the same as on other difficulties.
Code analysis:
Code analysis by  can be found in this comment.

## Comments (4)

### Comment 1: etch (2022-12-16T11:29:02.944-0800)

This bug effects also affects other explosions in the game, such as TNT explosions. It doesn't affect bed and respawn anchor explosions (because their damage source is specified as a BadRespawnPointDamageSource with scaleWithDifficulty = true) and creeper explosions (because it dies and the causingEntity is null).
Code Analysis (yarn mappings):
Scaling damage with difficulty is done in the damage method of the PlayerEntity class:

```public boolean damage(DamageSource source, float amount) {
    ...
    if (source.isScaledWithDifficulty()) {
        if (this.world.getDifficulty() == Difficulty.PEACEFUL) {
            amount = 0.0f;
        }
        if (this.world.getDifficulty() == Difficulty.EASY) {
            amount = Math.min(amount / 2.0f + 1.0f, amount);
        }
        if (this.world.getDifficulty() == Difficulty.HARD) {
            amount = amount * 3.0f / 2.0f;
        }
    }
    if (amount == 0.0f) {
        return false;
    }
    return super.damage(source, amount);
}```
Whether the damage is scaled is determined on if the scaleWithDifficulty field of source is true. In the damage method of the EndCrystalEntity class, these two lines handle the explosion:

```DamageSource damageSource = source.getAttacker() != null ? DamageSource.explosion(this, source.getAttacker()) : null;
this.world.createExplosion(this, damageSource, null, this.getX(), this.getY(), this.getZ(), 6.0f, false, World.ExplosionSourceType.BLOCK);```
In the case of TNT lit by a player, it explodes without specifying the damage source, instead having a getCausingEntity method that is called in Explosion.getCausingEntity which is called in DamageSource.explosion which is called in the Explosion constructor called in World.createExplosion.
In both these cases, DamageSource.explosion is called:

```public static DamageSource explosion(@Nullable Explosion explosion) {
    return explosion != null ? DamageSource.explosion(explosion.getEntity(), explosion.getCausingEntity()) : DamageSource.explosion(null, null);
}

public static DamageSource explosion(@Nullable Entity explosion, @Nullable Entity attacker) {
    if (attacker != null && explosion != null) {
        return new ProjectileDamageSource("explosion.player", explosion, attacker).setScaledWithDifficulty().setExplosive();
    }
    if (explosion != null) {
        return new EntityDamageSource("explosion", explosion).setScaledWithDifficulty().setExplosive();
    }
    return new DamageSource("explosion").setScaledWithDifficulty().setExplosive();
}```
Because both attacker and explosion are not null, a ProjectileDamageSource is created which extends EntityDamageSource which overrides the isScaledWithDifficulty method in DamageSource.
Instead of

```public boolean isScaledWithDifficulty() {
    return this.scaleWithDifficulty;
}```
it's

```public boolean isScaledWithDifficulty() {
    return this.source instanceof LivingEntity && !(this.source instanceof PlayerEntity);
}```
This is done to have difficulty scaling apply only to mobs and not players. Since a player lit the TNT and a player hit the end crystal, this will be false, so the damage of the explosion will not be scaled.
Proposed Fix:
Change EntityDamageSource.isScaledWithDifficulty to

```public boolean isScaledWithDifficulty() {
    return this.scaleWithDifficulty || (this.source instanceof LivingEntity && !(this.source instanceof PlayerEntity));
}```
This shouldn't break anything to my knowledge.
Edit:
Because of MC-258561 and  it's probably better to create a separate damage source for explosions instead of using the one for projectiles.

### Comment 2: ampolive (2023-02-17T14:54:07.148-0800)

Can no longer reproduce in 23w07a. This seems to have been fixed, at least for players.
Edit: This seems to have been fixed in 23w06a.

### Comment 3: Fusion Fusion (2023-03-14T10:39:56.690-0700)

This should also be fixed for mobs, at least. People often use buffed zombies as dummies to practice Crystal PvP, so it's a shame that the lowered damage still applies for mobs.

### Comment 4: ampolive (2023-03-14T10:43:49.305-0700)

Please create a new ticket for this issue.

# MC-150183: Iron golems produce walking particles for barrier blocks

**Mojira URL:** [https://bugs.mojang.com/browse/MC-150183](https://bugs.mojang.com/browse/MC-150183)

## Report details

- **Mojira categories:** Particles
- **Project:** MC
- **Issue key:** MC-150183
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2019-04-28T08:33:34.723-0700
- **Updated:** 2025-05-29T09:20:49.254-0700
- **Resolution date:** 2023-09-01T06:05:06.822-0700
- **Affects versions:** Minecraft 1.14; Minecraft 1.14.3 Pre-Release 3; 1.15.1; 1.16.2; 20w51a; 21w03a; 1.16.5; 21w06a; 21w07a; 21w08b; 21w10a; 21w20a; 1.17 Release Candidate 2; 1.17; 1.17.1; 21w41a; 1.18.1; 1.18.2; 22w12a; 1.19; 1.19.1 Pre-release 1; 1.19.2; 1.19.3; 23w05a
- **Fix versions:** 1.20 Pre-release 3
- **Labels:** barrier; block; invisible-blocks; iron_golem; particles
- **Watchers:** 2
- **Attachments:** 6
- **Attachment filenames:** 2019-04-28_11.29.29.png; 2019-04-28_11.29.31.png; MC-150183.mp4; MC-150183.png; MC-150183 - Current Code.png; MC-150183 - Fixed Code.png
- **Issue links:** Relates:outward:MC-122547:Barriers can produce fall particles

## Description

The Bug
When anything other than iron golems walk on barriers, walk particles don't appear. This makes sense since the block is invisible. What doesn't make sense is the fact that when an iron golem walks on a barrier block, red walk particles appear when I don't think they should.
Steps to Reproduce
- Switch into creative mode, give yourself some barriers, and place them down.

```
/give @s minecraft:barrier
```

- Summon an iron golem on top of the barrier blocks and wait for it to begin walking.

- Take note as to whether or not iron golems produce walking particles when traveling over barrier blocks.

Observed Behavior
Iron golems produce walking particles when traveling over barrier blocks.
Expected Behavior
Iron golems would not produce walking particles when traveling over barrier blocks.

## Comments (17)

### Comment 1: migrated (2019-04-28T08:33:34.723-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: Avoma (2020-12-21T04:22:13.131-0800)

Can confirm in 20w51a.

### Comment 3: Avoma (2021-02-01T10:22:21.956-0800)

Can confirm in 21w03a.

### Comment 4: Avoma (2021-02-17T05:33:41.784-0800)

Can confirm in 21w06a.

### Comment 5: Avoma (2021-02-23T08:14:35.253-0800)

Can confirm in 21w07a.

### Comment 6: Avoma (2021-03-01T07:02:30.495-0800)

Can confirm in 1.16.5 and 21w08b.

### Comment 7: Avoma (2021-03-15T02:30:10.449-0700)

Can confirm in 21w10a. Video attached.

### Comment 8: Avoma (2021-07-29T07:00:51.626-0700)

Can confirm in 1.17.1.

### Comment 9: Avoma (2021-10-20T03:04:00.292-0700)

I am able to confirm this behavior in 21w41a. Here are some extra details regarding this problem.
The Bug:
Iron golems produce walking particles when traveling over barrier blocks.
Steps to Reproduce:
- Switch into creative mode, give yourself some barriers, and place them down.

```/give @s minecraft:barrier```
- Summon an iron golem on top of the barrier blocks and wait for it to begin walking.

- Take note as to whether or not iron golems produce walking particles when traveling over barrier blocks.

Observed Behavior:
Iron golems produce walking particles when traveling over barrier blocks.
Expected Behavior:
Iron golems would not produce walking particles when traveling over barrier blocks.

### Comment 10: Avoma (2021-12-06T01:40:09.948-0800)

I can confirm this behavior in 1.18. Here's a code analysis of this issue.
Code Analysis:
The following is based on a decompiled version of Minecraft 1.19.2 using MCP-Reborn.
net.minecraft.world.entity.animal.IronGolem.java

```public class IronGolem extends AbstractGolem implements NeutralMob {
   ...
   public void aiStep() {
      super.aiStep();
      ...
      if (this.getDeltaMovement().horizontalDistanceSqr() > (double)2.5000003E-7F && this.random.nextInt(5) == 0) {
         int i = Mth.floor(this.getX());
         int j = Mth.floor(this.getY() - (double)0.2F);
         int k = Mth.floor(this.getZ());
         BlockState blockstate = this.level.getBlockState(new BlockPos(i, j, k));
         if (!blockstate.isAir()) {
            this.level.addParticle(new BlockParticleOption(ParticleTypes.BLOCK, blockstate), this.getX() + ((double)this.random.nextFloat() - 0.5D) * (double)this.getBbWidth(), this.getY() + 0.1D, this.getZ() + ((double)this.random.nextFloat() - 0.5D) * (double)this.getBbWidth(), 4.0D * ((double)this.random.nextFloat() - 0.5D), 0.5D, ((double)this.random.nextFloat() - 0.5D) * 4.0D);
         }
      }
      ...```
If we look at the above class, we can see that there is only one necessary check that is carried out before allowing an iron golem to produce walking particles. This check is to see if the block below them is air, and if it is, walking particles won't be produced, but if it isn't, walking particles based on the block that the iron golem is standing on will be produced. The game doesn't check the RenderShape of the block that the iron golem standing on before allowing it to produce walking particles, therefore resulting in this problem occurring.
Fix:
Simply changing some lines of code to check the RenderShape of the block that the iron golem is standing on before allowing it to produce walking particles, will resolve this problem.
Current Code:

```...
BlockState blockstate = this.level.getBlockState(new BlockPos(i, j, k));
if (!blockstate.isAir()) {
...```
Fixed Code:

```...
BlockPos blockpos = new BlockPos(i, j, k);
BlockState blockstate = this.level.getBlockState(blockpos);
if (blockstate.getRenderShape() != RenderShape.INVISIBLE) {
...```

### Comment 11: Avoma (2022-01-02T06:18:22.796-0800)

Can confirm in 1.18.1.

### Comment 12: Avoma (2022-03-31T09:15:58.260-0700)

Can confirm in 1.18.2.

### Comment 13: Avoma (2022-06-22T10:52:07.689-0700)

Can confirm in 1.19 and 1.19.1 Pre-release 1.

### Comment 14: Avoma (2022-09-25T05:38:36.685-0700)

Can confirm in 1.19.2.

### Comment 15: Avoma (2022-10-08T15:48:44.567-0700)

Following on from my code analysis, I've double-checked my proposed fix and I can confidently confirm that it's fully functioning and works as expected, so I've attached two screenshots to this report, one of which shows the current code and the other that shows the fixed code. I feel this information may be quite insightful hence my reasoning for providing it.

### Comment 16: muzikbike (2023-06-01T05:52:33.809-0700)

This does not seem to happen anymore as of 1.20-rc1. Can we find the exact fix version (possibly pre-release 3 as per )?

### Comment 17: Avoma (2023-08-21T01:16:54.469-0700)

This issue was present in 1.20 Pre-release 2, but no longer occurs in versions above or equal to 1.20 Pre-release 3. This issue was fixed in 1.20 Pre-release 3.

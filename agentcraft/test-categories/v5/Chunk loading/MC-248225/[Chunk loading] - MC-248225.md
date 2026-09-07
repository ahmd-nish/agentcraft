# MC-248225: Incorrect BlockPos getSquaredDistance() calculation

**Mojira URL:** [https://bugs.mojang.com/browse/MC-248225](https://bugs.mojang.com/browse/MC-248225)

## Report details

- **Mojira categories:** Chunk loading
- **Project:** MC
- **Issue key:** MC-248225
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2022-01-22T13:56:14.475-0800
- **Updated:** 2025-04-29T20:12:54.093-0700
- **Resolution date:** 2022-01-29T04:43:22.787-0800
- **Affects versions:** 1.14.4; 1.18.1; 22w03a
- **Fix versions:** 22w05a
- **Labels:** POI; geode; pathfinding; portal; raid; rendering; world-generation
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** image-2022-01-22-16-55-48-277.png; MC-248225.zip

## Description

The Bug
Calculation of BlockPos getSquaredDistance() is incorrect; the method is used to get the distance between two BlockPos, which return offset. This method was not intended to be used against two BlockPos, although it is used everywhere. Recent code like Sculk Sensors does it correctly by specifying that it should not be treated as a BlockPos. This results in issues across several parts of the game, including geode generation, chunk rendering, points of interest (POI) and pathfinding in general.
Attached below is an image visualizing the current broken calculation and the expected calculation.
Code Analysis
Code analysis using 1.18.1 Yarn Mappings.
If you look at this code:

```
BlockPos.ORIGIN.getSquaredDistance(BlockPos.ORIGIN)
```
When run you would expect the result to be 0, although the value is actually 0.75.
This is due to getSquaredDistance automatically setting treatAsBlockPos to true, which in this case shouldn't happen since it's already a BlockPos. Here's the code for getSquaredDistance:
net.minecraft.util.math.Vec3i.class

```
public double getSquaredDistance(Vec3i vec) {
    //By default: treatAsBlockPos is true
    return this.getSquaredDistance(vec, true);
}

public double getSquaredDistance(Position pos, boolean treatAsBlockPos) {
    return this.getSquaredDistance(pos.getX(), pos.getY(), pos.getZ(), treatAsBlockPos);
}

public double getSquaredDistance(Vec3i vec, boolean treatAsBlockPos) {
    return this.getSquaredDistance((double)vec.x, (double)vec.y, (double)vec.z, treatAsBlockPos);
}

public double getSquaredDistance(double x, double y, double z, boolean treatAsBlockPos) {
    //Add 0.5D if it should be converted to a blockpos
    double d = treatAsBlockPos ? 0.5D : 0.0D;
    double e = (double)this.getX() + d - x;
    double f = (double)this.getY() + d - y;
    double g = (double)this.getZ() + d - z;
    return e * e + f * f + g * g;
}
```
As you can see. Asking for the distance between two BlockPos adds 0.5D, which it should not do since BlockPos is already a BlockPos...
Fix
The fix is simply to override getSquaredDistance in BlockPos so treatAsBlockPos is set to false by default.
Alternatively, you could just change the default to false, since the default value is only ever used for BlockPos calculations. Yes...
Steps to recreate
Download the world zip & follow the instructions. It will show you one of the many directional bias that this bug adds.

Affected methods
Now it's time to mention what exactly is broken by this code.
Method Naming Format uses both 1.18.1 Yarn Mappings (left) and Mojang Mappings (right).
You will notice a pattern with these, usually it's the distance formula having an offset center.
- WorldRenderer#method_38549 / LevelRenderer#initializeQueueForFullUpdate
Chunk Render Queue will load in the wrong order under specific conditions. Due to the distance sorting using an offset distance. Favors negative coordinates.

- WorldRenderer#updateChunks / LevelRenderer#compileChunks
If using chunkBuilderMode: NEARBY then the chunks that are chosen to render immediately because they are nearby will contain chunks that actually shouldn't be considered nearby, and might be missing chunks that should be considered nearby.

- LongJumpTask#run / LongJumpToRandomPos#start
The wrong jump might be chosen due to offset distance center calculation.

- WalkHomeTask#shouldRun / SetClosestHomeAsWalkTarget#checkExtraStartConditions
Distance needs to be below 4 blocks away to be able to run the task. Due to the bug, it's possible for locations that are 6.75 blocks away to be valid!
After running calculations that means that some positions can be offset by up to 3.75 for this task.

- WanderAroundTask#keepRunning / MoveToTargetSink#tick
If the distance to the next target is bigger than 4 then it will go to that location. Due to this bug, its possible for the location to be 0.75 blocks away while still being valid

- MoveThroughVillageGoal#canStart / MoveThroughVillageGoal#canUse
When starting the goal, villagers search for POI's within the village near them. The distance calculation center is offset which sometimes results in invalid POI's being chosen.

- MobEntity#isInWalkTargetRange / Mob#isWithinRestriction
On average there's an 8.30% chance of failing every time due to the bug. If the entity is leashed, the failure chance is 23.64%. If the entity is not leashed the failure chance is 7.80%. All these failures are just due to miss calculations of the BlockPos distance. A failure is when it returns the opposite boolean value that it should have due to the distance being incorrect.
This is actually the cause of Mob Pathfinding being directional. It's been noticed many times but a bug report does not seem to exist on it. I noticed that mobs group up over time in the North West (,) corner a lot more often.
Turns out that it's caused by this bug.
I will actually be making another bug report of this one specifically cause I have a lot more technical descriptions nevermind I'm too lazy

- BeeEntity$FindHiveGoal#getNearbyFreeHives / Bee$BeeLocateHiveGoal#findNearbyHivesWithSpace
Favors negative coordinates and sometimes picks negative coordinate even if a positive coordinate is closer

- GravityField$Point#getGravityFactor / PotentialCalculator$PointCharge#getPotentialChange
Have not dug into this one yet. Although I believe it just makes the gravity factors/potential charge weaker and higher when it shouldn't be

- Raid#moveRaidCenter / Raid#moveRaidCenterToNearbyVillageSection
Distance calculation for the POI's to choose is offset. Basically making the raid center calculation offset, resulting in some invalid blocks being valid, and some valid blocks becoming invalid.

- Raid#removeObsoleteRaiders / Raid#updateRaiders
If a raider is more than 12544 distance away, he will be removed from the raid.
Although there's a chance that he's removed earlier at: 12352.75 or much further at: 12662.75

- RaidManager#getRaidAt / Raids#getNearbyRaid
The raid center distance is offset, causing some raids which are in range to not be valid. While others that aren't supposed to be in range can be chosen.

- PortalForcer#createPortal
Portal placing location might be further than the closest location, some locations that should be in range also become invalid.

- ChunkGenerator#locateStructure / ChunkGenerator#findNearestMapFeature
When searching for strongholds. After the first stronghold is found, if there is a stronghold that's even closer, it might miss it due to the bug.

- ForestRockFeature#generate / BlockBlobFeature#place
When placing rocks for the Forest Rock Feature. Some valid spots will be invalid while other spots that were invalid are now valid.

- GeodeFeature#generate / GeodeFeature#place
Causes some deformation in the geode shape & block placement

- PointOfInterestStorage#getInCircle / PoiManager#getInRange
The range center is offset, causing some blocks which are in range to not be valid. While others that aren't supposed to be valid can be chosen.

- PointOfInterestStorage#getSortedPositions / PoiManager#findAllClosestFirst
Sorts the POI's in the incorrect order, due to some distances seeming closer than they are.

- PointOfInterestStorage#getNearestPosition / PoiManager#findClosest
Sorts the POI's in the incorrect order, due to some distances seeming closer than they are. Causing the first POI to be pulled out to sometimes be incorrect

- GameEventDebugRenderer$Listener#isTooFar / GameEventListenerRenderer$TrackedListener#isExpired
Might not expire/remove itself at right time xD

I am so sorry if you read through that entire thing...
Most of these are used in many other places. Which becomes a nice little maze to traverse.
TL;DR this is terribly broken

## Comments (2)

### Comment 1: migrated (2022-01-22T13:56:14.475-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: FX - PR0CESS (2022-01-22T16:59:44.451-0800)

This has been in the game since at least 1.14.4
Not sure before then

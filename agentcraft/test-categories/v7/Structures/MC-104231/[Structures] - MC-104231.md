# MC-104231: Loading a custom structure doesn't load rails correctly

**Mojira URL:** [https://bugs.mojang.com/browse/MC-104231](https://bugs.mojang.com/browse/MC-104231)

## Report details

- **Mojira categories:** Structures
- **Project:** MC
- **Issue key:** MC-104231
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2016-06-22T12:45:18.323-0700
- **Updated:** 2025-04-26T05:08:29.041-0700
- **Resolution date:** 2025-04-11T09:25:19.310-0700
- **Affects versions:** Minecraft 1.10; Minecraft 1.10.1; Minecraft 1.10.2; Minecraft 16w33a; Minecraft 1.12.2; Minecraft 1.13-pre3; 1.16.1; 20w28a; 1.16.3; 1.17.1; 1.18; 1.19; 1.20.1; 1.20.4; 1.21
- **Fix versions:** 25w16a
- **Area:** Platform
- **Game mode:** Creative
- **Labels:** rails; structure_block
- **Watchers:** 1
- **Attachments:** 4
- **Attachment filenames:** 180 degree rotation rail bug.png; NBTData.jpg; Step1.png; Step2.png
- **Issue links:** Relates:inward:MC-148191:Rails don't generate properly in mansion rooms | Relates:outward:MC-248855:Structure blocks do not rotate item frames correctly when loading in certain cases | Duplicate:inward:MC-268435:Rails sometimes generate in the wrong orientation in custom structures | Relates:outward:MC-42375:DataValue of Rail ignored when using /setblock /clone /fill | Duplicate:inward:MC-196102:Rails Rotation is missing two cases. | Duplicate:inward:MC-196041:Structure blocks sometimes break powered rails | Duplicate:inward:MC-132023:Structure blocks mess up rails | Duplicate:inward:MC-105242:Structure block error with rails

## Description

What is happening?
Probably Minecraft have bad days and don't want to load world/structures/structure.nbt/palette/(noname)/Properties/shape
String
.
Unexpected is that the shape String is loaded normally for stairs that have also this variable.
How to reproduce
- Build some rail art as shown on

- . You have to build it in the directions of the world shown in screenshot.

- Save it as a new structure using a structure block

- When you load this structure first time, you will see that it messed up the rail art as can be seen on

- When you load it second time, it will load normally

Code analysis
Code analysis by  can be found in this comment.

## Comments (13)

### Comment 1: migrated (2016-06-22T12:45:18.323-0700)

This comment contained multiple image attachments (4), please login to view the attachments.

### Comment 2: migrated (2016-06-22T23:53:28.592-0700)

Confirmed for 1.10-pre2, 1.10-pre1, 16w21b, 16w20a

### Comment 3: migrated (2016-06-23T08:49:56.290-0700)

Confirmed for 1.10.2

### Comment 4: migrated (2016-08-23T17:46:33.254-0700)

Still an issue in 16w33a.
Also probably won't be fixed for the same reason it wasn't in MC-42375 (because of Searge's comment on MC-31365)

### Comment 5: migrated (2018-01-29T16:20:52.855-0800)

Structure blocks have a bug rotating rails. The 90 and 270 degree rotation work fine but 180 degree have a bug where straight rails can rotate into a broken state when loading in a structure with straight rails. All other types of rails, curved or sloped rails can get into an odd state but when attempting to reload the structure a 2nd time the reload fixes the miss connected rails, all but the straight rails. Picture attached shows the bug were straight rails are saved into the structure and when the structure is rotated 180 degrees the rails don’t load correctly.
This is caused by rails having no set 180 degree rotation. The switch case lacks that rotation as it naturally doesn't have to rotate. But what happens is that the default rotation is chosen and the default rotation is the same rotation you place rails at. In some instances this angle is 90 degrees from the single placed rail causing the error. BlockRail.java, BlockRailDetector.java and BlockRailPowered.java all have the same exact method “withRotation”. This method lacks the 3 180 orentations that are related to straight rails. The switch statement fails and the rotation ends up setting the default rail orientation for the straight rails.
Code suggestion would be to move this method to the superclass and add the missing rotations to the 180 degree turn. Code suggestion for clarity.

```public IBlockState withRotation(IBlockState state, Rotation rot)
    {
        switch (rot)
        {
            case CLOCKWISE_180:
                switch ((BlockRailBase.EnumRailDirection)state.getValue(SHAPE))
                {
                    // missing direction statement.
                    case NORTH_SOUTH:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.NORTH_SOUTH);
                    // and this one.
                    case EAST_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.EAST_WEST);

                    case ASCENDING_NORTH:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_SOUTH);

                    case ASCENDING_SOUTH:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_NORTH);

                    case SOUTH_EAST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.NORTH_WEST);

                    case SOUTH_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.NORTH_EAST);

                    case NORTH_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.SOUTH_EAST);

                    case NORTH_EAST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.SOUTH_WEST);
                }

            case COUNTERCLOCKWISE_90:
                switch ((BlockRailBase.EnumRailDirection)state.getValue(SHAPE))
                {
                    case ASCENDING_EAST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_NORTH);

                    case ASCENDING_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_SOUTH);

                    case ASCENDING_NORTH:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_WEST);

                    case ASCENDING_SOUTH:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_EAST);

                    case SOUTH_EAST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.NORTH_EAST);

                    case SOUTH_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.SOUTH_EAST);

                    case NORTH_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.SOUTH_WEST);

                    case NORTH_EAST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.NORTH_WEST);

                    case NORTH_SOUTH:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.EAST_WEST);

                    case EAST_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.NORTH_SOUTH);
                }

            case CLOCKWISE_90:
                switch ((BlockRailBase.EnumRailDirection)state.getValue(SHAPE))
                {
                    case ASCENDING_EAST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_SOUTH);

                    case ASCENDING_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_NORTH);

                    case ASCENDING_NORTH:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_EAST);

                    case ASCENDING_SOUTH:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.ASCENDING_WEST);

                    case SOUTH_EAST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.SOUTH_WEST);

                    case SOUTH_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.NORTH_WEST);

                    case NORTH_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.NORTH_EAST);

                    case NORTH_EAST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.SOUTH_EAST);

                    case NORTH_SOUTH:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.EAST_WEST);

                    case EAST_WEST:
                        return state.withProperty(SHAPE, BlockRailBase.EnumRailDirection.NORTH_SOUTH);
                }

            default:
                return state;
        }
    }```

### Comment 6: migrated (2018-06-25T17:39:47.429-0700)

I get bugged rails even with no rotation applied.
 By the way, confirmed for 1.13-pre3.

### Comment 7: markderickson (2020-07-09T07:21:30.890-0700)

Hi there!
I can confirm this for 1.16.1 and 20w28a.

### Comment 8: Nethonos (2021-08-26T07:51:19.440-0700)

Can confirm for 1.17.1

### Comment 9: Nethonos (2021-11-23T05:28:41.092-0800)

Can confirm in 1.18-pre6

### Comment 10: Nethonos (2021-12-03T05:02:59.058-0800)

Can confirm in 1.18

### Comment 11: Sniper1.1 (2022-10-23T05:29:05.679-0700)

can confirm in 1.19

### Comment 12: Gatinh0 (2023-07-07T16:45:24.027-0700)

Can confirm for 1.20.1.
This affects not just creative mode loading structure blocks, but also datapacks procedurally loading a structure during worldgen such as a village house or a street.

### Comment 13: Sniper1.1 (2023-10-06T08:25:32.167-0700)

This isn't completely fixed in 23w40a, but is better. It seems rails for the most part do load properly, but in instances like Step1.png and Step2.png where multiple rails run near each other, they may connect incorrectly. However, issues as seen in 180 degree rotation rail bug.png seem resolved. So, improvements have been made but overall this issue is still somewhat present in 23w40a.

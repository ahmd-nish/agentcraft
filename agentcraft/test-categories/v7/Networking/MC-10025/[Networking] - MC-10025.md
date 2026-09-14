# MC-10025: Burn time indicator of a furnace not working correctly after reloading the world

**Mojira URL:** [https://bugs.mojang.com/browse/MC-10025](https://bugs.mojang.com/browse/MC-10025)

## Report details

- **Mojira categories:** Networking
- **Project:** MC
- **Issue key:** MC-10025
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2013-02-18T20:05:40.602-0800
- **Updated:** 2025-04-26T02:40:36.582-0700
- **Resolution date:** 2024-11-22T03:55:00.723-0800
- **Affects versions:** Minecraft 1.4.7; Snapshot 13w07a; Minecraft 1.5; Snapshot 13w11a; Minecraft 1.5.1; Minecraft 1.5.2; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 13w36a; Minecraft 13w36b; Minecraft 1.7.4; Minecraft 1.7.10; Minecraft 1.10.2; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w38a; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w48a; Minecraft 17w50a; Minecraft 18w01a; Minecraft 18w03b; Minecraft 18w06a; Minecraft 18w09a; Minecraft 18w10d; Minecraft 18w20c; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 19w14a; Minecraft 1.14.3; 1.14.4; 19w39a; 1.15 Pre-release 6; 1.15.1; 20w07a; 1.16; 1.16.1; 1.16.2; 1.16.3 Release Candidate 1; 1.16.3; 1.16.4 Pre-release 1; 1.16.4 Pre-release 2; 1.16.4; 20w45a; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w14a; 21w15a; 21w16a; 21w17a; 21w18a; 21w19a; 21w20a; 1.17 Pre-release 1; 1.17 Pre-release 4; 1.17; 1.17.1 Pre-release 1; 1.17.1; 21w37a; 21w41a; 1.18 Pre-release 7; 1.18 Pre-release 8; 1.19; 1.19.2; 1.19.3; 23w03a; 23w04a; 23w05a; 23w06a; 23w07a; 1.19.4 Pre-release 3; 1.19.4; 23w13a; 23w14a; 1.20 Pre-release 1; 1.20 Pre-release 2; 1.20 Pre-release 4; 1.20.1; 23w31a; 23w32a; 23w33a; 23w35a; 1.20.2 Pre-release 1; 1.20.2 Pre-release 2; 1.20.2; 23w40a; 23w41a; 23w42a; 23w44a; 1.20.4; 24w03b; 24w04a; 24w05a; 24w11a; 24w12a; 1.20.6; 1.21; 1.21.3
- **Fix versions:** 1.21.4 Pre-Release 2
- **Area:** Platform
- **Labels:** furnace; rendering; smelting
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** 2016-09-19_14.59.18.png; 23w31a.png; Snippet.txt
- **Issue links:** Relates:outward:MC-274088:Spawn chunks do not load most things except redstone | Relates:inward:MC-26304:Brewing stands reset brew cycle when unloaded | Duplicate:inward:MC-269927:Fuel indicator (fire symbol) in furnace resets to full on world reload if no fuel is present. | Relates:inward:MC-264260:Furnace GUI is displayed incorrectly when modifying block data | Relates:inward:MC-80938:Non-default BurnTime, CookTime and CookTimeTotal values of furnace can cause GUI to be displayed incorrectly | Duplicate:inward:MC-265797:Furnace doesn't store initial burn time. | Duplicate:inward:MC-264677:Furnace GUI is sometimes displayed incorrectly after relogging | Duplicate:inward:MC-242790:The progress bar of furnace displays wrongly after reload the game | Duplicate:inward:MC-229700:Infinite furnace | Duplicate:inward:MC-172513:Furnace fuel bug in snapshot 20w07a and Nether loading sound while in furnace UI. | Duplicate:inward:MC-199798:Furnace Smelting Rendering Animation Offset | Duplicate:inward:MC-205978:furnace visual bug after game crash | Duplicate:inward:MC-201776:Blast furnace refill of fuel in nether | Duplicate:inward:MC-195242:Going in and out of the nether resets the instance of a fuel in a Furnace. | Duplicate:inward:MC-194129:The furnace fuel indicator does not run out until the last item. | Duplicate:inward:MC-193199:visual "Infinite" fuel glitch with lava | Duplicate:inward:MC-191271:Furnace Won't show how much fuel is Left when I quit and rejoin | Duplicate:inward:MC-169324:Viewing a furnace during a server restart refreshes the fuel consumed | Duplicate:inward:MC-129851:Furnace interface bug | Duplicate:inward:MC-120834:Infinite fuel in Furnace | Duplicate:inward:MC-27369:Lava Furnace Bug | Duplicate:inward:MC-24413:Furnace Fire Meter Inaccuracy | Duplicate:inward:MC-37534:A furnace can lose track of progress, flame only starts down when less than a smelt's worth of time remains. | Duplicate:inward:MC-28415:Forever Burning Furnace- Hopper use glitch? | Duplicate:inward:MC-9288:Leaving game when furnace is on causes it to burn repeatedly | Duplicate:inward:MC-28309:Coal Block is an infinite source of fire power | Duplicate:inward:MC-52555:Lava Fuel in Furnace | Duplicate:inward:MC-48292:furnace fuel level indicator not updating for Lava Buckets after save&quit and relogin. single player. | Duplicate:inward:MC-25812:Infinite Furnace with coal block when I leave it burning while I go to the nether in hardcore | Duplicate:inward:MC-21643:Furnaces with semi-infinite fuel! | Duplicate:inward:MC-19821:furnace power entering and coming back from nether | Duplicate:inward:MC-16379:furnaces don't display fire level | Duplicate:inward:MC-12954:furnance that dosent stop smealting

## Description

The bug
When you start a furnace burning and then swap out what's in the fuel slot and save and quit, the next time you load the burn time indicator will glitch. The reason for this is that the NBT file for furnaces does not store the max fuel burn time and instead dynamically gets it from the fuel slot, which may no longer contain the same item as was used to initially fuel the furnace. This can be seen in the code snippet attached.
To reproduce
- Start furnace burning with a fuel other than a stick.

- Allow the burn time to visibly decrease.

- Swap the fuel with something that burns shorter than the original fuel.

- Save and quit.

- Reload the save.

- Open the furnace.

- The burn time indicator will have increased.

With particularly large differences (lava bucket to stick), the progress bar may wrap around the top of the screen and display twice (see
).
Fix
Rather than attempting to guess the total burn time of the original item, it should be saved too:
TileEntityFurnace

```
public void readFromNBT(NBTTagCompound compound)
    {
        super.readFromNBT(compound);
        this.furnaceItemStacks = NonNullList.<ItemStack>withSize(this.getSizeInventory(), ItemStack.EMPTY);
        ItemStackHelper.loadAllItems(compound, this.furnaceItemStacks);
        this.furnaceBurnTime = compound.getShort("BurnTime");
        this.cookTime = compound.getShort("CookTime");
        this.totalCookTime = compound.getShort("CookTimeTotal");
        //this.currentItemBurnTime = getItemBurnTime(this.furnaceItemStacks.get(1));
        this.currentItemBurnTime = compound.getShort("BurnTimeTotal"); // added

        if (compound.hasKey("CustomName", 8))
        {
            this.furnaceCustomName = compound.getString("CustomName");
        }
    }

    public NBTTagCompound writeToNBT(NBTTagCompound compound)
    {
        super.writeToNBT(compound);
        compound.setShort("BurnTime", (short)this.furnaceBurnTime);
        compound.setShort("CookTime", (short)this.cookTime);
        compound.setShort("CookTimeTotal", (short)this.totalCookTime);
        compound.setShort("BurnTimeTotal", (short)this.currentItemBurnTime); // added
        ItemStackHelper.saveAllItems(compound, this.furnaceItemStacks);

        if (this.hasCustomName())
        {
            compound.setString("CustomName", this.furnaceCustomName);
        }

        return compound;
    }
```

## Comments (42)

### Comment 1: migrated (2013-02-18T20:05:40.602-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2013-02-21T11:30:18.503-0800)

Unable to reproduce. Please provide a step by step list on how to reproduce. ie:
1. do this
2. now this
3. and finally this

### Comment 3: migrated (2013-02-21T14:04:30.256-0800)

Confirmed in 13w07a. Just a visuall glitch with the burn time indicator, the burning process is correctly finished after smelting the amount of items according to the fuel type.

### Comment 4: migrated (2013-02-26T09:24:20.030-0800)

The fuel source does not need to be swapped, either. Simply unloading the chunk and loading it again is enough to trigger the glitch.
I first noticed it when I used lava buckets to start a bunch of furnaces and went to the Nether to refill the buckets. When I came back, this glitch had appeared.

### Comment 5: migrated (2013-05-03T00:07:25.794-0700)

Can confirm in 1.5.2 using lava buckets. Apparently, empty bucket or its removal is being treated as if you were swapping the fuel.

### Comment 6: kumasasa (2013-06-29T15:56:30.251-0700)

Confirmed for 1.6.1 and block of coal

### Comment 7: migrated (2013-09-08T03:43:26.646-0700)

This still happens in 1.6.2, and the 1.7 snapshots.

### Comment 8: migrated (2014-01-24T07:46:55.431-0800)

I can confirm this for version 14w04a

### Comment 9: migrated (2014-01-24T07:50:15.059-0800)

Galaxy_2Alex - I don't see the 14w03b as released as of right this moment, just the tweet that it is coming "sometime today"
EDIT: and 3 minutes later, there it is....

### Comment 10: migrated (2014-07-21T14:52:54.484-0700)

I can confirm this on 1.7.10
It is just a visual glitch though, so there is no need to put this as a high priority really.

### Comment 11: galaxy_2alex (2014-10-25T04:27:00.367-0700)

Is this still a concern in the current Minecraft version 1.8.1 Prerelease 3 / Launcher version 1.5.3 or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 12: migrated (2016-03-17T08:59:33.892-0700)

No response for over a year.

### Comment 13: migrated (2016-07-29T13:23:45.270-0700)

Confirmed for 1.10.2
Also relating to MC-64354 (coal blocks not decreasing)

### Comment 14: migrated (2018-08-25T04:36:50.167-0700)

Confirmed for 1.13.1.

### Comment 15: migrated (2019-07-16T13:41:26.567-0700)

confirmed for 1.14.3, happens also with lava bucket without intentional switching out of fuel item since full bucket changes to empty bucket

### Comment 16: migrated (2020-06-24T14:34:56.079-0700)

Can confirm for 1.16.1

### Comment 17: pulpetti (2020-07-17T05:20:06.321-0700)

Can confirm for 20w29a

### Comment 18: migrated (2020-11-07T09:49:05.857-0800)

Confirmed for 1.16.4

### Comment 19: Brevort (2021-05-30T16:40:36.629-0700)

Does this also occur when switching dimensions or unloading and reloading the chunks in ways other than reloading the world?
Never mind, that's MC-137146.

### Comment 20: Avoma (2022-09-14T12:19:09.899-0700)

Can confirm in 1.19.2.

### Comment 21: j_p_smith (2023-08-10T06:53:43.635-0700)

The broken GUI is fixed in 23w32a, but the burn time indicator is still incorrect.

### Comment 1: migrated (2013-02-18T20:05:40.602-0800)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: migrated (2013-02-21T11:30:18.503-0800)

Unable to reproduce. Please provide a step by step list on how to reproduce. ie:
1. do this
2. now this
3. and finally this

### Comment 3: migrated (2013-02-21T14:04:30.256-0800)

Confirmed in 13w07a. Just a visuall glitch with the burn time indicator, the burning process is correctly finished after smelting the amount of items according to the fuel type.

### Comment 4: migrated (2013-02-26T09:24:20.030-0800)

The fuel source does not need to be swapped, either. Simply unloading the chunk and loading it again is enough to trigger the glitch.
I first noticed it when I used lava buckets to start a bunch of furnaces and went to the Nether to refill the buckets. When I came back, this glitch had appeared.

### Comment 5: migrated (2013-05-03T00:07:25.794-0700)

Can confirm in 1.5.2 using lava buckets. Apparently, empty bucket or its removal is being treated as if you were swapping the fuel.

### Comment 6: kumasasa (2013-06-29T15:56:30.251-0700)

Confirmed for 1.6.1 and block of coal

### Comment 7: migrated (2013-09-08T03:43:26.646-0700)

This still happens in 1.6.2, and the 1.7 snapshots.

### Comment 8: migrated (2014-01-24T07:46:55.431-0800)

I can confirm this for version 14w04a

### Comment 9: migrated (2014-01-24T07:50:15.059-0800)

Galaxy_2Alex - I don't see the 14w03b as released as of right this moment, just the tweet that it is coming "sometime today"
EDIT: and 3 minutes later, there it is....

### Comment 10: migrated (2014-07-21T14:52:54.484-0700)

I can confirm this on 1.7.10
It is just a visual glitch though, so there is no need to put this as a high priority really.

### Comment 11: galaxy_2alex (2014-10-25T04:27:00.367-0700)

Is this still a concern in the current Minecraft version 1.8.1 Prerelease 3 / Launcher version 1.5.3 or later? If so, please update the affected versions in order to best aid Mojang ensuring bugs are still valid in the latest releases/pre-releases.

### Comment 12: migrated (2016-03-17T08:59:33.892-0700)

No response for over a year.

### Comment 13: migrated (2016-07-29T13:23:45.270-0700)

Confirmed for 1.10.2
Also relating to MC-64354 (coal blocks not decreasing)

### Comment 14: migrated (2018-08-25T04:36:50.167-0700)

Confirmed for 1.13.1.

### Comment 15: migrated (2019-07-16T13:41:26.567-0700)

confirmed for 1.14.3, happens also with lava bucket without intentional switching out of fuel item since full bucket changes to empty bucket

### Comment 16: migrated (2020-06-24T14:34:56.079-0700)

Can confirm for 1.16.1

### Comment 17: pulpetti (2020-07-17T05:20:06.321-0700)

Can confirm for 20w29a

### Comment 18: migrated (2020-11-07T09:49:05.857-0800)

Confirmed for 1.16.4

### Comment 19: Brevort (2021-05-30T16:40:36.629-0700)

Does this also occur when switching dimensions or unloading and reloading the chunks in ways other than reloading the world?
Never mind, that's MC-137146.

### Comment 20: Avoma (2022-09-14T12:19:09.899-0700)

Can confirm in 1.19.2.

### Comment 21: j_p_smith (2023-08-10T06:53:43.635-0700)

The broken GUI is fixed in 23w32a, but the burn time indicator is still incorrect.

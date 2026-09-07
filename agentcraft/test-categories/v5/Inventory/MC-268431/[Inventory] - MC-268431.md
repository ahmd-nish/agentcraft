# MC-268431: External inventory changes except for the hotbar are not registered in a creative mode item selection screen

**Mojira URL:** [https://bugs.mojang.com/browse/MC-268431](https://bugs.mojang.com/browse/MC-268431)

## Report details

- **Mojira categories:** Inventory; Networking
- **Project:** MC
- **Issue key:** MC-268431
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2024-02-09T08:26:05.236-0800
- **Updated:** 2025-04-26T15:19:05.175-0700
- **Resolution date:** 2024-12-12T15:19:27.215-0800
- **Affects versions:** 1.20.4; 24w06a; 1.21; 24w33a
- **Fix versions:** 24w38a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** image-2024-07-19-18-31-08-177.png; image-2024-07-19-18-31-56-719.png
- **Issue links:** Relates:inward:MC-86455:Pick-block creates ghost items in Creative when hotbar is full | Relates:inward:MC-265640:Moving items before and after switching to the Survival inventory tab desyncs the hotbar

## Description

External inventory changes (e.g. by picking up items) are not registered on the client if you are in creative mode inventory and are not in the Survival Inventory tab, causing a desync.
Steps to reproduce:
- Fill your hotbar with items.

- Go into the creative mode inventory and go to any tab, but the inventory tab (e.g. the search tab).

- While in the tab, take any other item and throw it onto the ground.

- Wait until you pick it up and observe whether or not the item appears in the inventory.

Expected behavior:
The item is picked up and should show up in the inventory.
Actual behavior:
The item does not appear in the inventory. However, if you try to remove that particular item, e.g. using /clear @s <item>, the server will report that the item indeed was in the inventory.
Code analysis:
net.minecraft.client.multiplayer.ClientPacketListener

```
public void handleContainerSetSlot(ClientboundContainerSetSlotPacket packet) {
    // ...
    boolean conditional = false; // Line 1200

    if (minecraft.screen instanceof CreativeModeInventoryScreen x) { // Line 1202
        conditional = !x.isInventoryOpen(); // Line 1203
    }
    // 0 means player inventory
    if (packet.getContainerId() == 0 && InventoryMenu.isHotbarSlot(slotId)) {
        // ...
        player.inventoryMenu.setItem(slotId, packet.getStateId(), item);
    } else if (packet.getContainerId() == player.containerMenu.containerId && (packet.getContainerId() != 0 || !conditional)) {
        player.containerMenu.setItem(slotId, packet.getStateId(), item);
    }
}
```
This method is responsible for all of the single slot synchronization on the client side.
Because of it, inventory changes are almost completely ignored if they occur in a non-hotbar slot (first condition) and you are in the creative mode inventory (Line 1202), but not in the "Survival Inventory" tab (Line 1203). (why?)
Potential fix:
Just remove those weird conditions. Why do they even exist in the first place?

```
public void handleContainerSetSlot(ClientboundContainerSetSlotPacket packet) {
    // ...
    if (packet.getContainerId() == 0) {
        // ...
        player.inventoryMenu.setItem(slotId, packet.getStateId(), item);
    } else if (packet.getContainerId() == player.containerMenu.containerId) {
        player.containerMenu.setItem(slotId, packet.getStateId(), item);
    }
}
```
Also, because this is a synchronization step, the client should be able to be confident about that particular remote slot, shouldn't it? So please also consider changing this:
net.minecraft.world.inventory.AbstractContainerMenu

```
public void setItem(int slotId, int stateId, ItemStack item) {
    getSlot(slotId).set(item); // Line 593
    setRemoteSlot(slotId, item); // New line
    this.stateId = stateId; // Line 594
}
```
That is the setItem method from above, by the way.

## Comments (4)

### Comment 1: migrated (2024-02-09T08:26:05.236-0800)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: BugTracker_ (2024-07-19T08:32:37.594-0700)

Can confirm in 1.21: (I dropped wool)

### Comment 3: migrated (2024-08-29T20:14:51.097-0700)

I just ran into this, too, on 1.21.1.
If instead of clearing, you switch to survival and click on the slot where the picked up item should be, it de-ghosts and you pick it up.

### Comment 4: SoloAlguien (2024-12-12T03:40:23.736-0800)

Fixed in 24w38a.

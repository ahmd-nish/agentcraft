# MC-252409: Memory statistics within the debug menu contain some unnecessary spaces

**Mojira URL:** [https://bugs.mojang.com/browse/MC-252409](https://bugs.mojang.com/browse/MC-252409)

## Report details

- **Mojira categories:** Debug
- **Project:** MC
- **Issue key:** MC-252409
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Low
- **Created:** 2022-06-02T04:01:25.785-0700
- **Updated:** 2025-04-11T10:31:58.108-0700
- **Resolution date:** 2023-12-12T01:22:50.397-0800
- **Affects versions:** 1.18.2; 1.19 Pre-release 5; 1.19 Release Candidate 1; 1.19 Release Candidate 2; 1.19; 1.19.1 Pre-release 1; 1.19.1 Pre-release 2; 1.19.1 Pre-release 5; 1.19.1 Release Candidate 2; 1.19.1; 1.19.2; 22w45a; 1.19.3; 1.19.4; 1.20.1; 1.20.3 Release Candidate 1
- **Fix versions:** 23w51a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 3
- **Attachment filenames:** MC-252409.png; MC-252409 - Analysis.png; unknown.png
- **Issue links:** Relates:inward:MC-187372:There is no space between fps limit/vsync and graphics level in the debug screen

## Description

The Bug:
Memory statistics within the debug menu contain some unnecessary spaces.
See
 for all occurrences of this issue.
Steps to Reproduce:
- Enable the debug menu by hitting the "F3" key.

- Look towards the top right of the debug menu and look closely at the memory statistics.

- Take note as to whether or not memory statistics within the debug menu contain some unnecessary spaces.

Observed Behavior:
Unnecessary spaces are present.
Expected Behavior:
Unnecessary spaces would not be present.
Code Analysis:
Code analysis by  can be found below.
The following is based on a decompiled version of Minecraft 1.19 Release Candidate 1 using Mojang mappings.
net.minecraft.client.gui.components.DebugScreenOverlay.java

```
public class DebugScreenOverlay extends GuiComponent {
   ...
   protected List<String> getSystemInformation() {
      ...
      ArrayList arrayList = Lists.newArrayList((Object[])new String[]{String.format("Java: %s %dbit", System.getProperty("java.version"), this.minecraft.is64Bit() ? 64 : 32), String.format("Mem: % 2d%% %03d/%03dMB", l4 * 100L / l, DebugScreenOverlay.bytesToMegabytes(l4), DebugScreenOverlay.bytesToMegabytes(l)), String.format("Allocation rate: %03dMB /s", DebugScreenOverlay.bytesToMegabytes(this.allocationRateCalculator.bytesAllocatedPerSecond(l4))), String.format("Allocated: % 2d%% %03dMB", l2 * 100L / l, DebugScreenOverlay.bytesToMegabytes(l2)), "", String.format("CPU: %s", GlUtil.getCpuInfo()), "", String.format("Display: %dx%d (%s)", Minecraft.getInstance().getWindow().getWidth(), Minecraft.getInstance().getWindow().getHeight(), GlUtil.getVendor()), GlUtil.getRenderer(), GlUtil.getOpenGLVersion()});
      ...
```
If we look at the above class, we can see that memory statistics within the debug menu contain some unnecessary spaces. This is evident through the following pieces of code:

```
... String.format("Mem: % 2d%% %03d/%03dMB" ...
```

```
... String.format("Allocation rate: %03dMB /s" ...
```

```
... String.format("Allocated: % 2d%% %03dMB" ...
```

## Comments (7)

### Comment 1: migrated (2022-06-02T04:01:25.785-0700)

This comment contained multiple image attachments (3), please login to view the attachments.

### Comment 2: Moesh (2023-07-12T00:12:35.965-0700)

Please do not file bugs about text spacing or other text errors on the debug screen. Thanks!

### Comment 3: Avoma (2023-07-12T02:59:17.837-0700)

That's completely fine! Thanks for letting me know!

### Comment 4: migrated (2023-07-12T03:03:41.438-0700)

In that case  is also invalid, but I guess lack of space is more important/confusing than abundance.

### Comment 5: Moesh (2023-07-13T01:37:40.901-0700)

Spoke to the team, they're happy to keep these in their backlog. I would recommend placing any future ones together.

### Comment 6: Avoma (2023-07-13T01:43:05.620-0700)

That's fine; thank you very much! We can always add any future problems regarding the text within debug menu to this report. I'm more than happy to do that. Thanks once again!

### Comment 7: migrated (2023-12-03T15:41:24.884-0800)

Can confirm in 1.20.3 Release Candidate 1

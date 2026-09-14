# MC-273629: Adding effects with an effects_changed advancement causes a packet error (ConcurrentModificationException) if it was triggered by Milk

**Mojira URL:** [https://bugs.mojang.com/browse/MC-273629](https://bugs.mojang.com/browse/MC-273629)

## Report details

- **Mojira categories:** Commands; Data Packs
- **Project:** MC
- **Issue key:** MC-273629
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2024-06-19T13:28:29.386-0700
- **Updated:** 2025-04-26T15:50:57.721-0700
- **Resolution date:** 2024-08-16T04:56:41.852-0700
- **Affects versions:** 1.21
- **Fix versions:** 24w34a
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** effect-bug-1.zip

## Description

When editing effects in a certain way via datapacks, sometimes a packet error can occur that kicks the player from the server. It happens in the following very specific situation:
- An advancement exists that uses the effects_changed trigger

- The advancement points to a function that gives the player at least 2 different effects

- A player triggers the advancement by specifically drinking milk to clear an existing effect. This does not occur when using "/effect clear" to do the exact same thing.

Steps to Reproduce This Issue:
- Install the provided datapack

- Give yourself any effect, by any means (commands or potions or whatever)

- Drink milk.

Expected behavior: The datapack simply detects effects_changed and then gives the player infinite regen and night vision, so after drinking milk, your previous effect should be gone, and you should now have the regen and night vision. (This is exactly what happens when using "/effect clear" instead of milk.)
Observed Behavior: You'll be kicked from the server, and the server will print an error message to the logs. Note that if you're not in single player, the server will not crash; it will keep running, but the affected player will be forcibly disconnected.
Server Error Log:

```
[14:06:13] [Server thread/WARN]: Failed to handle packet for /127.0.0.1:53539
z: Ticking player
    at aqv.m(SourceFile:652) ~[server-1.21.jar:?]
    at aru.d(SourceFile:268) ~[server-1.21.jar:?]
    at vt.b(SourceFile:401) ~[server-1.21.jar:?]
    at art.c(SourceFile:176) ~[server-1.21.jar:?]
    at net.minecraft.server.MinecraftServer.c(SourceFile:1032) ~[server-1.21.jar:?]
    at apn.c(SourceFile:299) ~[server-1.21.jar:?]
    at net.minecraft.server.MinecraftServer.a(SourceFile:912) ~[server-1.21.jar:?]
    at net.minecraft.server.MinecraftServer.y(SourceFile:697) ~[server-1.21.jar:?]
    at net.minecraft.server.MinecraftServer.a(SourceFile:281) ~[server-1.21.jar:?]
    at java.base/java.lang.Thread.run(Thread.java:1583) [?:?]
Caused by: java.util.ConcurrentModificationException
    at java.base/java.util.HashMap$HashIterator.remove(HashMap.java:1619) ~[?:?]
    at btn.es(SourceFile:952) ~[server-1.21.jar:?]
    at cvd.a(SourceFile:27) ~[server-1.21.jar:?]
    at cuq.a(SourceFile:389) ~[server-1.21.jar:?]
    at btn.L_(SourceFile:3278) ~[server-1.21.jar:?]
    at aqv.L_(SourceFile:1398) ~[server-1.21.jar:?]
    at btn.a(SourceFile:3154) ~[server-1.21.jar:?]
    at aqv.a(SourceFile:1923) ~[server-1.21.jar:?]
    at btn.J(SourceFile:3141) ~[server-1.21.jar:?]
    at btn.l(SourceFile:2469) ~[server-1.21.jar:?]
    at cmx.l(SourceFile:312) ~[server-1.21.jar:?]
    at aqv.m(SourceFile:588) ~[server-1.21.jar:?]
    ... 9 more
```

## Comments (2)

### Comment 1: migrated (2024-06-19T13:28:29.386-0700)

This comment contained an image attachment, please login to view the attachment.

### Comment 2: [Mod] ManosSef (2024-06-19T14:00:01.693-0700)

Can confirm.

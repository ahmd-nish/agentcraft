# MC-180: When reaching the other side of a nether portal the animation plays forever until stepped out of

**Mojira URL:** [https://bugs.mojang.com/browse/MC-180](https://bugs.mojang.com/browse/MC-180)

## Report details

- **Mojira categories:** Player; Rendering
- **Project:** MC
- **Issue key:** MC-180
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2012-10-24T13:29:21.312-0700
- **Updated:** 2025-05-29T09:20:48.402-0700
- **Resolution date:** 2023-10-15T07:28:48.419-0700
- **Affects versions:** Minecraft 1.4.1; Minecraft 1.4.2; Minecraft 1.4.3; Minecraft 1.4.4; Minecraft 1.4.5; Snapshot 12w50b; Snapshot 13w02b; Snapshot 13w03a; Minecraft 1.5; Snapshot 13w11a; Minecraft 1.5.1; Snapshot 13w16a; Minecraft 1.5.2; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 13w38a; Minecraft 13w38b; Minecraft 13w38c; Minecraft 13w42b; 1.15.2; 20w14a; 20w15a; 20w21a; 1.16 Pre-release 2; 20w27a; 20w28a; 20w29a; 20w30a; 1.16.2 Pre-release 1; 1.16.3; 1.16.4 Pre-release 2; 1.16.4; 20w46a; 20w48a; 20w49a; 20w51a; 21w03a; 1.16.5; 21w05a; 21w05b; 21w06a; 21w07a; 21w08b; 21w11a; 21w14a; 21w15a; 21w17a; 21w20a; 1.17 Pre-release 1; 1.17; 1.17.1 Release Candidate 1; 1.17.1; 21w37a; 21w39a; 21w41a; 21w42a; 1.18.1; 1.18.2; 22w15a; 1.19; 1.19.1; 1.19.2; 1.19.3; 23w03a; 23w04a; 23w07a; 1.19.4; 23w14a; 23w17a
- **Fix versions:** 1.20 Pre-release 1
- **Labels:** nether_portal; overlay
- **Watchers:** 2
- **Attachments:** 6
- **Attachment filenames:** 2020-07-07_09.28.07.png; 2020-07-07_09.29.35.png; 2021-05-12_14.38.48.png; 2021-05-12_14.44.59.png; MC-180.mp4; MC-180 how it used to work in 1.3.2.mp4
- **Issue links:** Relates:inward:MC-262509:Portal animation still sometimes plays infinitely after travelling through it | Duplicate:inward:MC-177439:Portal animation still plays in circumstances where it will not teleport the player | Duplicate:inward:MC-217613:Nether portal animation does not slow to a stop on the other side | Duplicate:inward:MC-884:Nether portal teleportation issue | Relates:outward:MC-233:The portal travel sounds travel.ogg / trigger.ogg swapped / played at wrong time | Relates:inward:MC-193749:Nether portals play the trigger sound again when the other dimension is loaded

## Description

Info for snapshot video creators
Here are two gifs which can be used to compare the two versions of the nether portal exit animation:
- Correct animation, used up until 1.2.5 (broke in 1.3.1 snapshot 12w18a) and is now used again as of 1.20-pre1: https://cdn.discordapp.com/attachments/399390463930400778/1097153888597069844/1point2point5-netherportal-anim.gif

- Incorrect animation, used from 12w34a to 23w18a and now fixed as of 1.20-pre1: https://cdn.discordapp.com/attachments/399390463930400778/1097156653687787692/1point19point4-netherportal-anim.gif

Note that the "Entering the Nether" message being absent in modern versions is a separate bug and is not yet fixed (). The absence of inner faces in nether portal blocks is also a completely separate issue (MC-262512).
The bug
When you reach the other side of a nether portal the animation plays forever until you step out of it, even in creative. The animation is completely unnecessary here.
This bug first appeared in 1.4 snapshot 12w34a - versions 12w32a and earlier are completely unaffected (but many are affected by MC-217613).
I'd recommend fixing this and MC-217613 at the same time. A table explaining the expected behaviour can be found here: https://minecraft.fandom.com/wiki/Java_Edition_1.3.1/List_of_broken_features#Nether_portal_exit_animation
Refer to Ismael Rosillo's code analysis below for how these issues can be fixed (and why MC-217613 cannot be considered a duplicate of this issue).
How to reproduce
- Build a nether portal

- Enter it

- Stay in the exit portal

- The animation will start playing when it shouldn't

## Comments (67)

### Comment 1: migrated (2012-10-24T13:29:21.312-0700)

This comment contained multiple image attachments (6), please login to view the attachments.

### Comment 2: migrated (2012-10-24T13:51:54.752-0700)

But you're still in the portal, are you not? The animation is caused by being inside the portal block, not by actually teleporting.

### Comment 3: migrated (2012-10-24T14:12:42.585-0700)

The animation feels like its the prelude to teleporting, not the act of standing inside a portal, so is confusing when it remains when passing through to the other side.

### Comment 4: migrated (2012-10-24T15:10:02.094-0700)

It's because you're entering the new nether-portal block in the nether, and so the effect starts.

### Comment 5: migrated (2012-10-25T11:58:47.512-0700)

if it's on a server be sure the nether is actived

### Comment 6: migrated (2012-11-01T07:25:11.969-0700)

I confirm this. It didn't happen in 1.3.2 It's happening in 1.4.2 and it is very annoying. In 1.3.2 the effect would start playing only if the player would leave the gate block and return back to the gate.

### Comment 7: migrated (2012-11-06T00:23:10.399-0800)

I happened in 1.3 for me...

### Comment 8: migrated (2012-11-13T10:34:52.403-0800)

I have a one year old gaming high end pc. And i have to add to this point: this happens mostly while spawning new biomes that arent already on the discovered minecraft map. I have also an issue.. it kinda lacks. Especially in multiplayer games. But hey.. my pc works it out fine in the end. what kind of pc configuration do you guys have? (RAM; GRAFIK.. etc)

### Comment 9: migrated (2012-11-14T11:39:05.595-0800)

Saskia this is not affected by pc specs or creation of new chunks. It happens even no new chunks are about to be created. Enter a nether portal and wait to be transferes to the other end. When that happens, don't move out of the portal. The animation is going start as if you are about to be teleported again, but you won't.

### Comment 10: migrated (2012-11-17T18:45:03.064-0800)

This used to only happen in multiplayer-servers, but with the code merge... yeah. The problem is NOT the texture animating, that makes perfect sense, the problem is the nauseating warping of the world that going on at the same time.

### Comment 11: migrated (2012-11-18T12:18:58.445-0800)

Well, maybe it should teleport you back to the nether if you stand in the arrival portal for that long.

### Comment 12: migrated (2012-11-20T14:20:35.307-0800)

It won't teleport you back. Why don't you just try it and see for yourself.

### Comment 13: migrated (2012-11-20T14:26:08.354-0800)

This doesn't affect gameplay, so it isn't a bug. Please resolve.

### Comment 14: migrated (2012-11-22T02:06:43.433-0800)

This is not an intended feature, unless you have proof that it is. Also it did not happen in previous versions. And finally since the portal is not going to teleport the player back why would the teleportation animation start? So it is a bug. It doesn't make any sense otherwise.
EDIT: I've played minecraft 1.2.4 , 1.2.5 , 1.3.1 and 1.3.2 before 1.4.2 and it didn't occur. I've never used any mod or texture pack other than the default.

### Comment 15: migrated (2012-11-24T18:36:12.402-0800)

This has happened to me since Beta.

### Comment 16: migrated (2012-11-25T06:43:50.236-0800)

I think this was introduced in one of the 1.4 snapshots. Perhaps portals are just nauseating whether or not you teleport.

### Comment 17: shufboyardee (2012-12-06T08:25:50.085-0800)

It is counterintuitive, and because of that, just a bit disorienting; stepping into a portal has an increasing swirly animation, so when I appear in the nether I sort of do expect a decreasing swirly animation, instead of the swirls starting at zero and ramping up again.  Happens in 1.4.5.

### Comment 18: migrated (2013-01-06T20:51:02.841-0800)

This DID happen in 1.4.2 AND 1.3.2.

### Comment 19: migrated (2013-01-07T12:21:10.327-0800)

If I understand correct you mean that this didn't happen in any version other than 1.3.2 and 1.4.2 ?
1.4.6
http://youtu.be/imviP8S-biE
1.3.2
http://youtu.be/w734yujyAGo

### Comment 20: migrated (2013-01-25T13:01:44.951-0800)

The same bug in snapshot 13w04a
What's supposed to happen :
1-enter the nether portal
2-wait the animation
3-teleport to the nether
4-play bare-handed tennis with ghasts
What's happening :
1-enter the nether portal
2-instant teleportation to the nether wihtout the animation
3-after your arrival, the animation start and don't stop as long as you stay in the portal
4-be pretty confused
I think the cause is within the mobs-teleportation-to-the-nether-feature

### Comment 21: migrated (2013-01-25T16:19:12.806-0800)

You travel instantly in creative mode Ben, that is very much intended.

### Comment 22: migrated (2013-02-21T10:04:35.005-0800)

The problem is that there is no difference between standing in a portal, which will soon teleport you, and standing in a portal that will not.  The effect is the same.  The effect going from low levels to high levels of waviness strongly implies that something is powering up and about to happen.
If you come through a portal, and realize you want to go back (due to monsters, wrong destination, forgot something, etc.) and you move away and immediately back there's no way to tell if the portal is actually ramping up to teleport you or not.
Similarly if you don't want to go through a portal, but are sticking close to it for some reason (maybe hiding behind the obsidian from a ghast) you cant' easily tell if you've briefly moved too far away and the portal is actually going to send you somewhere.
- In short the wavy effect currently only provides the information: "you are standing in a portal".

- But it would be more informative if it meant, and players tend to expect it to mean: "you are about to be teleported".

To make this clear when arriving through a portal, when it isn't going to send you anywhere, the waving effect could reverse it self (from maximum to minimum) or it could wave at a constant moderate level.

### Comment 23: migrated (2013-03-14T17:48:41.334-0700)

Reversing the intensity would be awesome!

### Comment 24: Cultist_O (2013-04-10T06:26:13.561-0700)

I completely agree that it is counter intuitive, and that it implies you are about to be teleported. Furthermore, if you stand in the portal too long (because of lag, or something) it can make it very difficult to leave portals that have blocks or holes beside them, that would be easy to leave were this not the case.

### Comment 25: migrated (2013-06-20T15:41:37.551-0700)

I've been experiencing this since forever.

### Comment 26: migrated (2013-07-08T03:52:53.927-0700)

Then you probably started playing minecraft after 1.4 was released, right?

### Comment 27: migrated (2013-08-02T09:43:38.554-0700)

it's an old bug, it didn't started in 1.4 you probably haven't noticied because you exit the portal right way. Sorry for my bad english im brazilian.

### Comment 28: migrated (2013-10-11T19:39:44.737-0700)

This actually looked the way some people here are asking for, way back when in Beta, as I recall.

### Comment 29: FaRo1 (2020-07-13T03:05:58.339-0700)

Just because it's an old bug with portals? Or did you find a deeper reason why they're related?

### Comment 30: Avoma (2020-11-25T11:18:21.104-0800)

Can confirm for 20w48a.

### Comment 31: Avoma (2020-12-02T11:28:24.753-0800)

Can confirm in 20w49a.

### Comment 32: migrated (2020-12-15T08:12:58.179-0800)

I've been playing minecraft since 1.2 in 2012 and this is has consistently happened. The animation is triggered by you being in the portal, not you being in the act of teleportation.

### Comment 33: Avoma (2020-12-24T02:54:48.623-0800)

Can confirm in 20w51a.

### Comment 34: Avoma (2021-02-03T11:04:51.062-0800)

Can confirm in 21w05a.

### Comment 35: Avoma (2021-02-04T10:22:00.195-0800)

Can confirm in 21w05b.

### Comment 36: Avoma (2021-02-10T10:29:59.893-0800)

Can confirm in 21w06a.

### Comment 37: Avoma (2021-02-18T10:32:34.121-0800)

Can confirm in 21w07a.

### Comment 38: migrated (2021-02-28T08:34:54.447-0800)

Attached a video showing how it used to work in 1.3.2.

### Comment 39: Avoma (2021-03-18T02:50:04.113-0700)

Can confirm in 21w11a.

### Comment 40: migrated (2021-03-18T13:39:03.946-0700)

And 1.16.5.

### Comment 41: Avoma (2021-04-12T02:21:00.474-0700)

Can confirm in 21w14a.

### Comment 42: Avoma (2021-04-19T03:44:00.798-0700)

Can confirm in 21w15a.

### Comment 43: Avoma (2021-04-30T05:45:27.430-0700)

Can confirm in 21w17a.

### Comment 44: Avoma (2021-06-16T11:53:39.312-0700)

Can confirm in 1.17.

### Comment 45: ampolive (2021-07-04T10:21:48.008-0700)

Can confirm in 1.17.1 Release Candidate 1.

### Comment 46: ampolive (2021-09-16T17:12:08.469-0700)

Can confirm in 21w37a.

### Comment 47: ampolive (2021-09-29T11:12:29.315-0700)

Can confirm in 21w39a.

### Comment 48: ampolive (2021-10-13T10:23:27.033-0700)

Can confirm in 21w41a.

### Comment 49: ampolive (2021-10-23T07:04:05.426-0700)

Can confirm in 21w42a.

### Comment 50: Avoma (2022-01-08T07:29:48.936-0800)

Can confirm in 1.18.1.

### Comment 51: Avoma (2022-03-02T05:38:01.125-0800)

Can confirm in 1.18.2.

### Comment 52: Avoma (2022-06-08T05:25:12.555-0700)

Can confirm in 1.19.

### Comment 53: migrated (2022-07-23T15:11:25.333-0700)

you can only go throgh a portal once without stopping out because otherwise you  would travel from dimension to dimension for infinity loading and unloading chunks quickly. if many players did that it would cause massive lagg thats why.

### Comment 54: Cultist_O (2022-07-24T16:53:23.816-0700)

@HubbiGamingTV the expected behaviour is not to keep teleporting again without leaving the portal. The expected behaviour would be for the portal animation not to play once through, or for it to play in reverse.
The problem is: it looks like you're going to teleport again when you aren't. (Even worse, the animation keeps getting wonkier until you can't even see what's going on.) The recommended solution is to make the visual cues match what's happening, not to change the teleportation behaviour.
So it should play the wind up animation when you first enter the portal, then, once you're through the portal, it should either not play an animation, or play a wind down animation (ending in no animation)

### Comment 55: Avoma (2022-07-28T06:02:39.124-0700)

Can confirm in 1.19.1.

### Comment 56: Avoma (2022-08-06T11:52:56.751-0700)

Can confirm in 1.19.2.

### Comment 57: nitrodynamite18 (2022-10-20T09:10:20.985-0700)

It makes sense that your vision hasn't fully recovered because you're still in a portal between dimensions.

### Comment 58: Brain81505 (2023-01-18T06:22:55.301-0800)

Can confirm in 23w03a

### Comment 59: Brain81505 (2023-01-24T23:19:05.081-0800)

Can confirm in 23w04a

### Comment 60: Brain81505 (2023-02-01T08:03:46.636-0800)

Can confirm in 23w06a

### Comment 61: batbrain55 (2023-02-21T15:18:20.728-0800)

Can confirm in 23w07a.

### Comment 62: mattp12 (2023-03-20T18:24:00.315-0700)

Confirmed for 1.19.4.

### Comment 63: ISRosillo14 (2023-04-09T08:02:04.303-0700)

This comment is an extensive bug (and code) analysis of the fifth oldest persisting issue, along with a working and fully tested workaround (fix), so this comment will be split in different categories.
What @Connor Steppie Meant with MC-217613
Then, we have MC-217613 which indeed is (and it's not) a duplicate of this, depending on the point of view; Connor Steppie means that MC-217613 is the bug that refers to the lack of a slow-to-stop animation for the portal (it happened for the first time in 12w18a), while  refers to the visual "re-trigger" of the portal (it happenned for the first time in 12w34a). It's like these two bugs have been "stacked" or that they are "sister bugs", because they represent a very similar issue.
Code Analysis
Here, a bit of history of the code that worked, using Mojang's mapping names for this analysis:
- 1. Prior to 12w18a, it only worked on singleplayer, as the whole world was client. This is because the method we now call LocalPlayer.handleNetherPortalClient() (was part of aiStep() back then) handled the whole teleportation and then used the "distortion fade out" behaviour using field LocalPlayer.portalTime. The code below is a recreation of the sourcecode present in 12w17a, using mojang names and my own ones.

```public class LocalPlayer extends Player {
 ...
   public void aiStep() {
     ...
       this.oPortalTime = this.portalTime;

       if (this.isInsidePortal) {
           if (!this.level.isClientSide && this.vehicle != null) {
               this.startRiding((Entity)null);
           }

           if (this.minecraft.screen != null) {
               this.minecraft.setScreen((Screen)null);
           }

           if (this.portalTime == 0.0F) {
               this.minecraft.soundManager.play("portal.trigger", 1.0F, this.random.nextFloat() * 0.4F + 0.8F);
           }

           this.portalTime += 0.0125F;

           //START OF CODE REMOVED IN 12w18a
           if (this.portalTime >= 1.0F) {
               this.portalTime = 1.0F;

               if (!this.level.isClientSide) {
                   this.portalCooldown = 10;
                   this.minecraft.soundManager.play("portal.travel", 1.0F, this.random.nextFloat() * 0.4F + 0.8F);
                   byte newDimension = 0;

                   if (this.dimension == -1) {
                       newDimension = 0;
                   } else {
                       newDimension = -1;
                   }

                   this.minecraft.changeDimension(newDimension);
                   this.takeAchievement(Achievements.portal);
               }
           }
           //END OF REMOVED CODE

           this.isInsidePortal = false;
       } else if (this.hasEffect(MobEffects.CONFUSION) && this.getEffect(MobEffects.CONFUSION).getDuration() > 60) {
           this.portalTime += 0.006666667F;

           if (this.portalTime > 1.0F) {
               this.portalTime = 1.0F;
           }
       } else {
           if (this.portalTime > 0.0F) {
               this.portalTime -= 0.05F;
           }

           if (this.portalTime < 0.0F) {
               this.portalTime = 0.0F;
           }
       }

       if (this.portalCooldown > 0) {//old equivalent to Entity.processPortalCooldown()
           this.portalCooldown--;
       }
     ...
   }
  ...
}```

- 2. After the changes made in 12w18a, the code described above was completely removed without adding a replacement, causing the unwanted behavior described in MC-217613.

- 3. In 12w34a, the way nether portals were handled by entities was changed internally, causing the actual behavior where the animation plays forever.

Note in the code that method this.minecraft.changeDimension(newDimension) was also removed from Minecraft.java and also it was forgotten to be re-added for the client listener, causing .
Workaround and Fix
After the client-server singleplayer split up, the game switched to fully use the network system, and the source code described in history would not be able to just be copied and pasted, however, it's still useful for reference.
A possible way to fix this is to let the client know when a dimension change was caused by a nether portal to set the proper animation.
But first, we are going to head to LocalPlayer.java and add a new method (named justPostalTraveled() in this example), that will prevent the player to enter to the in-portal state, and set the Animation/Portal Effect at 100%. This will make the player think it's just exiting a portal and will decrease the Animation/Portal Effect at every aiStep()->handleNetherPortalClient() (This would also fix MC-193749). Now there's a problem with the animation effect: the animation starts before the Downloading Terrain screen is gone, causing the animation to be gone at the time or shortly after the game is rendering the world. To fix this, we are gonna make handleNetherPortalClient() know when it should progress the animation using a check. The end result is shown here in the code:

```public class LocalPlayer extends AbstractClientPlayer {
 ...
   private void handleNetherPortalClient() {
      this.oPortalTime = this.portalTime;
      boolean shouldStatusProgress = !(this.minecraft.screen instanceof ReceivingLevelScreen);

      if (this.isInsidePortal) {
         if (this.minecraft.screen != null && !this.minecraft.screen.isPauseScreen() && !(this.minecraft.screen instanceof DeathScreen) && shouldStatusProgress) {
            if (this.minecraft.screen instanceof AbstractContainerScreen) {
               this.closeContainer();
            }

            this.minecraft.setScreen((Screen)null);
         }

         if (this.portalTime == 0.0F) {
            this.minecraft.getSoundManager().play(SimpleSoundInstance.forLocalAmbience(SoundEvents.PORTAL_TRIGGER, this.random.nextFloat() * 0.4F + 0.8F, 0.25F));
         }

         this.portalTime += 0.0125F;
         this.isInsidePortal = false;
      } else if (this.hasEffect(MobEffects.CONFUSION) && this.getEffect(MobEffects.CONFUSION).getDuration() > 60) {
         this.portalTime += 0.006666667F;
      } else if (shouldStatusProgress) {
         if (this.portalTime > 0.0F) {
            this.portalTime -= 0.05F;
         }
      }

      this.portalTime = Mth.clamp(this.portalTime, 0.0F, 1.0F);

      if (shouldStatusProgress) {
          this.processPortalCooldown();
      }
   }

   public void justPortalTraveled() {
       this.isInsidePortal = false;
       this.oPortalTime = this.portalTime = 1.0F;
       this.setPortalCooldown();
   }
 ...
}```
In other hand, we need to use this new method somewhere, and returning to the second paragraph, we'll make the client know when the player used a portal. I added a condition at the packet ClientboundRespawnPacket.java and I called it boolean fromPortal. It will also be read and written to the packet.
The change is quite obvious so I will not show the end result for that. Instead we are going to make this fix fully efective. At the ClientPacketListener.java at method handleRespawn(), after the player is being initialized and "adjusted", let's check whether if the player came from a portal (using the previously added fromPortal field) to call for justPortalTraveled():

```public class ClientPacketListener implements TickablePacketListener, ClientGamePacketListener {
 ...
   public void handleRespawn(ClientboundRespawnPacket p_105066_) {
      ...
      localplayer1.resetPos();
      localplayer1.setServerBrand(s);
      this.level.addPlayer(i, localplayer1);
      localplayer1.setYRot(-180.0F);
      localplayer1.input = new KeyboardInput(this.minecraft.options);
      this.minecraft.gameMode.adjustPlayer(localplayer1);
      localplayer1.setReducedDebugInfo(localplayer.isReducedDebugInfo());
      localplayer1.setShowDeathScreen(localplayer.shouldShowDeathScreen());
      localplayer1.setLastDeathLocation(p_105066_.getLastDeathLocation());

      if (packet.isPortalTravel()) {
         localplayer.justPortalTraveled();
      }

      if (this.minecraft.screen instanceof DeathScreen) {
         this.minecraft.setScreen((Screen)null);
      }

      this.minecraft.gameMode.setLocalMode(p_105066_.getPlayerGameType(), p_105066_.getPreviousPlayerGameType());
   }
 ...
}```
The fromPortal field should be true only when we are sure that the player is naturally changing from dimensions, like in ServerPlayer.changeDimension(ServerLevel), which is triggered only when the player is joing to change dimensions throught portals.
However, this fix didn't always work; in certain cases that i couldn't determine, the glitched animation played intead. That left me confused for a while until I found an alternative to this fix.
The new fix comes from the same concept of letting the player know whether or not the dimension travel was a because of a portal, but splitting ClientboundRespawnPacket.java's dimension change function into ClientboundDimensionTravelPacket.java. This new packet didn't create a new player instance and will reuse the previous one. I'm sure of something; that the previous fix did not work because the player could have lost some data. This new fix has worked at the 100% of tests. This is the new dimension travel packet handler:

```public class ClientPacketListener implements TickablePacketListener, ClientGamePacketListener {
 ...
   @Override
   public void handleDimensionTravel(ClientboundDimensionTravelPacket packet) {
      PacketUtils.ensureRunningOnSameThread(packet, this, this.minecraft);
      Holder<DimensionType> holder = this.registryAccess.compositeAccess().registryOrThrow(Registries.DIMENSION_TYPE).getHolderOrThrow(packet.getDimensionType());
      LocalPlayer localplayer = this.minecraft.player;
      ResourceKey<Level> newDimension = packet.getDimension();
      ResourceKey<Level> oldDimension = localplayer.level.dimension();

      if (newDimension != oldDimension) {
         Scoreboard scoreboard = this.level.getScoreboard();
         Map<String, MapItemSavedData> map = this.level.getAllMapData();
         boolean flag = packet.isDebug();
         boolean flag1 = packet.isFlat();
         ClientLevel.ClientLevelData clientlevel$clientleveldata = new ClientLevel.ClientLevelData(this.levelData.getDifficulty(), this.levelData.isHardcore(), flag1);
         this.levelData = clientlevel$clientleveldata;
         this.level = new ClientLevel(this, clientlevel$clientleveldata, newDimension, holder, this.serverChunkRadius, this.serverSimulationDistance, this.minecraft::getProfiler, this.minecraft.levelRenderer, flag, packet.getSeed());
         this.level.setScoreboard(scoreboard);
         this.level.addMapData(map);
         Component title;

         if (newDimension == Level.OVERWORLD) {//this is exta code from my mod, it fixes MC-12789
             ResourceLocation resourcelocation = oldDimension.location();
             String s = resourcelocation.toLanguageKey("dimension");
             title = Component.translatable("menu.leavingDimension", Language.getInstance().has(s) ? Component.translatable(s) : Component.literal(resourcelocation.toString()));
         } else {
             ResourceLocation resourcelocation = newDimension.location();
             String s = resourcelocation.toLanguageKey("dimension");
             title = Component.translatable("menu.enteringDimension", Language.getInstance().has(s) ? Component.translatable(s) : Component.literal(resourcelocation.toString()));
         }

         this.minecraft.setLevel(this.level, new ReceivingLevelScreen(title));
         localplayer.fishing = null;//This a fix for an issue that happened in one of my tests. Since the player instance is not a new one and because the client doesn't unload entities from previous level (yeah client worlds work like that) and the player doesn't to check if the fishing rod is a valid entity to unset it, I had to put that here.

         if (packet.isPortalTravel()) {
             localplayer.justPortalTraveled();
             this.minecraft.getSoundManager().play(SimpleSoundInstance.forLocalAmbience(SoundEvents.PORTAL_TRAVEL, this.random.nextFloat() * 0.4F + 0.8F, 0.25F));
             //You can see the portal travel sound playing from here and not from levelEvent() because with this fix we no longer really need to use another packet (I removed the level event 1032 as well)
         }
      }

      if (localplayer.hasContainerOpen()) {
         localplayer.closeContainer();
      }

      localplayer.setLevel(this.level);

      if (newDimension != oldDimension) {
         this.minecraft.getMusicManager().stopPlaying();
      }

      this.level.addPlayer(localplayer.getId(), localplayer);
   }
 ...
}```
Well I hope my fix is clear to understand, if not, or if there are any questions, feel free to ask  It's time to get this fixed

### Comment 64: ISRosillo14 (2023-05-03T03:57:19.326-0700)

Can confirm in 23w17a. It would be a please that the code analysis became added to the bug description.

### Comment 65: MishaGold (2023-05-10T06:01:54.591-0700)

IT WAS FIXED!! YAY

### Comment 66: muzikbike (2023-05-10T06:18:19.109-0700)

I can confirm that this bug, MC-193749 and MC-217613 are all fixed in 1.20-pre1. , however, does not seem to be.

### Comment 67: icny (2023-05-10T14:15:11.633-0700)

fixed!

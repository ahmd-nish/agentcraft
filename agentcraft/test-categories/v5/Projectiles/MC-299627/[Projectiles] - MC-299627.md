# MC-299627: Entity interpolation for high speed projectiles is wildly inaccurate

**Mojira URL:** [https://bugs.mojang.com/browse/MC-299627](https://bugs.mojang.com/browse/MC-299627)

## Report details

- **Mojira categories:** Networking; Projectiles
- **Project:** MC
- **Issue key:** MC-299627
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2025-07-10T21:30:47.643-0700
- **Updated:** 2025-08-05T03:29:38.267-0700
- **Resolution date:** 2025-08-05T03:29:38.212-0700
- **Affects versions:** 1.21.7
- **Fix versions:** 25w32a
- **Area:** Platform
- **Votes:** 50
- **Watchers:** 1
- **Attachments:** 1
- **Attachment filenames:** lerp.mp4
- **Issue links:** Relates:inward:MC-65312:Projectiles stutter / glitch while flying | Relates:inward:MC-124197:Arrow entitydata on server is not synced with client | Relates:inward:MC-139548:Projectiles are rendered incorrectly if their Motion tag was recently changed | Relates:inward:MC-80142:The acceleration of wither skulls, small/dragon fireballs and wind charges is not synced correctly, leading to stuttering during flight

## Description

Whilst testing arrows launched at high speeds I’ve noticed that the motion of the arrows seems really strange. After investigating further I have found there are wild inaccuracies in the way projectiles are rendered to the client each frame. This appears to only affect projectile entities and not other types of entities like TnT.
I have included a video clearly demonstrating the issue. In the video the green hitbox represents the actual position of the projectile entity, whilst the white hitbox follows the entity as it is rendered for the client. For very low speeds of around 1 block per tick its not very noticable, but once you start getting to higher speeds the discrepancy becomes very pronounced.
To reproduce the setup you can use the following commands:
summon minecraft:arrow ~ ~1 ~ {Motion:[0.0,1.0,0.0]}
summon minecraft:arrow ~ ~1 ~ {Motion:[0.1,1.0,0.0]}
summon minecraft:arrow ~ ~1 ~ {Motion:[0.0,10.0,0.0]}
summon minecraft:arrow ~ ~1 ~ {Motion:[1.0,10.0,0.0]}
Thanks to Velizar we now know exactly what part of the code is causing this issue. When the game goes to compile entity data to transmitto the client. It clamps the motion values to a range of [-3.9,3.9] and multiplies by 8000 to ensure the data is transmitted in 32 signed integer format. This seems like a completely unnecessary networking optimization that just detracts from the visual accuracy of gameplay features. Included is the code that causes this issue.

```
package net.minecraft.network.protocol.game;

import net.minecraft.network.FriendlyByteBuf;
import net.minecraft.network.codec.StreamCodec;
import net.minecraft.network.protocol.Packet;
import net.minecraft.network.protocol.PacketType;
import net.minecraft.util.Mth;
import net.minecraft.world.entity.Entity;
import net.minecraft.world.phys.Vec3;

public class ClientboundSetEntityMotionPacket implements Packet<ClientGamePacketListener> {
	public static final StreamCodec<FriendlyByteBuf, ClientboundSetEntityMotionPacket> STREAM_CODEC = Packet.codec(
		ClientboundSetEntityMotionPacket::write, ClientboundSetEntityMotionPacket::new
	);
	private final int id;
	private final int xa;
	private final int ya;
	private final int za;

	public ClientboundSetEntityMotionPacket(Entity entity) {
		this(entity.getId(), entity.getDeltaMovement());
	}

	public ClientboundSetEntityMotionPacket(int i, Vec3 vec3) {
		this.id = i;
		double d = 3.9;
		double e = Mth.clamp(vec3.x, -3.9, 3.9);
		double f = Mth.clamp(vec3.y, -3.9, 3.9);
		double g = Mth.clamp(vec3.z, -3.9, 3.9);
		this.xa = (int)(e * 8000.0);
		this.ya = (int)(f * 8000.0);
		this.za = (int)(g * 8000.0);
	}

	private ClientboundSetEntityMotionPacket(FriendlyByteBuf friendlyByteBuf) {
		this.id = friendlyByteBuf.readVarInt();
		this.xa = friendlyByteBuf.readShort();
		this.ya = friendlyByteBuf.readShort();
		this.za = friendlyByteBuf.readShort();
	}

	private void write(FriendlyByteBuf friendlyByteBuf) {
		friendlyByteBuf.writeVarInt(this.id);
		friendlyByteBuf.writeShort(this.xa);
		friendlyByteBuf.writeShort(this.ya);
		friendlyByteBuf.writeShort(this.za);
	}

	@Override
	public PacketType<ClientboundSetEntityMotionPacket> type() {
		return GamePacketTypes.CLIENTBOUND_SET_ENTITY_MOTION;
	}

	public void handle(ClientGamePacketListener clientGamePacketListener) {
		clientGamePacketListener.handleSetEntityMotion(this);
	}

	public int getId() {
		return this.id;
	}

	public double getXa() {
		return this.xa / 8000.0;
	}

	public double getYa() {
		return this.ya / 8000.0;
	}

	public double getZa() {
		return this.za / 8000.0;
	}
}
```

## Comments (6)

### Comment 1: cubicmetre (2025-07-10T21:30:48.571-0700)

This comment contained multiple media attachments (2), please login to view the attachments.

### Comment 2: clamlol (2025-07-11T22:29:56.809-0700)

Can confirm, it is sufficient to run the fourth command while looking upwards with hitboxes enabled.

### Comment 3: kanjiirahlni (2025-07-15T00:10:21.276-0700)

yeah. in the latest update, something feels VERY wrong with projectiles such as arrows and tridents. If a skeleton charges up a shot before you raise your shield, the fired arrow WILL hit you, regardless of the fact that you had the shield up before the arrow was fired (and no, it’s not a lag/server issue. this happens on single player, and it’s also when getting shot from right in front of you, so it’s not that you’re not blocking the arrows, it’s that they bypass the shield for some reason if you aren’t blocking before they charge a shot).
Player fired arrows/tridents now seemingly pass straight through mobs and deal no damage well over 25% of the time. At first I thought “wow, my aim must have suddenly gotten terrible!”, but then I turned on hitboxes. Nope, my aim is still pretty perfect, it’s just that arrows/tridents for some reason will just clip through a mob and deal no damage (often appearing to harmlessly bounce off said mob, but the resulting arrow will always be where it would have landed had no mob been there at all. It’s EXTREMELY FRUSTRATING when it happens with creepers, cuz the “missed” shot from point blank will result in you having to tank the blast that otherwise wouldn’t have happened had the projectile collision actually worked)
ANOTHER issue is that arrows fired from the bow will sometimes not appear. No arrow flying, no particle trail, nothing. it can still impact enemies (provided the collision actually works), but it’s very annoying trying to calculate trajectory if you can’t even see where your previous projectile went.

### Comment 4: kanjiirahlni (2025-07-15T00:13:40.336-0700)

to clarify, the arrow not appearing after it’s fired WILL appear embedded into the surface it would have hit if it didn’t hit any mobs. it’s just not visible while it’s in flight, occasionally.

### Comment 5: Shahzar Nayab (2025-08-03T03:09:59.332-0700)

Can confirm, this bug has not been patched in 1.21.8

### Comment 6: Shahzar Nayab (2025-08-03T03:11:21.558-0700)

May be related to MC-275564

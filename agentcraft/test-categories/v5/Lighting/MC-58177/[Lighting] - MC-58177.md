# MC-58177: Night vision rendered darker and orange when nearing light sources with brightness on moody

**Mojira URL:** [https://bugs.mojang.com/browse/MC-58177](https://bugs.mojang.com/browse/MC-58177)

## Report details

- **Mojira categories:** Lighting; Rendering
- **Project:** MC
- **Issue key:** MC-58177
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Created:** 2014-06-20T00:03:05.400-0700
- **Updated:** 2025-04-29T20:47:56.509-0700
- **Resolution date:** 2021-12-05T19:37:33.768-0800
- **Affects versions:** Minecraft 14w25b; Minecraft 14w26b; Minecraft 14w26c; Minecraft 14w27a; Minecraft 14w27b; Minecraft 14w30c; Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.2-pre1; Minecraft 1.10.2; Minecraft 1.11; Minecraft 1.12.1; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 18w22a; Minecraft 1.13-pre1; Minecraft 1.13-pre6; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 18w30b; Minecraft 1.13.1; Minecraft 1.13.2; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 19w07a; Minecraft 1.14 Pre-Release 5; Minecraft 1.14.2; 1.14.4; 19w35a; 19w42a; 19w44a
- **Fix versions:** 19w45a
- **Labels:** brightness; color; light; night-vision; rendering
- **Watchers:** 1
- **Attachments:** 17
- **Attachment filenames:** 2014-06-20_14.47.00.png; 2014-06-20_14.47.02.png; 2014-06-20_15.04.22.png; 2014-06-20_15.04.24.png; 2014-06-22_22.19.52.png; 2014-06-22_22.20.11.png; 2014-06-24_15.05.44.png; 2014-06-24_15.06.17.png; 2014-06-24_15.06.25.png; 2014-06-25_16.38.46.png; 2014-06-25_16.38.51.png; 2014-06-25_16.41.28.png; 2014-06-25_16.41.46.png; 2014-06-25_16.41.50.png; 2014-06-25_16.46.38.png; 2014-06-25_16.46.40.png; screenshot-1.png
- **Issue links:** Relates:inward:MC-48666:Cobwebs are affected by block lighting in full sky lighting | Cloners:inward:MC-199559:Light appears darker and orange when Night Vision is active | Relates:outward:MCPE-116172:Night Vision doesn't work properly under moody brightness

## Description

The bug
When exploring mineshafts using night vision, I found that the blocks nearing light sources always become darker and more orange. But the block just beside the light source is normal.
How to reproduce
- Set brightness in video options to minimum

- Make/Go to a place with light level 0. (Note: It does something else if exposed to sky, but still looks weird though.)

- Get Night Vision effect.

- Place any kind of light source.

- The blocks near but not beside the light source are rendered darker. (Note: Lava blocks and Fire blocks are rendered too dark too!)

New founds added 6/24:
Finally I got the idea why night vision looks weird under night sky. I found a ravine with a hole above it, and compare to the non exposed area, the place under the night sky are extremely blue.
How to reproduce
- Set brightness in video options to minimum

- Make (since it's a little difficult to find) a huge (at least 30x10x30) room with light level 0. (Suggested that use stone with some lapis ores)

- Get Night Vision effect.

- Make sure it's night time in game.

- Break a hole on the roof.

- Enjoy! Don't forget to try Fire blocks, they look FUNNY!! (?! Just kidding XD)

Code analysis
Code analysis by  can be found in this comment.

## Comments (20)

### Comment 1: migrated (2014-06-20T00:03:05.400-0700)

This comment contained multiple image attachments (17), please login to view the attachments.

### Comment 2: migrated (2014-06-20T10:47:16.472-0700)

Is your Java already the latest Java, if it is please add it to the "Java 7" in your environment.

### Comment 3: migrated (2014-06-20T10:49:22.726-0700)

can confirm with brightness on minimal

### Comment 4: kumasasa (2014-06-22T13:20:50.294-0700)

Somewhat confirmed with brightness on minimum.

### Comment 5: migrated (2014-06-25T01:42:47.293-0700)

Lava blocks and Fire blocks also have REALLY WEIRD dark blue color! :I

### Comment 6: migrated (2014-06-25T07:52:13.779-0700)

Confirmed for 14w26a and b

### Comment 7: migrated (2014-07-07T07:44:25.767-0700)

Still a concern in 14w27a and 14w27b.

### Comment 8: kumasasa (2014-07-26T00:42:22.864-0700)

Is this still an issue in 14w30c ?

### Comment 9: migrated (2014-07-28T20:55:04.543-0700)

Yes~ It still works for me

### Comment 10: Sonicwave (2014-12-25T14:46:11.422-0800)

Still an issue up to 1.8.2-pre1.

### Comment 11: migrated (2016-11-19T15:14:53.061-0800)

Can confirm for 1.11. Easiest to see with moody brightness and smooth lighting off.

### Comment 12: migrated (2017-08-29T05:24:39.882-0700)

The issue appears to be that some values can be outside of the range expected by the night vision effect code.
Fix is easy, just requires moving the code in EntityRenderer.updateLightmap() a little:

```private void updateLightmap(float partialTicks)
{
	// ...

	// move this block from here ---
	if (this.mc.player.isPotionActive(MobEffects.NIGHT_VISION))
	{
		float f15 = this.getNightVisionBrightness(this.mc.player, partialTicks);
		float f12 = 1.0F / f8;

		if (f12 > 1.0F / f9)
		{
			f12 = 1.0F / f9;
		}

		if (f12 > 1.0F / f10)
		{
			f12 = 1.0F / f10;
		}

		f8 = f8 * (1.0F - f15) + f8 * f12 * f15;
		f9 = f9 * (1.0F - f15) + f9 * f12 * f15;
		f10 = f10 * (1.0F - f15) + f10 * f12 * f15;
	}

	if (f8 > 1.0F)
	{
		f8 = 1.0F;
	}

	if (f9 > 1.0F)
	{
		f9 = 1.0F;
	}

	if (f10 > 1.0F)
	{
		f10 = 1.0F;
	}

	// to here ---

	float f16 = this.mc.gameSettings.gammaSetting;
	float f17 = 1.0F - f8;
	float f13 = 1.0F - f9;
	float f14 = 1.0F - f10;
	f17 = 1.0F - f17 * f17 * f17 * f17;
	f13 = 1.0F - f13 * f13 * f13 * f13;
	f14 = 1.0F - f14 * f14 * f14 * f14;
	f8 = f8 * (1.0F - f16) + f17 * f16;
	f9 = f9 * (1.0F - f16) + f13 * f16;
	f10 = f10 * (1.0F - f16) + f14 * f16;
	f8 = f8 * 0.96F + 0.03F;
	f9 = f9 * 0.96F + 0.03F;
	f10 = f10 * 0.96F + 0.03F;

	// ...
}```

### Comment 13: migrated (2018-09-01T16:07:36.758-0700)

Confirmed for 1.13.1.

### Comment 14: migrated (2019-04-20T04:53:38.834-0700)

Confirmed for 1.14-prerelease-5

### Comment 15: Silicon42 (2019-10-17T15:55:10.708-0700)

Confirmed for 19w42a. It also affects the UI, color now, tinting it blue and darkening it. Should I make a separate bug report for that?

### Comment 16: [Mod]Les3awe (2019-10-17T16:00:59.961-0700)

@, 19w42a is this ticket MC-161849.

### Comment 17: tryashtar (2019-11-07T10:41:49.271-0800)

Is this fixed in 19w45a? It's hard for me to tell

### Comment 18: TheBoy358 (2019-11-07T10:45:51.502-0800)

Yeah it seem to be fixed in 19w45a for me.

### Comment 19: TheBoy358 (2019-11-08T06:26:12.724-0800)

Still fixed in 19w45b.

### Comment 20: migrated (2021-12-05T19:37:33.768-0800)

this seems to be a glitch in 1.18!

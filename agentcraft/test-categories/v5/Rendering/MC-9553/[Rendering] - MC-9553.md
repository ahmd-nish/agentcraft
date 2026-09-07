# MC-9553: Wrong rendering order of particles, hitboxes, clouds, transparent blocks, breaking animations and various other transparent textures

**Mojira URL:** [https://bugs.mojang.com/browse/MC-9553](https://bugs.mojang.com/browse/MC-9553)

## Report details

- **Mojira categories:** Rendering
- **Project:** MC
- **Issue key:** MC-9553
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2013-02-10T03:22:12.161-0800
- **Updated:** 2025-04-29T10:58:43.904-0700
- **Resolution date:** 2024-02-03T00:10:59.574-0800
- **Affects versions:** Snapshot 13w06a; Snapshot 13w07a; Snapshot 13w09a; Snapshot 13w09b; Snapshot 13w09c; Snapshot 13w10a; Snapshot 13w10b; Minecraft 1.5; Snapshot 13w11a; Minecraft 1.5.1; Snapshot 13w16a; Snapshot 13w16b; Minecraft 1.5.2; Snapshot 13w17a; Snapshot 13w18a; Snapshot 13w18b; Snapshot 13w18c; Snapshot 13w19a; Snapshot 13w21a; Snapshot 13w21b; Snapshot 13w22a; Snapshot 13w23a; Snapshot 13w23b; Snapshot 13w24a; Snapshot 13w24b; Snapshot 13w25a; Snapshot 13w25b; Snapshot 13w25c; Snapshot 13w26a; Minecraft 1.6; Minecraft 1.6.1; Minecraft 1.6.2; Minecraft 1.6.3; Minecraft 1.6.4; Minecraft 13w36a; Minecraft 13w36b; Minecraft 13w37a; Minecraft 13w37b; Minecraft 13w38a; Minecraft 13w38b; Minecraft 13w38c; Minecraft 13w39a; Minecraft 13w39b; Minecraft 13w41a; Minecraft 13w41b; Minecraft 13w42a; Minecraft 13w42b; Minecraft 13w43a; Minecraft 1.7; Minecraft 1.7.1; Minecraft 1.7.2; Minecraft 13w47a; Minecraft 13w47b; Minecraft 13w47c; Minecraft 13w47d; Minecraft 13w47e; Minecraft 13w48a; Minecraft 13w48b; Minecraft 13w49a; Minecraft 1.7.3; Minecraft 1.7.4; Minecraft 14w02a; Minecraft 14w02b; Minecraft 14w02c; Minecraft 14w03a; Minecraft 14w03b; Minecraft 14w04a; Minecraft 14w04b; Minecraft 14w05a; Minecraft 14w05b; Minecraft 14w06a; Minecraft 14w06b; Minecraft 14w07a; Minecraft 14w08a; Minecraft 1.7.5; Minecraft 14w10b; Minecraft 14w10c; Minecraft 14w11b; Minecraft 1.7.9; Minecraft 14w17a; Minecraft 14w18a; Minecraft 14w20a; Minecraft 14w20b; Minecraft 14w21a; Minecraft 14w21b; Minecraft 14w25b; Minecraft 1.7.10; Minecraft 14w28a; Minecraft 14w28b; Minecraft 14w29a; Minecraft 14w29b; Minecraft 14w30b; Minecraft 14w30c; Minecraft 14w31a; Minecraft 14w32a; Minecraft 14w32b; Minecraft 14w32c; Minecraft 14w32d; Minecraft 14w33c; Minecraft 14w34a; Minecraft 14w34b; Minecraft 14w34c; Minecraft 14w34d; Minecraft 1.8-pre1; Minecraft 1.8-pre2; Minecraft 1.8; Minecraft 1.8.1; Minecraft 1.8.3; Minecraft 1.8.4; Minecraft 1.8.8; Minecraft 15w31c; Minecraft 15w32a; Minecraft 15w32b; Minecraft 15w32c; Minecraft 15w33b; Minecraft 15w33c; Minecraft 15w34d; Minecraft 15w35b; Minecraft 15w35e; Minecraft 15w36b; Minecraft 15w36c; Minecraft 15w36d; Minecraft 15w39c; Minecraft 15w40b; Minecraft 15w41b; Minecraft 15w42a; Minecraft 15w43a; Minecraft 15w43c; Minecraft 15w44a; Minecraft 15w44b; Minecraft 15w45a; Minecraft 15w46a; Minecraft 15w47a; Minecraft 15w47c; Minecraft 15w50a; Minecraft 15w51b; Minecraft 16w05b; Minecraft 16w06a; Minecraft 16w07a; Minecraft 16w07b; Minecraft 1.9 Pre-Release 1; Minecraft 1.9 Pre-Release 2; Minecraft 1.9 Pre-Release 3; Minecraft 1.9 Pre-Release 4; Minecraft 1.9; Minecraft 1.9.1 Pre-Release 1; Minecraft 1.9.1 Pre-Release 2; Minecraft 1.9.1 Pre-Release 3; Minecraft 1.9.2; Minecraft 1.9.3 Pre-Release 1; Minecraft 1.9.3 Pre-Release 3; Minecraft 1.9.4; Minecraft 16w20a; Minecraft 16w21a; Minecraft 16w21b; Minecraft 1.10 Pre-Release 1; Minecraft 1.10 Pre-Release 2; Minecraft 1.10; Minecraft 1.10.1; Minecraft 1.10.2; Minecraft 16w32b; Minecraft 16w33a; Minecraft 16w35a; Minecraft 16w36a; Minecraft 16w39b; Minecraft 16w39c; Minecraft 16w40a; Minecraft 16w43a; Minecraft 16w44a; Minecraft 1.11 Pre-Release 1; Minecraft 1.11; Minecraft 16w50a; Minecraft 1.11.2; Minecraft 17w06a; Minecraft 17w13b; Minecraft 17w16b; Minecraft 17w17b; Minecraft 17w18a; Minecraft 17w18b; Minecraft 1.12 Pre-Release 1; Minecraft 1.12 Pre-Release 2; Minecraft 1.12 Pre-Release 3; Minecraft 1.12 Pre-Release 4; Minecraft 1.12 Pre-Release 5; Minecraft 1.12 Pre-Release 6; Minecraft 1.12 Pre-Release 7; Minecraft 1.12; Minecraft 17w31a; Minecraft 1.12.1 Pre-Release 1; Minecraft 1.12.1; Minecraft 1.12.2 Pre-Release 1; Minecraft 1.12.2 Pre-Release 2; Minecraft 1.12.2; Minecraft 17w43a; Minecraft 17w43b; Minecraft 17w45b; Minecraft 17w46a; Minecraft 17w47a; Minecraft 17w47b; Minecraft 17w48a; Minecraft 18w03b; Minecraft 18w05a; Minecraft 18w06a; Minecraft 18w07a; Minecraft 18w07b; Minecraft 18w07c; Minecraft 18w08a; Minecraft 18w08b; Minecraft 18w09a; Minecraft 18w10a; Minecraft 18w10b; Minecraft 18w10c; Minecraft 18w10d; Minecraft 18w11a; Minecraft 18w14a; Minecraft 18w14b; Minecraft 18w15a; Minecraft 18w16a; Minecraft 18w19a; Minecraft 18w19b; Minecraft 18w20a; Minecraft 18w20b; Minecraft 18w20c; Minecraft 18w21a; Minecraft 18w21b; Minecraft 18w22a; Minecraft 18w22b; Minecraft 18w22c; Minecraft 1.13-pre1; Minecraft 1.13-pre2; Minecraft 1.13-pre3; Minecraft 1.13-pre4; Minecraft 1.13-pre5; Minecraft 1.13-pre6; Minecraft 1.13-pre7; Minecraft 1.13-pre8; Minecraft 1.13-pre9; Minecraft 1.13-pre10; Minecraft 1.13; Minecraft 18w30a; Minecraft 18w30b; Minecraft 18w31a; Minecraft 18w32a; Minecraft 18w33a; Minecraft 1.13.1-pre1; Minecraft 1.13.1-pre2; Minecraft 1.13.1; Minecraft 1.13.2-pre1; Minecraft 1.13.2-pre2; Minecraft 1.13.2; Minecraft 18w43a; Minecraft 18w43b; Minecraft 18w43c; Minecraft 18w44a; Minecraft 18w45a; Minecraft 18w46a; Minecraft 18w47a; Minecraft 18w47b; Minecraft 18w48a; Minecraft 18w48b; Minecraft 18w49a; Minecraft 18w50a; Minecraft 19w02a; Minecraft 19w03a; Minecraft 19w03b; Minecraft 19w03c; Minecraft 19w04a; Minecraft 19w04b; Minecraft 19w05a; Minecraft 19w06a; Minecraft 19w07a; Minecraft 19w08a; Minecraft 19w08b; Minecraft 19w09a; Minecraft 19w11a; Minecraft 19w11b; Minecraft 19w12b; Minecraft 19w13a; Minecraft 19w13b; Minecraft 19w14a; Minecraft 19w14b; Minecraft 1.14 Pre-Release 1; Minecraft 1.14 Pre-Release 2; Minecraft 1.14 Pre-Release 3; Minecraft 1.14 Pre-Release 5; Minecraft 1.14; Minecraft 1.14.1 Pre-Release 1; Minecraft 1.14.1; Minecraft 1.14.2 Pre-Release 1; Minecraft 1.14.2 Pre-Release 2; Minecraft 1.14.2 Pre-Release 3; Minecraft 1.14.2 Pre-Release 4; Minecraft 1.14.2; Minecraft 1.14.3 Pre-Release 1; Minecraft 1.14.3 Pre-Release 2; Minecraft 1.14.3 Pre-Release 3; Minecraft 1.14.3 Pre-Release 4; Minecraft 1.14.3; Minecraft 1.14.4 Pre-Release 1; Minecraft 1.14.4 Pre-Release 2; Minecraft 1.14.4 Pre-Release 3; Minecraft 1.14.4 Pre-Release 4; Minecraft 1.14.4 Pre-Release 5; Minecraft 1.14.4 Pre-Release 6; 1.14.4 Pre-Release 7; 1.14.4; 19w34a; 19w35a; 19w36a; 19w37a; 19w38b; 19w38a
- **Fix versions:** 19w39a
- **Labels:** cloud; fire; flame; heart; ice; ink; particle; rendering; texture; torch; water
- **Watchers:** 1
- **Attachments:** 101
- **Attachment filenames:** 1.8 XPOrb shadows.png; 14w30c colored glass.png; 14w30c Ender Dragon Death.png; 14w30c Ender Dragon Death Other Mobs infront.png; 14w30c moving worldborder.png; 18w07b Ink squid particles black and blue.png; 2013-02-27_21.46.57.png; 2013-10-21_14.05.44.png; 2013-10-27_11.37.03.png; 2013-11-17_17.12.53.png; 2014-01-24_11.03.24.png; 2014-01-25_00.12.39.png; 2014-02-07_15.46.15.png; 2014-02-23_16.24.54.png; 2014-03-14_16.46.52.png; 2014-03-25_23.47.43.png; 2014-04-25_09.48.12.png; 2014-09-06_23.31.14.png; 2015-03-21_21.26.41.png; 2015-08-29_10.28.11.png; 2015-09-04_18.27.42-.png; 2015-09-06_21.07.24.png; 2015-10-23_13.50.16.png; 2015-10-23_13.54.34.png; 2015-10-23_13.54.41.png; 2015-10-28_18.31.08.png; 2015-11-20_22.55.35.png; 2015-11-20_22.55.56.png; 2015-11-20_22.56.36.png; 2015-11-20_22.56.55.png; 2015-11-20_22.57.53.png; 2015-12-12_15.56.26.png; 2015-12-25_09.44.35.png; 2015-12-25_09.44.42.png; 2015-12-29_17.57.41.png; 2015-12-29_17.58.05.png; 2016-01-08_18.26.40.png; 2016-02-05_20.19.10.png; 2016-02-05_20.19.12.png; 2016-06-28_19.38.50.png; 2017-06-17_14.51.29.png; 2017-06-17_14.53.09.png; 2017-11-29_01.22.19.png; 2018-01-22_20.35.27.png; 2018-02-15_16.05.04.png; 2018-03-08_18.54.31.png; 2018-04-10_15.28.07.png; 2018-04-10_15.53.36.png; 2018-05-11_20.53.26.png; 2018-05-13_14.29.47.png; 2018-05-15_22.08.07.png; 2018-06-17_16.13.25.png; 2018-06-21_10.18.14.png; 2018-06-21_10.19.09.png; 2018-06-21_10.19.17.png; 2018-06-21_10.35.26.png; 2018-06-28_21.59.09.png; 2018-07-12_14.44.38.png; 2018-07-18_14.50.10.png; 2018-11-07_16.44.36.png; 2019-04-24_23.57.20.png; 2019-05-19_13.57.44.png; 2019-05-28_05.00.09.png; 2019-06-25_16.50.58.png; 2019-07-16_11.10.06.png; 2019-07-16_11.11.17.png; 2019-07-16_11.16.41.png; 2019-07-16_11.21.29.png; 2019-07-16_11.24.32.png; 4dddda7acbaf3d4aef48c5851d14dc00.png; 5b949f363fe1abc5c1009b6c217f7a29.png; Burning Phantom Rendering Bug.png; Campfire.png; clouds_glass.jpg; e3aa86b47f9227e3aa87434f0d578ace.png; glass campfire.png; GlassOverEffectParticles1.png; GlassOverEffectParticles2.png; hitbox_player_shulker.png; image.jpg; image-2018-11-15-00-36-54-543.png; image-2019-08-21-10-47-01-772.png; map marker text.jpg; phantom_water.png; phantom_water2.png; Phantom wing visual bug.png; Phantom wing visual bug 2.png; Screenshot_1.png; Screenshot_2.png; Screenshot_3.png; Screenshot_4.png; Screenshot_5.png; Screenshot_6.png; Screenshot_7.png; Screenshot_8.png; screenshot-1.png; slime-blocks-clouds.png; water_hitbox.jpg; water bug.png; water bug2.png; water bug3.png
- **Issue links:** Relates:inward:MC-161885:Many transparent things do not render behind slimes | Relates:inward:MC-200056:Some particles render behind the outline of the targeted block | Relates:outward:MC-36228:The outline of the block I point at is not visible under/behind  water. | Duplicate:inward:MC-10353:Block breaking particles are drawn behind the selection box | Duplicate:inward:MC-10358:transparent digging particles | Duplicate:inward:MC-10392:Torch Flame Visuals | Duplicate:inward:MC-10448:Particles effects are faded by clouds | Duplicate:inward:MC-10457:Clouds render in front of other particles | Duplicate:inward:MC-10458:Block breaking animation incorrect | Duplicate:inward:MC-10537:''block break bug'' | Duplicate:inward:MC-10549:Fire particles turn (almost) invisible on ice (they don't make the ice see-throught, though) | Duplicate:inward:MC-10608:Clouds overlap block breaking particals | Duplicate:inward:MC-10610:Particles faded | Duplicate:inward:MC-10684:Transparent Particles | Duplicate:inward:MC-10710:Torch Bug | Duplicate:inward:MC-10765:Particles becoming opaque | Duplicate:inward:MC-10790:Particles behind clouds | Duplicate:inward:MC-10809:Hearts from breeding animals appear "behind" water and ice | Duplicate:inward:MC-10852:Can See Digging Animation Through Potion Bubbles | Duplicate:inward:MC-11013:Particles appear to be above the clouds when breaking blocks or any particles | Duplicate:inward:MC-11026:Clouds Overlap Particles | Duplicate:inward:MC-11043:Breaking blocks in front of water makes particles look like they are in the water | Duplicate:inward:MC-11099:Block Selector Overlays Block Particles | Duplicate:inward:MC-11125:Particles of a block breaking are underwater while the block was out | Duplicate:inward:MC-11145:Can see the outline of blocks while breaking them in creative | Duplicate:inward:MC-11172:When destroying a block the particles render behind the clouds | Duplicate:inward:MC-11278:Whenever I break a block the particles seem to go inside the lock, making the block semi-invisible. It's kinda wierd. | Duplicate:inward:MC-11283:Log hit box doesn't immedietly disappear | Duplicate:inward:MC-11476:Particles appear behind block breaking cracks | Duplicate:inward:MC-11486:Particles render under water or portal | Duplicate:inward:MC-11535:particles fade | Duplicate:inward:MC-11591:Flame particle glitch | Duplicate:inward:MC-11655:Particle rendering order problem | Duplicate:inward:MC-11722:Wire-frame rendered above particles | Duplicate:inward:MC-11758:Block effects are shown over particles | Duplicate:inward:MC-11840:Particles can be seen through | Duplicate:inward:MC-11871:Hit box is visible through particle effects | Duplicate:inward:MC-11933:Particles Appear Underwater if Water is Behind the Object | Duplicate:inward:MC-11946:Transparent Particles | Duplicate:inward:MC-12033:Tallgrass Animation Bug | Duplicate:inward:MC-12050:While breaking a block you can see the crack through the particals. | Duplicate:inward:MC-12066:Particles | Duplicate:inward:MC-12312:When I break blocks with water in the background, the particles that come off it are almost invisible because they are blue | Duplicate:inward:MC-12406:Particles shown under the outline of a block | Duplicate:inward:MC-12407:Particles appear underwater/Under block selector no matter what height they are generated at | Duplicate:inward:MC-12420:Water looks as if it is a layer infront of Food particles | Duplicate:inward:MC-12430:Particles being overlayed by water. | Duplicate:inward:MC-12445:Particles have a lower opacity than previous versions. | Duplicate:inward:MC-12711:Hitbox and splash potion | Duplicate:inward:MC-12901:Torch Fire Particles Dim when viewed over water | Duplicate:inward:MC-13027:Water behind Particles let the particles look transparency | Duplicate:inward:MC-13081:Entities and some blocks are visible through particles | Duplicate:inward:MC-13178:picture problem - the fire of the torch | Duplicate:inward:MC-13318:Block breaking particles are rendered behind block selection line | Duplicate:inward:MC-13536:Some particles, such as torch flame and food crumbs, render behind water or rails. | Duplicate:inward:MC-13868:Tame hearts appear behind water | Duplicate:inward:MC-13920:Particles | Duplicate:inward:MC-14363:Food particles show under water when on land | Duplicate:inward:MC-14771:incorrect particle texture | Duplicate:inward:MC-14932:Wireframe is rendered on top of particles | Duplicate:inward:MC-14981:Water makes hearts glitch | Duplicate:inward:MC-15262:Torch flame in front of water apears to be behind. | Duplicate:inward:MC-15268:Particle Viewing Error | Duplicate:inward:MC-15421:Particles appear behind water all the time | Duplicate:inward:MC-15473:Graphical bug when destroying block | Duplicate:inward:MC-15632:Torch effect bug | Duplicate:inward:MC-15754:Torches in water cause torch to dim. | Duplicate:inward:MC-15788:Strange effect of the nether portal when you look at it while you eat | Duplicate:inward:MC-16007:breeding heart particles are behind water. | Duplicate:inward:MC-16481:Heart animation behind water when near coast | Duplicate:inward:MC-16499:Taming heart's texture behind water | Duplicate:inward:MC-16515:Graphical Issue while looking through blaze smoke | Duplicate:inward:MC-16589:Water and hearts from dogs rendering incorrectly | Duplicate:inward:MC-16789:Chicken Heart and water merge | Duplicate:inward:MC-16957:Particules bug with water | Duplicate:inward:MC-17078:particle bug | Duplicate:inward:MC-17635:Bug | Duplicate:inward:MC-18028:Water being displayed over a broken block | Duplicate:inward:MC-18119:Block particles covered by water | Duplicate:inward:MC-18300:Particles turn invisible/highlights glass when in front of glass | Duplicate:inward:MC-18314:Anvil Particles glitching in front of water. | Duplicate:inward:MC-18675:Torch bug | Duplicate:inward:MC-18767:Can see blocks and clouds through fire smoke | Duplicate:inward:MC-19289:Water Particle issues | Duplicate:inward:MC-20956:[Visual] Lakes outline in Beacon Beam | Duplicate:inward:MC-21528:a | Duplicate:inward:MC-21629:Particles appear to be behind water. | Duplicate:inward:MC-23616:Torches Fire Glitching | Duplicate:inward:MC-24608:water texture will come in front of "animal-love-hearts" | Duplicate:inward:MC-24943:animal heart bug | Duplicate:inward:MC-25093:Particles show as if they are underwater | Duplicate:inward:MC-28161:transparent torches | Duplicate:inward:MC-28303:There is a particle bug with water | Duplicate:inward:MC-28393:Visual Bug | Duplicate:inward:MC-29282:Particles Bug | Duplicate:inward:MC-29393:Particle effects not keeping their color | Duplicate:inward:MC-30444:When Eating Any Food You Can't See The Food Particles When Water Is Behind It | Duplicate:inward:MC-30464:Error graphics. | Duplicate:inward:MC-30491:Love Entities and the Ocean | Duplicate:inward:MC-30528:Entities not apear on water | Duplicate:inward:MC-30625:Particle Effects disappear when facing water. (Not blend in) | Duplicate:inward:MC-31199:Mushroom Soup particles render like they would behind ice | Duplicate:inward:MC-33250:Particle Effect Water Graphic Error | Duplicate:inward:MC-33657:Water texture is rendering over the particle effect | Duplicate:inward:MC-34656:Particle effects appear behind stained glass | Duplicate:inward:MC-34658:Rendering Clouds | Duplicate:inward:MC-34674:clouds are rendered in front of partialy transparent blocks when viewed from above | Duplicate:inward:MC-34965:Clouds don't render properly Y Coordinate 127 and above | Duplicate:inward:MC-35010:Collision box too visible under water | Duplicate:inward:MC-35197:When you look at clouds through stained glass blocks or panes they are still white. | Duplicate:inward:MC-35248:cloud render | Duplicate:inward:MC-35336:Heart bug.. | Duplicate:inward:MC-35831:When facing towards water particles will appear blue | Duplicate:inward:MC-36223:Particles under breaking animation | Duplicate:inward:MC-36298:Paticels and Water | Duplicate:inward:MC-36742:Bug on "Breaking Ice" animation | Duplicate:inward:MC-36799:Block selector is hard to see when transparent blocks are against water blocks | Duplicate:inward:MC-37009:Block breaking effects show through potion particles, possibly more. | Duplicate:inward:MC-37125:Tesselation alpha unaffected by clouds | Duplicate:inward:MC-37194:Rendering Bug with clouds and particles | Duplicate:inward:MC-37475:Torch Flame Behind Water | Duplicate:inward:MC-37574:"Transparent" ice breaking animation. | Duplicate:inward:MC-38275:1.6.4's particle glitches have transferred into 1.7.2 | Duplicate:inward:MC-38716:Launch a firework in front of water and the water covers the exploding sparkles | Duplicate:inward:MC-38727:This is just a weird bug where you break a block and the particles make the blocks underneath transparent. Weird... but not serious. | Duplicate:inward:MC-38770:Water and stained glass render through fireworks, nothing else | Duplicate:inward:MC-38850:Torch flames are blue when water is behind it | Duplicate:inward:MC-38896:Colored glass makes clouds appear above them. | Duplicate:inward:MC-39665:Torch transparency w/ water bug | Duplicate:inward:MC-39720:Particles bug | Duplicate:inward:MC-39835:Water and Stained glass | Duplicate:inward:MC-40389:Torch fire is transparent to water | Duplicate:inward:MC-40696:Pixles Behind Water | Duplicate:inward:MC-40701:Partiсles bug | Duplicate:inward:MC-41115:FireWork Particles display behind water | Duplicate:inward:MC-41305:Breaking Vines Bug | Duplicate:inward:MC-41438:The "frame" that appears around blocks when you look at them, looks as if it is behind the ice | Duplicate:inward:MC-41600:Particles going -behind- water, not in front | Duplicate:inward:MC-41724:Minecraft Effects Glitch | Duplicate:inward:MC-41757:Part of water disappearing under leaves | Duplicate:inward:MC-41943:Bug in 1.7.2 when breaking ice with a certain block under it will take over the particles instead of the ice particles | Duplicate:inward:MC-42090:If Breaking animation is fully opaque, it will override all ice/water/stained glass | Duplicate:inward:MC-42292:Torch (and maybe other) particles are blue tinted when water is behind it | Duplicate:inward:MC-43945:Breaking Glass Xray through water | Duplicate:inward:MC-44113:Minecraft Torch Flame Layering | Duplicate:inward:MC-44402:Particles seen over water are strangely transparent... | Duplicate:inward:MC-44418:Clouds appearing weird through water. | Duplicate:inward:MC-44480:Particles load weirdly with a slime block | Duplicate:inward:MC-44507:Clouds render incorrectly through water. | Duplicate:inward:MC-44518:Particle effects go through slime block | Duplicate:inward:MC-44612:Bug Clouds on Ice | Duplicate:inward:MC-44743:colored windows and clouds | Duplicate:inward:MC-44923:Coloured Transparent Block Bug | Duplicate:inward:MC-44941:I can see clouds through block particles | Duplicate:inward:MC-44983:Slime block particles are rendered behind another Slime block | Duplicate:inward:MC-45096:Particle Visibility w/ Slime Blocks | Duplicate:inward:MC-45098:Clouds Visible through Slime Blocks | Duplicate:inward:MC-45323:Visual bug when viewing clouds through stained glass at night | Duplicate:inward:MC-45389:Particles don't show up correctly in front of water | Duplicate:inward:MC-45396:Clouds bug | Duplicate:inward:MC-45401:Particle bug | Duplicate:inward:MC-45676:Hit box of blocks hides next to slime blocks | Duplicate:inward:MC-45700:Particles | Duplicate:inward:MC-46073:Particles through water | Duplicate:inward:MC-46147:Slime Blocks and smoke | Duplicate:inward:MC-46397:glass entity glitch | Duplicate:inward:MC-46701:hitbox made ​​underwater | Duplicate:inward:MC-47303:Breaking Block Particle Near Slime Block Goes into the slime block | Duplicate:inward:MC-47402:Item Fragments | Duplicate:inward:MC-47487:Rendering inconsistency for Barrier blocks in creative mode | Duplicate:inward:MC-47767:Barrier new creative particles Issues | Duplicate:inward:MC-47808:Iron bars hitbox is wrong | Duplicate:inward:MC-47956:Barrier particle bugs when displaying next to a slime block | Duplicate:inward:MC-48096:Particle Effect Bug | Duplicate:inward:MC-48100:Barrier Z-Fighting | Duplicate:inward:MC-48119:barriers layering over each other and Disappearing texture | Duplicate:inward:MC-48217:Barrier Texture Overlap Glitch | Duplicate:inward:MC-48289:Barrier Texture vs. Stained Glass | Duplicate:inward:MC-48433:particles and water | Duplicate:inward:MC-48619:Barrier particle x-ray | Duplicate:inward:MC-48715:Particles render behind water | Duplicate:inward:MC-48746:Transparency with transparency | Duplicate:inward:MC-48783:Barrier blocks and hitboxes don't appear when there's a slime block behind them | Duplicate:inward:MC-48915:Particle against water in 1.7.4 | Duplicate:inward:MC-48992:Barrier Blocks | Duplicate:inward:MC-49034:Invisible Charged Creepers render incorrectly | Duplicate:inward:MC-49064:Overlap/overlay error | Duplicate:inward:MC-49092:Image of Barrier Block | Duplicate:inward:MC-49107:Block Outline Box Render | Duplicate:inward:MC-49135:Slime block visible through particles | Duplicate:inward:MC-49186:the barrier blocks texture glitches out | Duplicate:inward:MC-49263:Particle of Barrier in Slime Block | Duplicate:inward:MC-49419:Wireframe On Barriers do not Show up when with water | Duplicate:inward:MC-49464:Glass pane section invisible when in front of water | Duplicate:inward:MC-49505:Particles and blocks outlines appear behind water even though it's not | Duplicate:inward:MC-49552:Slime Blocks are visible through particles | Duplicate:inward:MC-49746:slime block glitch | Duplicate:inward:MC-50141:Pieces of food makes water / lava weird while eating | Duplicate:inward:MC-50172:Torch flame appears behind water when in front | Duplicate:inward:MC-50694:Barrier img tinted with stained glass | Duplicate:inward:MC-51112:Barrier overlapping | Duplicate:inward:MC-51394:Torch fire is blue when put against a water background | Duplicate:inward:MC-51460:Strange Barrier Visuals | Duplicate:inward:MC-51494:Glass not showing itself properly | Duplicate:inward:MC-51537:Texture Bug - Barrier | Duplicate:inward:MC-51580:Water texture dissapears when breaking a transparent block | Duplicate:inward:MC-51697:Partical glitch | Duplicate:inward:MC-51737:I found a bit of  visual glitch when "Messing around" | Duplicate:inward:MC-52391:cloud + translucent block bug | Duplicate:inward:MC-52507:Weird render of barrier w/ water behind | Duplicate:inward:MC-52623:Z-level with fog and block breaking particles | Duplicate:inward:MC-52687:You Cannot see particles in front of slime blocks. | Duplicate:inward:MC-53314:Stained Glass Glitch | Duplicate:inward:MC-53428:Particle Bug w/ Worldborder | Duplicate:inward:MC-53828:Water rendering in front of particles | Duplicate:inward:MC-53829:River and Ocean Biomes show different shades through Stained Glass. | Duplicate:inward:MC-54222:Slime blocks invisible trough clouds | Duplicate:inward:MC-54507:Water renders on top of the World Border animation | Duplicate:inward:MC-54596:Water goes through barrier block particles | Duplicate:inward:MC-54661:Worldborder rendering incorrectley in front of water | Duplicate:inward:MC-55001:Can't see beacon beam | Duplicate:inward:MC-55047:Slime blocks render behind ice | Duplicate:inward:MC-55306:Stained glass viewed through stained glass brightness | Duplicate:inward:MC-55400:Water disapear behind exploding firework | Duplicate:inward:MC-55561:Fireworks near ice causes part of ice to not render | Duplicate:inward:MC-55665:The texture of the "tinted glasses" disappears with fireworks | Duplicate:inward:MC-55888:Depth level of snowflakes | Duplicate:inward:MC-55998:Slimeblock rendering hitboxes incorrectly | Duplicate:inward:MC-56056:Clouds are Bugged when looking from the top throw Colored Glass | Duplicate:inward:MC-56176:Rendering | Duplicate:inward:MC-56232:Wolf heart particles overlaying with ice incorrectly | Duplicate:inward:MC-56365:Cloud shows through slime block | Duplicate:inward:MC-57842:Wierd SlimeBlock Render Glitch | Duplicate:inward:MC-57947:Oddly rendered clouds looking through portals | Duplicate:inward:MC-58085:Elder Guardian effect makes some things not render behind it | Duplicate:inward:MC-58305:Ice graphical bug when looking from certain angle | Duplicate:inward:MC-59410:Slime block transparency bug | Duplicate:inward:MC-59424:F3+B blue line of sight does not render infront of chests | Duplicate:inward:MC-59660:Particles turn blue when faced with water | Duplicate:inward:MC-60870:Strange Particle Effect | Duplicate:inward:MC-61078:Water textures are rendered before any particles | Duplicate:inward:MC-61446:Multiplayer Water Glitch | Duplicate:inward:MC-61745:Clouds render funny through portals if above. | Duplicate:inward:MC-61972:Minor Stained Glass Bug | Duplicate:inward:MC-62072:When you stand above a torch and look at the flame, and water is behins your view, the flames are behind the water | Duplicate:inward:MC-62126:Flowing water looks glitchy when looked at through regular water | Duplicate:inward:MC-62251:Stained glass rendering improperly (bottom layer rendering above the top layer) | Duplicate:inward:MC-62360:The dark blue shapes in frozen river's ice | Duplicate:inward:MC-62664:Fireballs hide in Water | Duplicate:inward:MC-62871:Unsure if this is a bug or not? Slime blocks viewed awkwardly? | Duplicate:inward:MC-63639:World Border renders behind Water | Duplicate:inward:MC-64234:error with the color glass panel and color glass | Duplicate:inward:MC-65012:Ice blocks' breaking animation color ignores translucent/transparent blocks, including itself | Duplicate:inward:MC-65038:Torch Bug | Duplicate:inward:MC-66443:Slight Visual/graphical bug | Duplicate:inward:MC-66670:Beacon beam "aura" renders behind certain tile entities | Duplicate:inward:MC-67249:Name Plates do not appear in front of burning mob's fire | Duplicate:inward:MC-67354:Slime Block Renders incorrectly in-hand | Duplicate:inward:MC-67556:Leaves underwater have "falling water" sides (visual issue) | Duplicate:inward:MC-67584:Slime Block | Duplicate:inward:MC-67690:Blocks, which placed in void (in non-generated chunks), will be shows up in another non-generated chunks | Duplicate:inward:MC-67718:Transperancy Bug | Duplicate:inward:MC-67960:Slimeblock Rendering | Duplicate:inward:MC-68138:Beacons are not visible through clouds | Duplicate:inward:MC-68195:Stained Glass Pane changes the color of lines | Duplicate:inward:MC-68249:Fireworks cause water to glitch out. | Duplicate:inward:MC-68357:Slime blocks have no wire frame | Duplicate:inward:MC-68742:Cloud behind waterfall is drawn like it is in front of waterfall | Duplicate:inward:MC-68761:Invalid World border rendering | Duplicate:inward:MC-68870:Shifting in front of a portal causes player name to dim | Duplicate:inward:MC-69527:Clouds appear through slime blocks | Duplicate:inward:MC-69592:Clouds shown behind water | Duplicate:inward:MC-69629:Particles appear behind transparent blocks | Duplicate:inward:MC-69955:Transparent | Duplicate:inward:MC-69969:Water is rendered in front of effect particles. | Duplicate:inward:MC-69991:Slime Blocks in Sky | Duplicate:inward:MC-70449:Invisible user behind sneaking username | Duplicate:inward:MC-70826:Rendering issue when more than one transparent is overlayed | Duplicate:inward:MC-71340:Graphic Bug with the slimeblock | Duplicate:inward:MC-71794:Grafic issue when looking at water y=255+ | Duplicate:inward:MC-72074:Snow Transparency color changes abnormally with water background | Duplicate:inward:MC-72416:Nether portal texture is in front of entity boxes | Duplicate:inward:MC-72514:See-through Player Names Clip Through Other Players / Entities | Duplicate:inward:MC-72773:Firework/Water transparency | Duplicate:inward:MC-73214:Water Turns Invisible When Breaking Glass Panes | Duplicate:inward:MC-73603:Horse Killing Gets Achievement "Cow Tipper" | Duplicate:inward:MC-73609:Slime blocks held in player hand render behind chests and item frames | Duplicate:inward:MC-74018:Water blocks render over rain particles. | Duplicate:inward:MC-74051:Sign and Water bug | Duplicate:inward:MC-74497:Weird rendering through transparant blocks as Dropped-Item entities and as a part of an ArmorStand | Duplicate:inward:MC-74626:Transparent Queue Shader Error (Fireworks over Water) | Duplicate:inward:MC-74744:Hit boxes render behind water when actually in front of water | Duplicate:inward:MC-75158:Unrendered Clouds appearing when looking through Custom Names | Duplicate:inward:MC-76154:Firework Particles rendered behind water | Duplicate:inward:MC-76214:Decoration Blocks in Minecarts cover hitboxlines | Duplicate:inward:MC-76319:A salute does invisible the block of mucus, the block of mucus publishes black displacements | Duplicate:inward:MC-76509:entity opacity | Duplicate:inward:MC-77313:Rain layer rendered behind glass if underwater | Duplicate:inward:MC-77567:Glass blocks not rendering good | Duplicate:inward:MC-77589:Bad crack texture while breaking stained glass | Duplicate:inward:MC-78285:Clouds through stained glass | Duplicate:inward:MC-78535:Glass break particles | Duplicate:inward:MC-78647:Clouds make water invisible/Clouds render in front of water | Duplicate:inward:MC-78778:Incorect glass panel breaking animation | Duplicate:inward:MC-78923:Water sometimes doesn't get the ice overlay | Duplicate:inward:MC-79630:bugs with slime block | Duplicate:inward:MC-79684:Minecrfat slime block texture bug | Duplicate:inward:MC-79796:Buggy Ice Texture | Duplicate:inward:MC-80784:Blocks/Entities not rendering when looking through transparent block model. | Duplicate:inward:MC-81285:Slime Blocks in Held by Other Players are Overlapped by Water | Duplicate:inward:MC-82462:Visual bug with capes and stained glass | Duplicate:inward:MC-82680:we can see through walls with pumpkin on an armor stand or a player | Duplicate:inward:MC-85409:Water can be seen through certain particles | Duplicate:inward:MC-85613:The clouds are shown on the Semi transparent block. | Duplicate:inward:MC-85932:Lingering Potion Particles Render Behind Water | Duplicate:inward:MC-86162:Water render problem | Duplicate:inward:MC-86199:Particles appear as if they're under the ocean | Duplicate:inward:MC-86481:Reeds' block outline invisible with water background | Duplicate:inward:MC-87047:Clouds can be seen through slime blocks | Duplicate:inward:MC-87092:Slime Blocks Above Clouds | Duplicate:inward:MC-87445:Snowflakes and other particles render underneath water | Duplicate:inward:MC-87623:Strange texture of water through World Borders | Duplicate:inward:MC-87647:Clouds with ice are glitchy | Duplicate:inward:MC-87649:Slime block on hand with F5 is gone on sign | Duplicate:inward:MC-88070:Wrong hitbox render layer | Duplicate:inward:MC-88393:You can see water thru particles | Duplicate:inward:MC-88986:Lingering  rendering not correct near water | Duplicate:inward:MC-89438:Particles is Wrong When We Look At Glass or Water | Duplicate:inward:MC-90277:fireworks over water glitch | Duplicate:inward:MC-90383:Cloud Transparency is wrong after y = 127 | Duplicate:inward:MC-90426:When standing on a slime block above clouds, clouds are glichy | Duplicate:inward:MC-90597:Graphical bug with ice and frosted ice | Duplicate:inward:MC-90736:The seethough bug | Duplicate:inward:MC-91208:Particles from breaking stained glass blocks and panes allow you to see through water | Duplicate:inward:MC-92325:Slime Block Rendering | Duplicate:inward:MC-92925:Lingering potions and Potions particles textures change color when overlaying water | Duplicate:inward:MC-93070:Unable to through Slime rendering the particles / entity / Some of block | Duplicate:inward:MC-93341:Slime Texture and Lighting issue. | Duplicate:inward:MC-93883:Chest rendering over displayed hitboxs and certain blocks in hand. | Duplicate:inward:MC-93957:Water texture not showing under ice blocks | Duplicate:inward:MC-94315:Glass and water disappear when seen through firework explosion. | Duplicate:inward:MC-94444:Vines allow you to see through water! | Duplicate:inward:MC-94551:Transparency in particles allows seeing through opaque blocks | Duplicate:inward:MC-94652:Disappearing Stained Glass Panes with Fireworks | Duplicate:inward:MC-94748:Water overlaps Lingering potion particles | Duplicate:inward:MC-94791:Particle effects don't show behind multiple/"circled" glass panes on ArmorStands | Duplicate:inward:MC-95622:New Particle -> Old bugs | Duplicate:inward:MC-96011:Slime Block Submerged In Water Graphical Glitches | Duplicate:inward:MC-96019:Debug hitboxes rendering without depth test | Duplicate:inward:MC-96456:Fireworks make water turn invisable | Duplicate:inward:MC-96748:Mob When Close To Charge Creeper Is Weird | Duplicate:inward:MC-97024:A Bug In The Minecraft Version 16w06a! | Duplicate:inward:MC-98019:ArmorStand Hand Item Disappears In Front Of Chest | Duplicate:inward:MC-98035:Semi transparent block on heads render behind other blocks | Duplicate:inward:MC-98162:Lingering Potions cause wrong rendering of water | Duplicate:inward:MC-99029:Water is visible through thick lingering potions | Duplicate:inward:MC-99724:Elytra transparency issues | Duplicate:inward:MC-100408:potion IDK WHAT THIS IS | Duplicate:inward:MC-100562:Lingering potion | Duplicate:inward:MC-101335:Water is being rendered "above" particles | Duplicate:inward:MC-101361:Potions particles are strange if they are above water | Duplicate:inward:MC-101831:Stained glass appearing through potion effects | Duplicate:inward:MC-102009:Minecraft PC: Nether Portal Blocks Render in Front of Particles (from Lingering Potion) | Duplicate:inward:MC-102195:I reported this bug also in the 1.9 snapshot | Duplicate:inward:MC-102761:FireWorks | Duplicate:inward:MC-103946:Clouds render in front of Nether portal | Duplicate:inward:MC-104180:Blocks' bounding boxes in incorrect color | Duplicate:inward:MC-104463:Nether portal , walter through walter | Duplicate:inward:MC-104536:f3 g and cloud cause the borders not being seen | Duplicate:inward:MC-105326:Rendering issues with entity hitboxes | Duplicate:inward:MC-105938:Minor Fireworks Glitch | Duplicate:inward:MC-106247:Block hotbox outlines do not appear underwater | Duplicate:inward:MC-106267:Rain Renders Behind | Duplicate:inward:MC-108121:Can see water through beacon edges | Duplicate:inward:MC-108256:glass on supercharged slime machine renders wrongly when moved after a long while | Duplicate:inward:MC-108602:Spell particle invisible in front of custom textures | Duplicate:inward:MC-108818:When player fall on lily pad, a breaking particles are wrong | Duplicate:inward:MC-110000:Chest will missing when see through a slime | Duplicate:inward:MC-110332:ArmorStand with Slime in hand does not render correctly | Duplicate:inward:MC-110847:Clouds overlay water | Duplicate:inward:MC-110932:When glass is dropped you can see through all glass. | Duplicate:inward:MC-111474:Firework particles make water disappear [16w50a] | Duplicate:inward:MC-111486:Firework blast sees through water | Duplicate:inward:MC-111514:Firework Trails render behind Water. | Duplicate:inward:MC-112029:Sign se thru bug | Duplicate:inward:MC-112090:When a fire work trail goes past a lake it will be show under the lake texture and not on top | Duplicate:inward:MC-113509:Black background in nametags renders behind banners | Duplicate:inward:MC-114005:Firework transparent blocks glitch | Duplicate:inward:MC-114620:Slime blocks make transparent entities in front of them invisible/look like they're behind them. | Duplicate:inward:MC-114632:Nameplates don't occlude certain block entities | Duplicate:inward:MC-116846:Cloud bright true nether portal | Duplicate:inward:MC-117513:Blocks' hitboxes are invisible when inside water | Duplicate:inward:MC-117973:The clouds seem to be in the foreground if you look through glass and colored glass panels | Duplicate:inward:MC-118285:Particles from fireworks are faded when pass over water | Duplicate:inward:MC-118405:Fireworks: Water shows up too vividly when firework is fading out | Duplicate:inward:MC-118883:Ice blocks don't render properly behind beds when held in the hand | Duplicate:inward:MC-118922:1.12 WitchMagic particle displays behind water | Duplicate:inward:MC-119065:When stained glass is dropped on shulker boxes, you can see through the box and to the blocks behind it. | Duplicate:inward:MC-119124:Posion and slimeblock overlay | Duplicate:inward:MC-119632:Player model disappears behind lightning bolt | Duplicate:inward:MC-120398:Firworks not render water | Duplicate:inward:MC-120399:Minecraft fireworks render water not working | Duplicate:inward:MC-121540:Glass block hitbox is hidden when we look at water | Duplicate:inward:MC-122516:Glass dropped onto shulker box makes it go invisible | Duplicate:inward:MC-123127:View direction of item frames render in wrong order with hitboxes shown | Duplicate:inward:MC-124476:ice cross | Duplicate:inward:MC-125223:If a colored glass block is on a chest then you can look through the chest | Duplicate:inward:MC-125241:Block hovering border does not appear underwater | Duplicate:inward:MC-125332:Squid black ink render | Duplicate:inward:MC-125537:Squid ink particles above water are bugged | Duplicate:inward:MC-125771:Block selection not showing up underwater | Duplicate:inward:MC-125802:The light of the beacon dont work on water | Duplicate:inward:MC-126223:no outline for blocks underwater | Duplicate:inward:MC-126753:Phantom wings above water visual glitch | Duplicate:inward:MC-126760:New Phantom's model | Duplicate:inward:MC-126764:Phantom model glitch | Duplicate:inward:MC-126770:Phantom Wing Glitch | Duplicate:inward:MC-126790:Phantom texture glitch | Duplicate:inward:MC-126822:Phatom wing bug | Duplicate:inward:MC-126844:Phantom wings visual glitch | Duplicate:inward:MC-126845:There is no water visible through Phantom's wings | Duplicate:inward:MC-126885:Problem with phantoms' wings | Duplicate:inward:MC-126886:Phantoms' Wings do not render properly over Water & other Translucent Objects | Duplicate:inward:MC-126891:hitbox will disapear when underwater | Duplicate:inward:MC-126956:Selected block (looked at block) not outlined when underwater | Duplicate:inward:MC-126973:Viewing water through the wings of the Phantom make water transparent. | Duplicate:inward:MC-127076:Phantom's wings display bug | Duplicate:inward:MC-127089:Squid ink visual glitch | Duplicate:inward:MC-127103:Transparent wings (Phantom) | Duplicate:inward:MC-127131:Phantom wing visibiltiy bug | Duplicate:inward:MC-127574:Phantom wings bug | Duplicate:inward:MC-128026:FIX F5 ice and water glitch | Duplicate:inward:MC-128063:No block edges underwater | Duplicate:inward:MC-128235:Phantom's problems? | Duplicate:inward:MC-128402:Fence renders its hitbox behind a cloud | Duplicate:inward:MC-128421:Water see trough glitch with dropped stained glass(panes) | Duplicate:inward:MC-128744:Block edges appear to be under water | Duplicate:inward:MC-129011:Underside of Phantom wings look strange underwater. | Duplicate:inward:MC-129094:Glass pane makes shulker boxes transparent | Duplicate:inward:MC-129162:Tainted glass appear in squid ink | Duplicate:inward:MC-129167:Ink particles' colour is different from different side? | Duplicate:inward:MC-129187:Z index of glass display and water bottle splash potion effect | Duplicate:inward:MC-129288:Water texture doesn't show when phantom flies over | Duplicate:inward:MC-129331:Water not rendering behind pahntom wings | Duplicate:inward:MC-129387:Phantom error texture | Duplicate:inward:MC-129457:X-ray through the back of the Phantom wings | Duplicate:inward:MC-129458:X-ray through the back of the Phantom wings | Duplicate:inward:MC-129519:Water doesn't render behind phantom wings | Duplicate:inward:MC-129544:The block the player is pointing at doesn't have the slender cubic frame when the player is completely in water | Duplicate:inward:MC-129553:Fix visual glitch on Phantom mob | Duplicate:inward:MC-129901:Block outline doesn't show when underwater | Duplicate:inward:MC-130120:Block outlines are missing | Duplicate:inward:MC-130312:Phantom wings don't show water | Duplicate:inward:MC-130459:No Falling or Breaking Particles for stained glass | Duplicate:inward:MC-130710:Clouds Visible Through Water | Duplicate:inward:MC-130766:See through ice with Phantom wings | Duplicate:inward:MC-131128:When looking through a phantom's wing water doesn't render (best seen when summoning a phantom with no AI) | Duplicate:inward:MC-131135:Transparency bug with Phantom above water | Duplicate:inward:MC-131183:Glitch with soft lighting | Duplicate:inward:MC-131629:Transparent Phantom Wings | Duplicate:inward:MC-131741:Particles behind falling water texture | Duplicate:inward:MC-131936:Looks like night vision when you look on a giant phantom's wings. | Duplicate:inward:MC-132983:When looking at Phantom it doesnt show water texture when looking down at it. | Duplicate:inward:MC-133064:Water not rendered through transparent texture parts of Phantom wings | Duplicate:inward:MC-133301:Cant see blocks or entities while in a cloud (in 3rd person) | Duplicate:inward:MC-133350:Color of ink particles underwater | Duplicate:inward:MC-133456:Potion particles render behind water | Duplicate:inward:MC-133533:Bug with particles | Duplicate:inward:MC-133572:Water overlaps particle "Squid Ink" on land. | Duplicate:inward:MC-133843:Water not rendering when seen through phantom wings | Duplicate:inward:MC-133846:Visual glitch with ice and water in third person perspective | Duplicate:inward:MC-133987:Phantoms Texture Acts WeIrd When Over Water | Duplicate:inward:MC-134017:Phantoms have a glitched model view, over water | Duplicate:inward:MC-134236:Phantom wings transparency | Duplicate:inward:MC-134721:Mobs make water invisible | Duplicate:inward:MC-134743:Text on signs renders behind chests. | Duplicate:inward:MC-135527:GLASS block on top on a bed visual glitch | Duplicate:inward:MC-136037:The phantom's wings make the water glitch a bit | Duplicate:inward:MC-136243:bugs texture phantom | Duplicate:inward:MC-136247:Barrier Block's Collision Box Is Slightlly Lighter Underwater Than On Land | Duplicate:inward:MC-136507:Phantom glitch | Duplicate:inward:MC-136532:Phantom's Body Messes up when over water | Duplicate:inward:MC-137128:phantoms transparency appears weird when above water | Duplicate:inward:MC-137269:Phantom mob wing makes water transparent | Duplicate:inward:MC-137351:Translucent models cause entities to disappear | Duplicate:inward:MC-137908:Water/particle bug | Duplicate:inward:MC-137962:Barrier block outline render failure | Duplicate:inward:MC-138047:Phantom Bug | Duplicate:inward:MC-138809:Alpha Opacity items make NBT blocks invisible when item is dropped in front of NBT block. | Duplicate:inward:MC-139484:You can see through water through an enderman's mouth | Duplicate:inward:MC-139682:No outlines on barriers on the water surface. | Duplicate:inward:MC-139987:Witch particle renders behind all other particles | Duplicate:inward:MC-140629:Agressive Endermen Block Water Visuals At Mouth | Duplicate:inward:MC-141615:Boat Rendering Bug with Transparent Textures | Duplicate:inward:MC-141752:glass makes invisible water | Duplicate:inward:MC-141982:Can't see water through smoke | Duplicate:inward:MC-141993:Smoke Particles 'Overwrite' Water Blocks | Duplicate:inward:MC-142002:seeing water through the campfire smoke particles not working correctly | Duplicate:inward:MC-142015:Campfire problem. | Duplicate:inward:MC-142111:Campfire smoke overlays water | Duplicate:inward:MC-142126:smoke particles from campfire make water invisible when seen through smoke | Duplicate:inward:MC-142240:particle glitch | Duplicate:inward:MC-142266:Water not visible through smoke. | Duplicate:inward:MC-142355:When you put Campfire next to water, the smoke from Campfire hides part of the water. | Duplicate:inward:MC-142367:Phantoms And CampFires Transparent Area On Item Will Mess Up Water | Duplicate:inward:MC-142764:Campfire Particle Glitch | Duplicate:inward:MC-142886:Leaf destroy bug | Duplicate:inward:MC-142903:Problem with the new campfires. | Duplicate:inward:MC-143101:Water not visible behind fading campfire smoke | Duplicate:inward:MC-143303:Guardian jumpscare | Duplicate:inward:MC-143868:Campfire Nether Portal Bug | Duplicate:inward:MC-143919:Campfire smoke appears behind water | Duplicate:inward:MC-143925:Particles and Water | Duplicate:inward:MC-143930:Can see water through campfire smoke | Duplicate:inward:MC-144006:Texture bug | Duplicate:inward:MC-144060:Smoke layer goes under distant background ocean water | Duplicate:inward:MC-144146:Campfire Smoke Particle Order | Duplicate:inward:MC-144257:The purple gates of hell were covered with smoke from the campfire. | Duplicate:inward:MC-144391:Water can be seen perfectly through smoke, but everything else is blocked normally | Duplicate:inward:MC-144867:Visual Glitch w/ Campfires & Nether portals | Duplicate:inward:MC-145361:Snapshot: Campfire Smoke | Duplicate:inward:MC-145473:Transparent blocks (glass) are visible through particles. | Duplicate:inward:MC-145626:Campfire Smoke is behind far water? | Duplicate:inward:MC-145764:Weird textures campfire smoke | Duplicate:inward:MC-145889:Campfire visual glitch | Duplicate:inward:MC-145947:You could see water through particles | Duplicate:inward:MC-146101:A Graphical Bug With Campfires | Duplicate:inward:MC-146372:Glass on armorstand's head rendering glitch | Duplicate:inward:MC-146502:Glass Visable Through Smoke | Duplicate:inward:MC-147074:I can see the water through the campfire smoke | Duplicate:inward:MC-147079:Campfire | Duplicate:inward:MC-147120:Water not affected by smoke | Duplicate:inward:MC-147228:Water Visibility Through Campfire smoke | Duplicate:inward:MC-147702:Clouds fully visible in half-transparent blocks | Duplicate:inward:MC-148008:Water visible through fireplace smoke | Duplicate:inward:MC-148124:Clouds draw on top of water without any fog or distorsion | Duplicate:inward:MC-148334:Agua en lagos y/o océanos pueden verse a través de el humo que produce las fogatas | Duplicate:inward:MC-148348:Water can be seen through campfire smoke particles | Duplicate:inward:MC-148503:Smoke-Water bug | Duplicate:inward:MC-148542:Smoke and Water | Duplicate:inward:MC-148763:Some blocks are highlighted through flash particles | Duplicate:inward:MC-148824:Water does not appear under phantom wing | Duplicate:inward:MC-148861:Glass blocks & panes are odd with campfire smoke | Duplicate:inward:MC-149118:Campfire smoke becomes transparent if you look at water through it. | Duplicate:inward:MC-149174:A lot of glitches about overlapping transparent blocks, particles and water | Duplicate:inward:MC-149262:A 1.14 smoke bug | Duplicate:inward:MC-149289:Campfire smoke doesn't block water | Duplicate:inward:MC-149477:Water is visible through smoke particles of campfire | Duplicate:inward:MC-149513:Campfire Glitch Glitch | Duplicate:inward:MC-149581:Campfire Smoke layering behind water | Duplicate:inward:MC-149608:smoke  disappears with water background | Duplicate:inward:MC-149636:If you have water and you have a campfire, the water will clip through the smoke no matter how far away you are. | Duplicate:inward:MC-149851:La fumée des feux de camps à un bug de rendu quand elle passe devant de l'eau | Duplicate:inward:MC-149855:Campfire smoke | Duplicate:inward:MC-149921:Whenever smoke from a campfire covers a body of water the water bleeds through. | Duplicate:inward:MC-149948:The Minecraft Campfire Particle effects allows water to be seen through it (Doesn't render properly with water in the distance) | Duplicate:inward:MC-149955:Campfire smoke water | Duplicate:inward:MC-150007:Nether portal bugged over campfire smoke | Duplicate:inward:MC-150131:Water texture is above the smoke particles | Duplicate:inward:MC-150212:Campfire smoke behind water leaves the water visible and not the ground | Duplicate:inward:MC-150290:Portal rendering over smoke particles | Duplicate:inward:MC-150302:Some particles still are glitched when looking through water, water overlays particles. | Duplicate:inward:MC-150309:Water Texture Visible like Xray through campfire smoke | Duplicate:inward:MC-150312:All particles render behind fluids and nether portal | Duplicate:inward:MC-150328:Breaking glass Displays water invisible. | Duplicate:inward:MC-150336:Phantom over water rendering error | Duplicate:inward:MC-150568:You can see water and netherportal through campfire smoke. | Duplicate:inward:MC-150672:Seeing water through smoke | Duplicate:inward:MC-150726:you see the water through the smoke | Duplicate:inward:MC-150743:Campfire Smoke renders behind animated blocks | Duplicate:inward:MC-150891:Nether Portal Animation Shows In Front of Smoke from Campfires | Duplicate:inward:MC-150894:1.14 Campfire Visual Bug | Duplicate:inward:MC-150913:Water is visible through campfire smoke | Duplicate:inward:MC-150931:Able to see liquids through smoke particles | Duplicate:inward:MC-151254:Minecraft bonfire smoke low opacity infront of water | Duplicate:inward:MC-151310:Light from the portal to hell is visible through the smoke | Duplicate:inward:MC-151341:Blocks of mucus, glass and water shine through the smoke of the fire. | Duplicate:inward:MC-151433:You can see water thorugh the campfire smoke | Duplicate:inward:MC-151556:Smoke from campfires is "see-through" | Duplicate:inward:MC-151559:Campfire smoke render issues | Duplicate:inward:MC-151708:Błąd graficzny z ogniskiem | Duplicate:inward:MC-151749:Campfire Smoke particles appear behind water | Duplicate:inward:MC-151757:Water and campfire smoke rendered in wrong order | Duplicate:inward:MC-151871:smoke particles are gliched with water | Duplicate:inward:MC-151924:Stained glass lets you see through chests. | Duplicate:inward:MC-151930:Stained glass can be seen through some of the particle effects. | Duplicate:inward:MC-151940:see stained glass through campfire smoke | Duplicate:inward:MC-151973:Bug Visual Nether Portal + Humo Campfire | Duplicate:inward:MC-152022:Graphics bug with fireplace particles | Duplicate:inward:MC-152135:Particles and Water | Duplicate:inward:MC-152259:you see the blocks through the wings of the phantom | Duplicate:inward:MC-152303:Water overlaps smoke from campfire | Duplicate:inward:MC-152427:Water renders on top of campfire smoke | Duplicate:inward:MC-152605:snow particles being blocked out by distant water bodies | Duplicate:inward:MC-152655:Water can be seen through the smoke from the campfire | Duplicate:inward:MC-153050:Bug while looking at windows through camp fire smoke. | Duplicate:inward:MC-153080:Water is visible through campfire particles | Duplicate:inward:MC-153281:Portal rendering above smoke particles | Duplicate:inward:MC-153520:Smoke Particle Rendering Order | Duplicate:inward:MC-153588:Water and Nether Portal can be seen through campfire particles | Duplicate:inward:MC-153851:Campfire smoke goes behind water | Duplicate:inward:MC-154043:Water Disappears | Duplicate:inward:MC-154443:particles | Duplicate:inward:MC-154457:black out glass | Duplicate:inward:MC-154503:Transparent blocks overlay particles | Duplicate:inward:MC-154586:Water can be seen through campfire smoke | Duplicate:inward:MC-154758:Water Body showing through Campfire Smoke | Duplicate:inward:MC-155158:Texture glitch with fireplace | Duplicate:inward:MC-155242:Visual campfire glass pane bug | Duplicate:inward:MC-155632:Water Transparent when breaking Leaf Blocks | Duplicate:inward:MC-155993:Campfire Smoke does not obscure water | Duplicate:inward:MC-156188:The water is seen through the smoke from campfire | Duplicate:inward:MC-156200:I can see water through the smoke of a camp fire | Duplicate:inward:MC-156542:water becomes invisible through glass | Duplicate:inward:MC-156601:Nether portals render in front of particles | Duplicate:inward:MC-156868:Water visible behind smoke from fireplace | Duplicate:inward:MC-156888:Slime block being held while sleeping displays behind certain objects | Duplicate:inward:MC-156893:Smoke from Campfire is overlapped by water and Portal blocks | Duplicate:inward:MC-157035:Campfire smoke gets darker when entering the "ocean" | Duplicate:inward:MC-157371:You can see the Purple Nether Portal and Water through the campfire smoke | Duplicate:inward:MC-157428:The colored smoke from the bonfire is visible through the collected smoke | Duplicate:inward:MC-157434:Hitbox lines render wrongly | Duplicate:inward:MC-157529:Particles go under the water block when shown | Duplicate:inward:MC-157660:A small bug on stained glass | Duplicate:inward:MC-157768:Weird water-logging on stained glass panes that are connected to all 4 sides. | Duplicate:inward:MC-157800:Visual bug/Campfire smoke | Duplicate:inward:MC-157912:When looking at smoke (from a campfire) water does not render correctly | Duplicate:inward:MC-158191:enderman | Duplicate:inward:MC-158250:Water visible through campfire particles | Duplicate:inward:MC-158477:The Smoke from a campfire with slime blocks behind it makes the color go off | Duplicate:inward:MC-158501:Flowing water can be seen through campfire smoke | Duplicate:inward:MC-158603:Water sill visible in capfire smoke | Duplicate:inward:MC-158952:Дым залетает за полублок цветного стекла | Duplicate:inward:MC-158967:Campfire Smoke and Water Graphics Glitch | Duplicate:inward:MC-159333:Nether portal overlapping | Duplicate:inward:MC-159390:Bells are invisible through slime (mob). | Duplicate:inward:MC-159692:Can see water through smoke | Duplicate:inward:MC-159744:Smoke From Campfires Color Affected By Water Behind | Duplicate:inward:MC-159891:Water texture not drawn because of Enderman Model | Duplicate:inward:MC-160441:Smoke texture from campfire appears behind water | Duplicate:inward:MC-160574:phantom wings make the vision of the water invisible | Duplicate:inward:MC-160976:Water renders over any particle effect | Duplicate:inward:MC-161242:Nether Portals are visible through campfire smoke | Duplicate:inward:MC-161401:Block hightlight becomes transperent when looking through at a certain block | Duplicate:inward:MC-161616:Fireworks make stained glass behind it clear | Duplicate:inward:MC-161621:Water and ice are visible behind the smoke texture | Duplicate:inward:MC-161783:Water overlaps smoke | Duplicate:inward:MC-161821:Nether portal appears in front of campfire smoke | Duplicate:inward:MC-161919:When destroying transparent leaves, water texture does not appear. | Duplicate:inward:MC-162449:Boat behind particles | Duplicate:inward:MC-162509:water can be seen through smoke | Duplicate:inward:MC-163613:the smoke from fireplace is layered beneth the water | Duplicate:inward:MC-163616:Space under enderman's head does't render item frames | Duplicate:inward:MC-163677:When another player is holding glass and you look through it, it does not show the ocean | Duplicate:inward:MC-163678:When another player is holding glass and you look through it, it changes the oceans colder and other blocks | Duplicate:inward:MC-163836:you dont see banners trou dropped collord glass pane | Duplicate:inward:MC-164221:Water rendering in front of campfire smoke | Duplicate:inward:MC-164322:breaking animation on leaves will make water behind the leaves invisible | Duplicate:inward:MC-164415:Phantom's Wings have the same light engine issue as other particles effects do/did. | Duplicate:inward:MC-164682:Campfire smoke visual bug | Duplicate:inward:MC-165049:Dropped glass blocks see trough certain blocks | Duplicate:inward:MC-165538:Water texture shows in front of campfire smoke. | Duplicate:inward:MC-165885:slime blocks & clouds | Duplicate:inward:MC-165921:Water and glass | Duplicate:inward:MC-166605:Nether portal bugged with smoke from a fireplace | Duplicate:inward:MC-3477:Chickens glitching through half slabs | Relates:inward:MC-35920:Some translucent parts of entities make translucent blocks, block entities and some entities invisible (depending on loading order) | Relates:inward:MC-38022:Order of rendering translucent block faces fails to update with camera position | Relates:inward:MC-46857:Weird Stained Glass Renders Incorrectly Underwater. | Relates:inward:MC-63468:Entities and tile entities are invisible through lightning bolt | Relates:inward:MC-85420:Mobs are invisible through stained glass pane in hand of other mobs | Relates:inward:MC-87049:Firework light flash glitches from many explosions | Relates:inward:MC-94627:Transparent maps don't render certain blocks/tile entities behind them | Relates:inward:MC-103212:F3+B Hitbox not rendering in front of block 36 | Relates:inward:MC-154023:Campfire smoke disappears when launching several rockets at the same time. | Relates:inward:MC-161879:Hitbox of transparent blocks, such as slime blocks, stained glass or ice, appears behind the block texture | Duplicate:inward:MCL-3477:slime Block render

## Description

Mod Notice
Please do not attach any more images to this ticket.
For any new instances of this issue occurring (or similar), please perform a search on the bug tracker for reports, else create a new ticket for the specific issue being observed. To better address issues moving forward, individual problems will be tracked separately, instead of a "global" report such as this.
Affected cases
- Some particles render behind transparent blocks, hitboxes, breaking animations and transparent clouds, often making them barely visible. Particles known to have this issue: End rod, potion, fireowork, ink, rain and snow particles. In older versions, this was a general issue with all types of particles, some have been fixed since then.

- As of 13w41a, hitboxes render in front of transparent blocks - it simply looks weird when you can see the hitbox of blocks through the water surface (see

- ) or the rear (normally less visible) parts of the hitbox through a transparent block like ice or stained glass. As of 1.7, the behavior changed: Hitboxes now render behind transparent blocks!

- Transparent clouds 1 always render in front of transparent blocks and hitboxes (looks pretty weird, see

- ).

- The energy field around invisible charged creepers renders behind water and transparent clouds, but in front of hitboxes. Particles and other transparent blocks show no rendering order problems in this case. You can spawn invisible charged creepers with the following command:

```
/summon creeper ~ ~1 ~ {powered:1b,ActiveEffects:[{Id:14,Duration:2000000}]}
```

- The firework explosion light flash causes water and transparent clouds to always be rendered behind it, making them disappear.

- The outer, transparent part of the beacon beam, the transparent text overlay of named map markers (close to a map's edge) as well as the outer transparent part of Phantom wings render behind water, transparent clouds and transparent blocks, making them disappear.

- Ice blocks render incorrectly in third person

Notes
1 "Transparent clouds" means: Clouds turn transparent when you move above y=128 (MC-997). Before Jeb reverted the fix of MC-997, clouds were always transparent at all heights, which can be seen here
)
Code analysis
See this comment.
Mod edit: Added comment by
Some updates from snapshot 18w22a (and possibly earlier)
Issues resolved in snapshot 18w22a:
- Hitboxes now render underwater and through water.

- Non-transparent particles render correctly in front of transparent blocks (ex breaking stone in front of water).

Issues new to 18w22a:
- Hitboxes render completely behind transparent blocks (ice, colored glass) making them hard to see.

Issues still present in 18w22a:
- Beacon beam outer aura renders behind transparent blocks at any height.

- Transparent particles render in place of transparent blocks. (Ex: break stained glass in front of ocean, squid ink looking upward in water, etc.)

- Charged creeper aura renders in place of transparency (water, ice, etc.)

- Phantom wings render in place of transparency.

- Ice still renders strangely at far distances.

- Clouds still render in front of transparent blocks/water when placed above the cloud height.

- Firework particles still render in behind transparent blocks.

I'm sure I forgot many of them, but these are the ones that are easily noticed to me.

## Comments (100)

### Comment 1: migrated (2013-02-10T03:22:12.161-0800)

This comment contained multiple image attachments (101), please login to view the attachments.

### Comment 2: migrated (2013-02-10T07:14:27.130-0800)

Confirmed.

### Comment 3: migrated (2013-02-27T13:00:58.452-0800)

Same with particles and clouds.

### Comment 4: migrated (2013-02-27T13:04:44.560-0800)

Particles fade when see from below clouds. I added 2 screenshots to it. Really easy to reproduce. Seems happening through water too.

### Comment 5: migrated (2013-02-28T08:07:48.063-0800)

They also go "behind" ice. Boring bug, I hope this will be fixed soon.

### Comment 6: _zombiehunter (2013-02-28T08:29:17.771-0800)

Confirmed. Same problem with ice too.

### Comment 7: migrated (2013-03-01T08:09:46.601-0800)

confirmed for 13w09c
I think this has something to do with the fix of [MC-997]

### Comment 8: migrated (2013-03-01T16:48:46.296-0800)

Definitely.

### Comment 9: migrated (2013-03-02T07:23:02.680-0800)

Confirmed to also occurs with block breaking particles, and other types too I'd imagine

### Comment 10: migrated (2013-03-02T14:21:05.969-0800)

glad to see zombie hunter is on these bugs so fast.

### Comment 11: migrated (2013-03-04T19:16:22.874-0800)

Confirmed on 13w10a, with all particles, ALL OF THEM

### Comment 12: migrated (2013-03-05T16:26:52.858-0800)

I confirm it for 13w10a as well. It's a obvious bug to even a casual player becuase it happens even if there are blocks between the clouds and the block being mined.

### Comment 13: migrated (2013-03-06T13:07:54.676-0800)

Half Confirmed for 13w10b, it still is bad for ice/water, clouds seam to been fixed
edit
Added this to the notable bugs for 13w10b: http://www.minecraftwiki.net/wiki/Version_history/Development_versions#Minecraft_1.5_Snapshots_.26_Pre-releases

### Comment 14: migrated (2013-03-06T15:46:34.245-0800)

This is a similar bug:
Things like name tags don't show through signs.

### Comment 15: _zombiehunter (2013-03-07T03:46:16.819-0800)

@Corbin:
No, not fixed for clouds. Still happens in 13w10b, no differene to previous snapshots

### Comment 16: migrated (2013-03-07T07:56:42.187-0800)

As of 1.5pre still happening.

### Comment 17: migrated (2013-03-07T10:05:58.471-0800)

Confirmed for 1.5pre as well

### Comment 18: migrated (2013-03-07T10:06:16.326-0800)

here you can see that the particles being generated when mining the wood log appear as if they were behind the cracks

### Comment 19: _zombiehunter (2013-03-07T11:27:52.450-0800)

OK, tested with 1.5-pre, the particle+clouds or hitbox+clouds rendering now is fixed (maybe becauce Jeb reverted the cloud transparency bug MC-9553?). Paticles in front of other transparent textures still do weird.

### Comment 20: migrated (2013-03-08T09:21:47.952-0800)

I had this happen to me as well in 1.5pre.

### Comment 21: migrated (2013-03-13T15:06:04.493-0700)

This still happens in the release version of 1.5 (should be the same as the 1.5pre).

### Comment 22: migrated (2013-03-14T22:54:03.018-0700)

This picture shows a particle layering error. The wood block being broken is emitting particles, but the largest particle in this picture shows that both the block selection outline and the breaking overlay are overlapping the particles in front of it.

### Comment 23: migrated (2013-03-20T00:00:26.358-0700)

1.5.1pre fixed the performance issues for me, the particle rendering/layering bug is still there though.

### Comment 24: migrated (2013-03-21T04:29:45.624-0700)

Yep, the particules are rendered on wrong layout...

### Comment 25: alex_dlc (2013-03-22T18:38:35.658-0700)

just started seeing this bug in 1.5.1

### Comment 26: migrated (2013-03-23T09:41:18.139-0700)

Confirmed on 1.5.1. Very, very annoying and also makes the prespective look weird, especailly in the fourth screenshot (eating Rotten Flesh while looking at water).

### Comment 27: migrated (2013-03-28T04:07:08.842-0700)

if this was photoshop, I'd say they're in the wrong layer.... but yeah this has been bothering me for w while now, I try not to look at water while eating...

### Comment 28: migrated (2013-03-29T13:43:56.111-0700)

same happens to me, can someone just explain why this happen?

### Comment 29: migrated (2013-03-29T15:02:42.714-0700)

Melih is sort of right... The game renders half-transparent stuff like water, ice and clouds with a separate shader (=on a separate layer) and at the end of the rendering it gets blend together. I wrote some shader stuff before myself and these sort of things are tricky to get right without affecting performance too much. In this case it looks like the z-buffer for particles and transparent stuff aren't compared properly when blending them together.
But Mojang already said, they want to rewrite the rendering code for the next release and so I guess this will be fixed soon.

### Comment 30: migrated (2013-03-30T18:18:13.535-0700)

It's annoying and weird because the hitbox looks like it's taller than the cloud or lower than the water

### Comment 31: migrated (2013-03-31T02:56:14.386-0700)

A quick fix which should look better in most cases could be to render particles always in front of transparent stuff (= reverse the order of the "layers"), but as I haven't seen the source code I don't know how easy that would be.

### Comment 32: migrated (2013-04-18T14:42:44.841-0700)

This still occurs in 13w16a, and does look weird, so would be nice to have it fixed!

### Comment 33: migrated (2013-04-19T03:23:14.173-0700)

Aristotle, this is not the right place to report new bugs. For example the pressure plate issue is already reported as MC-13610.

### Comment 34: migrated (2013-04-25T20:41:40.928-0700)

Can reproduce:
Java JRE7
Windows 7 Ultimate x64
AMD Athlon(tm) II X4 640 Processor
4,00 GB DDR3 RAM
ATI Radeon HD 5450

### Comment 35: migrated (2013-05-02T09:53:30.793-0700)

Will it be fixed soon ? The bug has been reported 3 version ago and seem like a major visual problem...

### Comment 36: _zombiehunter (2013-05-02T10:03:36.208-0700)

I think they need to rewrite the rendering engine to fix this, dunno if the new engine will be included in 1.6 ...

### Comment 37: alex_dlc (2013-05-10T08:42:18.722-0700)

Have you guys noticed that chests appear infront of the effect particles? Try giving yourself any effect and then look at either a normal or ender chest.

### Comment 38: _zombiehunter (2013-05-10T08:52:44.245-0700)

@Alejandro de la Cruz:
Cannot confirm this for chests. Only happens with transparent textures like ice, water, etc ... (tested with 13w19a)

### Comment 39: alex_dlc (2013-05-10T09:05:02.146-0700)

@zombie hunter:
I cant confirm on my PC either, but I have noticed it in some Youtube videos, for example this one from ChimneySwift11:
www.youtube.com/watch?v=PxJeOajecmg&feature=player_detailpage#t=786s
Maybe someone should add a screenshot of this?

### Comment 40: _zombiehunter (2013-05-10T09:12:26.502-0700)

@Alejandro de la Cruz:
Not relevant for this bug tracker. As you can see many times in the video, they're using several mods. This bug tracker is only for unmodded Minecraft. Many mods cause visual problems, but it's up to the mod developers to fix this.

### Comment 41: alex_dlc (2013-05-10T09:15:51.207-0700)

Im pretty sure that none of the mods used would cause that. But ill try to ask him if he can reproduce that bug with a clean jar

### Comment 42: migrated (2013-05-10T12:46:20.739-0700)

Does it with a clean jar for me. A fresh dev build.

### Comment 43: alex_dlc (2013-05-10T13:21:23.518-0700)

@Steve Dawson:
The effect particles and chest thing?

### Comment 44: migrated (2013-05-11T05:21:50.195-0700)

Bug is still present in Development and Release versions.

### Comment 45: migrated (2013-05-19T08:35:03.173-0700)

Yes, particles seem to be drawn before most other things, so they appear below water, too. Try it yourselves, put a torch next to water and look at it so the flames are in front of the water, or rather, so they would be in front of the water.

### Comment 46: migrated (2013-05-25T12:16:38.442-0700)

giving a golden apple to a tamed horse near any part of water will show the heart's texture behind the water texture

### Comment 47: migrated (2013-05-27T14:00:16.779-0700)

Yeah I noticed this a while ago too

### Comment 48: migrated (2013-05-28T14:30:54.071-0700)

if you go above the clods, the clouds are in front of particles (does not happen if you are beiond clouds)
P.S.: Sorry, i'm brazilian, bad english =S

### Comment 49: migrated (2013-05-29T06:38:01.714-0700)

I noticed this recently while playing with a mod that hasn't released for 1.5.2 (beta access, effectively) and it was hard to notice so I wasn't sure if I was seeing it correctly until sometime later when I was digging upwards (breaking logs, so good contrast between the particles and the breaking animation as well as the particles being comparatively large due to them falling towards the camera).  Then I had to check if it was a vanilla problem (vs. Forge vs. the specific mod), then I did the right thing and searched the bug tracker.
Good to see that it's been reported.

### Comment 50: pokechu22 (2013-06-17T13:18:42.233-0700)

The same thing happens with the black border around blocks and particles, though that is the least obvious part.

### Comment 51: migrated (2013-06-21T09:41:50.568-0700)

Would like to clarify that it seems ANY particles are drawn behind any translucent render in-game, e.g. water, nether portal, clouds.  Most distracting with eating particles, as most obvious there.  Ruins the depth of the game.  Seems to be a simple layering bug, but seeing as it has existed for so long and not been fixed, it must be more complicated than that.

### Comment 52: migrated (2013-06-21T09:46:31.607-0700)

If by "so long" you mean since snapshot 13w06a (mid February of this year)...

### Comment 53: _zombiehunter (2013-06-21T10:02:15.699-0700)

@Draco Silverwing:
That's indeed long for an obvious bug like that! Particles worked fine up to 13w06a and as Christopher Durham said, it's probably a simple layering bug which could be fixed quite fast by the devs. It's just sad that no dev cares about this, any statement on this topic would be nice ... I mean: This bug is reaching 100 upvotes now!

### Comment 54: migrated (2013-06-21T10:07:28.116-0700)

Fixed fast + devs don't care != must be more complicated.

### Comment 55: migrated (2013-06-23T08:16:57.266-0700)

Still exists in 13w25c. 1.6 is due for next week and I'm becoming increasingly concerned that this annoying bug won't be fixed by then. I'm surprised it's taking so long to acknowledge and fix. I know from a development perspective that Minecraft is complex software and inevitably suffers from a lot of bugs, but this issue sounds like a simple rendering/draw order mix-up like a few other people have said.

### Comment 56: migrated (2013-06-23T08:24:13.632-0700)

i think they are making a ne rendering system from scratch, fixing this and another rendering bugs, that's hy they are taking all that time...

### Comment 57: migrated (2013-06-25T08:00:44.556-0700)

Confirmed as still an issue in the 1.6 pre-release.

### Comment 58: migrated (2013-06-28T09:54:39.337-0700)

Just another ex. w/fireworks in case it is needed.

### Comment 59: _zombiehunter (2013-07-01T05:31:23.365-0700)

And finally the bug made it to the top 10 of the popular issues list ... after months of waiting and more than 80 dublicates still not fixed

### Comment 60: migrated (2013-07-16T06:42:18.000-0700)

Wow. You'd think the devs would do something...

### Comment 61: migrated (2013-07-19T01:54:10.762-0700)

Another screenshot, It fails at leafes too. I hope to see an fix soon because this is a litle bit annoying :S

### Comment 62: migrated (2013-08-09T17:38:18.095-0700)

This guy got screenshots of all Visual glitches provided by this bad rendering bug...

### Comment 63: migrated (2013-08-30T22:01:17.971-0700)

I just noticed it today and thought it was one of my mods messing up or something but when i switched back to completely vanilla it was there...hopefully its fixed soon

### Comment 64: migrated (2013-09-05T12:59:31.394-0700)

This bug  is in snapshot 13w36a as well as 1.6.x

### Comment 65: migrated (2013-09-05T13:07:49.306-0700)

John: That was already added like 4 hours ago.
12:40PM
Change By: 	zombie hunter
Affects Version/s: 	Snapshot 13w36a

### Comment 66: _zombiehunter (2013-09-13T13:25:31.415-0700)

@MisterSanderson:
We already have some screenshots of torch flames in front of water here, just saying ...

### Comment 67: migrated (2013-10-10T08:31:18.760-0700)

Still happening in 13w41a

### Comment 68: migrated (2013-10-10T15:58:30.645-0700)

torches, particles and eating food are still not rendered properly.

### Comment 69: _zombiehunter (2013-10-11T04:01:13.791-0700)

It would be the right time to fix this after fixing  .
@Mods:
I would consider MC-34656 a dublicate of this, not a "relates to"

### Comment 70: migrated (2013-10-11T19:12:44.274-0700)

I would have assumed 13w41a/b would've fixed this, as the issue appears to stem from particles being rendered as translucent (due to the translucent particle feature added to beacons) but it is in fact still present.

### Comment 71: _zombiehunter (2013-10-13T06:03:00.670-0700)

Generalized the title and description of the ticket to cover MC-34658 and MC-35010 !!!

### Comment 72: migrated (2013-10-21T05:08:37.338-0700)

In 13w42b clouds behind stained glass aren’t rendered at all.

### Comment 73: _zombiehunter (2013-10-21T05:14:29.256-0700)

@Dirk Sohler:
More or less the same as MC-36228, also very similar to MC-35716. I'll mention this here, but it's practically a new bug, so you better create a separate ticket if there isn't already one. If it's really the same bug, I would generalize MC-36228 to include clouds and other "invisible behind stained glass" stuff ... (>>> @Marios or any mod)

### Comment 74: _zombiehunter (2013-10-22T10:05:09.334-0700)

MC-35716 and MC-36228 are fixed as of 1.7, but clouds seen through stained glass are still invisible. Hitboxes now render behind transparent blocks (stained glass, etc.) all the time!

### Comment 75: migrated (2013-10-25T09:19:56.407-0700)

Confirmed for 1.7.2

### Comment 76: _zombiehunter (2013-10-29T06:33:05.806-0700)

Hmmm .... the bevahior of clouds changed again from 1.7 to 1.7.2. They are no longer invisible, but they render in front of transparent blocks, like they did in 13w41a/b.

### Comment 77: migrated (2013-11-05T22:01:03.936-0800)

I believe clouds are still transparent, they just don't look that way from the ground. This is because there is also an issue with the z-depth rendering between the clouds and sky at certain angles.
When looked at from above you can see the ground thru them (easily checked in AMPLIFIED world. But when you get below the clouds they 'look' solid because you are seeing the cloud + sky rendered together. At night you can see the stars in the cloud and if you get the cloud in front of a tall mountain you will still see the stars and even the moon as well. It is not as obvious in the daytime until you get the sun involved as the sky and cloud are so similar in color.
Looking at the four screenshots I attached 2 - is in the cloud and it is transparent and can still see the mountain, 3 is just a little bit below the cloud and it is still transparent, but 4 - when dropping just a little bit more below the cloud the sky and cloud combine so you can no longer see the mountain but can see the sky and sun (which is behind the mountain, you can see the halo in pic 1).

### Comment 78: migrated (2013-11-06T08:08:19.843-0800)

The water overlays everything that ist transparent.

### Comment 79: _zombiehunter (2013-11-06T13:04:22.574-0800)

@Rick Mc Glenister:
Your screenshots actually show MC-997, please delete them here, they have nothing to do with the rendering order bug.
@DFG:
Same with you. The server shown in your screenshot seems to be modded, I can't reproduce this in vanilla 1.7.2

### Comment 80: migrated (2013-11-06T18:42:20.120-0800)

@zombie_hunter
The core of my observations is that the render order is broken for clouds, as well as particle etc.. I do not agree that cloud bottoms are solid so never searched for 'cloud transparency' issue.
I believe my screenshot showed that clouds are transparent on the bottom, but when viewed from too far below appear to be solid because the render order is wrong. I did not make this clear, the sun or moon or stars are always visible through the clouds (would say sky as well but this can only be inferred). Hence; clouds are transparent on all sides.
The reason for the apparent solidity of the cloud bottoms is that the render order is broken. Instead of the render order being cloud - mountain - sun - sky it is cloud - sun - sky - mountain, and since the sky is not transparent you can't see the mountain through the cloud so the bottom "appears" solid. The exact same thing happens during the night ie the mountain rendered incorrectly at the back of the list.
The keys to this are the sun, moon, and stars all of which are visible through the cloud bottom. If the cloud bottom was not transparent you would not see them.
Screenshot info: created in plain MC 1.7.2, in creative mode, in an AMPLIFIED world (seed -7693758492202460580), location x:2387, Y:-3568. In a default world, in survival, with same seed the same effects can be seen.

### Comment 81: migrated (2013-11-06T19:00:22.650-0800)

The point is that you have shown a different issue entirely, although we recognize it is a perfectly legitimate issue.

### Comment 82: migrated (2013-11-06T19:23:29.405-0800)

I would like to point out that this particle issue was solved by Forge at some point as far back as 1.5.  They simply moved the "litparticles" and "particles" rendering towards the bottom of the function which renders the world.  Literally about eight lines worth of code moved into a different position seems to fix it without ill effect.
By default, the selection box, water, block destruction progress, weather, and hand are rendering on top of it, in that order.  Forge positions it so that only the hand is rendered on top (as well as some Forge hooks, but that obviously doesn't apply to vanilla).
I realize that this is a trivial bug in the grand scheme of things, but I hope that this information will help put a quick end to this bug whenever someone can attend to it.

### Comment 83: migrated (2013-11-06T20:03:07.013-0800)

@ Anon Ymus
Ok, I just took my observation as an extension of this issue.
Since my observation seems to be 'opposed' to the 977 issue would you recommend that I post there? Or rather that I should start a new issue?

### Comment 84: migrated (2013-11-06T22:11:42.818-0800)

@zombie hunter no the server is vanilla i just changed the prefixes in the scoreboard file in world/data to show admin  and owner in front of the name.

### Comment 85: _zombiehunter (2013-11-07T02:43:59.570-0800)

@DFG:
In this case, your issue could be MC-36329 or something similar. At least it's not the particle/hitbox/clouds/etc rendering order thing described here.

### Comment 86: migrated (2013-11-07T16:03:15.965-0800)

@Rick
Your issue actually shows exactly what MC-997 says. If you have further information, you should put it there.

### Comment 87: migrated (2013-11-07T19:49:33.089-0800)

@Anon Ymus
Thanks.

### Comment 88: migrated (2013-11-25T09:34:08.606-0800)

issue still present in 13w47e
http://i.imgur.com/sfUBOrw.png
http://i.imgur.com/FnIWbSH.png

### Comment 89: migrated (2013-12-12T07:45:18.929-0800)

Please see 'breakingice' pics.
This is what happens when there's any pixel in any value of alpha except 0 (blank) when breaking Ice/Stained Glass.  It will 'erase' all textures behind it rather than layering over top the box.  Figuring it's something with that renderpass overlapping and ignoring everything passed before it?

### Comment 90: migrated (2014-01-22T09:42:32.498-0800)

This is still an issue in Minecraft version 14w03b.

### Comment 91: windsdon (2014-01-24T15:52:17.530-0800)

Block breaking particles render over smoke (and possibly other particles).
Please see 2014-01-24_11.03.24.png

### Comment 92: migrated (2014-02-03T18:19:49.689-0800)

Also happens with nether portals held by other players.

### Comment 93: _zombiehunter (2014-02-07T05:30:29.945-0800)

Barrier particles in front of water behave like all other particles too: They render behind water ...

### Comment 94: migrated (2014-02-13T12:16:37.717-0800)

Here you can check out another bug very silmilar to yours: MC-47808

### Comment 95: _zombiehunter (2014-02-13T12:27:24.893-0800)

@KaliNuska:
Ah, yes. It's not just similar, it's actually a dublicate ... the "hitboxes render behind transparent blocks" problem again

### Comment 96: migrated (2014-02-13T14:06:09.374-0800)

According to Ryan, this issue is very difficult to solve. Maybe it will be fixed later though.

### Comment 97: migrated (2014-02-14T06:35:11.360-0800)

Still affects 07a

### Comment 98: _zombiehunter (2014-02-18T11:08:35.535-0800)

Added the rendering order problem seen on invisible charged creepers (see dublicate MC-49034) to the description.

### Comment 99: KnightMiner (2014-02-19T06:51:25.348-0800)

Still in 14w08a

### Comment 100: migrated (2014-02-23T06:41:48.234-0800)

Added a photo of Clouds rendering in front of slime blocks
Edit: Still present in 1.7.6-pre1
Actually this is not needed to be added to the affected versions

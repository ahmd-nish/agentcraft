# MC-270862: Firework Star item displays have inconsistent color updates

**Mojira URL:** [https://bugs.mojang.com/browse/MC-270862](https://bugs.mojang.com/browse/MC-270862)

## Report details

- **Mojira categories:** Commands; Items
- **Project:** MC
- **Issue key:** MC-270862
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Very Important
- **Created:** 2024-04-17T07:21:02.861-0700
- **Updated:** 2025-03-20T21:46:46.108-0700
- **Resolution date:** 2024-04-19T01:23:42.387-0700
- **Affects versions:** 1.20.5 Pre-Release 3; 1.20.5 Pre-Release 4
- **Fix versions:** 1.20.5 Release Candidate 2
- **Area:** Platform
- **Watchers:** 1
- **Attachments:** 2
- **Attachment filenames:** javaw_qqCLfaSZ8s.jpg; javaw_SwDKsDE3nx.jpg

## Description

This issue started with 1.20.5 Pre-Release 3.
If you summon multiple item displays with a firework star that have different colors for the explosion, then try to update them with a different color, the behavior is inconsistent. Sometimes one will update, but the other won't even though the data itself does update. And if you update another data property on one of the item displays, the colors seem to swap with other item displays nearby.

Steps to Reproduce:
1. Summon two item displays with a firework star item

```
/summon minecraft:item_display ~ ~ ~ {item:{id:"firework_star",components:{"minecraft:firework_explosion":{shape:"small_ball",colors:[I; -1]}}}}

/summon minecraft:item_display ~ ~ ~ {item:{id:"firework_star",components:{"minecraft:firework_explosion":{shape:"small_ball",colors:[I; -1]}}}}
```
2. Try to change the colors value on one of the displays

```
/data modify entity @e[type=minecraft:item_display,limit=1,sort=nearest] item.components."minecraft:firework_explosion".colors set value [I; -65536]
```
3. The color may or may not update from step 2, but if you quit and rejoin the world, the colors of the item displays will either be still white, or both will change to red.

Observed Results:
The colors of the different item displays change to different values other than what they contain in their item data.
Expected Results:
The color of the firework star item display should remain consistent with the data contained in item.components.minecraft:firework_explosion.colors

Screenshots/Videos:
After modifying the colors data on one of the firework star items:
After quitting and rejoining the world:

Notes:
It also happens even when you summon multiple item displays and try to merge the display with a firework star item and a firework explosion, the color is inconsistent.
It may have something to do with the item data serialization issue that was fixed in 1.20.5 Pre-Release 3.

## Comments (4)

### Comment 1: migrated (2024-04-17T07:21:02.861-0700)

This comment contained multiple image attachments (2), please login to view the attachments.

### Comment 2: [Mod] violine1101 (2024-04-17T16:45:04.259-0700)

Please provide some steps to reproduce the issue. You can use the template from the bug tracker guidelines. This allows us to understand the issue more clearly, as well as reproduce and fix it.
In case you use any commands, please include the exact commands used. You can include commands in code blocks (located under the plus icon, or using {code} in text mode) to not mess up the formatting.
This issue is being temporarily resolved as Awaiting Response. Once the requested information has been delivered, the report will be reopened automatically.
Quick Links:
📓 Bug Tracker Guidelines – 💬 Community Support – 📧 Mojang Support (Technical Issues) – 📧 Microsoft Support (Account Issues)
📓 Project Summary – ✍️ Feedback and Suggestions – 📖 Game Wiki

### Comment 3: migrated (2024-04-17T23:41:27.223-0700)

Steps to reproduce:
- Run the following command twice.

```/summon minecraft:item_display ~ ~ ~ {item: {id: firework_star, components: {firework_explosion: {shape: small_ball, colors: [I; 0]}}}}```

- Modify one of them with following command.

```/data modify entity @e[type=minecraft:item_display,limit=1,sort=nearest] item.components."minecraft:firework_explosion".colors set value [I; 16777215]```

- Quit and rejoin.

- Both firework stars are displayed white.

### Comment 4: [Mod] violine1101 (2024-04-18T04:46:26.914-0700)

Thanks, confirmed!

# MC-254506: Font file of some Korean completed font area is wrong

**Mojira URL:** [https://bugs.mojang.com/browse/MC-254506](https://bugs.mojang.com/browse/MC-254506)

## Report details

- **Mojira categories:** Internationalisation
- **Project:** MC
- **Issue key:** MC-254506
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Normal
- **Created:** 2022-07-23T08:22:05.429-0700
- **Updated:** 2025-04-11T12:47:44.052-0700
- **Resolution date:** 2023-04-25T08:51:25.203-0700
- **Affects versions:** 1.19; 1.19.1 Release Candidate 2; 1.19.2; 1.19.3
- **Fix versions:** 23w17a
- **Labels:** font; texture
- **Watchers:** 1
- **Attachments:** 18
- **Attachment filenames:** duplicates.png; duplicates-1.png; image-2022-07-24-00-34-36-730.png; image-2022-07-24-00-36-30-152.png; image-2022-07-24-00-40-35-889.png; image-2022-07-24-00-41-04-098.png; image-2022-07-24-00-43-44-145.png; image-2022-07-24-00-44-51-361.png; image-2022-07-24-00-46-56-218.png; image-2022-07-24-00-49-01-447.png; image-2022-07-24-00-51-42-080.png; image-2022-07-24-00-54-09-377.png; image-2022-07-24-00-56-21-024.png; image-2022-07-24-07-52-16-797.png; image-2022-07-24-08-04-19-062.png; image-2022-07-24-08-04-44-640.png; image-2022-07-24-08-05-16-226.png; screenshot-1.png
- **Issue links:** Duplicate:inward:MC-254519:Some Korean letters display incorrect letter, such as '윌' displaying as '월' | Duplicate:inward:MC-254554:font texture error | Duplicate:inward:MC-259287:U+C70C looks like U+C6D4 | Duplicate:inward:MC-259981:Some of KR unicode font textures display wrong character | Relates:outward:MC-34573:Font file of Unicode Page C2 (Korean) shows character '숼'(U+C23C) at the position of '쉴'(U+C274)

## Description

https://youtu.be/tHu7Ht6NJac :: One korean youtuber says the font of 윌[wi:l] and 월[weol] is identical
This is actually a dupe of MC-34573, but some are not fixed then.
Gonna add the examples soon. (I should unpack the minecraft file to check out where is wrong but I'm writing on mobile lol)

:: Locations ::
unicode_page_b2.png, 1.12.2:

```
뉘뉙뉚뉛뉜뉝뉞뉟눨눩눪눫눬눭눮눯뉨뉩뉪뉫뉬뉭뉮눷뉰눹뉲눻뉴
```
 should be

```
뉘뉙뉚뉛뉜뉝뉞뉟뉠뉡뉢뉣뉤뉥뉦뉧뉨뉩뉪뉫뉬뉭뉮뉯뉰뉱뉲뉳뉴
```
unicode_page_b4.png, 1.12.2:

```
뒤뒥뒦뒨뒩뒪뒫둴둵둶둷둸둹둺둻뒴뒵뒶뒷뒸뒹뒺뒃뒼뒅뒾뒇듀
```
 should be

```
뒤뒥뒦뒨뒩뒪뒫뒬뒭뒮뒯뒰뒱뒲뒳뒴뒵뒶뒷뒸뒹뒺뒻뒼뒽뒾뒿듀
```
unicode_page_b6.png & unicode_page_b7.png, 1.12.2:

```
뛰뛱뛲뛳뛴뛵뛶뛷뛀뛁뛂뛃뛄뛅뛆뛇뜀뜁뜂뜃뜄뜅뜆뛏뜈뛑뜊뛓뜌
```
 should be

```
뛰뛱뛲뛳뛴뛵뛶뛷뛸뛹뛺뛻뛼뛽뛾뛿뜀뜁뜂뜃뜄뜅뜆뜇뜈뛸뜊뜋뜌
```
unicode_page_bb.png, 1.12.2:

```
뮈뮉뮊뮋뮌뮍뮎뮏뭘뭙뭚뭛뭜뭝뭞뭟뮘뮙뮚뮛뮜뮝뮞뭧뮠뭩뮢뭫뮤
```
 should be

```
뮈뮉뮊뮋뮌뮍뮎뮏뮐뮑뮒뮓뮔뮕뮖뮗뮘뮙뮚뮛뮜뮝뮞뮟뮠뮐뮢뮣뮤
```
unicode_page_bd.png, 1.12.2:

```
뷔뷕뷖뷗뷘뷙뷚뷛붤붥붦붧붨붩붪뭟뷤뷥뷦뷧뷨뷩뷪붳뷬붵뷮붷뷰
```
 should be

```
뷔뷕뷖뷗뷘뷙뷚뷛뷜뷝뷞뷟뷠뷡뷢뷣뷤뷥뷦뷧뷨뷩뷪뷫뷬뷭뷮뷯뷰
```
unicode_page_c0.png, 1.12.2:

```
쀠쀡쀢쀣쀤쀥쀦쀧뿰뿱뿲뿳뿴뿵뿶뿷쀰쀱쀲쀳쀴쀵쀶뿿쀸쀁쀺쀃쀼
```
 should be

```
쀠쀡쀢쀣쀤쀥쀦쀧쀨쀩쀪쀫쀬쀭쀮쀯쀰쀱쀲쀳쀴쀵쀶쀷쀸쀹쀻쀻쀼
```

unicode_page_c2.png, 1.12.2:

```
쉬쉭쉮쉯쉰쉱쉲쉳쉴숽숾숿쉀쉁쉂쉃쉼쉽쉾쉿슀슁슂쉋슄쉍슆슇슈
```
 should be

```
쉬쉭쉮쉯쉰쉱쉲쉳쉴쉵쉼쉷쉸쉹쉺쉻쉼쉽쉾쉿슀슁슂슃슄슅슆슇슈
```

unicode_page_c4.png, 1.12.2:

```
쒸쒹쒺쒼쒿쒈쒉쒊쒋쒌쒍쒎쒏쓈쓉쓊쓋쓌쓍쓎쒗쓐쒙쓒쒛쓔
```
 should be

```
쒸쒹쒺쒼쒿쓀쓁쓂쓃쓄쓅쓆쓇쓈쓉쓊쓋쓌쓍쓎쓏쓐쓑쓒쓓쓔
```

unicode_page_c7.png, 1.12.2:

```
위윅윆윇윈윉윊윋월웕웖웗웘웙웚웛윔윕윖윗윘윙윚웣윜웥윞웧유
```
 should be
위윅윆윇윈윉윊윋윌윍윎윏윐윑윒윓윔윕윖윗윘윙윚윛윜윝윞윟유

Like this, unicode_page_c9.png (쥐~쥫), unicode_page_cb.png (쮜~쮷), unicode_page_cd.png & unicode_page_ce.png (취~츃), unicode_page_d4.png (퓌~퓧) are misdotted as the pattern of those up.

Note: the affected version could not be fixed to 1.12+, but could include the entire ones since unicode font is introduced.

## Comments (6)

### Comment 1: migrated (2022-07-23T08:22:05.429-0700)

This comment contained multiple image attachments (18), please login to view the attachments.

### Comment 2: migrated (2022-07-23T09:06:24.733-0700)

[Additional notes]
I paused writing those since it's too much and complecated to write down even for korean natives. However, I think I demonstrated the useful patterns and wrong locations under those pattern, so it should be enough for readers to understand.
One more reading-related bug, ending with 'ㅡㅎ' and 'ㅜㅎ' is identical, seems to be non-fixable without enlarging the font, so that's not mentioned on the main content.

### Comment 3: ampolive (2022-07-23T10:35:04.451-0700)

Is this still the case in 1.19?

### Comment 4: migrated (2022-07-23T15:41:43.225-0700)

Yeah, but I'll SHA+MD5 the resource file to double-check it.{} welp the hash is different so I opened the texture to check out
Here's the extracted 1.12.2 texture and the extracted 1.19 one.
I'll submit some input data of them on 1.19 too, so plz wait a bit.
Or you can just tellraw that strange korean textlines but hashing them would be faster
— add —
Here's the screenshot. I titled the save with "뉘뉙뉚뉛뉜뉝뉞뉟뉠뉡뉢뉣뉤뉥뉦뉧뉨뉩뉪뉫뉬뉭뉮뉯뉰뉱뉲뉳뉴" to easily check the difference.

### Comment 5: migrated (2022-07-24T10:04:32.140-0700)

I wrote down some code and found these 200 pairs of duplicates. Textures are from 1.19 assets.

### Comment 6: migrated (2022-08-10T09:57:56.829-0700)

Still the case on 1.19.2

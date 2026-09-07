# MC-301735: Server Management Protocol Kick command parameter mis match

**Mojira URL:** [https://bugs.mojang.com/browse/MC-301735](https://bugs.mojang.com/browse/MC-301735)

## Report details

- **Mojira categories:** Dedicated Server
- **Project:** MC
- **Issue key:** MC-301735
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Confirmed
- **Mojang priority:** Important
- **Created:** 2025-09-01T18:34:49.493-0700
- **Updated:** 2026-03-11T03:44:24.038-0700
- **Resolution date:** 2025-09-23T07:31:42.846-0700
- **Affects versions:** 25w35a; 1.21.9 Pre-Release 1; 1.21.9 Pre-Release 2
- **Fix versions:** 1.21.9 Pre-Release 4
- **Area:** Platform HC
- **Votes:** 4
- **Watchers:** 0
- **Attachments:** 0

## Description

According to the information provided by the rpc.discover command, the kick command should require an array as input. This would be consistent with other similar commands.
- Steps to reproduce the issue

- setup the Management protocol

- Attempt to send a kick command as described by the command discovery
Kick parameters provided by discovery:

```
"params": [
  {
    "name": "kick",
    "schema": {
      "items": {
        "$ref": "#/components/schemas/kick_player"
      },
      "type": "array"
    },
    "required": true
  }
]
```

Example payload that produces the error:

```
{"method":"minecraft:players/kick","id":0,"params":[[{"players":[{"name":"jSdCool"}],"message":{"literal":"kick test"}}]]}
```
- Expected result

The target player is kicked from the server
- Actual result

The following error is received due to the fact the server was expecting an object not an array
Invalid params: Not a JSON object: [{"players":[{"name":"jSdCool"}],"message":{"literal":"kick test"}}]

## Comments (4)

### Comment 1: Julian Vennen (2025-09-15T02:12:33.341-0700)

Issue persists on 25w37a

### Comment 2: Julian Vennen (2025-09-16T08:28:20.295-0700)

Issue still exists on 1.21.9-pre1

### Comment 3: Julian Vennen (2025-09-19T13:35:28.169-0700)

The issue continues to occur on 1.21.9-pre2.

### Comment 4: Julian Vennen (2025-09-23T03:52:33.389-0700)

Still present on 1.21.9-pre3

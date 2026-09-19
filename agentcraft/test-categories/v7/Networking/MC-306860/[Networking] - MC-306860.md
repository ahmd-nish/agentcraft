# MC-306860: Player object text components in server status messages (MotD) are no longer replaced by fallback text

**Mojira URL:** [https://bugs.mojang.com/browse/MC-306860](https://bugs.mojang.com/browse/MC-306860)

## Report details

- **Mojira categories:** Networking
- **Project:** MC
- **Issue key:** MC-306860
- **Issue type:** Bug
- **Status:** Resolved
- **Resolution:** Fixed
- **Confirmation status:** Community Consensus
- **Mojang priority:** Important
- **Created:** 2026-03-14T10:15:21.211-0700
- **Updated:** 2026-03-16T03:03:02.385-0700
- **Resolution date:** 2026-03-16T03:03:02.330-0700
- **Affects versions:** 26.1 Pre-Release 2
- **Fix versions:** 26.1 Pre-Release 3
- **Area:** Platform HC
- **Watchers:** 2
- **Attachments:** 2
- **Attachment filenames:** example.png; Minecraft Screenshot 2026.03.15 - 18.44.44.17.png

## Description

Infomation from changelog 26.1 Pre-Release 1:
Objects of type player (player heads) no longer can be used in server status messages (MotD)
But in 26.1 Pre Release 2, player object text component is rendered as normal in motd. Instead, sprite object text component is rendered as fallback text.
The reason I discovered it is I have sent a fake status_response data packet to client and make payload {"description":[{player:{name:alex}},{sprite:\'block/stone\'}],"players":{"max":20,"online":0},"version":{"name":"26.1 Pre-Release 2","protocol":1073742123},"enforcesSecureChat":true} today. Motd are displayed as <a player head sprite>[blocks/stone] , not [alex head]<stone sprite>, It is against at the info in changelog 26.1 Pre-Release 1.
Because we cannot send motd which used non-pure-string text component to client in vanilla server, I cannot give a vaild way to reproduce it.  But I think, since Mojang knows motd can only be string in vanilla server but still record it in changelog, I should report this behavior.

## Comments (2)

### Comment 1: Automation for Jira (2026-03-14T10:15:28.594-0700)

Thank you for helping us improve Minecraft! We saved your files:

### Comment 2: BugTracker_ (2026-03-15T09:02:09.712-0700)

Can confirm:
How to Reproduce:

- Make sure you have Python installed

- Save this following script as a .py file:

```import socket
import json

def encode_varint(value):
    result = bytearray()
    while True:
        byte = value & 0x7F
        value >>= 7
        if value != 0:
            byte |= 0x80
        result.append(byte)
        if value == 0:
            break
    return bytes(result)

def decode_varint(data, pos=0):
    result = 0
    shift = 0
    while pos < len(data):
        byte = data[pos]
        pos += 1
        result |= (byte & 0x7F) << shift
        shift += 7
        if not (byte & 0x80):
            return result, pos
    raise ValueError("Ran out of data reading VarInt")

def encode_string(text):
    encoded = text.encode('utf-8')
    return encode_varint(len(encoded)) + encoded

def build_packet(packet_id, data=b''):
    id_bytes = encode_varint(packet_id)
    content = id_bytes + data
    return encode_varint(len(content)) + content

def recv_exact(sock, n):
    data = b''
    while len(data) < n:
        chunk = sock.recv(n - len(data))
        if not chunk:
            raise ConnectionError("Client disconnected early")
        data += chunk
    return data

def recv_packet(sock):
    length_bytes = bytearray()
    while True:
        byte = recv_exact(sock, 1)[0]
        length_bytes.append(byte)
        if not (byte & 0x80):
            break
        if len(length_bytes) >= 5:
            raise ValueError("VarInt too long")
    length, _ = decode_varint(bytes(length_bytes))
    content = recv_exact(sock, length)
    packet_id, offset = decode_varint(content)
    payload = content[offset:]
    return packet_id, payload

STATUS_JSON = {
    "description": [
        {"player": {"name": "alex"}},
        {"sprite": "block/stone"}
    ],
    "players": {"max": 20, "online": 0},
    "version": {"name": "26.1 Pre-Release 2", "protocol": 1073742123},
    "enforcesSecureChat": True
}

def handle_client(conn, addr):
    print(f"\n[+] Client connected from {addr}")
    try:
        packet_id, payload = recv_packet(conn)
        if packet_id != 0x00:
            return
        pos = 0
        protocol_ver, pos = decode_varint(payload, pos)
        addr_len, pos = decode_varint(payload, pos)
        server_addr = payload[pos:pos + addr_len].decode('utf-8')
        pos += addr_len
        server_port = int.from_bytes(payload[pos:pos+2], 'big')
        pos += 2
        next_state, pos = decode_varint(payload, pos)
        if next_state != 1:
            return
        packet_id, _ = recv_packet(conn)
        json_str = json.dumps(STATUS_JSON)
        response_packet = build_packet(0x00, encode_string(json_str))
        conn.sendall(response_packet)
        print(f"    Payload sent: {json_str}")
        try:
            packet_id, ping_payload = recv_packet(conn)
            if packet_id == 0x01:
                conn.sendall(build_packet(0x01, ping_payload))
        except Exception:
            pass
    except Exception as e:
        print(f"    Error: {e}")
    finally:
        conn.close()
        print(f"[-] Client disconnected.")

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server.bind(('0.0.0.0', 25565))
    server.listen(5)
    print("Mock server running on port 25565. Add 127.0.0.1 in Minecraft.")
    print("Press Ctrl+C to stop.")
    try:
        while True:
            conn, addr = server.accept()
            handle_client(conn, addr)
    except KeyboardInterrupt:
        print("\nStopped.")
    finally:
        server.close()

if __name__ == '__main__':
    main()```

- Open Command Prompt or Powershell and run the .py  file: python _.py

- Launch Minecraft Java Edition 26.1 Pre Release 2

- Go to Multiplayer and add the following server address: 127.0.0.1

- Click done and observe the MOTD displayed under the server name in the list.

Expected Result:
- {"player": {"name": "alex"}} should render as fallback text ([alex]), as player objects are no longer permitted in Motd’s

- {"sprite": "block/stone"} should render as a visible block sprite icon.

Observed Result:
- {"player": {"name": "alex"}} renders as a player head sprite, it is not being blocked as the changelog states it should be

- {"sprite": "block/stone"} renders as the fallback text [block/stone], the sprite is not rendering.

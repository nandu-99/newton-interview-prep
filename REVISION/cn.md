# Computer Networks Master Revision Notes

## Basics of Computer Networks

A **computer network** is a collection of devices connected together to share data and resources.

```text
Device A ──── Network ──── Device B
              (wired / wireless)
```

### Why Networks?

* Share resources (files, printers, internet)
* Communication (email, messaging)
* Centralized data storage
* Remote access

### Types of Networks

| Type | Scope | Example |
| ---- | ----- | ------- |
| **LAN** (Local Area Network) | Single building / campus | Office network |
| **WAN** (Wide Area Network) | Cities / countries | The Internet |
| **MAN** (Metropolitan Area Network) | City-wide | Cable TV network |
| **PAN** (Personal Area Network) | Around a person | Bluetooth |

### Key Devices

| Device | Role |
| ------ | ---- |
| **Router** | Connects different networks, routes packets between them |
| **Switch** | Connects devices within the same network (LAN) |
| **Hub** | Broadcasts to all devices (dumb, replaced by switches) |
| **Modem** | Converts digital ↔ analog signals for ISP connection |

### Bandwidth vs Latency

* **Bandwidth** → how much data can be transferred per second (Mbps, Gbps).
* **Latency** → time for data to travel from source to destination (ms).

---

## OSI Model

The **OSI (Open Systems Interconnection)** model is a conceptual framework that standardizes how data travels across a network in **7 layers**.

```text
Layer 7 → Application   → HTTP, FTP, DNS, SMTP
Layer 6 → Presentation  → Encryption, Compression, Encoding
Layer 5 → Session       → Start, manage, end sessions
Layer 4 → Transport     → TCP, UDP — end-to-end delivery
Layer 3 → Network       → IP — routing between networks
Layer 2 → Data Link     → MAC address — delivery within same network
Layer 1 → Physical      → Cables, signals, bits
```

**Mnemonic (top → bottom):** All People Seem To Need Data Processing

### What each layer does

| Layer | Key Responsibility | Protocol / Example |
| ----- | ------------------ | ------------------ |
| Application | User-facing services | HTTP, FTP, DNS |
| Presentation | Format, encrypt, compress data | SSL/TLS, JPEG |
| Session | Open and close communication sessions | NetBIOS |
| Transport | Reliable delivery, segmentation, ports | TCP, UDP |
| Network | Logical addressing, routing | IP, ICMP |
| Data Link | Physical addressing (MAC), error detection | Ethernet, Wi-Fi |
| Physical | Raw bit transmission over medium | Cables, radio waves |

### Data Encapsulation

As data travels down the layers (sender), each layer **adds a header** (encapsulation).
As data travels up (receiver), each layer **removes its header** (decapsulation).

```text
Application  → Data
Transport    → Segment  (adds port info)
Network      → Packet   (adds IP address)
Data Link    → Frame    (adds MAC address)
Physical     → Bits
```

---

## TCP/IP Model

The **TCP/IP model** is the practical model used on the internet — 4 layers (maps to OSI).

```text
TCP/IP Layer       OSI Equivalent
─────────────────────────────────
Application    →   Layer 7, 6, 5
Transport      →   Layer 4
Internet       →   Layer 3
Network Access →   Layer 2, 1
```

| TCP/IP Layer | Protocols |
| ------------ | --------- |
| Application | HTTP, HTTPS, DNS, FTP, SMTP |
| Transport | TCP, UDP |
| Internet | IP, ICMP, ARP |
| Network Access | Ethernet, Wi-Fi |

**OSI = theoretical reference. TCP/IP = what the internet actually uses.**

---

## IP Addressing and Ports

### IP Address

A **unique address** identifying a device on a network.

**IPv4** → 32-bit, written as 4 octets: `192.168.1.1`
**IPv6** → 128-bit, written in hex: `2001:0db8:85a3::8a2e:0370:7334`

```text
IPv4 → ~4 billion addresses (exhausted)
IPv6 → ~340 undecillion addresses
```

### Public vs Private IP

| Type | Range | Use |
| ---- | ----- | --- |
| Private | 192.168.x.x, 10.x.x.x, 172.16-31.x.x | Inside home/office network |
| Public | Everything else | Visible on the internet |

* **NAT (Network Address Translation)** → router maps many private IPs to one public IP.

### Localhost

`127.0.0.1` → loopback address, refers to your own machine. Used for local testing.

### Subnet Mask

Determines which part of an IP is the **network** and which is the **device**.

```text
IP:      192.168.1.10
Mask:    255.255.255.0
Network: 192.168.1.0
Device:  .10
```

### Ports

A **port** identifies a specific process/service on a device. IP gets you to the machine; port gets you to the right service.

```text
IP Address → which machine
Port       → which service on that machine
```

| Port | Service |
| ---- | ------- |
| 80 | HTTP |
| 443 | HTTPS |
| 22 | SSH |
| 21 | FTP |
| 53 | DNS |
| 3306 | MySQL |
| 5432 | PostgreSQL |

* **Well-known ports** → 0–1023 (reserved for standard services)
* **Registered ports** → 1024–49151
* **Ephemeral ports** → 49152–65535 (temporary, used by clients)

---

## DNS

**DNS (Domain Name System)** → translates human-readable domain names into IP addresses.

```text
google.com  →  DNS  →  142.250.195.46
```

### Why DNS?

IP addresses are hard to remember. DNS acts as the internet's phone book.

### DNS Resolution Process

```text
1. Browser cache         → already know the IP? Use it.
2. OS cache / hosts file → check local system cache.
3. Recursive Resolver    → your ISP's DNS server queries on your behalf.
4. Root Name Server      → knows where .com, .org, .in servers are.
5. TLD Name Server       → knows who manages google.com.
6. Authoritative Server  → returns the actual IP for google.com.
7. IP returned to browser → connection begins.
```

### DNS Record Types

| Record | Purpose |
| ------ | ------- |
| **A** | Domain → IPv4 address |
| **AAAA** | Domain → IPv6 address |
| **CNAME** | Domain → another domain (alias) |
| **MX** | Mail server for the domain |
| **NS** | Authoritative name server |
| **TXT** | Text data (used for verification, SPF) |

### TTL (Time to Live)

How long a DNS record is cached. After TTL expires, the resolver fetches a fresh record.

---

## HTTP and HTTPS

**HTTP (HyperText Transfer Protocol)** → protocol for transferring data between browser and server.

```text
Client (Browser) ──── HTTP Request ────► Server
Client           ◄─── HTTP Response ─── Server
```

### HTTP Request Structure

```text
Method  : GET
URL     : /products/1
Headers : Host, Content-Type, Authorization, ...
Body    : (for POST/PUT — the data being sent)
```

### HTTP Methods

| Method | Purpose |
| ------ | ------- |
| GET | Retrieve data |
| POST | Create new data |
| PUT | Update (replace entire resource) |
| PATCH | Update (partial update) |
| DELETE | Remove data |

### HTTP Status Codes

```text
1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client Error
5xx → Server Error
```

| Code | Meaning |
| ---- | ------- |
| 200 | OK |
| 201 | Created |
| 204 | No Content |
| 301 | Moved Permanently |
| 400 | Bad Request |
| 401 | Unauthorized |
| 403 | Forbidden |
| 404 | Not Found |
| 500 | Internal Server Error |

### HTTPS

**HTTPS = HTTP + TLS (Transport Layer Security)**

* Data is **encrypted** in transit — cannot be read by a third party.
* Uses **SSL/TLS certificates** to verify server identity.
* Browser shows a padlock icon.

```text
HTTP  → plain text (insecure)
HTTPS → encrypted (secure)
```

### TLS Handshake (simplified)

```text
1. Client → Server : "Hello, here are the cipher suites I support"
2. Server → Client : Certificate (proves server identity) + chosen cipher
3. Client verifies certificate with Certificate Authority (CA)
4. Shared secret key established → all traffic encrypted from here
```

### HTTP Versions

| Version | Key Feature |
| ------- | ----------- |
| HTTP/1.1 | Persistent connections, one request at a time per connection |
| HTTP/2 | Multiplexing — multiple requests over one connection |
| HTTP/3 | Uses QUIC (UDP-based) — faster, less latency |

---

## TCP vs UDP

Both are **Transport Layer** protocols.

### TCP (Transmission Control Protocol)

**Connection-oriented, reliable, ordered delivery.**

```text
1. Connection established (3-way handshake)
2. Data sent in segments, each acknowledged
3. Lost segments retransmitted
4. Connection closed (4-way handshake)
```

**3-Way Handshake:**

```text
Client → SYN      → Server   (I want to connect)
Client ← SYN-ACK ← Server   (OK, I'm ready)
Client → ACK      → Server   (Great, let's go)
```

### UDP (User Datagram Protocol)

**Connectionless, fast, no guarantee of delivery or order.**

```text
Sender → sends packets → done (no handshake, no ACK)
Receiver → may get all, some, or none — in any order
```

### TCP vs UDP

| Feature | TCP | UDP |
| ------- | --- | --- |
| Connection | Required (handshake) | None |
| Reliability | Guaranteed delivery | No guarantee |
| Order | In-order delivery | No ordering |
| Speed | Slower (overhead) | Faster |
| Error Checking | Yes (retransmit on loss) | Basic checksum only |
| Use Cases | HTTP, Email, File Transfer | Video streaming, Gaming, DNS, VoIP |

**Rule of thumb:**
* Need reliability → **TCP**
* Need speed, can tolerate some loss → **UDP**

---

## Client-Server Architecture

A model where **clients** request services and **servers** provide them.

```text
Client ──── Request ────► Server
Client ◄─── Response ─── Server
```

### Client

* Initiates the request.
* Examples: browser, mobile app, CLI tool.

### Server

* Listens for incoming requests, processes them, sends a response.
* Examples: web server (Nginx, Apache), API server, database server.

### Key Characteristics

* **Centralized** → server is the single source of truth.
* **Scalable** → multiple clients can connect to one server.
* **Stateless (HTTP)** → each request is independent; server doesn't remember previous requests by default.
* **Stateful** → server remembers session state (via cookies, sessions, tokens).

### Types of Servers

| Server Type | Role |
| ----------- | ---- |
| Web Server | Serves static files (HTML, CSS, images) |
| Application Server | Runs business logic, handles API requests |
| Database Server | Stores and retrieves data |
| DNS Server | Resolves domain names |
| Proxy Server | Intermediary between client and server |

### Peer-to-Peer (P2P) — alternative model

No central server. Each node is both client and server. Example: BitTorrent, Blockchain.

---

## Network Communication Flow

What happens at each layer when you send data:

```text
SENDER                              RECEIVER
─────────────────────────────────────────────
Application → creates data          Application ← reads data
Transport   → adds port (segment)   Transport   ← removes port
Network     → adds IP (packet)      Network     ← removes IP
Data Link   → adds MAC (frame)      Data Link   ← removes MAC
Physical    → sends bits ──────────► Physical  ← receives bits
```

### Key Protocols at Each Step

```text
Application : HTTP, DNS, FTP
Transport   : TCP (segments) / UDP (datagrams)
Network     : IP (routing), ICMP (ping/errors), ARP (IP → MAC)
Data Link   : Ethernet, Wi-Fi (MAC addressing)
Physical    : Cables, fiber, radio waves
```

### ARP (Address Resolution Protocol)

Resolves IP address → MAC address within the same network.

```text
"Who has 192.168.1.5?" → broadcast
"That's me, MAC = AA:BB:CC:DD:EE:FF" → reply
```

### ICMP (Internet Control Message Protocol)

Used for error messages and diagnostics.

* `ping` → uses ICMP echo request/reply to test connectivity.
* `traceroute` → shows hops a packet takes to reach destination.

---

## What Happens When You Access a URL

Full flow for typing `https://www.google.com` in a browser:

```text
1. URL Parsing
   Browser parses: protocol (HTTPS), domain (www.google.com), path (/)

2. DNS Resolution
   Browser cache → OS cache → Recursive resolver → Root → TLD → Authoritative
   Returns IP: 142.250.195.46

3. TCP Connection (3-Way Handshake)
   Client → SYN → Server (port 443 for HTTPS)
   Client ← SYN-ACK ← Server
   Client → ACK → Server

4. TLS Handshake
   Exchange certificates, verify identity, agree on encryption keys.
   Encrypted tunnel established.

5. HTTP Request Sent
   GET / HTTP/1.1
   Host: www.google.com
   (over the encrypted TLS connection)

6. Server Processes Request
   Web server receives request → application logic runs → fetches data if needed.

7. HTTP Response Sent
   HTTP/1.1 200 OK
   Content-Type: text/html
   (HTML content in body)

8. Browser Renders the Page
   Parses HTML → fetches CSS, JS, images (new requests for each)
   Builds DOM → renders page visually.

9. Connection Closed (or kept alive for reuse)
   FIN → FIN-ACK → ACK (TCP 4-way teardown)
```

### Summary

```text
URL → DNS → IP → TCP Handshake → TLS Handshake → HTTP Request
→ Server Logic → HTTP Response → Browser Render
```

---

## One-Line Definitions

* **Network** → connected devices sharing data and resources.
* **LAN** → network within a building.
* **WAN** → network spanning cities/countries; the internet is a WAN.
* **Router** → connects different networks and routes packets.
* **Switch** → connects devices within the same network.
* **OSI Model** → 7-layer conceptual framework for network communication.
* **TCP/IP Model** → 4-layer practical model used on the internet.
* **IP Address** → unique identifier for a device on a network.
* **Port** → identifies a specific service on a device.
* **DNS** → translates domain names to IP addresses.
* **HTTP** → protocol for transferring data between browser and server.
* **HTTPS** → HTTP with TLS encryption.
* **TLS** → protocol that encrypts data in transit.
* **TCP** → reliable, ordered, connection-oriented transport protocol.
* **UDP** → fast, connectionless, no delivery guarantee.
* **3-Way Handshake** → SYN → SYN-ACK → ACK to establish TCP connection.
* **Client** → initiates requests.
* **Server** → listens for and responds to requests.
* **ARP** → resolves IP address to MAC address.
* **ICMP** → protocol for network diagnostics (ping, traceroute).
* **Latency** → time for data to travel from source to destination.
* **Bandwidth** → max data transfer rate of a connection.
* **NAT** → maps multiple private IPs to one public IP.
* **Status 200** → OK. **404** → Not Found. **500** → Server Error.

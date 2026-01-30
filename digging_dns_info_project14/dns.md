#### What’s the IP address of microsoft.com?

```
; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> microsoft.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 56002
;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;microsoft.com.                 IN      A

;; ANSWER SECTION:
microsoft.com.          1071    IN      A       13.107.253.70
microsoft.com.          1071    IN      A       13.107.226.70

;; Query time: 9 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Fri Jan 30 07:00:39 MST 2026
;; MSG SIZE  rcvd: 74
```
13.107.253.70 or 13.107.226.70

#### What’s the mail exchange for google.com?

```
; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> mx google.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 10643
;; flags: qr rd ra; QUERY: 1, ANSWER: 1, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;google.com.                    IN      MX

;; ANSWER SECTION:
google.com.             117     IN      MX      10 smtp.google.com.

;; Query time: 17 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Fri Jan 30 07:02:10 MST 2026
;; MSG SIZE  rcvd: 60
```
smtp.google.com.

#### What are the name servers for duckduckgo.com?

```
; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> ns duckduckgo.com
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 51651
;; flags: qr rd ra; QUERY: 1, ANSWER: 8, AUTHORITY: 0, ADDITIONAL: 1

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 65494
;; QUESTION SECTION:
;duckduckgo.com.                        IN      NS

;; ANSWER SECTION:
duckduckgo.com.         86400   IN      NS      dns1.p05.nsone.net.
duckduckgo.com.         86400   IN      NS      ns02.quack-dns.com.
duckduckgo.com.         86400   IN      NS      ns04.quack-dns.com.
duckduckgo.com.         86400   IN      NS      dns4.p05.nsone.net.
duckduckgo.com.         86400   IN      NS      ns01.quack-dns.com.
duckduckgo.com.         86400   IN      NS      ns03.quack-dns.com.
duckduckgo.com.         86400   IN      NS      dns3.p05.nsone.net.
duckduckgo.com.         86400   IN      NS      dns2.p05.nsone.net.

;; Query time: 53 msec
;; SERVER: 127.0.0.53#53(127.0.0.53) (UDP)
;; WHEN: Fri Jan 30 07:07:50 MST 2026
;; MSG SIZE  rcvd: 218
```
See above.


### Following the process in the Digging from a Root Name Server in the section above, start with a root name server and dig your way down to www.yahoo.com (NOT yahoo.com).


```
dig @yf4.a1.b.yahoo.net me-ycpi-cf-www.g06.yahoodns.net

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> @yf4.a1.b.yahoo.net me-ycpi-cf-www.g06.yahoodns.net
; (1 server found)
;; global options: +cmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 23001
;; flags: qr aa rd; QUERY: 1, ANSWER: 3, AUTHORITY: 0, ADDITIONAL: 1
;; WARNING: recursion requested but not available

;; OPT PSEUDOSECTION:
; EDNS: version: 0, flags:; udp: 1232
;; QUESTION SECTION:
;me-ycpi-cf-www.g06.yahoodns.net. IN    A

;; ANSWER SECTION:
me-ycpi-cf-www.g06.yahoodns.net. 60 IN  A       74.6.160.106
me-ycpi-cf-www.g06.yahoodns.net. 60 IN  A       69.147.80.12
me-ycpi-cf-www.g06.yahoodns.net. 60 IN  A       69.147.80.15

;; Query time: 21 msec
;; SERVER: 68.180.130.15#53(yf4.a1.b.yahoo.net) (UDP)
;; WHEN: Fri Jan 30 07:20:35 MST 2026
;; MSG SIZE  rcvd: 108
```
See above.

With trace.

```
$ dig +trace www.yahoo.com

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> +trace www.yahoo.com
;; global options: +cmd
.                       4882    IN      NS      i.root-servers.net.
.                       4882    IN      NS      m.root-servers.net.
.                       4882    IN      NS      e.root-servers.net.
.                       4882    IN      NS      f.root-servers.net.
.                       4882    IN      NS      c.root-servers.net.
.                       4882    IN      NS      h.root-servers.net.
.                       4882    IN      NS      b.root-servers.net.
.                       4882    IN      NS      j.root-servers.net.
.                       4882    IN      NS      k.root-servers.net.
.                       4882    IN      NS      g.root-servers.net.
.                       4882    IN      NS      a.root-servers.net.
.                       4882    IN      NS      d.root-servers.net.
.                       4882    IN      NS      l.root-servers.net.
;; Received 239 bytes from 127.0.0.53#53(127.0.0.53) in 0 ms

com.                    172800  IN      NS      a.gtld-servers.net.
com.                    172800  IN      NS      b.gtld-servers.net.
com.                    172800  IN      NS      c.gtld-servers.net.
com.                    172800  IN      NS      d.gtld-servers.net.
com.                    172800  IN      NS      e.gtld-servers.net.
com.                    172800  IN      NS      f.gtld-servers.net.
com.                    172800  IN      NS      g.gtld-servers.net.
com.                    172800  IN      NS      h.gtld-servers.net.
com.                    172800  IN      NS      i.gtld-servers.net.
com.                    172800  IN      NS      j.gtld-servers.net.
com.                    172800  IN      NS      k.gtld-servers.net.
com.                    172800  IN      NS      l.gtld-servers.net.
com.                    172800  IN      NS      m.gtld-servers.net.
com.                    86400   IN      DS      19718 13 2 8ACBB0CD28F41250A80A491389424D341522D946B0DA0C0291F2D3D7 71D7805A
com.                    86400   IN      RRSIG   DS 8 1 86400 20260212050000 20260130040000 21831 . mioL1VIQ4yewjWwM6ErcYwlOF2j2FPBgqc55lrBJuh5C64MkGD6MeuLE TJ0n8vTqgK1Xm66/r7YF2K8/czr9odvu/brkVjtSa3XmVIVpcbYm4LkK wKJ14WlUG9ky8JJLuv5WeMjcRaJT6m3q37/Mea27Vtv0+GVhrJ3Z+KBZ c/ztcJRRWDZV+AARcVbuNZ3i1F/4ulC2xIV4tCuyOfiWQCASIsVJKVJJ soshTwp3Kz8CTHNGAGpK1SCQtVoGfI/0x/I0n1LsaiuFzoef45lgGiMh XwEF6GTMlgDd5ieyjkbkzPfqyoyj8tKuJ6O4+m1nwqY7ogOAwPZlGFxG GB7oFw==
;; Received 1173 bytes from 170.247.170.2#53(b.root-servers.net) in 83 ms

yahoo.com.              172800  IN      NS      ns1.yahoo.com.
yahoo.com.              172800  IN      NS      ns5.yahoo.com.
yahoo.com.              172800  IN      NS      ns2.yahoo.com.
yahoo.com.              172800  IN      NS      ns3.yahoo.com.
yahoo.com.              172800  IN      NS      ns4.yahoo.com.
CK0POJMG874LJREF7EFN8430QVIT8BSM.com. 900 IN NSEC3 1 1 0 - CK0Q3UDG8CEKKAE7RUKPGCT1DVSSH8LL NS SOA RRSIG DNSKEY NSEC3PARAM
CK0POJMG874LJREF7EFN8430QVIT8BSM.com. 900 IN RRSIG NSEC3 13 2 900 20260203002713 20260126231713 35511 com. bTdDPRr2AKmY55XgS2AYbKVp7QYc8GHPp+ix6JYteFj61N3dGW7n2Q+l 4C5wvliRwczTaDArpgeWQTIiOxENxQ==
GPIOQL0L7VJL2SB4CTA1LU5TC263MU96.com. 900 IN NSEC3 1 1 0 - GPIOVE5CC3CA0D1H14G1GI4J0835GEKB NS DS RRSIG
GPIOQL0L7VJL2SB4CTA1LU5TC263MU96.com. 900 IN RRSIG NSEC3 13 2 900 20260203021337 20260127010337 35511 com. KjklrxiJvGyJiVRIFZd4BpEMVMvdnqO9kZO2LTP52Czs3j3VevZxCCzd ChWQBJ3ciXdnDfYeod22cq/R/WdFnA==
;; Received 681 bytes from 2001:502:8cc::30#53(h.gtld-servers.net) in 53 ms

www.yahoo.com.          60      IN      CNAME   me-ycpi-cf-www.g06.yahoodns.net.
;; Received 115 bytes from 2001:4998:1b0::7961:686f:6f21#53(ns1.yahoo.com) in 21 ms

$ dig +trace me-ycpi-cf-www.g06.yahoodns.net

; <<>> DiG 9.18.39-0ubuntu0.24.04.2-Ubuntu <<>> +trace me-ycpi-cf-www.g06.yahoodns.net
;; global options: +cmd
.                       4855    IN      NS      j.root-servers.net.
.                       4855    IN      NS      d.root-servers.net.
.                       4855    IN      NS      m.root-servers.net.
.                       4855    IN      NS      h.root-servers.net.
.                       4855    IN      NS      g.root-servers.net.
.                       4855    IN      NS      b.root-servers.net.
.                       4855    IN      NS      i.root-servers.net.
.                       4855    IN      NS      f.root-servers.net.
.                       4855    IN      NS      c.root-servers.net.
.                       4855    IN      NS      l.root-servers.net.
.                       4855    IN      NS      a.root-servers.net.
.                       4855    IN      NS      k.root-servers.net.
.                       4855    IN      NS      e.root-servers.net.
;; Received 239 bytes from 127.0.0.53#53(127.0.0.53) in 0 ms

net.                    172800  IN      NS      a.gtld-servers.net.
net.                    172800  IN      NS      b.gtld-servers.net.
net.                    172800  IN      NS      c.gtld-servers.net.
net.                    172800  IN      NS      d.gtld-servers.net.
net.                    172800  IN      NS      e.gtld-servers.net.
net.                    172800  IN      NS      f.gtld-servers.net.
net.                    172800  IN      NS      g.gtld-servers.net.
net.                    172800  IN      NS      h.gtld-servers.net.
net.                    172800  IN      NS      i.gtld-servers.net.
net.                    172800  IN      NS      j.gtld-servers.net.
net.                    172800  IN      NS      k.gtld-servers.net.
net.                    172800  IN      NS      l.gtld-servers.net.
net.                    172800  IN      NS      m.gtld-servers.net.
net.                    86400   IN      DS      37331 13 2 2F0BEC2D6F79DFBD1D08FD21A3AF92D0E39A4B9EF1E3F4111FFF2824 90DA453B
net.                    86400   IN      RRSIG   DS 8 1 86400 20260212050000 20260130040000 21831 . aR2py86GlMD8ifru6c8YWh2wCo24TkN7g7IBNsN2+8wu7UwfxGDmqT2X h7vurhmEJPMz964qn8n0yarMn1Rz0UjK4cnVUWkXPnpT5F0P4VuGxvb0 g8MqmpSFXE16nY4ZTMJR4xAxoQRbSHM4j4v4+S0a5Gaa3gq10FcYyKEk 6PqwabGZ6/Mm45j9VwK/cjOad6ai+hsOTxOrw812U+uI+qOr+O7vBJoE 9S6RL/IudXpuVTPRVNAUtOzPIVwgrcq1xxC+8s7WQ6bbUQhi+4NLr4Tp tHllOqLSIM9WWAkqlkMp7qjX6l8h6ZjVqA0PngCWlFLCI23ZAI6ruxKw pgq0bA==
;; Received 1188 bytes from 2001:500:a8::e#53(e.root-servers.net) in 25 ms

yahoodns.net.           172800  IN      NS      ns1.yahoo.com.
yahoodns.net.           172800  IN      NS      ns5.yahoo.com.
yahoodns.net.           172800  IN      NS      ns2.yahoo.com.
yahoodns.net.           172800  IN      NS      ns3.yahoo.com.
yahoodns.net.           172800  IN      NS      ns4.yahoo.com.
A1RT98BS5QGC9NFI51S9HCI47ULJG6JH.net. 900 IN NSEC3 1 1 0 - A1RTLNPGULOGN7B9A62SHJE1U3TTP8DR NS SOA RRSIG DNSKEY NSEC3PARAM
A1RT98BS5QGC9NFI51S9HCI47ULJG6JH.net. 900 IN RRSIG NSEC3 13 2 900 20260203033105 20260127022105 44109 net. /tshU5AdS77HZpKh7pBR5RILXzrNRU8Xv6Kc4HYSMLNLK/0bcjsOV2lO 4NUGqirlmzn0Mm7UBIPtc2IwtAVemQ==
CT797V4834THT0QIVOD0277MAON61O1F.net. 900 IN NSEC3 1 1 0 - CT7ABB2BJDNK3TNJ5QM1N945TG3CI6I7 NS DS RRSIG
CT797V4834THT0QIVOD0277MAON61O1F.net. 900 IN RRSIG NSEC3 13 2 900 20260205032948 20260129021948 44109 net. zQoO555WDNv1MVK8Cg4JzXtxY7cfwzoynDWQzEqsWZMMHDBXUJ1ZZKc6 1qelR7Uohyff6gjxWJOd2KIlsO4UYA==
;; Received 516 bytes from 2001:502:8cc::30#53(h.gtld-servers.net) in 53 ms

g06.yahoodns.net.       172800  IN      NS      yf4.a1.b.yahoo.net.
g06.yahoodns.net.       172800  IN      NS      yf1.a1.b.yahoo.net.
g06.yahoodns.net.       172800  IN      NS      yf2.a1.b.yahoo.net.
g06.yahoodns.net.       172800  IN      NS      yf3.a1.b.yahoo.net.
;; Received 174 bytes from 68.142.255.16#53(ns2.yahoo.com) in 26 ms

me-ycpi-cf-www.g06.yahoodns.net. 60 IN  A       69.147.80.15
me-ycpi-cf-www.g06.yahoodns.net. 60 IN  A       69.147.80.12
;; Received 92 bytes from 68.142.254.15#53(yf1.a1.b.yahoo.net) in 24 ms
```


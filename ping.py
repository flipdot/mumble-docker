#!/usr/bin/env python3
# -*- coding: utf-8
# Based on pcgod's mumble-ping script found at http://0xy.org/mumble-ping.py.

from struct import *
import socket, sys, time, datetime

if len(sys.argv) < 3:
    print("Usage: %s <host> <port>" % sys.argv[0])
    sys.exit(1)

host = sys.argv[1]
port = int(sys.argv[2])

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.settimeout(1)

buf = pack(">iQ", 0, datetime.datetime.now().microsecond)
s.sendto(buf, (host, port))

try:
    data, addr = s.recvfrom(1024)
except socket.timeout:
    print("%d:NaN:NaN" % (time.time()))
    sys.exit(2)

print("recvd %d bytes" % len(data))

r = unpack(">bbbbQiii", data)

version = r[1:4]
ts = r[4]
users = r[5]
max_users = r[6]
bandwidth = r[7]

ping = (datetime.datetime.now().microsecond - r[4]) / 1000.0
if ping < 0: ping = ping + 1000

print("# Version %d.%d.%d, %d/%d Users, ping %.1fms, %dkbit/s" %
      (version + (users, max_users, ping, bandwidth/1000)))

print("users =", users)

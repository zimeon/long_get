#!/usr/bin/python
#
# Do a GET that will timeout because it includes a content which 
# is not sent. Created to simulate errors seen at arXiv that
# generated spurious 500 responses which should instead be
# 408.
#
# 2016-02-09 Simeon Warner
#
import socket
import sys
import time
import urlparse

def send(socket, str):
    print("> %s" % (str))
    socket.send(str + "\r\n")

def long_get(url):
    print("\nDoing GET on %s" % (url))
    url = urlparse.urlparse(url)
    path = url.path if url.path!="" else "/"
    host = url.netloc
    port = url.port if url.port is not None else 80
    s = socket.socket(socket.AF_INET)
    s.settimeout(1000) #avoid timeout in client
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((host, port))
    send(s, "GET %s HTTP/1.1" % (path))
    send(s, "Host: %s" % (host))
    send(s, "User-Agent: long_get")
    send(s, "Content-Length: 1000")
    send(s, "")
    start_time = time.time()
    #send(s, "incomplete junk data")
    # Expect timeout.... show response
    data = (s.recv(10000))
    # https://docs.python.org/2/howto/sockets.html#disconnecting
    s.shutdown(1)
    s.close()
    duration = (time.time() - start_time)
    print("\nAfter %ds, got:\n< %s" % (duration, data.replace("\n","\n< ")))

for url in sys.argv[1:]:
    long_get(url)

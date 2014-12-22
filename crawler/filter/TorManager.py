__author__ = 'j'

import urllib2
from TorCtl import TorCtl
import socket

class TorManager:

    def __init__(self):
        pass


    def newId(self):
        print ">>>GETTING NEW IDENTITY"
        success = False
        s = socket.socket()
        s.connect(('localhost', 9050))
        s.send("AUTHENTICATE\r\n")
        resp = s.recv(1024)
        if resp.startswith('250'):
            s.send("signal NEWNYM\r\n")
            resp2 = s.recv(1024)
        if resp.startswith('250'):
            success = True
        return success

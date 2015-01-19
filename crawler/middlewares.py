import socket
import random
from crawler.filter import ProxyParser
import urllib2

class ProxyMiddleware(object):
    socket.setdefaulttimeout(50)
    proxyList = ProxyParser.ProxyParser().proxyList
    print proxyList

    def pickProxy(self):
        return self.checkWorkingSingleProxy(self.proxyList)

    def process_request(self, request, spider):
        print ">>>Selecting proxy....."
        proxy = self.checkWorkingSingleProxy(self.proxyList)
        if proxy == None:
            proxy = self.checkWorkingSingleProxy(self.proxyList)
        request.meta['proxy'] = "http://"+proxy+"/"
        print ">>>Selected proxy: "+proxy

    def checkWorkingSingleProxy(self, proxyList):
        randomNumber = random.randint(0,len(proxyList)-1)
        item = proxyList[randomNumber]
        if self.is_bad_proxy(item):
            print "Bad Proxy", item
            item = self.checkWorkingSingleProxy(proxyList)
        else:
            return item

    def is_bad_proxy(self, pip):
        try:
            proxy_handler = urllib2.ProxyHandler({'http': pip})
            opener = urllib2.build_opener(proxy_handler)
            opener.addheaders = [('User-agent', 'Mozilla/5.0')]
            urllib2.install_opener(opener)
            req=urllib2.Request('http://tweakers.net/pricewatch/352536/kingston-kta-mb1600s-4g/specificaties/')  # change the url address here
            sock=urllib2.urlopen(req)
        except urllib2.HTTPError, e:
            print 'Error code: ', e.code
            return e.code
        except Exception, detail:
            print "ERROR:", detail
            return 1
        return 0
"""
#Tor settings
class RandomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua  = random.choice(settings.USER_AGENT_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)

class TorProxyMiddleware(object):
    torMan = TorManager.TorManager()
    if not(torMan.newId()):
        torMan.newId()
    def process_request(self, request, spider):
        request.meta['proxy'] = settings.HTTP_PROXY

class RetryMiddlewareTor(RetryMiddleware):
    def process_response(self, request, response, spider):
        if response.status in [str(403)]:
            print ">>>exec \'killall -HUP tor\'"
            os.system("killall -HUP tor")
        return response
"""

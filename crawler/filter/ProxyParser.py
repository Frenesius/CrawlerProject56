__author__ = 'j'
class ProxyParser:
    proxyList = None
    def __init__(self):
        self.proxyList = self.getProxies()

    def getProxies(self):
        proxyList = []
        f = open("crawler/configs/proxy")
        for proxy in f:
            proxyList.append(str(proxy).replace("\n", ""))
        return proxyList
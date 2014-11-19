import ConfigParser
import json

class ParseLinks():
    def __init__(self):
        pass

    def parseLinks(self, linkString, amountInt):
        linkArray = []
        for x in range(1,amountInt):
            parsedLink = linkString+ str(x)
            linkArray.append(parsedLink)
        return linkArray

    def getLinks(self, configPath):
        links = []
        conf = ConfigParser.ConfigParser()
        conf.read(configPath)
        for x in range(1,100):
            a = "ROW"+str(x)
            if conf.has_section(a):
                crawl = conf.get(a, 'crawl')
                if crawl == "1":
                    links.append(x)
        return links

    def getCrawlLinks(self, path):
        links = []
        f = open('crawler/link-config/' + path, 'r')
        for line in f:
            links.append(line.strip("\n"))
        return links

    def printDebug(self, arr):
        for x in range(len(arr)):
            print arr[x]

    def getPriceConfigDict(self, path):
        json_data=open(path)
        a = json_data.readline()
        data = json.loads(a)
        json_data.close()
        return data

    def getPriceCrawlLinks(self, path):
        dict = self.getPriceConfigDict(path)
        LinksList = []
        for key, value in dict.iteritems():
            LinksList.append(str(key))
        return LinksList

    def getEANList(self, path):
        dict = self.getPriceConfigDict(path)
        EANList = []
        for key, value in dict.iteritems():
            EANList.append(str(value))
        return EANList
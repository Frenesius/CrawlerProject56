import ConfigParser
class ParseLinks():

    def __init__(self):
        pass

    def parseLinks(self, linkString, amountInt):
        linkArray = []
        print linkString
        print amountInt
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
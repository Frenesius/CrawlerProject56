import ConfigParser

__author__ = 'j'
class ParseConfig:
    xpathkey = None
    xpathvalue = None
    crawl = None
    crawlList = 0
    config = ConfigParser.ConfigParser()
    file = "crawler/crawl-conf/GPU.conf" #7

    try:
        config.read(file)
        xpathkey = config.get('DEFAULT', 'xpathkey')
        xpathvalue = config.get('DEFAULT', 'xpathvalue')
        crawl = config.get('DEFAULT', 'crawl')
    except:
        print "Something went wrong while reading the file: " + file

    def __init__(self):
        pass

    def sumSection(self):
        conf = self.config
        conf.read(self.file)

        sumCrawl = 0
        for x in range(1,100):
            a = "ROW"+str(x)
            if conf.has_section(a):
                crawl = conf.get(a, 'crawl')
                if crawl == "1":
                    sumCrawl += 1
        return sumCrawl

    def getCrawlList(self, filePath):
        try:
            conf = ConfigParser.ConfigParser()
            file = filePath
            conf.read(file)
        except:
            "CrawlList wrong"
        listCrawl = []
        for x in range(1,100):
            a = "ROW"+str(x)
            if conf.has_section(a):
                crawl = conf.get(a, 'crawl')
                if crawl == "1":
                    listCrawl.append(x)
        return listCrawl

    def getValuexPath(self, int, filePath):
        conf = ConfigParser.ConfigParser()
        file = filePath
        conf.read(file)

        if conf.has_option("ROW"+str(int), "xpathvalue"):
            customPath = conf.get("ROW"+str(int), "xpathvalue")
        else:
            customPath = conf.get("DEFAULT", "xpathvalue")
        return customPath

    def getKeyxPath(self, int, filePath):
        conf = ConfigParser.ConfigParser()
        file = filePath
        conf.read(file)

        if conf.has_option("ROW"+str(int), "xpathkey"):
            customPath = conf.get("ROW"+str(int), "xpathkey")
        else:
            customPath = conf.get("DEFAULT", "xpathkey")
        return customPath
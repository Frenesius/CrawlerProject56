import ConfigParser

__author__ = 'j'
class ParseConfig:
    xpathkey = None
    xpathvalue = None
    crawl = None
    crawlList = 0

    try:
        config = ConfigParser.ConfigParser()
        file = "../crawler/crawl-conf/GPU.conf" #7
        config.read(file)


        xpathkey = config.get('DEFAULT', 'xpathkey')
        xpathvalue = config.get('DEFAULT', 'xpathvalue')
        crawl = config.get('DEFAULT', 'crawl')
    except:
        print "Something went wrong while reading the file: " + file

    def getConfig(self):
        config = ConfigParser.ConfigParser()
        try:
            file = "../crawl-conf/GPU.conf" #7
            config.read(file)
        except:
            print "Something went wrong while reading the file: " + file

        return config

    def __init__(self):
        pass

    def sumSection(self):
        try:
            conf = ConfigParser.ConfigParser()
            file = "../crawl-conf/GPU.conf"
            conf.read(file)
        except:
            "sumSection Wrong"

        sumCrawl = 0
        for x in range(1,100):
            a = "ROW"+str(x)
            if conf.has_section(a):
                crawl = conf.get(a, 'crawl')
                if crawl == "1":
                    sumCrawl += 1
        return sumCrawl

    def getCrawlList(self):
        try:
            conf = ConfigParser.ConfigParser()
            file = "crawler/crawl-conf/GPU.conf"
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
p = ParseConfig()
p.getCrawlList()
import ConfigParser

__author__ = 'j'
class ParseConfig:
    xpathkey = None
    xpathvalue = None
    crawl = None
    crawlList = 0

    try:
        config = ConfigParser.ConfigParser()
        file = "crawl-conf/GPU.conf" #TODO fix exception
        config.read(file)

        xpathkey = config.get('DEFAULT', 'xpathkey')
        xpathvalue = config.get('DEFAULT', 'xpathvalue')
        crawl = config.get('DEFAULT', 'crawl')
    except:
        print "Something went wrong while reading the file: " + file

    def getConfig(self):
        config = ConfigParser.ConfigParser()
        try:
            file = "crawl-conf/GPU.conf" #TODO fix exception
            config.read(file)
        except:
            print "Something went wrong while reading the file: " + file

        return config

    def __init__(self):
        pass

    def sumSection(self):
        conf = ConfigParser.ConfigParser()
        file = "crawl-conf/GPU.conf"
        conf.read(file)

        sumCrawl = 0
        for x in range(1,100):
            a = "ROW"+str(x)
            if conf.has_section(a):
                crawl = conf.get(a, 'crawl')
                if crawl == "1":
                    sumCrawl += 1
        return sumCrawl


p = ParseConfig()

print p.sumSection()
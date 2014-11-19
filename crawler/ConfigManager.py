import ConfigParser

__author__ = 'j'
class ParseConfig:
    xpathkey = None
    xpathvalue = None
    crawl = None
    crawlList = 0
    config = ConfigParser.ConfigParser()
    file = "crawler/configs/GPU.conf" #7

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
        '''
        Gives the List back of the Sections (TableRows) that needs to be crawled.
        :param filePath: Path to the config file.
        :return: Array with the rows.
        '''
        try:
            conf = ConfigParser.ConfigParser()
            conf.read(filePath)
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

    def getxPathPriceCrawler(self, int, filePath):
        conf = ConfigParser.ConfigParser()
        file = filePath
        conf.read(file)
        pathDict = {
            'xpathshopname':None,
            'xpathshopscore':None,
            'xpathdelivery':None,
            'xpathbareprice':None,
            'xpathshopprice':None,
            'xpathclickout':None,
            }
        #####
        if conf.has_option("ROW"+str(int), "xpathshopname"):
            pathDict['xpathshopname'] = conf.get("ROW"+str(int), "xpathshopname")
        else:
            pathDict['xpathshopname'] = conf.get("DEFAULT", "xpathshopname")
        #####
        if conf.has_option("ROW"+str(int), "xpathshopscore"):
            pathDict['xpathshopscore'] = conf.get("ROW"+str(int), "xpathshopscore")
        else:
            pathDict['xpathshopscore'] = conf.get("DEFAULT", "xpathshopscore")
        #####
        if conf.has_option("ROW"+str(int), "xpathdelivery"):
            pathDict['xpathdelivery'] = conf.get("ROW"+str(int), "xpathdelivery")
        else:
            pathDict['xpathdelivery'] = conf.get("DEFAULT", "xpathdelivery")
        #####
        if conf.has_option("ROW"+str(int), "xpathbareprice"):
            pathDict['xpathbareprice'] = conf.get("ROW"+str(int), "xpathbareprice")
        else:
            pathDict['xpathbareprice'] = conf.get("DEFAULT", "xpathbareprice")
        #####
        if conf.has_option("ROW"+str(int), "xpathshopprice"):
            pathDict['xpathshopprice'] = conf.get("ROW"+str(int), "xpathshopprice")
        else:
            pathDict['xpathshopprice'] = conf.get("DEFAULT", "xpathshopprice")
        #####
        if conf.has_option("ROW"+str(int), "xpathclickout"):
            pathDict['xpathclickout'] = conf.get("ROW"+str(int), "xpathclickout")
        else:
            pathDict['xpathclickout'] = conf.get("DEFAULT", "xpathclickout")
        #####
        return pathDict
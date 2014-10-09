import scrapy
from scrapy import Spider
from crawler import ParseConfig
import Config as config

class MainSpider(scrapy.Spider):
    name = None
    pathName = None
    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None

    if name in config.componentList:
        print 1
        start_urls = config.componentList[name]
        print 2
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        print "PARSING #####################################"
        p = ParseConfig.ParseConfig()
        listCrawl = p.getCrawlList(self.path)
        print "SECTIONS FOUND: " + str(p.sumSection())

        for x in listCrawl:
            key = response.xpath(p.getKeyxPath(x, self.path) % x).extract()
            value= response.xpath(p.getValuexPath(x, self.path) % x ).extract()
            print "ROW",x, key, value
        print "DONE PARSING #####################################"
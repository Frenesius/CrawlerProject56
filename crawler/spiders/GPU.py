
import scrapy
from scrapy import Spider
from crawler import ParseConfig
import Config as config
import crawler.filter.FilterDict as filter
class GPU(scrapy.Spider):
    name = "GPUcrawl";
    pathName = "GPUpath"
    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None


    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        gpuDict = dict()

        print "         PARSING"
        p = ParseConfig.ParseConfig()
        listCrawl = p.getCrawlList(self.path)
        print "         SECTIONS FOUND: " + str(p.sumSection())

        for x in listCrawl:
            key = response.xpath(p.getKeyxPath(x, self.path) % x).extract()
            value= response.xpath(p.getValuexPath(x, self.path) % x ).extract()

            gpuDict.update({str(key): str(value)})

        print "         DONE PARSING"
        print "         Parsing Dict"
        filter.FilterDict().printDict(filter.FilterDict().getDict(gpuDict))
        print "         SUCCESS"







'''
import scrapy

from crawler import ParseConfig
from crawler.templates import GenericSpider
import Config as config

class CPU(scrapy.Spider):
    name = "CPUcrawl"
    pathName = "CPUpath"

    allowed_domains = ["tweakers.net"]
    start_urls = []
    path = None

    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        p = ParseConfig.ParseConfig()
        listCrawl = p.getCrawlList(self.path)
        print "SECTIONS FOUND: " + str(p.sumSection())
        for x in listCrawl:

            key = response.xpath(p.getKeyxPath(x, self.path) % x).extract()
            value= response.xpath(p.getValuexPath(x, self.path) % x ).extract()
            print "ROW",x, key, value
'''
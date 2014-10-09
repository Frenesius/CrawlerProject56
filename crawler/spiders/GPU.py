import scrapy
from scrapy import Spider
from crawler import ParseConfig


class GPU(scrapy.Spider):
    name = "GPUcrawl";
    allowed_domains = ["tweakers.net"]
    start_urls = ["http://tweakers.net/pricewatch/416125/msi-geforce-gtx-970-gaming-4g/specificaties/"]

    def parse(self, response):
        p = ParseConfig.ParseConfig()
        listCrawl = p.getCrawlList()
        print "SECTIONS FOUND: " + str(p.sumSection())
        for x in listCrawl:

            key = response.xpath(p.getKeyxPath(x) % x).extract()
            value= response.xpath(p.getValuexPath(x) % x ).extract()
            print key, value


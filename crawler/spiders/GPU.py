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

        print "SECTIONS FOUND: " + p.sumSection()
        for x in listCrawl:
            key = response.xpath("//*[@id='tab:specificaties']/table/tr["+str(x)+"]/td[1]/text()").extract()
            value= response.xpath("//*[@id='tab:specificaties']/table/tr["+str(x)+"]/td[2]/text()").extract()
            print key, value


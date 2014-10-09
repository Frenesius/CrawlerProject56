import scrapy
from scrapy import Spider
from crawler import ParseConfig


class GPU(scrapy.Spider):
    name = "GPUcrawl";
    allowed_domains = ["tweakers.net"]
    start_urls = ["http://tweakers.net/pricewatch/416125/msi-geforce-gtx-970-gaming-4g/specificaties/"]

    def parse(self, response):
        p = ParseConfig.ParseConfig()
        listCrawl = p.getCrawlList("crawler/crawl-conf/GPU.conf")
        print "SECTIONS FOUND: " + str(p.sumSection())
        for x in listCrawl:

            key = response.xpath(p.getKeyxPath(x, "crawler/crawl-conf/GPU.conf") % x).extract()
            value= response.xpath(p.getValuexPath(x, "crawler/crawl-conf/GPU.conf") % x ).extract()
            print "ROW",x, key, value


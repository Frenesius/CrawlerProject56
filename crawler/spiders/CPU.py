__author__ = 'j'
import scrapy
from scrapy import Spider
from crawler import ParseConfig


class CPU(scrapy.Spider):
    name = "CPUcrawl";
    allowed_domains = ["tweakers.net"]
    start_urls = [""]

    def parse(self, response):
        p = ParseConfig.ParseConfig()
        listCrawl = p.getCrawlList()

        for x in listCrawl:
            key = response.xpath("//*[@id='tab:specificaties']/table/tr["+str(x)+"]/td[1]/text()").extract() #
            value= response.xpath("//*[@id='tab:specificaties']/table/tr["+str(x)+"]/td[2]/text()").extract()   #
            print key, value

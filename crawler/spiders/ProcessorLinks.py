import scrapy
from scrapy import Spider
import re
from crawler.filter.LinkManager import ParseLinks

class ProcessorLinks(scrapy.Spider):
    name = "CPUlinks"
    linkString =  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    processorArr = []

    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 27)
    allowed_domains = ["tweakers.net"]


    def parse(self, response,):
        for x in range(1,101):
            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            pattern = r"(\[\])"
            if re.search(pattern, str(url)):
                continue
            else:
                self.processorArr.append(url)

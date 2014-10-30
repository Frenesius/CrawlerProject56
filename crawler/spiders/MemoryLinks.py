import re
import scrapy
from crawler.filter.ParseLinks import ParseLinks
from scrapy import Spider

class MemoryLinks(scrapy.Spider):
    name = "RAMlinks";
    linkString ='http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    ramArr = []

    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 48)
    allowed_domains = ["tweakers.net"]


    def parse(self, response,):
        for x in range(1,101):
            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            pattern = r"(\[\])"
            if re.search(pattern, str(url)):
                continue
            else:
                self.ramArr.append(url)

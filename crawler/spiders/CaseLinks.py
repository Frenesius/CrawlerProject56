import scrapy
from scrapy import Spider
import re
from crawler.filter.LinkManager import ParseLinks

class CaseLinks(scrapy.Spider):
    name = "CASElinks";
    linkString = 'http://tweakers.net/categorie/61/behuizingen/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    caseArr = []

    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 16)
    allowed_domains = ["tweakers.net"]


    def parse(self, response,):
        for x in range(1,101):
            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            pattern = r"(\[\])"
            if re.search(pattern, str(url)):
                continue
            else:
                self.caseArr.append(url)

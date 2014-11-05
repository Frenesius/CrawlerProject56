import re
import scrapy
from crawler.filter.LinkManager import ParseLinks


class LinkSpider(scrapy.Spider):
    name = " "
    linkString = ' '
    linksArr = []
    start_urls = None
    allowed_domains = ["tweakers.net"]

    def parse(self, response,):
        self.altParse(response)
        
    def altParse(self, response):
        for x in range(1,101):
            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            pattern = r"(\[\])"
            if re.search(pattern, str(url)):
                continue
            else:
                self.linksArr.append(url)
    print len(linksArr)

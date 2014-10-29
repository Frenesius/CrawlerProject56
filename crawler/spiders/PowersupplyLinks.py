import scrapy
from scrapy import Spider
import re
from crawler.filter.ParseLinks import ParseLinks

class PowersupplyLinks(scrapy.Spider):
    name = "PSUlinks";
    linkString = 'http://tweakers.net/categorie/664/voedingen/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    powerArr = []

    a = ParseLinks()
    start_urls = a.parseLinks(linkString, 16)
    allowed_domains = ["tweakers.net"]


    def parse(self, response,):

        print "start PARSING #####################################"
        for x in range(1,101):

            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            pattern = r"(\[\])"
            if re.search(pattern, str(url)):
                continue
            else:
                print url
                self.powerArr.append(url)

        print "DONE PARSING #####################################"
        print len(self.powerArr)
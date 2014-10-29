import scrapy
from scrapy import Spider
import re
from crawler.filter.ParseLinks import ParseLinks

class MotherboardLinks(scrapy.Spider):
    name = "MBlinks"
    linkString = 'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    motherboardArr = []

    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 12)
    allowed_domains = ["tweakers.net"]



    def parse(self, response,):

        print "start PARSING #####################################" #
        for x in range(1,101):
            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            pattern = r"(\[\])"
            if re.search(pattern, str(url)):
                continue
            else:
                print url #
                self.motherboardArr.append(url)

        print "DONE PARSING #####################################" #
        print len(self.motherboardArr) #
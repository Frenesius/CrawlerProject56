import scrapy
from scrapy import Spider

class MBxpath(scrapy.Spider):
    name = "MBlinks";
    start_urls = ['http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=1',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=2',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=3',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=4',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=5',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=6',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=7',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=8',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=9',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=10',
'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=11'







    ]
    allowed_domains = ["tweakers.net"]


    def parse(self, response):

        print "start PARSING #####################################"
        for x in range(1,101):
            print x
            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            print url

        print "DONE PARSING #####################################"
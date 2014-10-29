import scrapy
from scrapy import Spider
import re
class ProcessorLinks(scrapy.Spider):
    name = "CPUlinks";
    start_urls = ['http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=1',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=2',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=3',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=4',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=5',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=6',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=7',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=8',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=9',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=10',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=11',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=12',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=13',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=14',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=15',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=16',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=17',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=18',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=19',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=20',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=21',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=22',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=23',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=24',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=25',
                  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=26'





    ]
    allowed_domains = ["tweakers.net"]


    processorArr = []
    def parse(self, response,):

        print "start PARSING #####################################"
        for x in range(1,101):

            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            pattern = r"(\[\])"
            if re.search(pattern, str(url)):
                continue
            else:
                print url
                self.processorArr.append(url)

        print "DONE PARSING #####################################"
        print len(self.processorArr)
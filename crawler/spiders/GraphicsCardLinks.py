import scrapy
from scrapy import Spider
import re

class GraphicsCardLinks(scrapy.Spider):
    name = "GPUlinks";
    start_urls = ['http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=1',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=2',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=3',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=4',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=5',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=6',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=7',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=8',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=9',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=10',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=11',
                  'http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=12'




    ]
    allowed_domains = ["tweakers.net"]


    graphicsArr = []
    def parse(self, response,):

        print "start PARSING #####################################"
        for x in range(1,101):

            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            pattern = r"(\[\])"
            if re.search(pattern, str(url)):
                continue
            else:
                print url
                self.graphicsArr.append(url)

        print "DONE PARSING #####################################"
        print len(self.graphicsArr)
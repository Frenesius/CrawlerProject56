import scrapy
from scrapy import Spider

class RAMxpath(scrapy.Spider):
    name = "RAMlinks";
    start_urls = ['http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=1',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=2',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=3',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=4',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=5',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=6',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=7',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=8',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=9',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=10',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=11',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=12',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=13',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=14',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=15',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=16',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=17',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=18',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=19',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=20',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=21',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=22',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=23',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=24',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=25',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=26',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=27',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=28',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=29',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=30',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=31',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=32',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=33',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=34',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=35',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=36',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=37',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=38',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=39',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=40',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=41',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=42',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=43',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=44',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=45',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=46',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=47',
'http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page=48'






    ]
    allowed_domains = ["tweakers.net"]


    def parse(self, response):

        print "start PARSING #####################################"
        for x in range(1,101):
            print x
            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            print url

        print "DONE PARSING #####################################"
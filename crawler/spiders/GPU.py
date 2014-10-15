
import scrapy
from scrapy import Spider
from crawler import ParseConfig
import Config as config
import crawler.filter.FilterDict as filter
from crawler.neo4jdb import connection

class GPU(scrapy.Spider):
    name = "GPUcrawl";
    pathName = "GPUpath"
    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None


    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        '''
        Parses the crawled data into dictionary
        :param response: Response from Scrapy spider
        :return: None
        '''
        gpuDict = dict()

        print "         PARSING"
        p = ParseConfig.ParseConfig()
        listCrawl = p.getCrawlList(self.path)
        print "         SECTIONS FOUND: " + str(p.sumSection())

        for x in listCrawl:
            key = response.xpath(p.getKeyxPath(x, self.path) % x).extract()
            value= response.xpath(p.getValuexPath(x, self.path) % x ).extract()

            gpuDict.update({str(key).encode('ascii', errors='ignore'): str(value).encode('ascii', errors='ignore')})

        print "         DONE PARSING"
        print "         Parsing Dict"
        filter.FilterDict().filterDictionary(gpuDict)
        print "         SUCCESS"


        print "=====DEBUG======="

        '''
        Connect to DB and add a dict as node
        '''
        conn = connection.connection()
        conn.openDb()

        print "Reading the config: %s" % conn.isRead
        print "Database connection: %s" % conn.isConnect
        print "=====DEBUG======="







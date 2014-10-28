
import scrapy
from scrapy import Spider
from crawler import ParseConfig
import Config as config
import crawler.filter.FilterDict as filter
from crawler.neo4jdb import connection
from py2neo import neo4j, cypher, rel, node
import py2neo


class GPU(scrapy.Spider):
    name = "GPUcrawl";
    label = "GRAPHICSCARD"
    pathName = "GPUpath"
    relation = "GRAPHICSCARD"
    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None
    filteredDict = {}

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
        print "== Initializing =="
        conn = connection.connection()              #initiates connection
        graph_db = conn.openDb()

        nodeDict = dict()

        baseNode = conn.getNode(graph_db, self.label)
        baseNode.get_properties()
        baseNode.get_labels()

        print "\tParsing config"
        p = ParseConfig.ParseConfig()
        listCrawl = p.getCrawlList(self.path)
        print "\t\tSections Found: " + str(p.sumSection())

        for x in listCrawl:
            key = response.xpath(p.getKeyxPath(x, self.path) % x).extract()
            value= response.xpath(p.getValuexPath(x, self.path) % x ).extract()

            nodeDict.update({str(key): str(value)})

        print "\tDone parsing config"
        print "\tParsing Dict"
        self.filteredDict = filter.FilterDict().filterDictionary(nodeDict)
        print "\tDone Parsing Dict"


        print "== Adding Node to database =="
        print "\tReading the config: %s" % conn.isRead
        print "\tDatabase connection: %s" % conn.isConnect


        crawlNode, = graph_db.create(self.filteredDict)  #Creates Node
        crawlNode.add_labels(str(self.label))            #Adds label to the Node
        graph_db.create(rel(crawlNode, self.relation, baseNode))  #Created Relationship

        print "== Done :) =="







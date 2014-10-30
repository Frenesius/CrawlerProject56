
import scrapy
from crawler import ConfigManager
import Config as config
import crawler.filter.DictManager as filter
from crawler.neo4jdb import Neo4jDatabaseManager
from py2neo import rel, node


class GraphicsCardSpider(scrapy.Spider):
    '''
    Always include
        - name          The name of the crawler -> used for crawling i.e ```scrapy crawl name```
        - label         Label to get the BaseNode and give the relation the label
        - pathName      Name of the config files
        - relation      Relation name

    '''
    name = "GPUcrawl";          #name to crawl
    label = "GRAPHICSCARD"      #Label in database
    pathName = "GPUpath"        #
    relation = "GRAPHICSCARD"   #

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
        conn = Neo4jDatabaseManager.DatabaseConnectionNeo4j()              #initiates connection
        graph_db = conn.openDb()

        nodeDict = dict()

        baseNode = conn.getNode(graph_db, self.label)
        baseNode.get_properties()
        baseNode.get_labels()

        print "\tParsing config"
        p = ConfigManager.ParseConfig()
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
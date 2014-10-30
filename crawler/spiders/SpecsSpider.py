
import scrapy
from crawler import ConfigManager
import Config as config
import crawler.filter.DictManager as filter
from crawler.neo4jdb import Neo4jDatabaseManager
from py2neo import rel, node

class SpecsSpider(scrapy.Spider):
    '''
    Always include
        - name          The name of the crawler -> used for crawling i.e ```scrapy crawl name```
        - label         Label to get the BaseNode and give the relation the label
        - pathName      Name of the config files
        - relation      Relation name

    '''
    name = None           #name to craw, gets used to get the start_urls[]
    label = None      #Name of the Label that needs to be added to the Crawled Node
    pathName = None        #Used to get ConfigFile
    relation = None   #Name of the relation between the BaseNode and Crawled Node

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
        Parses the crawled data.
        Puts data in a Dict. Filters Dict. Creates Node. Adds label. Creates Relationships.
        :param response: Response from Scrapy spider
        :return: None
        '''
        print "== Initializing =="
        conn = Neo4jDatabaseManager.DatabaseConnectionNeo4j()               #initiates connection
        graph_db = conn.openDb()                                            #initiates connection

        nodeDict = dict()                                                   #Makes a dictionary for the node

        baseNode = conn.getNode(graph_db, self.label)                       #Gets the BaseNode from the database
        baseNode.get_properties()                                           #Need to ask for properties to use the BaseNode (Workaround)
        baseNode.get_labels()                                               #Need to ask for labels to use the BaseNode (Workaround)

        print "\tParsing config"
        configManager = ConfigManager.ParseConfig()                                     #Gets the config and fills the variables
        listCrawl = configManager.getCrawlList(self.path)                               #A list with all the xpaths
        print "\t\tSections Found: " + str(configManager.sumSection())                  #Shows how many Sections are found in the Config.

        for x in listCrawl:
            key = response.xpath(configManager.getKeyxPath(x, self.path) % x).extract()         #Gets the key from the source. xPath is from the config.
            value= response.xpath(configManager.getValuexPath(x, self.path) % x ).extract()     #Gets the value from the source. xPath is from the config.
            nodeDict.update({str(key): str(value)})                                             #Adds Key:Value to the dict.
        print "\tDone parsing config"

        print "\tParsing Dict"
        self.filteredDict = filter.FilterDict().filterDictionary(nodeDict)          #Filters the dict on empty values, '/xa0s' values and unicode.
        print "\tDone Parsing Dict"

        print "== Adding Node to database =="
        print "\tReading the config: %s" % conn.isRead
        print "\tDatabase connection: %s" % conn.isConnect

        crawlNode, = graph_db.create(self.filteredDict)                     #Creates Node.
        crawlNode.add_labels(str(self.label))                               #Adds label to the Node.
        graph_db.create(rel(crawlNode, self.relation, baseNode))            #Creates Relationship.

        print "== Done :) =="
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
    name = "SOUNDCARDprice"           #Name to craw, gets used to get the start_urls[]
    #label = None          #Name of the Label that needs to be added to the Crawled Node
    pathName = "SOUNDCARDpath"      #Used to get ConfigFile
    relation = None       #Name of the relation between the BaseNode and Crawled Node
    arrEanIdentifier = "SOUNDCARDEAN"
    start_urls = []
    allowed_domains = ["tweakers.net"]
    path = None
    JSONpath = "crawler/price-config/SOUNDCARD.json"
    filteredDict = {}
    arrEan = []
    y = -1

    if name in config.price_configs:
        start_urls = config.price_configs[name]
        path = config.price_configs[pathName]
        arrEan = config.price_configs[arrEanIdentifier]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        '''
        Parses the crawled data.
        Puts data in a Dict. Filters Dict. Creates Node. Adds label. Creates Relationships.
        :param response: Response from Scrapy spider
        :return: None
        '''
        self.parseSource(response)

    def parseSource(self, response):
        print "START"
        print "== Initializing =="
        self.y += 1
        nodeEAN = None
        conn = Neo4jDatabaseManager.DatabaseConnectionNeo4j()               #initiates connection
        graph_db = conn.openDb()                                            #initiates connection

        nodeDict = dict()                                                   #Makes a dictionary for the node
        #Try to get shopname node, fails? create
        # baseNode = conn.getNode(graph_db, self.label)                       #Gets the BaseNode from the database
        # baseNode.get_properties()                                           #Need to ask for properties to use the BaseNode (Workaround)
        # baseNode.get_labels()                                               #Need to ask for labels to use the BaseNode (Workaround)

        print "\tParsing config"
        configManager = ConfigManager.ParseConfig()                                     #Gets the config and fills the variables
        listCrawl = configManager.getCrawlList(self.path)                               #A list with all the xpaths

        print "\t\tSections Found: " + str(configManager.sumSection())                  #Shows how many Sections are found in the Config.

        for x in listCrawl:

            tempDict = configManager.getxPathPriceCrawler(x, self.path)
            xpathshopname = response.xpath(str(tempDict['xpathshopname']% x)).extract()
            xpathshopscore = response.xpath(str(tempDict['xpathshopscore']% x)).extract()
            xpathdelivery = response.xpath(str(tempDict['xpathdelivery']% x)).extract()
            xpathbareprice = response.xpath(str(tempDict['xpathbareprice']% x)).extract()
            xpathshopprice = response.xpath(str(tempDict['xpathshopprice']% x)).extract()
            xpathclickout = response.xpath(str(tempDict['xpathclickout']% x)).extract()

            nodeDict["xpathshopname"] = xpathshopname,
            nodeDict["xpathshopscore"] = xpathshopscore,
            nodeDict["xpathdelivery"] = xpathdelivery,
            nodeDict["xpathbareprice"] = xpathbareprice,
            nodeDict["xpathshopprice"] = xpathshopprice,
            nodeDict["xpathclickout"] = xpathclickout,
            nodeDict["EAN"] = self.arrEan[self.y]

            if filter.FilterDict().checkEmptyDicts(nodeDict) == True:
                pass
            else:
                self.filteredDict = filter.FilterDict().filterUnicode(nodeDict)
                print "====================================="
                print self.filteredDict



        print "\tDone parsing config"

        self.filteredDict = filter.FilterDict().filterUnicode(nodeDict)          #Filters the dict on empty values, '/xa0s' values and unicode.
        print "\tDone Parsing Dict"

        print "== Adding Node to database =="
        print "\tReading the config: %s" % conn.isRead
        print "\tDatabase connection: %s" % conn.isConnect
        print self.filteredDict
        print "== Done :) =="
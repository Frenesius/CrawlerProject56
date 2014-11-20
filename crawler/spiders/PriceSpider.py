import scrapy
from crawler import ConfigManager
import Config as config
import crawler.filter.DictManager as filter
from crawler.dbmanager import Neo4jDatabaseManager
from crawler.dbmanager import MySqlManager
from py2neo import rel, node
import time
import MySQLdb

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
    arrEanIdentifier = "SOUNDCARDEAN"
    relation = None       #Name of the relation between the BaseNode and Crawled Node

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
        print "== Initializing =="
        self.y += 1
        conn = Neo4jDatabaseManager.DatabaseConnectionNeo4j()               #initiates connection
        graph_db = conn.openDb()                                            #initiates connection
        nodeDict = dict()                                                   #Makes a dictionary for the node

        print "\tParsing config"
        configManager = ConfigManager.ParseConfig()                                     #Gets the config and fills the variables
        listCrawl = configManager.getCrawlList(self.path)                               #A list with all the xpaths

        for x in listCrawl:
            tempDict = configManager.getxPathPriceCrawler(x, self.path)
            nodeDict["xpathshopname"] = response.xpath(str(tempDict['xpathshopname']% x)).extract()
            nodeDict["xpathshopscore"] = response.xpath(str(tempDict['xpathshopscore']% x)).extract()
            nodeDict["xpathdelivery"] = response.xpath(str(tempDict['xpathdelivery']% x)).extract()
            nodeDict["xpathbareprice"] = response.xpath(str(tempDict['xpathbareprice']% x)).extract()
            nodeDict["xpathshopprice"] = response.xpath(str(tempDict['xpathshopprice']% x)).extract()
            nodeDict["xpathclickout"] = response.xpath(str(tempDict['xpathclickout']% x)).extract()
            nodeDict["EAN"] = self.arrEan[self.y]

            if filter.FilterDict().checkEmptyDicts(nodeDict) == True:
                pass
            else:
                self.filteredDict = filter.FilterDict().filterPriceDict(nodeDict)
                print self.filteredDict
                componentNode = conn.getNodeByEAN(graph_db, str(nodeDict["EAN"]))         #Gets the BaseNode from the database
                componentNode.get_properties()                                            #Need to ask for properties to use the BaseNode (Workaround)
                componentNode.get_labels()                                                #Need to ask for labels to use the BaseNode (Workaround)
                try:
                    shopNode = conn.getNodeByName(graph_db, str(nodeDict["xpathshopname"]))
                    shopNode.get_properties()                                             #Need to ask for properties to use the BaseNode (Workaround)
                    shopNode.get_labels()                                                 #Need to ask for labels to use the BaseNode (Workaround)
                except:
                    print "Shop not found!\nCreating new shop."

                    graph_db.create({"name": str(nodeDict["xpathshopname"])})
                    newShop = conn.getNodeByName(graph_db, str(nodeDict["xpathshopname"]))
                    newShop.add_labels("SHOP", str(nodeDict["xpathshopname"]))
                try:
                    shopNode = conn.getNodeByEAN(graph_db, str(nodeDict["EAN"]))
                    shopNode.get_properties()                                           #Need to ask for properties to use the BaseNode (Workaround)
                    shopNode.get_labels()                                               #Need to ask for labels to use the BaseNode (Workaround)
                except:
                    print "!! ShopNode not found !!"


























        print "\tDone parsing config"

        print "\tDone Parsing Dict"

        print "== Adding Node to database =="
        print "\tReading the config: %s" % conn.isRead
        print "\tDatabase connection: %s" % conn.isConnect
        print "== Done :) =="
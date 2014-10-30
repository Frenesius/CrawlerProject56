__author__ = 'j'
import Config as config
import SpecsSpider

class GraphicsCardSpider(SpecsSpider.SpecsSpider):
    name = "GPUcrawl"           #name to craw, gets used to get the start_urls[]
    label = "GRAPHICSCARD"      #Name of the Label that needs to be added to the Crawled Node
    pathName = "GPUpath"        #Used to get ConfigFile
    relation = "GRAPHICSCARD"   #Name of the relation between the BaseNode and Crawled Node
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response)

class ProcessorSpider(SpecsSpider.SpecsSpider):
    name = "PROCESSORcrawl"           #name to craw, gets used to get the start_urls[]
    label = "PROCESSOR"      #Name of the Label that needs to be added to the Crawled Node
    pathName = "PROCESSORpath"        #Used to get ConfigFile
    relation = "PROCESSOR"   #Name of the relation between the BaseNode and Crawled Node
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response)

class MemorySpider(SpecsSpider.SpecsSpider):
    name = "MEMORYcrawl"           #name to craw, gets used to get the start_urls[]
    label = "MEMORY"      #Name of the Label that needs to be added to the Crawled Node
    pathName = "MEMORYpath"        #Used to get ConfigFile
    relation = "MEMORY"   #Name of the relation between the BaseNode and Crawled Node
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response)

class PSUSpider(SpecsSpider.SpecsSpider):
    name = "PSUcrawl"           #name to craw, gets used to get the start_urls[]
    label = "PSU"      #Name of the Label that needs to be added to the Crawled Node
    pathName = "PSUpath"        #Used to get ConfigFile
    relation = "PSU"   #Name of the relation between the BaseNode and Crawled Node
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response)

class MotherboardSpider(SpecsSpider.SpecsSpider):
    name = "MOTHERBOARDcrawl"           #name to craw, gets used to get the start_urls[]
    label = "MOTHERBOARD"      #Name of the Label that needs to be added to the Crawled Node
    pathName = "MOTHERBOARDpath"        #Used to get ConfigFile
    relation = "MOTHERBOARD"   #Name of the relation between the BaseNode and Crawled Node
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response)

class CaseSpider(SpecsSpider.SpecsSpider):
    name = "CASEcrawl"           #name to craw, gets used to get the start_urls[]
    label = "CASE"               #Name of the Label that needs to be added to the Crawled Node
    pathName = "CASEpath"        #Used to get ConfigFile
    relation = "CASE"            #Name of the relation between the BaseNode and Crawled Node
    start_urls = []
    if name in config.componentList:
        start_urls = config.componentList[name]
        path = config.componentList[pathName]
    else:
        print("ERROR: key does not exist in dictonairy")

    def parse(self, response):
        SpecsSpider.SpecsSpider.parseSource(self, response)
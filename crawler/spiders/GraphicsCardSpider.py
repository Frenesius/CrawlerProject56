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
        SpecsSpider.SpecsSpider.testParse(self, response)
import SpecsSpider


class GraphicsCardSpider(SpecsSpider.SpecsSpider):
    '''
    Always include
        - name          The name of the crawler -> used for crawling i.e ```scrapy crawl name```
        - label         Label to get the BaseNode and give the relation the label
        - pathName      Name of the config files
        - relation      Relation name

    '''
    name = "GPUcrawl"           #name to craw, gets used to get the start_urls[]
    label = "GRAPHICSCARD"      #Name of the Label that needs to be added to the Crawled Node
    pathName = "GPUpath"        #Used to get ConfigFile
    relation = "GRAPHICSCARD"   #Name of the relation between the BaseNode and Crawled Node


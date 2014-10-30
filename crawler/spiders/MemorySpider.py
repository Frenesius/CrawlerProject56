__author__ = 'j'
import SpecsSpider
class MemorySpider(SpecsSpider.SpecsSpider):
    '''
    Always include
        - name          The name of the crawler -> used for crawling i.e ```scrapy crawl name```
        - label         Label to get the BaseNode and give the relation the label
        - pathName      Name of the config files
        - relation      Relation name

    '''
    name = "MEMORYcrawl"              #name to craw, gets used to get the start_urls[]
    label = "MEMORY"                   #Label in database
    pathName = "MEMORYpath"            #Used to get ConfigFile
    relation = "MEMORY"                #
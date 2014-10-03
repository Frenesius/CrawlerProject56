'''
Created on 30 Sep 2014

@author: j
'''
import scrapy

class GraphicsCard(scrapy.Item):

    key = scrapy.Field();
    value = scrapy.Field();



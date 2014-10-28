
import scrapy
from scrapy import Spider
from crawler import ParseConfig
import Config as config
import crawler.filter.FilterDict as filter
from crawler.neo4jdb import connection
from py2neo import neo4j, cypher, rel, node
import py2neo
import GPU


class CPU(GPU.GPU):
    name = "GPUcrawl";
    label = "CPU"
    pathName = "CPUpath"
    relation = "CPU"


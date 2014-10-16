__author__ = 'j'
from ConfigParser import SafeConfigParser
from py2neo import *
from py2neo import neo4j, cypher
from crawler.spiders import Config

class connection:
    '''
    Copied from github.com/Jiar/Neo4joctolove repo
    Configure database. Add Delete Modify

    '''
    url = None
    username = None
    password = None
    isRead = False
    isConnect = False
    db_path = "db_path"

#Get Data from db_config.conf
    parser = SafeConfigParser()
    try:
        parser.read('crawler/configs/db_config.conf')   #Defines Path
    except:
        print "Cannot open file \"db_config.conf\". Probably wrong path."

    url = parser.get('DATABASE', 'url')
    username = parser.get('DATABASE', 'username')
    password = parser.get('DATABASE', 'password')
    isRead = True

    def __init__(self):
        pass

    def openDb(self):
        graph_db = neo4j.GraphDatabaseService(self.url)
        self.isConnect = True
        return graph_db

    def closeDb(self):
        pass

    def getSomeData(self, graph_db):
        print graph_db.get_node(0)

    def getCountNodes(self, graph_db):
        print graph_db.get_node_count()

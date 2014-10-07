import ConfigParser
__author__ = 'j'
class ParseConfig:
    xpathkey = None
    xpathvalue = None
    crawl = None


    config = ConfigParser.ConfigParser()
    try:
        file = "crawl-conf/GPU.conf" #TODO fix exception
        config.read(file)
    except:
        print "Something went wrong while reading the file: " + file

    xpathkey = config.get('DEFAULT', 'xpathkey')
    xpathvalue = config.get('DEFAULT', 'xpathvalue')
    crawl = config.get('DEFAULT', 'crawl')

    for x in range(0, 33):
        print xpathkey % x
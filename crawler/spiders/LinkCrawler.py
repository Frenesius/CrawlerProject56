import LinkSpider
from crawler.filter.LinkManager import ParseLinks
class CaseLinks(LinkSpider.LinkSpider):
    name = "CASElinks"
    linksConf = "CASELink"
    linkString = 'http://tweakers.net/categorie/61/behuizingen/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 16)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class MotherboardLinks(LinkSpider.LinkSpider):
    name = "MBlinks"
    linksConf = "MOTHERBOARDLink"
    linkString = 'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 12)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class MemoryLinks(LinkSpider.LinkSpider):
    name = "RAMlinks"
    linksConf = "MEMORYLink"
    linkString ='http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 48)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class GrapihcsCardLinks(LinkSpider.LinkSpider):
    name = "GPUlinks"
    linksConf = "GPULink"
    linkString ='http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 12)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class ProcessorLinks(LinkSpider.LinkSpider):
    name = "CPUlinks"
    linksConf = "CPULink"
    linkString =  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 27)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)

class PowerSupplyLinks(LinkSpider.LinkSpider):
    name = "PSUlinks"
    linksConf = "PSULink"
    linkString = 'http://tweakers.net/categorie/664/voedingen/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 16)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response, self.linksConf)


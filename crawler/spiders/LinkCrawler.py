import LinkSpider
from crawler.filter.LinkManager import ParseLinks
class CaseLinks(LinkSpider.LinkSpider):
    name = "CASElinks"
    linkString = 'http://tweakers.net/categorie/61/behuizingen/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 16)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response)

class MotherboardLinks(LinkSpider.LinkSpider):
    name = "MBlinks"
    linkString = 'http://tweakers.net/categorie/47/moederborden/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 12)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response)

class MemoryLinks(LinkSpider.LinkSpider):
    name = "RAMlinks"
    linkString ='http://tweakers.net/categorie/545/geheugen-intern/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 48)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response)

class GrapihcsCardLinks(LinkSpider.LinkSpider):
    name = "GPUlinks"
    linkString ='http://tweakers.net/categorie/49/videokaarten/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 12)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response)

class ProcessorLinks(LinkSpider.LinkSpider):
    name = "CPUlinks"
    linkString =  'http://tweakers.net/categorie/46/processors/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 27)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response)

class PowerSupplyLinks(LinkSpider.LinkSpider):
    name = "PSUlinks"
    linkString = 'http://tweakers.net/categorie/664/voedingen/producten/?currFilters=q1YqSExPDc6sSlWyMjQwqAUA&pageSize=100&page='
    parseLinks = ParseLinks()
    start_urls = parseLinks.parseLinks(linkString, 16)
    allowed_domains = ["tweakers.net"]
    def parse(self, response,):
        LinkSpider.LinkSpider().altParse(response)


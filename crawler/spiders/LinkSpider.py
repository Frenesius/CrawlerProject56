import re
import scrapy
import crawler.filter.DictManager as DictMan

class LinkSpider(scrapy.Spider):
    name = " "
    linkString = None
    linksArr = []
    start_urls = None
    allowed_domains = ["tweakers.net"]

    def parse(self, response,):
        self.altParse(response, None)
        
    def altParse(self, response, linksConf1):
        for x in range(1,101):
            url = response.xpath('//*[@id="compareProductListing"]/table/tr[%s]/td[3]/p[2]/a/@href' % x).extract()
            pattern = r"(\[\])"
            if re.search(pattern, str(url)):
                continue
            else:
                self.linksArr.append(url)
        dictManager = DictMan.FilterDict()
        filteredArr = dictManager.filterArrUnicode(self.linksArr)

        f = open('crawler/link-config/' + linksConf1, 'w')
        for x in range(len(filteredArr)):
            f.write(str(filteredArr[x]) + "\n")
        f.close()


import re
import scrapy


class LinkSpider(scrapy.Spider):
    name = " "
    linkString = " "
    linksConf1 = " "
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
        f = open('crawler/link-config/' + linksConf1, 'w')
        for x in range(len(self.linksArr)):
            f.write(str(self.linksArr[x]) + "\n")
        f.close()
    print len(linksArr)


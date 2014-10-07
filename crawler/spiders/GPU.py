import scrapy
from scrapy import Spider


class GPU(scrapy.Spider):
    name = "GPUtest";
    allowed_domains = ["tweakers.net"]
    start_urls = ["http://tweakers.net/pricewatch/416125/msi-geforce-gtx-970-gaming-4g/specificaties/"]

    def parse(self, response):
        key = response.xpath("//*[@id='tab:specificaties']/table/tr[13]/td[1]/text()").extract()
        value= response.xpath("//*[@id='tab:specificaties']/table/tr[13]/td[2]/text()").extract()

        print key, value
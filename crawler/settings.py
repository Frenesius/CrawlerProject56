import crawler.filter.LinkManager as man
# -*- coding: utf-8 -*-

# Scrapy settings for tutorial project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#


BOT_NAME = 'crawler'

SPIDER_MODULES = ['crawler.spiders']
NEWSPIDER_MODULE = 'crawler.spiders'
DOWNLOAD_DELAY = man.ParseLinks().randomDelay(1,15)          #Proxy delay is already 3 seconds, not needed
COOKIES_ENABLED = False

# DOWNLOADER_MIDDLEWARES = {
#     'scrapy.contrib.downloadermiddleware.httpproxy.HttpProxyMiddleware': 110,
#     'crawler.middlewares.ProxyMiddleware': 100,
# }
# Retry many times since proxies often fail
RETRY_TIMES = 10000
# Retry on most error codes since proxies fail for different reasons
RETRY_HTTP_CODES = [500, 503, 504, 400, 403, 408]

#LOG_LEVEL = "INFO"
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tutorial (+http://www.yourdomain.com)'


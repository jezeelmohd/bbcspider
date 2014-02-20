# Scrapy settings for bbc project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'bbc'

SPIDER_MODULES = ['bbc.spiders']
NEWSPIDER_MODULE = 'bbc.spiders'
HTTPCACHE_ENABLED=True
HTTPCACHE_DIR='/home/tony/Desktop/bbc/cache'
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'bbc (+http://www.yourdomain.com)'
DOWNLOADER_MIDDLEWARES = {
	'scrapy.contrib.downloadermiddleware.httpcache.HttpCacheMiddleware': 300,
}

EXTENSIONS = {
    'scrapy.contrib.closespider.CloseSpider': 100,
}
CLOSESPIDER_PAGECOUNT=100000
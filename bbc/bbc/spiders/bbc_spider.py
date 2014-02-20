from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.log import ScrapyFileLogObserver
from scrapy.shell import inspect_response
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import FormRequest
from scrapy.http import Request
from dateutil import parser
from time import sleep
from scrapy import log
import requests
import re


class BBCspider(CrawlSpider):
	name ='bbc'
	start_urls = ['http://www.bbc.co.uk/news/']
	allowed_domains = ['bbc.co.uk']

	rules = (
		Rule(SgmlLinkExtractor(allow=('bbc.co.uk\/news\/.+')),follow=True,callback='parse_news'),
		)

	def parse_news(self,response):
		print '>>>>>>>>',response.url
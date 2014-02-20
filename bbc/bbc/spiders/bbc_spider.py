from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from getevents.consistency_check import consistency_check
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.log import ScrapyFileLogObserver
from scrapy.shell import inspect_response
from scrapy.spider import BaseSpider
from scrapy.selector import Selector
from scrapy.http import FormRequest
from getevents.items import *
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
		Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="mb10"]//a','//div[@class="span8"]/div/ul[1]//a')),follow=True,callback='parse_event'),
		)

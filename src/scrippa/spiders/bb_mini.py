from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware
from scrapy.http import Request
from scrippa.items import ScrippaItem
from scrapy.shell import inspect_response
from scrapy import log

class ScrippaSpider(BaseSpider):
    name = "scrippa"
    allowed_domains = ["fold3.com"]
    #user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20120427 Firefox/15.0a1"
    start_urls = [
      "http://www.fold3.com/browsemore/haouYr9gu_253/1_20/",
      "http://www.fold3.com/browsemore/haouYr9gu_253/21_40/"
    ]
    
    def parse(self, response):
	log.msg("mooooooooooooooooooonkety nusiness", level=log.DEBUG)
        print "Starting a parse ......"
        hxs = HtmlXPathSelector(response)
        yearLinks = hxs.select('//div[@id="browse"]/ul/li')
        urlbase="http://www.fold3.com"
        
        items = []
        
        for link in yearLinks:
            item = ScrippaItem()
            #item['title'] = link.select('a/text()').extract()
            year_url = link.select('a/@href').extract()[0]
            year = link.select('a/strong/text()').extract()[0]
            year_url = urlbase + year_url
            item['year_url'] = year_url
            item['year'] = year           
            items.append(item)
            yield Request(url=year_url, meta={'yearitem': item}, callback=self.parse_year)


    def parse_year(self, response):
        yritem = response.meta.get('yearitem', None)
        print "======== PARSING YEAR: " + yritem['year']
        
        # get datemonth url and go to it
        hxs = HtmlXPathSelector(response)
        monthLinks = hxs.select('//div[@id="browse"]/ul/li')
        year_title = hxs.select('//h1/text()').extract()
        yritem['year_title'] = year_title

        urlbase="http://www.fold3.com"

        for link in monthLinks:
            month_url = link.select('a/@href').extract()[0]
            month  = link.select('a/strong/text()').extract()[0]
            month_url = urlbase + month_url             
            yritem['month_url'] = month_url
            yritem['month'] = month  
            # yield Request(url=month_url, meta={'monthitem': yritem}, callback=self.parse_month)

	return yritem

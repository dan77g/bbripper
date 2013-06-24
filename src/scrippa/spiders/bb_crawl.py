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
            self.log("Looking at year " + year, level=log.WARNING)
            #yield Request(url=year_url, meta={'yearitem': item}, callback=self.parse_year)
            
        return item
            

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
            self.log("Looking at month " + month, level=log.WARNING)
            #yield Request(url=month_url, meta={'monthitem': yritem}, callback=self.parse_month)
            
        return yritem

    def parse_month(self, response):
        mnitem = response.meta['monthitem']
               
        # get report url and go to it
        hxs = HtmlXPathSelector(response)
        reportLinks = hxs.select('//div[@id="browse"]/ul/li')
        month_title = hxs.select('//h1/text()').extract()[0]
        mnitem['month_title'] = month_title
        mnitem['month'] = month_title
        urlbase="http://www.fold3.com"
        
        for link in reportLinks:
            report_url = link.select('a/@href').extract()[0]
            report = link.select('a/strong/text()').extract()[0]
            report_url = urlbase + report_url
            mnitem['report_url'] = report_url
            mnitem['report'] = report
            
            self.log("Looking at report " + report, level=log.WARNING)
                        
            print "======================="
            print "YEAR is " + mnitem['year']
            print "MONTH is " + mnitem['month']
            print "REPORT is " + mnitem['report']
            print "REPORT URL is " + mnitem['report_url']
            #yield Request(url=report_url, meta={'reportitem': mnitem}, callback=self.parse_report)

            
        return mnitem

    def parse_report(self, response):
        repitem = response.meta['reportitem']
        
        hxs = HtmlXPathSelector(response)
        imageLinks = hxs.select('//div[@id="browse"]/ul/li')
        urlbase="http://www.fold3.com"
        
        for link in imageLinks:
            img_url = link.select('a/@href').extract()[0]
            img_page = link.select('a/@title').extract()[0]
            img_url = urlbase + img_url
            repitem['img_url'] = img_url
                        
            self.log("Looking at img_url " + img_url, level=log.WARNING)
                        
            print "found img at " 
            print img_url 
            print " of page # "
            print img_page
            
        
        return repitem
            
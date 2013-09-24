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
    urlbase="http://www.fold3.com"
    repitems = []

    def parse(self, response):
        print "Starting a parse ......"
        hxs = HtmlXPathSelector(response)
        yearLinks = hxs.select('//div[@id="browse"]/ul/li')
        items = []
        
        for link in yearLinks:
            item = ScrippaItem()
            #item['title'] = link.select('a/text()').extract()
            year_url = link.select('a/@href').extract()[0]
            year = link.select('a/strong/text()').extract()[0]
            year_url = self.urlbase + year_url
            #item['year_url'] = year_url
            item['year'] = year           
            items.append(item)
            self.log("Looking at year " + year, level=log.WARNING)
            yield Request(url=year_url, meta={'yearitem': item}, callback=self.parse_year)
               

    def parse_year(self, response):
        yritem = response.meta.get('yearitem', None)
        print "======== PARSING YEAR: " + yritem['year']
        # get datemonth url and go to it
        hxs = HtmlXPathSelector(response)
        monthLinks = hxs.select('//div[@id="browse"]/ul/li')
        #year_title = hxs.select('//h1/text()').extract()
        #yritem['year_title'] = year_title
        yritems = []

        for link in monthLinks:
            month_url = link.select('a/@href').extract()[0]
            month  = link.select('a/strong/text()').extract()[0]
            month_url = self.urlbase + month_url             
            #yritem['month_url'] = month_url
            #yritem['month'] = month
            #yritems.append(yritem) 
            self.log("Looking at month " + month, level=log.WARNING)
            yield Request(url=month_url, meta={'monthitem': yritem}, callback=self.parse_month)
            
    def parse_month(self, response):
        mnitem = response.meta['monthitem']
        # get report url and go to it
        hxs = HtmlXPathSelector(response)
        reportLinks = hxs.select('//div[@id="browse"]/ul/li')
        #' TEST
        year = hxs.select('//h2/a/text()')[3].extract()
        month = hxs.select('//h2/a/text()')[4].extract()
        #month_title = hxs.select('//h1/text()').extract()[0]
        #mnitem['month_title'] = month_title
        #mnitem['month'] = month_title
        mnitems = []
        
        # FIXME - could be multiple pages ..... (if "Go to next page")
        for link in reportLinks:
            report_url = link.select('a/@href').extract()[0]
            report = link.select('a/strong/text()').extract()[0]
            report_url = self.urlbase + report_url
            mnitem['report_url'] = report_url
            mnitem['report'] = report
            mnitem['month'] = month
            mnitem['year'] = year            
            mnitems.append(mnitem)
            self.log("Looking at report " + report, level=log.WARNING)
            yield Request(url=report_url, meta={'reportitem': mnitem}, callback=self.parse_report)
 
    def parse_report(self, response):
        repitem = response.meta['reportitem']
        hxs = HtmlXPathSelector(response)
        imageLinks = hxs.select('//div[@id="browse"]/ul/li')
        month_title = hxs.select('//h2/text()').extract()[3]
        report_title = hxs.select('//h2/text()').extract()[4]
        
        # initialise repitems list if single page or Page 1 of multi
        if not hxs.select('//div[@class="paginate"]/a[@class="nav-next"]/@href') or hxs.select('//div[@class="paginate"]/b/text()').extract()[0] == '1': # either single page or first of multi page
            firstpage = True
            self.repitems = []  # reset global repitems
        
        # set up temporary list var
        tmpitems = []
        for link in imageLinks:
            img_url = link.select('a/@href').extract()[0]
            img_page = link.select('a/@title').extract()[0]
            img_url = self.urlbase + img_url
            repitem['img_url'] = img_url
            tmpitems.append(repitem)
            self.log("Looking at img_url " + img_url, level=log.WARNING)
            print "found img at: " + img_url 
            print "page no: " + img_page
            
        if not hxs.select('//div[@class="paginate"]/a[@class="nav-next"]/@href'): # either single page or last of multi page, either way return now
            self.repitems.extend(tmpitems)
            return self.repitems
        else: # we are midway through processing a multi-page, don't return yet
            self.repitems.extend(tmpitems)
            # extract next report page url to parse
            next_url = self.urlbase + hxs.select('//div[@class="paginate"]/a[@class="nav-next"]/@href').extract()[0]
            return Request(url=next_url, meta={'reportitem':repitem}, callback=self.parse_report)
            
                        
#    def parse_subreport(self, response):
#        subrepitem = response.meta['subreportitem']
#        
#        hxs = HtmlXPathSelector(response)
#        imageLinks = hxs.select('//div[@id="browse"]/ul/li')
#        month_title = hxs.select('//h2/text()').extract()[3]
#        report_title = hxs.select('//h2/text()').extract()[4]
#
#        urlbase="http://www.fold3.com"
#        subrepitems = []
#        
#        for link in imageLinks:
#            img_url = link.select('a/@href').extract()[0]
#            img_page = link.select('a/@title').extract()[0]
#            img_url = urlbase + img_url
#            subrepitem['img_url'] = img_url
#            subrepitems.append(subrepitem)
#                        
#            self.log("Looking at img_url " + img_url, level=log.WARNING)
#                        
#            print "found img at: " + img_url 
#            print "page no: " + img_page
#            
#        return subrepitems
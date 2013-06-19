from twisted.internet import reactor
from scrapy.crawler import Crawler
from scrapy.settings import Settings
from scrapy import log
from scrippa.spiders.bb_crawl  import ScrippaSpider

spider = ScrippaSpider(domain='fold3.com')
print "spider is " + str(ScrippaSpider)

crawler = Crawler(Settings())
crawler.configure()
crawler.crawl(spider)
print "Starting crawler"
crawler.start()

print "starting to log"
log.start()
reactor.run() # the script will block here

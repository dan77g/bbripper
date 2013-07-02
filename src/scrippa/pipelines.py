# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html

from scrapy import signals
from scrapy.contrib.exporter import JsonLinesItemExporter
from scrapy import log  

class ScrippaPipeline(object):
    
    def __init__(self):
        #self.files = {}
        #self.log("MMMMMMMMMMMMMMMMMMMMMMMMMMAAAAAAAAAAAATE", level=log.WARNING)
        print "DDDDDDDDDDDDDDDDDDDDDDDDDUUUUUUUUUUUUUUUUUUUUUUUUUUUDE"
        file = open('blimin_reports.json', 'w+b')
        
    
    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        file = open('duds_reports.json', 'w+b')
        #self.files[spider] = file
        self.exporter = JsonLinesItemExporter(file)
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        #file = self.files.pop(spider)
        #file.close()

    def process_item(self, item, spider):
        print "ScrippaPipeline: exporting item ============================== "
        self.exporter.export_item(item)
        return item


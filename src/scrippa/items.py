# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class ScrippaItem(Item):
    title = Field()
    year_url = Field()
    year = Field()
    year_title = Field()
    
    month_url = Field()
    month = Field()
    month_title = Field()
    
    report_url = Field()
    report = Field()
    
    img_url = Field()
    img = Field()

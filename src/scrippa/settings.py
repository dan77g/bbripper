# Scrapy settings for scrippa project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'scrippa'

SPIDER_MODULES = ['scrippa.spiders']
NEWSPIDER_MODULE = 'scrippa.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'scrippa (+http://www.yourdomain.com)'

ITEM_PIPELINES = [
    'scrippa.pipelines.ScrippaPipeline'
]
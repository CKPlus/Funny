# -*- coding: utf-8 -*-

# Scrapy settings for demo_crawer project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'demo_crawer'

SPIDER_MODULES = ['demo_crawer.spiders']
NEWSPIDER_MODULE = 'demo_crawer.spiders'

ITEM_PIPELINES = {  
    'demo_crawer.pipelines.DemoCrawerPipeline': 300,
    # 'demo_crawer.pipelines.StoreToDBPipeline': 500,
}  

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'demo_crawer (+http://www.yourdomain.com)'

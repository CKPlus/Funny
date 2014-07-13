# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy.item import Item, Field


class Ptt(Item):
    title = Field()
    url = Field()
    likes = Field()
    publish_date = Field()
    author = Field()
    content = Field()

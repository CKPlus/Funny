# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys, re
from scrapy.exceptions import DropItem
sys.path.append("../")
from my_sites.tikann.database import db_session
from my_sites.tikann.models import User, Article, Image


class DemoCrawerPipeline(object):

    # def __init__(self):

    def process_item(self, item, spider):
    	if not item['content']:
    	    raise DropItem("Missing content url in %s" % item)
        else:
            try:
                article = Article()
                
                article.author = item['author']
                article.publish_date = item['publish_date']
                article.title = item['title']
                article.likes = item['likes']
                article.url = item['url']
                
                for url in item['content']:
                    image = Image()
                    image.url = url
                    article.content.append(image)

                db_session.add(article)
                db_session.commit()
            except:
                db_session.rollback()
                raise
            finally:
                db_session.close()


            return item

    # def close_spider(self, spider):
    #     db_session.commit()


# class StoreToDBPipeline(object):
#     def process_item(self, item, spider):
#         try:
#             article = Article()
#             article.author = item['author']
#             article.publish_date = item['publish_date']
#             article.title = item['title']
#             article.like = item['likes']

#             db_session.append(article)
#             db_session.commit()
#         except Exception as e:
#             print 'Save to db error, messages : %s' % e

#         return item
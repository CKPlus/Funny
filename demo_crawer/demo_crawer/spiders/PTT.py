# -*- coding: utf-8 -*-
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy import log
from scrapy.http import Request
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.selector import Selector
from demo_crawer.items import Ptt

import functools

from urlparse import urljoin

class PttSpider(CrawlSpider):
    name = "PTT"
    allowed_domains = ["www.ptt.cc"]

    # start_urls = []
    # for i in range(1180, 1190):
    #     start_urls.append("http://www.ptt.cc/bbs/Beauty/index%s.html" % i) 

    start_urls = ["http://www.ptt.cc/bbs/Beauty/"]

    rules = (
        Rule(SgmlLinkExtractor(allow=('index\d\d\d\d\.html',), restrict_xpaths=('//*[@id="action-bar-container"]/div/div[2]/a[2]',),),
                               follow=True,
                               callback='parse_item',),
        # Rule(SgmlLinkExtractor(allow=('\.html',)), follow=False),
    )

    download_delay = .25

    def parse_item(self, response):
        sel = Selector(response)
        articles = sel.xpath('//div[@class="r-ent"]')
        for article in articles:
            item = Ptt()
            item['title'] = ''.join(article.xpath('div[@class="title"]/a/text()').extract())
            item['likes'] = ''.join(article.xpath('div[@class="nrec"]/span/text()').extract())
            item['url'] = ''.join(article.xpath('div[@class="title"]/a/@href').extract())
            item['publish_date'] = ''.join(article.xpath('div[@class="meta"]/div[@class="date"]/text()').extract())
            item['author'] = ''.join(article.xpath('div[@class="meta"]/div[@class="author"]/text()').extract())

            if item['url']:
                request = Request(urljoin(response.url, item['url']),
                                  meta={"item":item},
                                  callback=self.parse_article,)
                yield request
            else:
                yield item



    def parse_article(self, response):
        sel = Selector(response)
        item = response.request.meta['item']
        if not len(sel.xpath('//img/@src')) == 0:
            item['content'] = sel.xpath('//img/@src').extract()
        else:
            item['content'] = ""

        yield item

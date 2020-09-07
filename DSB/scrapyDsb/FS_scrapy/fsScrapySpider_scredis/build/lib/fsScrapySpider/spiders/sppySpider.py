# -*- coding: utf-8 -*-
import scrapy
import re
import json
import datetime
from ..items import FsscrapyspiderItem
import time
from scrapy_redis.spiders import RedisCrawlSpider, RedisSpider

class SppyspiderSpider(RedisSpider):
    name = 'sppySpider'
    allowed_domains = ['qc.wa.news.cn', 'www.xinhuanet.com']
    # start_urls = []

    # def start_requests(self):
    #     qwpyBaseUrl = 'http://qc.wa.news.cn/nodeart/list?nid=11148362&pgnum={}&cnt=10&tp=1&orderby=1?callback=jQuery112405951037093341978_1592276347200&_={}'
    #     zzsBaseUrl =  'http://qc.wa.news.cn/nodeart/list?nid=11148367&pgnum={}&cnt=10&tp=1&orderby=1?callback=jQuery1124016917371617397858_1592285480616&_={}'
    #     for i in range(1, 4):
    #         timeStr = int(time.time() * 1000)
    #         qwpyUrl = qwpyBaseUrl.format(i, timeStr, timeStr+1)
    #         yield scrapy.Request(url=qwpyUrl, callback=self.parse)
    #         zzsUrl = zzsBaseUrl.format(i, timeStr, timeStr)
    #         yield scrapy.Request(url=zzsUrl, callback=self.parse)

    redis_key = 'sppySpider:start_urls'


    def parse(self, response):
        baseStr = re.findall('\({(.*?)}\n\)', response.text)
        if len(baseStr)>0:
            daatStr = '{' + baseStr[0] + '}'
            dataJson = json.loads(daatStr)
            listJson = dataJson.get('data').get('list')
            for li in listJson:
                href = li.get('LinkUrl')
                title = li.get('Title')
                publiceTime = li.get('PubTime')
                Abstract = li.get('Abstract')
                allPics = li.get('allPics')
                if len(allPics)>0:
                    imageurl = allPics[0]
                else:
                    imageurl = ''
                yield scrapy.Request(url=href, meta={'href': href, 'title':title, 'imageurl':imageurl, 'abstract':Abstract}, callback=self.detailedParse)

    def detailedParse(self, response):
        item = FsscrapyspiderItem()
        item['title'] = response.meta['title']
        item['sourceurl'] = response.meta['href']
        item['createtime'] = datetime.datetime.now()
        content = response.xpath('//div[@id="p-detail"]')
        if len(content)==0:
            content = response.xpath('//div[@class="con_txt"]')
        item['outcontent'] = content.extract_first()
        item['imageurl'] = response.meta['imageurl']
        item['abstract'] = response.meta['abstract'][:150]
        item['contentcodetype'] = 'u'
        item['abstractcodetype'] = 'u'
        item['configid'] = 128
        item['categoryid'] = 1208
        item['host'] = 'http://www.xinhuanet.com'
        item['listurl'] = 'http://www.xinhuanet.com/food/sppy/qwpy.htm'
        item['believeable'] = 1
        item['weight'] = 0

        yield  item







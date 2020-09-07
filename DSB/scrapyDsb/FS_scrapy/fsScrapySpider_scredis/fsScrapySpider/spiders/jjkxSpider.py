# -*- coding: utf-8 -*-
import scrapy
from ..items import FsscrapyspiderItem
import datetime
from scrapy_redis.spiders import RedisSpider, RedisCrawlSpider



class JjkxspiderSpider(RedisSpider):
    name = 'jjkxSpider'
    allowed_domains = ['edu.foshan.gov.cn']
    # start_urls = ['http://edu.foshan.gov.cn/kx/jjkx/index.html']

    redis_key = 'jjkxSpider:start_urls'

    def parse(self, response):
        liList = response.xpath('//ul[@class="list"]/li')

        for li in liList:
            href = li.xpath('./a/@href').extract_first()
            title = li.xpath('./a/text()').extract_first()
            publiceTime = li.xpath('./span/text()').extract_first().replace('[','').replace(']','')
            data = (href, title, publiceTime)
            print(data)
            yield scrapy.Request(url=href, meta={'href': href, 'title':title},callback=self.detailedParse)


    def detailedParse(self, response):
        '''
            详细页解析
        :param response:
        :return:
        '''
        item = FsscrapyspiderItem()
        item['title'] = response.meta['title']
        item['sourceurl'] = response.meta['href']
        item['createtime'] = datetime.datetime.now()
        content = response.xpath('//div[@class="TRS_Editor"]')
        if len(content)==0:
            content = response.xpath('//div[@id="img-content"]')
        item['outcontent'] = content.extract_first()
        if len(content)>0:
            item['imageurl'] = content[0].xpath('.//img/@src').extract_first()
            item['abstract'] = ''.join(content[0].xpath('.//text()').extract())[:100].replace('\u3000', '').replace('\n', '').replace(' ', '')
        else:
            item['imageurl'] = ''
            item['abstract'] = ''
        item['contentcodetype'] = 'u'
        item['abstractcodetype'] = 'u'
        item['configid'] = ''
        item['categoryid'] = ''
        item['host'] = 'fsamr.foshan.gov.cn'
        item['listurl'] = 'http://fsamr.foshan.gov.cn/zwdt/sjdt/'
        item['believeable'] = 1
        item['weight'] = 0

        yield  item
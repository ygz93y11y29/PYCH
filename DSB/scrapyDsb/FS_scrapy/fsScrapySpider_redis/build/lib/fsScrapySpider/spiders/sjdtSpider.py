# -*- coding: utf-8 -*-
import scrapy
import datetime
from ..items import FsscrapyspiderItem


class SjdtspiderSpider(scrapy.Spider):
    name = 'sjdtSpider'
    allowed_domains = ['fsamr.foshan.gov.cn', 'foshan.gov.cn']
    start_urls = ['http://fsamr.foshan.gov.cn/zwdt/tzgg/', 'http://fsamr.foshan.gov.cn/zwdt/sjdt/']


    def parse(self, response):
        '''
            列表页解析
        :param response:
        :return:
        '''
        liList = response.xpath('//div[@class="news_list"]/ul/li')
        for li in liList:
            href = li.xpath('./a/@href').extract_first()
            title = li.xpath('./a/@title').extract_first()
            publiceTime = li.xpath('./span[@class="time"]/text()').extract_first()
            data = (href, title, publiceTime)
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
        content = response.xpath('//div[@class="content_article"]')
        if len(content)==0:
            content = response.xpath('//div[@class="TRS_Editor"]')
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

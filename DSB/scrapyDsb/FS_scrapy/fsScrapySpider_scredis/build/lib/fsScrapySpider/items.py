# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FsscrapyspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    sourceurl = scrapy.Field()
    createtime = scrapy.Field()
    imageurl = scrapy.Field()
    outcontent = scrapy.Field()
    contentcodetype = scrapy.Field()
    abstract = scrapy.Field()
    abstractcodetype = scrapy.Field()
    configid = scrapy.Field()
    categoryid = scrapy.Field()
    host = scrapy.Field()
    listurl = scrapy.Field()
    believeable = scrapy.Field()
    weight = scrapy.Field()








# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymssql
from .items import FsscrapyspiderItem

class FsscrapyspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class SQLServerPipeline(object):
    def __init__(self, host, database, user, password, port):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.port = port

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            host=crawler.settings.get('MYSQL_HOST'),
            database=crawler.settings.get('MYSQL_DATABASE'),
            user=crawler.settings.get('MYSQL_USER'),
            password=crawler.settings.get('MYSQL_USER'),
            port=crawler.settings.get('MYSQL_PORT')
        )

    def open_spider(self, spider):
        self.db = pymssql.connect(database="RPT_DB_V3", user="rip_conn", password="1234QWER!@#$", host="192.168.9.180", charset="utf8")
        #self.db = pymssql.connect(database="RPT_DB_V3", user="rip_conn", password="1234QWER!@#$", host="192.168.9.180",charset="utf8")
        self.cursor = self.db.cursor()
        # print(self.cursor)

    def close_spider(self, spider):
        self.cursor.close()
        self.db.close()

    def insert_fsNews(self, item):
        try:
            title = item["title"]
            sourceurl = item["sourceurl"]
            createtime = item["createtime"]
            imageurl = item["imageurl"]
            outcontent = item["outcontent"]
            contentcodetype = item["contentcodetype"]
            abstract = item["abstract"]
            abstractcodetype = item["abstractcodetype"]
            configid = item["configid"]
            categoryid = item["categoryid"]
            host = item["host"]
            listurl = item["listurl"]
            believeable = item["believeable"]
            weight = item["weight"]
            insert_sql = "INSERT INTO outsourceingcollection (title, sourceurl, createtime, imageurl, outcontent, contentcodetype, abstract, abstractcodetype,configid, categoryid, host, listurl, believeable, weight) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            data = (title, sourceurl, createtime, imageurl, outcontent, contentcodetype, abstract, abstractcodetype, configid,categoryid, host, listurl, believeable, weight)
            self.cursor.execute(insert_sql, data)
            self.db.commit()
            print("insert outsourceingcollection  susserd", )
        except Exception as error:
            print('insert           outsourceingcollection                               error ！ -> ', error)

    def process_item(self, item, spider):
        if isinstance(item, FsscrapyspiderItem):
            self.insert_fsNews(item)
        return item



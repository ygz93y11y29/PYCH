# -*- coding: utf-8 -*-
from scrapy.dupefilters import BaseDupeFilter
import redis
from scrapy.utils.request import request_fingerprint



class DupFilter(BaseDupeFilter):
    def __init__(self):
        self.conn = redis.Redis(host='192.168.10.3', port=6379, db=15, password='123456')

    def request_seen(self, request):
        """
        检测当前请求是否已经被访问过
        :param request:
        :return: True表示已经访问过；False表示未访问过
        """
        fid = request.url
        result = self.conn.sadd('visited_urls', fid)
        if result == 1:
            return False
        return True
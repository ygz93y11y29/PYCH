from scrapy_redis.dupefilter import RFPDupeFilter
from scrapy_redis.connection import get_redis_from_settings
from scrapy_redis import defaults


#д╛хо
class RedisDupeFilter(RFPDupeFilter):
    # @classmethod
    # def from_settings(cls, settings):
    #     """Returns an instance from given settings.
    #
    #     This uses by default the key ``dupefilter:<timestamp>``. When using the
    #     ``scrapy_redis.scheduler.Scheduler`` class, this method is not used as
    #     it needs to pass the spider name in the key.
    #
    #     Parameters
    #     ----------
    #     settings : scrapy.settings.Settings
    #
    #     Returns
    #     -------
    #     RFPDupeFilter
    #         A RFPDupeFilter instance.
    #
    #
    #     """
    #     server = get_redis_from_settings(settings)
    #     # XXX: This creates one-time key. needed to support to use this
    #     # class as standalone dupefilter with scrapy's default scheduler
    #     # if scrapy passes spider on open() method this wouldn't be needed
    #     # TODO: Use SCRAPY_JOB env as default and fallback to timestamp.
    #     key = defaults.DUPEFILTER_KEY % {'timestamp': 'xiaodongbei'}
    #     debug = settings.getbool('DUPEFILTER_DEBUG')
    #     return cls(server, key=key, debug=debug)


    def request_seen(self, request):
        """Returns True if request was already seen.

        Parameters
        ----------
        request : scrapy.http.Request

        Returns
        -------
        bool

        """
        fp = request.url

        # This returns the number of values added, zero if already exists.
        added = self.server.sadd(self.key, fp)
        return added == 0




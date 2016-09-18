import random
from douban.settings import UA_LIST


class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        ua = random.choice(UA_LIST)
        if ua:
            request.headers.setdefault('User-Agent', ua)
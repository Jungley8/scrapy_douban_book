# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
import time

class BookSubjectSpider(scrapy.Spider):
    name = "book_subject"
    allowed_domains = ["book.douban.com"]

    def start_requests(self):
        pages=[]
        data = open('bookid_list_85.txt').readlines()
        for line in data:
            url = "https://book.douban.com/subject/" +line[:-1]+'/'
            page=scrapy.Request(url)
            pages.append(page)
        return pages

    def parse(self, response):
        time.sleep(1);
        print "sleep a while"
        item = DoubanItem()
        sel = scrapy.Selector(response)

        item["name"] = sel.xpath(
            '//div[@id="wrapper"]/h1/span/text()').extract()[0].strip()
        item["score"] = sel.xpath(
            '//div[@class="rating_wrap clearbox"]//strong[@class="ll rating_num "]/text()').extract()[0].strip()
        item["subject_id"] = response.url[32:-1]
        print "scawling : ",item["name"]," id :",item["subject_id"]
        item['tags'] = ",".join(sel.xpath('//*[@id="db-tags-section"]/div/span/a/text()').extract())
        item['rating_people'] = sel.xpath('//*[@id="interest_sectl"]//div[@class="rating_sum"]//a[@class="rating_people"]/span/text()').extract()

        datas = response.xpath("//div[@id='info']//text()").extract()
        datas = [data.strip() for data in datas]
        datas = [data for data in datas if data != ""]
        # print datas

        for data in datas:
            # print data.encode("gb2312")
            if u"作者" in data:
                if u":" in data:
                    item["author"] = datas[datas.index(data) + 1]
                elif u":" not in data:
                    item["author"] = datas[datas.index(data) + 2]
            elif u"出版社:" in data:
                item["press"] = datas[datas.index(data)+1]
            elif u"出版年:" in data:
                item["date"] = datas[datas.index(data)+1]
            elif u"页数:" in data:
                item["page"] = datas[datas.index(data)+1]
            elif u"定价:" in data:
                item["price"] = datas[datas.index(data)+1]
            elif u"ISBN:" in data:
                item["ISBN"] = datas[datas.index(data)+1]
            elif u"统一书号:" in data:
                item["ISBN"] = datas[datas.index(data)+1]

        yield item

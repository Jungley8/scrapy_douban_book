# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import Rule
from douban.items import DoubanItem
import time
# import json


class BookSpider(scrapy.Spider):
    name = "book"
    baseurl = "https://book.douban.com"
    allowed_domains = ["book.douban.com"]
    start_urls = (
        'https://book.douban.com/tag/',
    )
    books_number = 0
    txt_id = 0
    rules = [
        Rule(LinkExtractor(allow=("https://book.douban.com/tag/[^/]+/?$"))),
    ]

    def parse(self, response):
        sel = scrapy.Selector(response)

        datas = sel.xpath("//*[@id='content']//table[@class='tagCol']//td")
        for data in datas:
            url = data.xpath("a/@href").extract()
            print "crawl booktag link: ", self.baseurl + url[0]
            yield scrapy.Request(self.baseurl + url[0], callback=self.parseTag)

    def parseTag(self, response):
        sel = scrapy.Selector(response)

        urls = sel.xpath(
            '//*[@id="subject_list"]//li[@class="subject-item"]//h2/a/@href').extract()
        for url in urls:
            print "crawl book link: ", url, ", id: ", url[32:-1]
            # url = https://book.douban.com/subject/3070863/
            subject_id = url[32:-1]
            # 先存在本地文件再逐步抓取书籍信息
            if self.books_number < 1000:
                f = open('bookid_list_' + bytes(self.txt_id) + '.txt', 'a')

                f.write(subject_id + "\n")
                self.books_number += 1
            else:
                self.txt_id += 1
                self.books_number = 0
        tagurl = sel.xpath(
            '//*[@id="subject_list"]/div[@class="paginator"]/span[@class="thispage"]/following-sibling::a[1]/@href').extract()
        if tagurl:
            print "crawl booktag link: ", self.baseurl + tagurl[0]
            yield scrapy.Request(self.baseurl + tagurl[0], callback=self.parseTag)

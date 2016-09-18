# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()                       # 书名
    author = scrapy.Field()                     # 作者
    press = scrapy.Field()                      # 出版社
    date = scrapy.Field()                       # 出版日期
    page = scrapy.Field()                       # 页数
    price = scrapy.Field()                      # 价格
    score = scrapy.Field()                      # 读者评分
    rating_people = scrapy.Field()              # 评人人数
    ISBN = scrapy.Field()                       # ISBN号
    subject_id = scrapy.Field()                 # 豆瓣书籍ID
    tags = scrapy.Field()                       # 标签

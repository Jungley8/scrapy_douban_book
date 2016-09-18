# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

from twisted.enterprise import adbapi
import MySQLdb
import MySQLdb.cursors


class DoubanPipeline(object):
    """ 将抓取到的数据存入mysql数据中 """

    def __init__(self):
        self.dbpool = adbapi.ConnectionPool("MySQLdb",
                                            db="douban",
                                            user="root",
                                            passwd="root",
                                            cursorclass=MySQLdb.cursors.DictCursor,
                                            charset="utf8",
                                            use_unicode=False
                                            )

    def process_item(self, item, spider):
        query = self.dbpool.runInteraction(
            self._conditional_insert, item)
        query.addErrback(self.handle_error)
        return item

    def _conditional_insert(self, tb, item):
        if item["page"] is None:
            item["page"] = 'unkown'
        tb.execute("select name from douban_books where subject_id = %s limit 1", (item["subject_id"],))
        result = tb.fetchone()
        if result:
            print "updating ", item['name']
            # tb.execute("update douban_books set author = %s, press= %s, date= %s, page= %s,rating_people = %s, price= %s, score= %s, ISBN= %s where name = %s limit 1", (item["author"], item["press"], item["date"], item["page"], item['rating_people'], item["price"], item["score"], item["ISBN"], item['name']))
        else:
            print "inserting ", item["name"],item["page"]
            tb.execute("insert into douban_books (name, author, press, date, page, price, score,rating_people, ISBN,subject_id,tags) values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)", (item["name"], item["author"], item["press"], item["date"], item["page"], item["price"], item["score"], item['rating_people'], item["ISBN"], item["subject_id"], item["tags"]))

    def handle_error(self, e):
        print(e)

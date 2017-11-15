# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MyjdscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    #图书排名
    BookNumber =scrapy.Field()
    #图书名称
    BookName = scrapy.Field()
    #图书ID
    BookID = scrapy.Field()
    #作者
    author = scrapy.Field()
    #出版社
    press = scrapy.Field()
    #定价
    price = scrapy.Field() 
    #京东价
    JDprice = scrapy.Field()

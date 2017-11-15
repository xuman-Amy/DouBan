#-*- coding:utf-8 -*-
from scrapy.selector import Selector
from MyJDScrapy.items import MyjdscrapyItem
from scrapy.http import Request
from scrapy.spiders import CrawlSpider
import requests
import json , re
import csv 
import codecs

class MyJDScrapy(CrawlSpider):
    name = "MyJDSpider"
    redis_key = "MyJDScrapy:start_urls"
    start_urls = ["http://book.jd.com/booktop/0-0-0.html?category=1713-0-0-0-10001-1#comfort"]
    def parse(self,response):
        item = MyjdscrapyItem()
        selector = Selector(response)
        Books = selector.xpath('/html/body/div/div/div/div/ul/li')
        for each in Books:
            BookNumber = each.xpath('div[@class="p-num"]/text()').extract()
            #图书名称
            BookName = each.xpath('div[@class="p-detail"]/a[@class="p-name"]/text()').extract()
            #作者
            author = each.xpath('div[@class="p-detail"]/dl[1]/dd/a[1]/text()').extract()
            #出版社
            press = each.xpath("div[@class='p-detail']/dl[2]/dd/a/text()").extract()
                
            temphref = each.xpath("div[@class='p-detail']/a/@href").extract()
            temphref = str(temphref) 
            #print('temphref'+temphref)
            BookID = str(re.search('com/(.*?)\.html',temphref).group(1))
            json_url = 'http://p.3.cn/prices/mgets?type=1&skuIds=J_' + BookID
            r = requests.get(json_url).text
            data = json.loads(r)[0]
            #定价
            price = data['m']
            #京东价
            JDprice = data['p']
                
            item['BookNumber'] = BookNumber
            item['BookName'] = BookName
            item['author'] = author
            item['press'] = press
            item['BookID'] = BookID
            item['price'] = price
            item['JDprice'] = JDprice
            
                
            yield item
                
        
        nextLink = selector.xpath("/html/body/div/div/div/div/div/span/a[@class='pn-next']/@href").extract()
        
        if nextLink:
            nextLink = "http:" + nextLink[0]
            print('##############'+nextLink+'###############')
            yield Request(nextLink,callback = self.parse)
                      
                
                
                
                
                
                
                
                
                
                
                
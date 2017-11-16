from scrapy.http import Request
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from DouBan.items import DoubanItem

class DouBan_Scrapy(CrawlSpider):
    name = "DouBanScrapy"
    start_urls = ["https://movie.douban.com/top250"]
    url = "https://movie.douban.com/top250"
    def parse(self,response):
        item = DoubanItem()
        selector = Selector(response)
        movies = selector.xpath("//div[@class='info']")
        for each in movies:
            title = each.xpath("div[@class='hd']/a/span[@class='title']/text()").extract()
            info = each.xpath("div[@class='bd']/p[1]/text()").extract()
            star = each.xpath("div/div[@class='star']/span[@class='rating5-t']/text()").extract()
            quote = each.xpath("div/p/span/text()").extract()
                
            item['title'] = title
            item['info'] = info
            item['star'] = star
            item['quote'] = quote
            
            yield item
        nextlink =selector.xpath("/html/body/div/div/div/div/div/span[@class='next']/a//@href").extract()
        if nextlink:
            nextlink = self.url + nextlink[0]
            print(nextlink)
            yield Request(nextlink,callback = self.parse)
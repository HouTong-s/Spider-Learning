# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DoubanmoviesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()                           #电影名称
    rate = scrapy.Field()                            #评分
    tag = scrapy.Field()                             #搜索的类别
    url = scrapy.Field()                             #详情页面的地址

class DetailItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()                           #电影名称
    rate = scrapy.Field()                            #评分
    url = scrapy.Field()     
    director = scrapy.Field()
    length = scrapy.Field()
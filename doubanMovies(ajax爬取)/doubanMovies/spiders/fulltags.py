import scrapy
from scrapy import Request
from doubanMovies.items import DoubanmoviesItem
import json
class BaseSpider(scrapy.Spider):
    name = 'full'
    tags = ["热门", "最新", "豆瓣高分", "冷门佳片", "华语", "欧美", "韩国", "日本"]
    current = 0
    def start_requests(self):
        url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%s&page_limit=50&page_start=0"%self.tags[0]
        yield Request(url)
    def parse(self, response):
        item = DoubanmoviesItem()  
        #获取到JSON格式的数据
        json_text = response.text
        #使用json.loads解码JSON数据，返回Python的数据类型
        #这里的movie_dict是一个字典类型
        movie_dict = json.loads(json_text)
        if len(movie_dict["subjects"]) == 0:          #如果没有数据，退出爬虫
            return
        #for循环遍历每部电影
        for one_movie in movie_dict["subjects"]:
            #获取电影名称
            item["title"] = one_movie["title"]
            #获取url
            item["url"] = one_movie["url"]
            #获取评分
            item["rate"] = one_movie["rate"]

            item["tag"] = self.tags[self.current]
            yield item
        self.current += 1
        if self.current < len(self.tags):
            url = "https://movie.douban.com/j/search_subjects?type=movie&tag=%s&page_limit=50&page_start=0"%self.tags[self.current]
            yield Request(url)
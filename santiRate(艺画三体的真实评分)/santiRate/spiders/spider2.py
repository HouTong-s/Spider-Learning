import scrapy
from scrapy import Request
import json
#爬取短评论
class LongCommentsSpider(scrapy.Spider):
    name = 'short'
    def start_requests(self):
        #这里的url是一个后端接口而不是网页           
        url = "https://api.bilibili.com/pgc/review/short/list?media_id=4315402&ps=20&sort=0"
        yield Request(url)
    def parse(self, response):
        item = {} 
        #获取到JSON格式的数据
        json_text = response.text
        #使用json.loads解码JSON数据，返回Python的数据类型
        #这里的movie_dict是一个字典类型
        all_dict = json.loads(json_text)
        data = all_dict["data"]
        next = data["next"]
        if next == 0:          #如果没有下一页数据，退出爬虫
            return
        #for循环遍历每部电影
        for one_comment in data["list"]:
            #获取电影名称
            item["rate"] = one_comment["score"]
            yield item
        next_url = "https://api.bilibili.com/pgc/review/short/list?media_id=4315402&ps=20&sort=0&cursor=%d"%next
        yield Request(next_url)
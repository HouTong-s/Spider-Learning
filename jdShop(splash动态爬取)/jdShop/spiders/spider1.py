#爬取JD商城，搜索结果为iphone的全部信息,这里需要滑动滚轮才能读取完一页的内容，故需要动态爬取
from scrapy import Request
from scrapy.spiders import Spider
from jdShop.items import JdshopItem            #导入Item模块
from selenium import webdriver                     #导入浏览器引擎模块
from scrapy import Request
from scrapy.spiders import Spider
#from yihaodian.items import YihaodianItem            #导入Item模块
from scrapy_splash import SplashRequest     #导入SplashRequest模块
# splash lua script
#以下lua脚本，实现把当前加载的最后一个商品用滚轮滚到页面的最上方
lua_script = """
    function main(splash, args)
        splash:go(args.url)
        splash:wait(args.wait)
        splash:runjs("arr = document.getElementsByClassName('gl-i-wrap'); arr[arr.length-1].scrollIntoView(true)")
        splash:wait(args.wait)
        return splash:html()
    end
    """
class PhoneSpider(Spider):
    name = 'iphone'                             #定义爬虫名称
    url = 'https://search.jd.com/Search?keyword=iphone'      #URL地址
    currentPage = 1
    #获取初始Request
    def start_requests(self):
        yield SplashRequest(self.url,                   #URL地址
                        callback=self.parse,         #回调函数
                        endpoint='execute', #Splash服务接口，执行lua脚本
                        args={'lua_source':lua_script, #lua source，
                                'images':0,              #不显示图片
                                'wait':3},                #等待时间
                        cache_args=['lua_source'])  #缓存
    # 数据解析
    def parse(self, response):
        item = JdshopItem()                            #定义Item对象
        list_selector = response.xpath("//div[@class='gl-i-wrap']")
        print("结果为："+str(len(list_selector)))
        for one_selector in list_selector:
            try:
                #价格,包含data-price属性的<i/>元素
                price = one_selector.xpath(".//i[@data-price]/text()").extract()[0]
                #标题
                title_array = one_selector.xpath("div[@class='p-name p-name-type-2']/a/em/text()").extract()
                #去除引号，换行号，前后的空格
                title = title_array[0].replace("\n","").replace("\"","").strip() + " iPhone "+ title_array[1].replace("\n","").replace("\"","").strip()
                #评论数量
                comments = one_selector.xpath("div[@class='p-commit']/strong/a/text()").extract()[0]
                #店铺名称
                storeName = one_selector.xpath("div[@class='p-shop']/span/a/text()").extract()[0]
                item["price"] = price
                item["title"] = title
                item["comments"] = comments
                item["storeName"] = storeName
                yield item
            except:
                continue
        #获取总页数
        if self.currentPage == 1:
            self.maxPage = int(response.xpath("//span[@class='p-skip']/em/b/text()").extract_first())
        self.currentPage += 1
        #获取下一页URL
        if self.currentPage <= self.maxPage:
            next_url = 'https://search.jd.com/Search?keyword=iphone&page=%d'%(2*self.currentPage-1)
            yield SplashRequest(next_url,
                                callback=self.parse,
                                endpoint='execute',
                                args={'lua_source': lua_script, 'images':0,
                                'wait':3})
#-＊-coding:utf-8-＊-
from scrapy import Request
from scrapy.spiders import Spider
from Second_hand_house.items import SecondHandHouseItem
class HotSalesSpider(Spider):
    #定义爬虫名称
    name = 'base'
    current_page = 1
    #获取初始Request
    def start_requests(self):
        url = "https://su.lianjia.com/ershoufang/"
        yield Request(url)
    #解析函数
    def parse(self, response):
        list_selector = response.xpath("//li/div[@class='info clear']")  
        
        for one_selector in list_selector:
            try:               
                name = one_selector.xpath("div[@class='title']/a/text()").extract_first()
                house_info = one_selector.xpath("div[@class='address']/div[@class='houseInfo']/text()").extract_first()       
                list = house_info.split("|")
                type = list[0].strip(" ")
                area = list[1].strip(" ")
                direction = list[2].strip(" ")
                fitment = list[3].strip(" ")
                total_price = one_selector.xpath("div[@class='priceInfo']/div[1]/span/text()").extract_first()
                unit_price = one_selector.xpath("div[@class='priceInfo']/div[2]/span/text()").extract_first()            
                item = SecondHandHouseItem()                
                #将已经获取的字段保存于item对象中
                item["name"] = name.strip(" ")             #名称
                item["type"] = type                           #户型
                item["area"] = area                           #面积
                item["direction"] = direction               #朝向
                item["fitment"] = fitment                    #是否装修
                item["total_price"] = total_price          #总价
                item["unit_price"] = unit_price            #单价                
                url = one_selector.xpath("div[@class='title']/a/@href").extract_first()
                print("一项为:"+str(item))
                yield Request(url,
                            meta={"item":item},
                            callback=self.property_parse)
            except:
                pass
        if self.current_page == 1:
            #属性page-data的值中包含总页数和当前页
            pages = response.xpath("//div[@class='page-box house-lst-page-box']"
                                        "//@page-data").re("\d+")
            #获取总页数
            #最多爬取5页就行了，多了会被检测到是爬虫
            self.total_page = min(5,int(pages[0]))
        self.current_page+=1                             #下一页的值
        if self.current_page<=self.total_page:       #判断页数是否已越界
            next_url = "https://su.lianjia.com/ershoufang/pg%d/"%(self.current_page)
            #（2）根据URL生成Request，使用yield提交给引擎
            yield Request(next_url)
    #详情页解析函数
    def property_parse(self, response):
        #1．获取产权信息
        elevator = response.xpath("//div[@class='base']/div[@class='content']/ul/li[11]/text()").extract_first()
        property = response.xpath("//div[@class='transaction']/div[@class='content']/ul/li[6]/span[2]/text()").extract_first()
        #2．获取主页面中的房屋信息
        item = response.meta["item"]
        #3．将产权信息添加到item中，返回给引擎
        item["property"] = property
        item["elevator"] = elevator
        yield item
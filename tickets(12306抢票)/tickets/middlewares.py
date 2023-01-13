# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class TicketsSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

from selenium.webdriver.common.by import By               #导入By模块
from selenium.webdriver.support.wait import WebDriverWait  #导入等待模块
from selenium.webdriver.support import expected_conditions as EC
                                                    #导入预期条件模块
from tickets.Tickets import Tickets               #导入购票类
import time
class TicketsDownloaderMiddleware(object):
    def process_request(self, request, spider):
        if spider.name == "tickets":               #判断name是tickets的爬虫
            self.tickets = Tickets()                #生成购票类的对象
            flag = 0                                    #是否需要跳转到票务查询页面
            count = 0                                   #计数器
            #1．判断出发地和目的地站点名称的合法性
            if self.tickets.site_is_exist()==-1:
                print("出发地的站点不存在，请重新设置。")
                return None
            elif self.tickets.site_is_exist()==-2:
                print("目的地的站点不存在，请重新设置。")
                return None
            #2．用户登录
            if self.tickets.login()==True:         # 登录成功
                while True:
                    count+=1                            #每循环一次加1
                    #3．查询票务信息
                    if self.tickets.query_tickets(flag) == True:
                    #4．获取预定的车次信息
                        result=self.tickets.get_ticket()
                        if -1==result:                #坐席不存在
                            self.tickets.show_message("坐席不存在，请确认坐席的正确性。")
                            break
                        elif -2==result:              #无票或车票还未开售
                            flag=1                      #无须重新加载票务查询页面
                            if count%100 == 0:
                                flag=0                  #重新加载票务查询页面
                                #单击登录的用户名，保持登录状态
                                self.tickets.keep_loading()
                        elif -3==result:              #预定的车次不存在
                            self.tickets.show_message("预定的车次不存在。")
                            break
                        elif 0==result:              #没查到任何结果，此时应该继续轮询
                            continue
                        else:#1：正常，已经单击了“预定”按钮
                            #5．预定车票
                            if self.tickets.order_ticket()==True:
                                #6．核对订单
                                if self.tickets.confirm_dialog()==True:
                                    #7．购票成功后，发送邮件
                                    if self.tickets.mail_to()==True:
                                        break           #购票成功，退出
                            flag = 0                   #重新跳转到票务查询页面
                    else:                               #超时
                        flag=0                          #重新跳转到票务查询页面
            else:
                self.tickets.show_message("登录超时，请重新启动程序。")
            time.sleep(500)                           #购票成功后，暂停一段时间，防止页面被关闭
        return None
    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)

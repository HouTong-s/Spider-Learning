#
#-＊-coding:utf-8-＊-
from scrapy import Request
from scrapy.spiders import Spider
from GetTeachers.items import GetteachersItem
class GetTeachersSpider(Spider):
    #定义爬虫名称
    name = 'base'

    #获取初始Request
    def start_requests(self):
        url = "https://yjsjy.uestc.edu.cn/gmis/jcsjgl/dsfc?yxsh=08&zydm=081200"
        #生成请求对象，设置url,  callback
        #callback默认为本类的parse()函数
        yield Request(url,callback=self.parse)
    #解析函数
    def parse(self, response):
        #使用xpath定位到小说内容的div元素，保存到列表中
        list_selector = response.xpath("//td[@valign='center']")
        #依次读取每部小说的元素，从中获取名称、作者、类型和形式
        for one_selector in list_selector:
            url = one_selector.xpath("a/@href").extract_first()
            if url != None:
                yield Request(response.urljoin(url),callback=self.detailsparse) 
    def detailsparse(self,response):
        item = GetteachersItem()
        teacher_code = response.xpath("//span[@id='Labeldsdm']/text()").extract_first()
        teacher_name = response.xpath("//span[@id='Labeldsxm']/text()").extract_first()
        sex = response.xpath("//span[@id='Labelxb']/text()").extract_first().strip()
        special_name = response.xpath("//span[@id='Labeltc']/text()").extract_first()
        professional_title = response.xpath("//span[@id='Labelzc']/text()").extract_first()
        degree = response.xpath("//span[@id='Labelxw']/text()").extract_first()
        属性 = response.xpath("//span[@id='Labelsx']/text()").extract_first().strip()
        mail_name = response.xpath("//span[@id='Labelemail']/text()").extract_first()
        mail_host = response.xpath("//span[@id='Labelemail']/following-sibling::span[2]/text()").extract_first()
        mail = mail_name+"@"+mail_host
        #string(路径)这样可以获取子元素的text()
        academic_experience = response.xpath("string(//span[@id='Labelxsjl'])").extract_first()
        profile = response.xpath("string(//span[@id='Labelgrjj'])").extract_first()
        research_project = response.xpath("string(//span[@id='lblKyxm'])").extract_first()
        research_findings = response.xpath("string(//span[@id='lblFbwz'])").extract_first()
        #这里不该加tbody，因为源代码中没有tbody，是chrome浏览器加的tbody，这里比较坑。源代码有时候又有tbody，反而得加上，所以得都试一次
        research_interests_table = response.xpath("//table[@cellspacing='0' and @border='1']/tr")
        research_interests = []
        for interest in research_interests_table:
            if interest.xpath("td[1]/text()").extract_first()!= "专业名称":
                temp = {}
                temp["专业名称"] = interest.xpath("td[1]/text()").extract_first()
                temp["研究方向"] = interest.xpath("td[2]/text()").extract_first()
                temp["招生类别"] = interest.xpath("td[3]/text()").extract_first()
                research_interests.append(temp)
        item["teacher_code"] = teacher_code
        item["teacher_name"] = teacher_name
        item["sex"] = sex
        item["special_name"] = special_name
        item["professional_title"] = professional_title
        item["degree"] = degree
        item["属性"] = 属性
        item["mail"] = mail
        item["academic_experience"] = academic_experience
        item["profile"] = profile
        item["research_project"] = research_project
        item["research_findings"] = research_findings
        item["research_interests"] = research_interests
        yield item

        

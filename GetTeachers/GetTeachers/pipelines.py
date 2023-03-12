# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import os

class GetteachersPipeline:
    def process_item(self, item, spider):
        folder = '学校导师'
        if not os.path.exists(folder):
            os.makedirs(folder)
        with open(folder+"/"+item["teacher_name"]+".txt",'a',encoding='utf-8') as f:
            interests = ""
            for i in item["research_interests"]:
                interests += i["专业名称"] +"  "+ i["研究方向"] +"  " +i["招生类别"] +"\n"
            content="导师代码： "+str(item["teacher_code"])+"\n" \
                    "导师姓名： "+str(item["teacher_name"])+"\n" \
                    "性    别： "+str(item["sex"])+"\n" \
                    "特    称： "+str(item["special_name"])+"\n" \
                    "职    称：	"+str(item["professional_title"])+"\n" \
                    "学    位：	"+str(item["degree"])+"\n" \
                    "属    性：	"+str(item["属性"])+"\n" \
                    "电子邮件： "+str(item["mail"])+"\n" \
                    "学术经历： "+str(item["academic_experience"])+"\n" \
                    "个人简介： "+str(item["profile"])+"\n" \
                    "科研项目：	"+str(item["research_project"])+"\n" \
                    "研究成果：	"+str(item["research_findings"])+"\n" \
                    "专业研究方向：\n 专业名称	研究方向	招生类别\n" + interests
            f.write(content)
            return item

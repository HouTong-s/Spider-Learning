# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubanmoviesPipeline:
    def process_item(self, item, spider):
        return item

#跟fulltags搭配，保存到csv文件中
class SaveToCSVFfile:
    tag = "none"
    file = None
    def process_item(self, item, spider):
        if self.tag != item["tag"] :
            if self.file != None:
                self.file.close()
            self.file = open(item["tag"]+".txt","a",encoding="utf-8")
            self.file.write("名字, 评分, url\n")
            self.file.write(item["title"]+", "+\
                            item["rate"]+", "+\
                            item["url"]+"\n")
        else:
            self.file.write(item["title"]+", "+\
                            item["rate"]+", "+\
                            item["url"]+"\n")

        return item
    def close_spider(self, spider):
        #关闭文件
        self.file.close()
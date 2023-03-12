# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class GetteachersItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    teacher_code = scrapy.Field()
    teacher_name = scrapy.Field()
    sex = scrapy.Field()
    special_name = scrapy.Field()
    professional_title = scrapy.Field()
    degree = scrapy.Field()
    属性 = scrapy.Field()
    mail = scrapy.Field()
    academic_experience = scrapy.Field()
    profile = scrapy.Field()
    research_project = scrapy.Field()
    research_findings = scrapy.Field()
    research_interests = scrapy.Field()

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class ShetuimgdownloadPipeline:
    def process_item(self, item, spider):
        return item
from scrapy.pipelines.images import ImagesPipeline           #导入图片管道类
from scrapy import Request
#图片管道，继承于ImagesPipeline
class SaveImagePipeline(ImagesPipeline):
    #构造图像下载的请求，URL从item["image_urls"]中获取
    def get_media_requests(self, item, info):
        #将照片主题作为参数传递出去（用于设置存储图片存储路径）
        return [Request(x, meta={"title":item["title"]}) for x in item.get(self.images_urls_field, [])]

    #设置图片存储路径及名称
    def file_path(self, request, response=None, info=None, *, item=None):
        #从Request的meta中获取图片类型
        title = request.meta["title"]
        #图片名称
        image_name = request.url.split("/")[-1]
        #图片存储形式：图片类型/图片名称(sha1哈希值).jpg
        return "%s/%s"%(title, image_name)
    #以下是设置缩略图存储路径及名称
    def thumb_path(self, request, thumb_id, response=None, info=None):
        #从Request的meta中获取图片类型
        title = request.meta["title"]
        image_name = request.url.split("/")[-1]
        #缩略图路径：图片类型名/big(或small)/图片名称
        return '%s/%s/%s' % (title, thumb_id, image_name)
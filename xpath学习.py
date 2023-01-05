from lxml import etree
#使用xpath提取html的元素
html_selector = etree.parse("movies.html",etree.HTMLParser())
root = html_selector.xpath("/html")
print(root)

title = html_selector.xpath("/html/head/title")
print(title)

head = html_selector.xpath("/html/head")
print(len(head))
#以下进行二次匹配
for i in head:
    head_name = i.xpath("title/text()")
    print("head_name为："+str(head_name))

#text()获取元素内的文本
title_name = html_selector.xpath("/html/head/title/text()")
print("title_name为："+str(title_name))
#双斜线来省略之前的路径
movie_names = html_selector.xpath("//p/text()")
print(movie_names)
#id来限定对象
name = html_selector.xpath("//div[@id='content']/h1/text()")
print(name)

#使用@获取属性的值
meta = html_selector.xpath("//meta/@charset")
print(meta)
#..来访问父节点
attr = html_selector.xpath("//h1/../@id")
print(attr)
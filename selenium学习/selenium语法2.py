from selenium import webdriver
import time
#options是为了防止他可能的报错
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=options)                         #声明Chrome浏览器对象
driver.get("https://www.suning.com/")            #请求页面
time.sleep(5)                                          #等待5秒钟
#将进度条下拉到页面底部
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
input()
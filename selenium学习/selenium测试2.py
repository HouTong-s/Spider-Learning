from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
driver = webdriver.Chrome()                              #声明Chrome浏览器对象

driver.get("https://www.suning.com/")                      #请求页面
input = driver.find_element(By.ID, 'searchKeywords')       #查找节点
#如下写法已经过时了：input = driver.find_element_by_id("searchKeywords")     
input.clear()                                               #清除输入框中默认文字
input.send_keys("iphone")                                #输入框中输入iphone
input.send_keys(Keys.RETURN)                            #回车功能
wait = WebDriverWait(driver, 10)                       #设置显式等待时间为10秒
#最多等待10秒，直到某个ID的标签被加载
wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'root990')))
#获取源代码
print(driver.page_source)
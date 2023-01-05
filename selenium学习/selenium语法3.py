from selenium import webdriver                #导入浏览器驱动模块
from selenium.common.exceptions import TimeoutException     #导入异常模块
#options是为了防止他可能的报错
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=options)                         #声明Chrome浏览器对象
driver.get("https://www.suning.com/")            #请求页面
driver.set_page_load_timeout(5)               #设置页面加载的超时时间
try:
    driver.get("https://www.suning.com/")    #请求页面
    #将进度条下拉到页面底部
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    print(driver.page_source)
except TimeoutException:
    print("time out")
driver.quit()                                     #退出当前驱动并关闭所有关联窗口

from selenium import webdriver
driver = webdriver.Chrome()                    #声明Chrome浏览器对象
driver.implicitly_wait(15)                     #隐性等待，最长等15秒
driver.get("https://www.suning.com/")        #请求页面
print(driver.page_source)

from selenium import webdriver                          #导入浏览器驱动模块
from selenium.webdriver.common.by import By          #导入定位方式模块
from selenium.webdriver.support.ui import WebDriverWait     #导入等待模块
from selenium.webdriver.support import expected_conditions as EC
                                                        #导入预期条件模块
from selenium.common.exceptions import TimeoutException     #导入异常模块
driver = webdriver.Chrome()                              #声明Chrome浏览器对象
driver.get("https://www.suning.com/")                 #请求页面
try:
    #生成WebDriverWait对象，指定最长时间
    input= WebDriverWait(driver, 10).until(
        #设定预期条件
        EC.presence_of_element_located((By.ID, "searchKeywords"))
    )
    print(input)
except TimeoutException:                                 #因超时抛出异常
    print("time out! ")
finally:
    driver.quit()                                           #退出
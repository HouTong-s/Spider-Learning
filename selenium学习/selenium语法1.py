from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()               #声明浏览器对象
"""
driver = webdriver.Chrome()
driver = webdriver.ie()                    #声明IE浏览器对象
driver = webdriver.firefox()              #声明FireFox浏览器对象
driver = webdriver.phantomjs()           #声明Phantomjs浏览器对象
driver = webdriver.safari()               #声明Safari浏览器对象
"""
driver.get("https://www.suning.com/")            #请求页面
#通过id查找节点
input_id = driver.find_element(By.ID, 'searchKeywords')
#通过name查找节点
input_name = driver.find_element(By.NAME,"index1_none_search_ss2")
#通过class查找节点
input_class = driver.find_element(By.CLASS_NAME ,"search-keyword")
#通过xpath查找节点
input_xpath = driver.find_element(By.XPATH,"//input[@id='searchKeywords']")
#通过css查找节点
input_css = driver.find_element(By.CSS_SELECTOR,'#searchKeywords')
print(input_id, input_name, input_class, input_xpath, input_css)

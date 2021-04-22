import time
from selenium import webdriver
driver = webdriver.Edge('F:\pthon\msedgedriver.exe')   #初始化
driver.implicitly_wait(10)    #默认等待10S
#打开网页
def open_url(url,driver):
    driver.get(url)
    driver.maximize_window()


#登录封装成函数
def login(username,password,driver):
    driver.find_element_by_id('username').send_keys(username)    #输入用户名
    driver.find_element_by_id('password').send_keys(password)  # 输入密码
    driver.find_element_by_id('btnSubmit').click()  # 点击登录


#查询零售出库
def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login(username,password,driver)
    driver.find_element_by_xpath('//span[text()="零售出库"]').click()
    #通过xpath进行切换iframe,输入查询单据信息
    driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/pages/materials/retail_out_list.html"]'))
    driver.find_element_by_id('searchNumber').send_keys(s_key)
    #点击搜索按钮
    driver.find_element_by_id('searchBtn').click()
    #查询结果的判断：是否包含806
    time.sleep(3)
    num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
    return num

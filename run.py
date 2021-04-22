from python_web import demo_02
from testdata import tset_data
from selenium import webdriver

driver=webdriver.Edge('F:\pthon\msedgedriver.exe')
driver.implicitly_wait(10)
#取出传参的实参
url = tset_data.url['url']
user = tset_data.user_info['username']
pwd = tset_data.user_info['password']
s_key = tset_data.s_key['s_key']
print(url,user,pwd,s_key)
#调用函数
result_num = demo_02.search_key(url=url,driver=driver,username=user,password=pwd,s_key=s_key)
if s_key in result_num:
    print('查询结果正确！')
else:
    print('查询结果错误！')
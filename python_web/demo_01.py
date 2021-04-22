'''
web自动化
代码python---浏览器驱动---浏览器
selenium库：
1、ide：录制脚本 -- 实际使用不多
2、RC：
3、webdriver：利用浏览器原生api，直接操作浏览器页面的元素  ---重点掌握
4、分布式


2、浏览器驱动
谷歌驱动：http://npm.taobao.org/mirrors/chromedriver/
火狐：https://github.com/mozilla/geckodriver/releases
IE：http://selenium-release.storage.googleapis.com/index.html
Edge：https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
safari：https://developer.apple.com/safari/download/
1）下载对应浏览器版本的驱动
2）解压后得到后缀exe的文件，放到python安装目录下

3、元素定位  ---获取页面元素，进行接下来的操作。例如输入、点击等等
八种元素定位：id、name、xpath、css、class、tag、link_text、partial_link_text
1）id：当前整个html页面唯一，类比身份证信息（进行元素定位的首选，动态id不做考虑)
2）xpath
a、绝对路径：基本不用，一旦页面发生修改，页面元素就定位不到
   相对路径：//标签名[@属性名=属性值]  举例：//input[@id='username'] 登录用户名输入框
b、层级定位：  找上层
//标签名[@属性名=属性值]//标签名[@属性名=属性值]  举例：//div[@class='pull-left info']//p
c、文本属性定位： //标签名[text()='柠檬erp']
4、前端基础知识：web页面=html+css+JavaScript   简单了解




web页面常用操作：
1、打开浏览器
driver = webdriver.Chrome()
driver.get('http://erp.lemfix.com/login.html')
2、最大化浏览器
driver.maximize_window()
3、前进，后退和刷新操作
driver.back() #返回到上一个页面
driver.forward() #前进到下一个页面
driver.refresh() #刷新页面
4、关闭浏览器
关闭Chromedriver服务： driver.quit()
关闭当前窗口：driver.close()

5、等待方式
强制等待：time.sleep()
隐式等待：可以设置一个等待时间，在这个等待时间还没结束之前元素找到了，不继续等待，执行下面的代码
注意：一个session会话里只需要调用一次，对整个driver周期都生效

'''
import time

from selenium import webdriver
#启动浏览器，打开一个网址
# driver = webdriver.Edge('F:\pthon\msedgedriver.exe')
# driver.get('http://erp.lemfix.com/login.html')
# time.sleep(3)
#driver.get('http://www.baidu.com')

#浏览器窗口最大化
#driver.maximize_window()
#后退、前进、刷新
# driver.back()
# time.sleep(3)
# driver.forward()
# time.sleep(3)
# driver.refresh()


#关闭浏览器
#driver.close()   #关闭当前浏览器
#driver.quit()    #退出driver，关闭所有关联的浏览器窗口

#用例一：打开一个erp网址
driver = webdriver.Edge('F:\pthon\msedgedriver.exe')
driver.implicitly_wait(10)    #默认等待10S
driver.get('http://erp.lemfix.com/login.html')


#用例二：输入正确的用户名和密码，点击登录
driver.find_element_by_id('username').send_keys('13916686542')    #输入用户名
driver.find_element_by_id('password').send_keys('lemon123')       #输入密码
driver.find_element_by_id('btnSubmit').click()                    #点击登录
#time.sleep(2)


#用例三：判断页面登录用户是否正确
#login_user = driver.find_element_by_xpath('//p').text  #获取登录后的用户信息
login_user = driver.find_element_by_xpath("//div[@class='pull-left info']//p").text
if login_user == '13916686542':
    print('这个登录用户名是：{}'.format(login_user))
else:
    print('这个登录用户名不正确！')


#用例四：点击零售出库
driver.find_element_by_xpath('//span[text()="零售出库"]').click()


'''
在一个固定的地方可以切换多个页面，并且其他内容不变（左侧栏、右侧内容、顶部导航等）
整个html页面下面嵌套了一个html页面----iframe框架
1、识别是否有子页面的方式，页面层级路径中出现iframe，就需要切换iframe，才可以进行定位
2、怎么切换iframe？drive.switch_to.frame()
1)id或name去切换
2）xpath切换
3)通过iframe下标来定位：从0开始，初始html页面是0第一个子页面就是1，driver.switch_to.frame(1)


'''
#通过id切换iframe
#driver.switch_to.frame('tabpanel-f73b6a64aa-frame')  #id是动态的，不能通过id进行切换
#通过xpath进行切换iframe
#driver.switch_to.frame(driver.find_element_by_xpath('//iframe[@src="/pages/materials/retail_out_list.html"]'))
#通过下标方式定位
driver.switch_to.frame(1)
#用例五：单据编号框，输入806
driver.find_element_by_id('searchNumber').send_keys('806')
#点击搜索按钮
driver.find_element_by_id('searchBtn').click()
#查询结果的判断：是否包含806
#driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@filed="number"]/div').text()
time.sleep(3)
num = driver.find_element_by_xpath('//tr[@id="datagrid-row-r1-2-0"]//td[@field="number"]/div').text
if '806' in num:
    print('查询结果正确！')
else:
    print('查询结果错误！')




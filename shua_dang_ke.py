# 导包
from time import sleep
from selenium import webdriver
# 获取浏览器驱动对象

driver = webdriver.Firefox()
driver.implicitly_wait(3)
# 打开url
driver.get("http://dkxx.henu.edu.cn/PartyStudy/Main/ChapterStudy.aspx")
# 操作元素

username = driver.find_element_by_css_selector("input#TxtNum")
# 输入用户名(根据自己的实际情况输入)
username.send_keys("**********")
password = driver.find_element_by_css_selector("input#TxtPwd")
# 输入密码(根据自己的实际情况输入)
password.send_keys("**********")
btn1 = driver.find_element_by_css_selector("input#RBT2")
btn1.click()
btn2 = driver.find_element_by_css_selector("input#login")
btn2.click()

driver.find_element_by_partial_link_text("党课学习").click()

driver.find_element_by_xpath("//tr[6]//td[4]//a[1]").click()

while True:
    print("等待200秒")
    sleep(200)
    print("保存")
    driver.find_element_by_partial_link_text("保存学习时间").click()
    print("确认弹出框")
    driver.switch_to.alert.accept()
    print("点击党课学习")
    driver.find_element_by_partial_link_text("党课学习").click()
    print("点击进入")
    driver.find_element_by_xpath("//tr[6]//td[4]//a[1]").click()
    print("------------------------")





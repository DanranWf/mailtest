# -*- coding: utf-8 -*-
from time import sleep

from selenium import webdriver
#1打开浏览器
driver = webdriver.Chrome()
try:
    driver.maximize_window()
    driver.implicitly_wait(5)
    #2输入126网址
    driver.get("http://www.126.com")
    #3在登录页面上输入用户名和密码，点击登录
    driver.switch_to.frame(driver.find_element_by_xpath("//*[contains(@id,'x-URS-iframe')]"))
    driver.find_element_by_name("email").send_keys("mailtesty")
    driver.find_element_by_name("password").send_keys("aa123456")
    driver.find_element_by_id('dologin').click()
    driver.switch_to.default_content()
    #4在进入后的页面点击写信
    driver.find_element_by_xpath("//span[text()='写 信']").click()
    #5输入收件人的信息和标题，编写信件，点击发送
    driver.find_element_by_xpath("//input[@role='combobox']").send_keys("ytq12875@126.com")
    driver.find_element_by_xpath("//input[@class='nui-ipt-input' and @tabindex='1']").send_keys("测试发送邮件")
    driver.switch_to.frame(driver.find_element_by_xpath("//iframe[@tabindex='1']"))
    driver.find_element_by_css_selector('.nui-scroll').send_keys('''
    亲爱的 ytq12875：
        这封信是来自于自动化邮件发送学习的！
    ''')
    driver.switch_to.default_content()
    driver.find_element_by_xpath("//span[text()='发送']").click()
    #6在查看了结果后退出邮件系统，退出浏览器
    if "发送成功" in driver.page_source:
        print("邮件发送成功了")
        driver.find_element_by_xpath("//a[text()='退出']").click()
    else:
        print("邮件发送失败了")
except Exception as e:
    print(e)
finally:
    sleep(5)
    driver.quit()

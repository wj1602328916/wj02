import time
from selenium import webdriver

web=webdriver.Firefox()
# 跳转到QQ邮箱登陆页面
web.get("https://mail.qq.com/")

# 切换到frame中
web.switch_to.frame('login_frame')
time.sleep(1)
# 输入QQ号
web.find_element_by_id("u").send_keys("1602328916")
time.sleep(1)
# 输入密码
web.find_element_by_id("p").send_keys("wj19891031")
time.sleep(1)
# 点击登陆按钮
web.find_element_by_xpath('//*[@id="login_button"]').click()
time.sleep(3)
# 切换到主文档
web.switch_to.default_content()
time.sleep(10)

# 点击写信
web.find_element_by_id("composebtn").click()
time.sleep(3)

# 切换到主frame
web.switch_to.frame("mainFrame")
time.sleep(3)
# 切换到子frame
web.switch_to.frame(0)
web.find_element_by_xpath('//*[@id="toAreaCtrl"]/div/input').send_keys("2172008912@qq.com")
web.find_element_by_id("subject").send_keys("星期四")
# web.find_element_by_css_selector("body").send_keys("今天星期四")
web.switch_to.default_content()

web.switch_to.frame(1)
web.find_element_by_css_selector("body").send_keys("今天星期四")
# web.find_element_by_xpath('//*[@id="toAreaCtrl"]/div/input').send_keys("2172008912@qq.com")
# web.find_element_by_id("subject").send_keys("星期四")
time.sleep(2)

web.find_element_by_css_selector("#frm > div:nth-child(12) > div:nth-child(1) > a:nth-child(2)").click()
time.sleep(5)
web.quit()

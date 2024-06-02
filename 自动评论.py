from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
driver = webdriver.Chrome()
driver.get('https://bc.forobot.cn/student')
print("请登录")
sleep(60)
print("开始")
driver.get('输入作品地址')
while True:
    input_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#comment"))
    )
    input_box.send_keys('评论内容')
    submit_button = driver.find_element(By.CSS_SELECTOR, "body > div.layui-main > div.comment.ui.segment.project-segment > div.comment-editor > div > button")
    submit_button.click()
driver.quit()

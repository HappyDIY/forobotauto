from selenium import webdriver
import time
Web = "输入作品地址"
driver = webdriver.Chrome()
js = "window.open('{}', '_blank');".format(Web)
for x in range(16):
    driver.execute_script(js)
current_windows = driver.window_handles
while True:
    for window in current_windows:
        driver.switch_to.window(window)
        driver.refresh()
# -*- coding: big5 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time
import re



driver = webdriver.Firefox(executable_path=r'E:\software\anaconda3\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')  # 建立 driver 物件
driver.get('https://www.facebook.com/Fund4Rich/videos/267834297120845/')  # 連線至指定的網頁



# 需要登入的「稍後再說」
ele = WebDriverWait(driver, 10).until(
    ec.visibility_of_element_located((By.ID, 'expanding_cta_close_button'))
)
ele.click()
# 打開留言
ele = driver.find_element_by_class_name('_2u_j')



    

while True:
    try:
        # 不要有正在跑的小圈圈
        WebDriverWait(driver, 8).until_not(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '.mls.img._55ym._55yn._55yo')))
        ele = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, 'UFIShareLink')))
        
    except ElementClickInterceptedException:
        print('remove')
        # 移除下面的橫幕
        js = "document.getElementById('u_0_c').remove();"
        driver.execute_script(js)
    except TimeoutException:
        print('ok 1')
    break




for ele in driver.find_elements(By.CSS_SELECTOR, '_ipm_2x0m'):
    ele.click()
print('ok 2\n')


for comment in driver.find_elements_by_css_selector('span.UFICommentBody'):

    print(comment)
    print('\nfinish.\n')

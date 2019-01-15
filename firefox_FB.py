# -*- coding: big5 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, ElementClickInterceptedException
import time
import re



driver = webdriver.Firefox(executable_path=r'E:\software\anaconda3\Lib\site-packages\selenium\webdriver\firefox\geckodriver.exe')  # �إ� driver ����
driver.get('https://www.facebook.com/Fund4Rich/videos/267834297120845/')  # �s�u�ܫ��w������



# �ݭn�n�J���u�y��A���v
ele = WebDriverWait(driver, 10).until(
    ec.visibility_of_element_located((By.ID, 'expanding_cta_close_button'))
)
ele.click()
# ���}�d��
ele = driver.find_element_by_class_name('_2u_j')



    

while True:
    try:
        # ���n�����b�]���p���
        WebDriverWait(driver, 8).until_not(ec.presence_of_element_located(
            (By.CSS_SELECTOR, '.mls.img._55ym._55yn._55yo')))
        ele = WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.CLASS_NAME, 'UFIShareLink')))
        
    except ElementClickInterceptedException:
        print('remove')
        # �����U�������
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

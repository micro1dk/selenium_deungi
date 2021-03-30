import os
import time

from selenium.webdriver.common.by import By

from pyautogui_class import * 
from selenium_class import * 

CURRENT_PATH = os.getcwd()
  #  f = open('./htmls/뭐지.html', 'w', encoding='utf-8')
  #   for p in browser.driver.page_source:
  #     f.write(p)

def main():
  try:
    browser = IEBrowser()
    gui = PyautoGUI()

    browser.visit('http://www.iros.go.kr')

    browser.click(By.XPATH, '//*[@id="gnb"]/li[2]/h2/a/strong')
    browser.click(By.XPATH, '//*[@id="snb"]/ul/li[2]/a')
    time.sleep(0.3)
    browser.click(By.XPATH, '//*[@id="snb"]/ul/li[2]/ul/li[1]/ul/li[1]/ul/li[1]/a')
    
    # 항상 로그인함.. 그래서 alert를 기다림
    alert = browser.wait_alert()
    if '인증서 로그인' in alert.text:
      browser.accept_alert(alert)

    # alert 승인 후 전자신청로그인 공인인증서.
    browser.wait_element_visible(By.XPATH, '//*[@id="content2"]/div/div[2]/div[1]/div[1]/div/a[1]', 7)
    browser.click(By.XPATH, '//*[@id="content2"]/div/div[2]/div[1]/div[1]/div/a[1]')
    
    # 공인인증서 입력 화면
    gui.click_element(
      [f'{CURRENT_PATH}\\images\\access\\auth_harddisk_1.PNG', f'{CURRENT_PATH}\\images\\access\\auth_harddisk_2.PNG', f'{CURRENT_PATH}\\images\\access\\auth_harddisk_3.PNG'],
      '공인인증서 로그인 중 하드디스크 버튼이 없음', 0.3, 2.1, True
    )
    time.sleep(0.4)

    gui.click_element(
      [f'{CURRENT_PATH}\\images\\access\\auth_park_1.PNG', f'{CURRENT_PATH}\\images\\access\\auth_park_2.PNG',],
      '공인인증서 로그인 중 박지환 선택지가 없음', 0.3, 1.2, True
    )
    
    for _ in range(4):
      pyautogui.press(['tab'])
      time.sleep(0.2)
    time.sleep(0.7)
    pyautogui.write('*pnk0070**')

    gui.click_element(
      f'{CURRENT_PATH}\\images\\access\\auth_ok.PNG',
      '공인인증서 로그인 중 확인버튼이 없음', 0.3, 1.2, True
    )
    
    browser.wait_element_visible(By.XPATH, '//*[@id="id_user_pin"]', 7)
    pyautogui.write('*PNK0070')
    browser.click(By.XPATH, '//*[@id="content2"]/form/div[2]/button')
    ### 로그인 완료
    
    ### 신규 클릭
    browser.click(By.XPATH, '//*[@id="Lcontent"]/form/div[7]/button[1]')
    time.sleep(0.4) # 더블클릭해야 들어가짐..?
    browser.click(By.XPATH, '//*[@id="Lcontent"]/form/div[7]/button[1]')

  except Exception as e:
    print('에러발생! : ', e)

main()
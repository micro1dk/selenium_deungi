import os
import sys
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from classes.pyautogui_class import PyautoGUI
from classes.selenium_class import IEBrowser

from paths import *

class Login(IEBrowser, PyautoGUI):
  def __init__(self):
    super().__init__()
    self.IMAGE_PATH = f'{IMAGE_PATH}\\access'

  def script(self):
    try:
      self.visit('http://www.iros.go.kr')
      
      self.close_new_window_by_selector('xpath', '/html/body/div[2]/div/label', 2, 0.3, 0.9)

      self.click_element('xpath', '//*[@id="gnb"]/li[2]/h2/a/strong')
      self.click_element('xpath', '//*[@id="snb"]/ul/li[2]/a')
      time.sleep(0.3)
      self.click_element('xpath', '//*[@id="snb"]/ul/li[2]/ul/li[1]/ul/li[1]/ul/li[1]/a')

      # 항상 로그인함.. 그래서 alert를 기다림
      alert = self.wait_alert()
      if '인증서 로그인' in alert.text:
        self.accept_alert(alert)

      # alert 승인 후 전자신청로그인 공인인증서
      self.wait_element_visible('xpath', '//*[@id="content2"]/div/div[2]/div[1]/div[1]/div/a[1]', 7)
      self.click_element('xpath', '//*[@id="content2"]/div/div[2]/div[1]/div[1]/div/a[1]')

      # 공인인증서 입력 화면
      self.click_image(
        [f'{self.IMAGE_PATH}\\auth_harddisk_1.PNG', f'{self.IMAGE_PATH}\\auth_harddisk_2.PNG', f'{self.IMAGE_PATH}\\auth_harddisk_3.PNG'],
        '공인인증서 로그인 중 하드디스크 버튼이 없음', 0.3, 2.7, True
      ); time.sleep(0.4)

      self.click_image(
        [f'{self.IMAGE_PATH}\\auth_park_1.PNG', f'{self.IMAGE_PATH}\\auth_park_2.PNG',],
        '공인인증서 로그인 중 박지환 선택지가 없음', 0.3, 1.2, True
      )

      for _ in range(4):
        self.press_key(['tab'])
        time.sleep(0.2)
      time.sleep(0.7)
      self.write_key('*pnk0070**'); time.sleep(0.2)
      self.press_key(['enter'])

      # 로그인 완료
      self.wait_element_visible('xpath', '//*[@id="id_user_pin"]', 7)
      self.write_key('*PNK0070')
      self.click_element('xpath', '//*[@id="content2"]/form/div[2]/button')
      
      self.close_new_window_by_selector('xpath', '//*[@id="doNotOpen"]', 2, 0.3, 0.9)  

    except Exception as e:
      print('에러발생: ', e)

def main():
  login = Login()
  login.script()
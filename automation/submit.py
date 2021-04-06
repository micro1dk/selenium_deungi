import os
import sys
import time

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from classes.pyautogui_class import PyautoGUI
from classes.selenium_class import IEBrowser

from paths import *

class Submit(IEBrowser, PyautoGUI):
  def __init__(self):
    super().__init__()
  
  def script(self):
    #신규 클릭
    self.click_element('xpath', '//*[@id="Lcontent"]/form/div[7]/button[1]')
    time.sleep(0.4) # 더블클릭해야 들어가짐..?
    self.click_element('xpath', '//*[@id="Lcontent"]/form/div[7]/button[1]')

    # 이제부터 시트 정보가 필요함

def main():
  submit = Submit()
  submit.script()
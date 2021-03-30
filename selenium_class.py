import time

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert

class IEBrowser:
  def __init__(self):
    self.driver = webdriver.Ie('./driver/IEDriverServer.exe')
  
  def visit(self, url):
    self.driver.get(url)

  def click(self, by, selector, timeout=7):
    self.wait_element_visible(by, selector, timeout)
    if by == By.XPATH:
      self.driver.find_element_by_xpath(selector).click()
    elif by == By.ID:
      self.driver.find_element_by_id(selector).click()
    elif by == By.CLASS_NAME:
      self.driver.find_element_by_class_name(selector).click()
    elif by == By.TAG_NAME:
      self.driver.find_element_by_tag_name(selector).click()

  def type_keys(self, by, selector, string):
    if by == By.XPATH:
      self.driver.find_element_by_xpath(selector).send_keys(string)
    elif by == By.ID:
      self.driver.find_element_by_id(selector).send_keys(string)
    elif by == By.CLASS_NAME:
      self.driver.find_element_by_class_name(selector).send_keys(string)
    elif by == By.TAG_NAME:
      self.driver.find_element_by_tag_name(selector).send_keys(string)

  ### alert 함수
  def wait_alert(self):
    t = 0
    while True:
      success, elem = self.exist_alert()
      if success:
        return elem
      time.sleep(0.3)
      t += 0.3
      if t >= 3:
        raise Exception('알러트없음')
      
  def exist_alert(self):
    try:
      alert = self.driver.switch_to.alert
      return True, alert
    except Exception as e:
      print(e)
      return False, None

  def accept_alert(self, alert):
    alert.accept()

  ### 로딩함수
  def wait_element_visible(self, by, selector, timeout):
    WebDriverWait(self.driver, timeout).until(
      EC.visibility_of_element_located((by, selector))
    )
  def wait_element_presence(self, by, selector, timeout):
    WebDriverWait(self.driver, timeout).until(
      EC.presence_of_element_located((by, selector))
    )
  def wait_element_inivisible(self, by, selector, timeout):
    WebDriverWait(self.driver, timeout).until(
      EC.invisibility_of_element_located((by, selector))
    )
  def wait_new_window(self, length, delay, timeout):
    t = 0
    while True:
      if len(self.driver.window_handles) >= length:
        return True
      time.sleep(delay)
      t += delay
      if t >= timeout:
        return False
  
  ### 스위치 함수
  def switch_windows(self, n):
    self.driver.switch_to.window(self.driver.window_handles[n - 1])

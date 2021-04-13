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
        # self.driver = webdriver.Chrome('./driver/chromedriver.exe')

    def visit(self, url):
        self.driver.get(url)

    def str_to_by(self, string):
        if string == 'xpath':
            return By.XPATH
        elif string == 'id':
            return By.ID
        elif string == 'class':
            return By.CLASS_NAME
        elif string == 'tag':
            return By.TAG_NAME

    def click_element(self, by, selector, timeout=7):
        self.wait_element_visible(by, selector, timeout)
        self.driver.find_element(self.str_to_by(by), selector).click()
        time.sleep(0.8)

    def type_keys(self, by, selector, string):
        self.driver.find_element(self.str_to_by(
            by), selector).type_keys(string)

    # alert 함수
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

    # 로딩함수
    def wait_element_visible(self, by, selector, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located((by, selector))
        )

    def wait_element_presence(self, by, selector, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.presence_of_element_located((by, selector))
        )

    def wait_element_invisible(self, by, selector, timeout=10):
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((by, selector))
        )

    def wait_new_window(self, length, delay=0.5, timeout=7):
        """
        새로운 창이 뜰 때까지 대기
        """
        t = 0
        while True:
            if len(self.driver.window_handles) >= length:
                return True
            time.sleep(delay)
            t += delay
            if t >= timeout:
                return False

    def wait_element_clickable(self, by, selector, timeout=7):
        WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable((by, selector))
        )

    # 스위치 함수
    def switch_windows(self, n):
        self.driver.switch_to.window(self.driver.window_handles[n - 1])

    def select_element(self, by, selector, value):
        """
        셀렉트 박스에서 어떤 값을 선택
        """
        select = Select(self.driver.find_element(self.str_to_by(by), selector))
        select.select_by_value(value)

    def exist_element(self, by, selector):
        try:
            t = self.driver.find_element(self.str_to_by(by), selector)
            del t
            return True
        except Exception as e:
            return False

    def close_new_window_by_selector(self, by, selector, n, delay=0.5, timeout=7):
        """
        timeout 만큼 새로운 윈도우가 뜨기를 기다린 후, 어떤 selector를 통해 새 윈도우를 닫습니다.
        새 창이 나오지 않을 때 작업 하지 않음
        """
        new_window = self.wait_new_window(n, delay, timeout)
        if new_window:
            self.switch_windows(n)
            self.click_element(by, selector)
            self.switch_windows(n - 1)

    def close_new_window(self, by, n, delay=0.5, timeout=7):
        """
        selenium driver close 기능을 이용하여 닫음
        """
        new_window = self.wait_new_window(n, delay, timeout)
        if new_window:
            self.switch_windows(n)
            self.driver.close()
            self.switch_windows(n - 1)

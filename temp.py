import os
import time

from pyautogui_class import * 
from selenium_class import * 

CURRENT_PATH = os.getcwd()

def main():
  try:
    browser = IEBrowser()
    gui = PyautoGUI()
    browser.visit('http://www.iros.go.kr/')
    
    exist_new_window = gui.click_element(
      f'{CURRENT_PATH}\\images\\access\\new_window.PNG',
      '', 0.3, 1.2, False
    )
    if exist_new_window:
      gui.click_element(
        f'{CURRENT_PATH}\\images\\access\\new_window_close.PNG',
        '오늘 열지 않음 창 닫기가 없음\nnew_window_close.PNG', 0.3, 1.2, True
      )

    gui.click_element(
      f'{CURRENT_PATH}\\images\\access\\tab_deungi_first.PNG',
      '등기신청버튼이 없음', 0.3, 1.2, True
    )


    gui.click_element(
      f'{CURRENT_PATH}\\images\\access\\corp_apply.PNG',
      '법인 버튼이 없음', 0.3, 1.2, True
    )
    time.sleep(0.3)
    gui.click_element(
      f'{CURRENT_PATH}\\images\\access\\corp_apply_next.PNG',
      '신청서작성 및 제출 버튼이 없음', 0.3, 1.2, True
    )
    
    not_login, elem = gui.wait_element_visible(
      [f'{CURRENT_PATH}\\images\\access\\if_not_login_msg.PNG', f'{CURRENT_PATH}\\images\\access\\if_not_login_warn.PNG'],
      0.3, 1.2
    )

    if not_login:
      
      gui.click_element(
        [f'{CURRENT_PATH}\\images\\common\\ok_normal.PNG', f'{CURRENT_PATH}\\images\\common\\ok_blue_1.PNG', f'{CURRENT_PATH}\\images\\common\\ok_blue_2.PNG', f'{CURRENT_PATH}\\images\\common\\ok_blue_3.PNG'],
        '', 0.3, 1.2, False
      )
      time.sleep(1)
      gui.click_element(
        f'{CURRENT_PATH}\\images\\access\\corp_login_btn.PNG',
        '전자신청로그인 버튼이 없음', 0.3, 2.1, True
      )

      gui.click_element(
        [f'{CURRENT_PATH}\\images\\access\\auth_harddisk_1.PNG', f'{CURRENT_PATH}\\images\\access\\auth_harddisk_2.PNG', f'{CURRENT_PATH}\\images\\access\\auth_harddisk_3.PNG'],
        '공인인증서 로그인 중 하드디스크 버튼이 없음', 0.3, 2.1, True
      )

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

      time.sleep(3)

      gui.click_element(
        f'{CURRENT_PATH}\\images\\access\\auth_ps_2.PNG',
        '사용자인증 중 사용자등록번호 문자가 없음', 0.3, 3, True
      )
      pyautogui.write('*PNK0070')
      gui.click_element(
        f'{CURRENT_PATH}\\images\\access\\auth_ok_complete.PNG',
        '사용자인증 중 확인버튼이 없음', 0.3, 1.2, True
      )

    ### 여기까지가 로그인~~
    gui.click_element(
      f'{CURRENT_PATH}\\images\\common\\close_btn.PNG',
      '', 0.3, 4.2, False
    )

    gui.click_element(
      f'{CURRENT_PATH}\\images\\new\\singyu.PNG',
        '신규버튼이 없음', 0.3, 1.2, True
    )

      


  except Exception as e:
    print('에러발생! : ', e)

main()
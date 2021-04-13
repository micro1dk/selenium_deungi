
import asyncio

from automation import *

from classes.selenium_class import IEBrowser

"""
납세번호는 비동기


"""

browser = IEBrowser()
loop = asyncio.get_event_loop()
loop.run_until_complete(login.main(browser.driver))
loop.close
# login.main(browser.driver)
# submit.main(browser.driver)

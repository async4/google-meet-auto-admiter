import re
import sys
import time

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, WebDriverException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys


class Admiter:
    def __init__(self, driver):
        self.driver = driver
        self.__connection = False
    
    @property
    def connection(self):
        return self.__connection
    
    @connection.setter
    def connection(self, value):
        self.__connection = value

    def connect(self):
        link = "https://apps.google.com/intl/en-US/meet/"
        print("🌐 waiting {}" .format(link))

        try:
            self.driver.get(link)
            print("✅ connection success")
            self.connection = True
        except:
            print("❌ connection error")
            self.connection = False

    def parse_url(self, url):
        regex = r"^((http|https)\:\/\/(meet\.google\.com\/)?[a-z]{0,}\-[a-z]{0,}\-[a-z]{0,})"
        matches = re.finditer(regex, url)
        
        for match_num, match in enumerate(matches, start=1):
            if match.group():
                return True

        return False

    def is_admit(self):
        admit_button = "//body/div[@id='yDmH0d']/div[3]/div[1]/div[2]/div[3]/div[3]/span[1]/span[1]"
        try:
            element = self.driver.find_element(By.XPATH, admit_button)
            element.click()
            print("🥳 Incoming request accepted")
        except:
            pass

    def listen(self):
        while self.connection:
            if self.driver:
                try:
                    current_url = self.driver.current_url
                    print("🟢 {}" .format(current_url))
                    
                    if self.parse_url(current_url):
                        self.is_admit()
                        pass

                except ConnectionRefusedError:
                    print("🔴 {}" .format("connection refused. reconnecting"))
                    continue
                except WebDriverException:
                    print("💀 Driver shutdown. ( {} )" .format(datetime.now()))
                    self.connection = False
                finally:
                    time.sleep(0.5)
            else:
                print("🔎 Driver not found")
                sys.exit()



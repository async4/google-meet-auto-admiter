import os
import sys
import time

from datetime import datetime

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from admiter import admiter as adm

base_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'google-meet-auto-admiter')
driver_url = os.path.join(base_dir, 'driver')

driver_win32_url = 'win32\{version}\chromedriver.exe'
driver_darwin_url = 'darwin/{version}/chromedriver'
driver_linux_url = 'linux/{version}/chromedriver'


def info(os_name, chromedriver_path):
    print("🕕 Time: {}\n💻 OS: {}\n🔥 Chrome Driver: {}\n" .format(datetime.now(), os_name, chromedriver_path))

def run(chromedriver_path):
    with webdriver.Chrome(executable_path=chromedriver_path) as driver:
        admiter = adm.Admiter(driver)
        admiter.connect()
        admiter.listen()

def main():
    os_name = sys.platform
    chromedriver_path = None

    if os_name == "win32":
        chromedriver_path = os.path.join(driver_url, driver_win32_url.format(version='86'))
    elif os_name == "darwin":
        chromedriver_path = os.path.join(driver_url, driver_darwin_url.format(version='86'))
    else:
        chromedriver_path = os.path.join(driver_url, driver_linux_url.format(version='86'))
    
    info(os_name, chromedriver_path)
    run(chromedriver_path)
    
    
if __name__ == '__main__':
    main()

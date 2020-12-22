import os
import sys
import time

from datetime import datetime
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from admiter import admiter as adm


def main():
    print("🕕 Time: {}\n💻 OS: {}\n" .format(datetime.now(), sys.platform))

    with webdriver.Chrome(ChromeDriverManager().install()) as driver:
        admiter = adm.Admiter(driver)
        admiter.connect()
        admiter.listen()
    
    
if __name__ == '__main__':
    main()

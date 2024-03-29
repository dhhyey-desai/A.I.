import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

from bs4 import BeautifulSoup
from urllib.parse import urlparse
import sys


class Fetcher:
    def __init__(self, url):
        self.driver = webdriver.PhantomJS()
        self.driver.wait = WebDriverWait(self.driver, 5)
        self.url = url
        print(self.url)

    def lookup(self):
        self.driver.get(self.url)
        try:
            ip = self.driver.wait.until(EC.presence_of_all_elements_located(
                (By.CLASS_NAME, "gsfi")
            ))
        except:
            print("Sorry that didn't work")

        soup = BeautifulSoup(self.driver.page_source, "html.parser")
        answer = soup.find_all(class_="_sPg")

        with open("test.html", "w+") as f:
            f.write(str(soup))

        if not answer:
            answer = soup.find_all(class_="rl7ilb")

        if not answer:
            answer = "I don't know."

        self.driver.quit()
        return answer[3].get_text()


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

class Scraper:
    @staticmethod
    def fetch_latest_version():
        options = Options()
        options.headless = True 
        options.add_argument('--disable-gpu')
        options.add_argument('--no-sandbox')

        service = Service(executable_path=GeckoDriverManager().install(), log_path='NUL')

        driver = webdriver.Firefox(service=service, options=options)

        try:
            driver.get("https://www.nvidia.com/en-in/geforce/drivers/results/228255/")
            driver.implicitly_wait(10)
            version_element = driver.find_element(By.ID, "ddVersion_td")
            version_text = version_element.text
            version_number = version_text.split(" - ")[0] if " - " in version_text else version_text
            return version_number.replace('.', '')
        finally:
            driver.quit()
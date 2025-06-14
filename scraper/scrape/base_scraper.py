from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

class BaseScraper:
    def __init__(self, headless: bool = True):
        chromium_options = Options()
        if headless:
            chromium_options.add_argument("--headless=new")
        chromium_options.add_argument("--disable-gpu")
        chromium_options.add_argument("--no-sandbox")

        self.driver = webdriver.Chrome(
            service=Service(ChromeDriverManager().install()),
            options=chromium_options
        )

    def get(self, url: str, delay: float = 1.0):
        """Navigate to a URL and wait for content to load."""
        self.driver.get(url)
        time.sleep(delay)
        return self.driver.page_source
    
    def quit(self):
        self.driver.quit()
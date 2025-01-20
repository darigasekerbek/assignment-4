import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
from PIL import Image


chrome_options = Options()
chrome_options.add_argument("--headless") 
chrome_options.add_argument("--disable-gpu")


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def test_google_search():
    try:
       
        driver.get("https://www.google.com")

        
        assert "Google" in driver.title

      
        screenshot_path = "screenshot_google_home.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")

       
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Test search")
        search_box.submit()

        time.sleep(3)  

      
        screenshot_after_search = "screenshot_google_search.png"
        driver.save_screenshot(screenshot_after_search)
        print(f"Screenshot saved at {screenshot_after_search}")

    except Exception as e:
        print(f"Test failed due to: {str(e)}")
        raise e

    finally:
        
        driver.quit()


if __name__ == "__main__":
    pytest.main()

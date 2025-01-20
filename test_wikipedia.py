import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

logging.basicConfig(
    filename="wikipedia_test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)

def test_wikipedia():
    try:
        logging.info("====== WebDriver manager ======")
        
        service = Service(ChromeDriverManager().install())  
        driver = webdriver.Chrome(service=service)

        logging.info("Открытие Wikipedia...")

        
        driver.get("https://www.wikipedia.org")
        
       
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "search")))

        logging.info("Запрос 'Python (programming language)' отправлен.")
        
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("Python (programming language)")
        search_box.send_keys(Keys.RETURN)

        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "mp-upper")))

        logging.info("Результаты поиска загружены.")

        header = driver.find_element(By.ID, "firstHeading")
        if "Python" in header.text:
            logging.info(f"Заголовок статьи: {header.text}")
        else:
            logging.error(f"Ошибка: Заголовок не соответствует ожиданиям.")
        
        driver.quit()
        logging.info("Браузер закрыт.")
    
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        driver.quit() 

if __name__ == "__main__":
    test_wikipedia()

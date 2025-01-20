import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# Устанавливаем логирование
logging.basicConfig(
    filename="wikipedia_test_log.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding='utf-8'
)

def test_wikipedia():
    try:
        logging.info("====== WebDriver manager ======")
        # Инициализация WebDriver с использованием Service
        service = Service(ChromeDriverManager().install())  # Установка и использование chromedriver через webdriver-manager
        driver = webdriver.Chrome(service=service)

        logging.info("Открытие Wikipedia...")

        # Открытие Wikipedia
        driver.get("https://www.wikipedia.org")
        
        # Убедимся, что страница загружена, подождав появления элемента
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.NAME, "search")))

        logging.info("Запрос 'Python (programming language)' отправлен.")
        
        # Ввод поиска в строку
        search_box = driver.find_element(By.NAME, "search")
        search_box.send_keys("Python (programming language)")
        search_box.send_keys(Keys.RETURN)

        # Ожидание появления результатов поиска
        WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, "mp-upper")))

        logging.info("Результаты поиска загружены.")

        # Ожидание появления заголовка статьи
        header = driver.find_element(By.ID, "firstHeading")
        if "Python" in header.text:
            logging.info(f"Заголовок статьи: {header.text}")
        else:
            logging.error(f"Ошибка: Заголовок не соответствует ожиданиям.")
        
        # Закрытие браузера
        driver.quit()
        logging.info("Браузер закрыт.")
    
    except Exception as e:
        logging.error(f"Ошибка: {e}")
        driver.quit()  # Закрытие браузера в случае ошибки

if __name__ == "__main__":
    test_wikipedia()

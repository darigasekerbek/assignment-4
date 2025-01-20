import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
import os
from PIL import Image

# Инициализация Chrome WebDriver
chrome_options = Options()
chrome_options.add_argument("--headless")  # Запуск в фоновом режиме
chrome_options.add_argument("--disable-gpu")

# Устанавливаем драйвер
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

def test_google_search():
    try:
        # Открытие страницы Google
        driver.get("https://www.google.com")

        # Проверка, что мы на главной странице Google
        assert "Google" in driver.title

        # Сохранение скриншота на главной странице
        screenshot_path = "screenshot_google_home.png"
        driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")

        # Поиск поля поиска и ввод запроса
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys("Test search")
        search_box.submit()

        time.sleep(3)  # Ждем загрузку результатов

        # Сохранение скриншота после поиска
        screenshot_after_search = "screenshot_google_search.png"
        driver.save_screenshot(screenshot_after_search)
        print(f"Screenshot saved at {screenshot_after_search}")

    except Exception as e:
        print(f"Test failed due to: {str(e)}")
        raise e

    finally:
        # Закрытие браузера
        driver.quit()

# Запуск теста
if __name__ == "__main__":
    pytest.main()

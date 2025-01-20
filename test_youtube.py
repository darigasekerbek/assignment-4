from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

def test_youtube():
    # Инициализация WebDriver с использованием Service
    service = Service(ChromeDriverManager().install())  # Установка и использование chromedriver через webdriver-manager
    driver = webdriver.Chrome(service=service)

    try:
        # Открытие YouTube
        driver.get("https://www.youtube.com")
        print("Открыт YouTube.")

        # Ожидание загрузки страницы и появления строки поиска
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.NAME, "search_query")))

        # Ввод поиска в строку
        search_box = driver.find_element(By.NAME, "search_query")
        search_box.send_keys("Selenium tutorial")
        search_box.send_keys(Keys.RETURN)

        # Ожидание появления результатов
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "contents")))

        # Ищем первое видео на странице
        first_video = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, "//ytd-video-renderer//a[@id='video-title']")))

        # Кликаем на первое видео
        first_video.click()
        print("Кликнули на видео.")

        # Ожидаем, что откроется новое окно или вкладка
        WebDriverWait(driver, 20).until(EC.number_of_windows_to_be(2))  # Ожидаем открытия нового окна

        # Переключаемся на новое окно
        main_window = driver.current_window_handle
        new_window = [window for window in driver.window_handles if window != main_window][0]
        driver.switch_to.window(new_window)
        print("Переключились на новое окно.")

        # Ожидаем, что видео загрузится
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, "video")))

        # Задержка для того, чтобы посмотреть результат (например, 10 секунд)
        time.sleep(10)

        print("Видео успешно открылось.")

    except Exception as e:
        print(f"Ошибка: {e}")

    finally:
        driver.quit()
        print("Браузер закрыт.")


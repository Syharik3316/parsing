from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def scrape_aliexpress(url):
    options = Options()
    options.headless = True
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    driver = webdriver.Chrome(options=options)

    results = []
    try:
        driver.get(url)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.TAG_NAME, 'body'))
        )
        time.sleep(2)

        try:
            title_el = driver.find_element(By.CSS_SELECTOR, 'h1.snow-ali-kit_Typography__base__1shggo')
            title = title_el.text.strip()
        except:
            title = 'Название не найдено'

        try:
            price_el = driver.find_element(By.CSS_SELECTOR, 'div.HazeProductPrice_SnowPrice__mainS__1wzo3')
            price = price_el.text.strip()
        except:
            price = 'Цена не найдена'

        results.append({'title': title, 'price': price})

    except Exception as e:
        print("Error during scraping:", e)
    finally:
        driver.quit()

    return results

from selenium import webdriver
from selenium.common.exceptions import (
    TimeoutException,
)
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from datetime import datetime

def setup_driver():
    with open("/Users/johndoe/PycharmProjects/baby_jacket_checker/web_scraping_baby_jacket/profile_path.txt", "r") as f:

        profile_path = f.read().strip()

    options = Options()
    options.add_argument("-profile")
    options.add_argument(profile_path)

    return webdriver.Firefox(options=options)


def get_availability(url):
    driver = setup_driver()
    size_available = ""
    wait = WebDriverWait(driver, 15)
    try:
        driver.get(url)

        size_dropdown = wait.until(
            EC.presence_of_element_located(
                (By.CSS_SELECTOR, "div[role='combobox'][aria-labelledby='size-input-label']")
            )
        )
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", size_dropdown)
        ActionChains(driver) \
            .move_to_element(size_dropdown) \
            .pause(0.2) \
            .click_and_hold(size_dropdown) \
            .pause(0.2) \
            .release(size_dropdown) \
            .perform()
        wait.until(
            lambda current_driver: current_driver.find_element(
                By.CSS_SELECTOR,
                "div[role='combobox'][aria-labelledby='size-input-label']",
            ).get_attribute("aria-expanded")
            == "true"
        )

        size_options = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[role='option']"))
        )

        for option in size_options:
            if option.text[0:2] == "80":
                size_available = option.text.strip()

    except TimeoutException:
        return None
    finally:
        driver.quit()
    return size_available

def write_to_file(size_available, log_reference):
    date = datetime.now().strftime("%Y-%m-%d-%H-%M")
    width = 12

    with open("/Users/johndoe/PycharmProjects/baby_jacket_checker/web_scraping_baby_jacket/main.log", "a") as logger:
        logger.write(f"{date}: {log_reference:^{width}} - {size_available}\n")
if __name__ == "__main__":
    write_to_file("https://www.nextdirect.com/hu/en/style/su148815/av0999")
    write_to_file("https://www.nextdirect.com/hu/en/style/su148815/g12753")

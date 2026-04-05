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
log_file = "/Users/johndoe/PycharmProjects/baby_jacket_checker/web_scraping_baby_jacket/main.log"
def setup_driver():

    profile_path = "/Users/johndoe/Library/Application Support/Firefox/Profiles/qyd7PSVJ.Profile 2"
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
        with open(log_file, "a") as f:
            f.write(f"TimeoutException on this url: {url}\n")
        return None
    finally:
        driver.quit()
    my_size = size_available.split()
    size_availability = [my_size[0] if my_size else None, my_size[-1] if my_size else None]

    print("SizeAvailability:", size_availability)
    return size_availability

def write_to_file(size_available, log_reference):
    date = datetime.now().strftime("%Y-%m-%d-%H-%M")
    width = 12

    with open(log_file, "a") as logger:
        logger.write(f"{date}: {log_reference:^{width}} - {size_available}\n")
if __name__ == "__main__":
    crocodile_size_available = get_availability("https://www.nextdirect.com/hu/en/style/su148815/av0999")
    write_to_file(crocodile_size_available, "crocodile")
    # write_to_file("https://www.nextdirect.com/hu/en/style/su148815/g12753","fox")

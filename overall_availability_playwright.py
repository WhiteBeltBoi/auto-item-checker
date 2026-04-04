from playwright.sync_api import sync_playwright
from datetime import datetime

def get_page_info(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)

        page = browser.new_page()
        page.goto(url)
        size_dropdown = page.locator("div[role='combobox'][aria-labelledby='size-input-label']")
        size_dropdown.click()

        size_options = page.locator("li[role='option'][data-value = '28']")
        # size_options.first.wait_for(state="visible")

        my_size = size_options.text_content().split()
        browser.close()

        size_availability =[my_size[0], my_size[-1] if my_size else None]

        return size_availability

def write_log(size_availability, type_):
    width = 10
    date = datetime.now().strftime("%Y-%m-%d-%H-%M")
    log_file = "/Users/johndoe/PycharmProjects/baby_jacket_checker/web_scraping_baby_jacket/main.log"
    with open(log_file, "a") as logger:
        logger.write(f"{date}: {type_:^{width}} - {size_availability[0]} : {size_availability[-1]}\n")


if __name__ == "__main__":
    result = get_page_info("https://www.nextdirect.com/hu/en/style/su148815/av0999")
    write_log(result, "crocodile")
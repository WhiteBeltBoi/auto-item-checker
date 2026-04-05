from playwright.sync_api import sync_playwright, TimeoutError as PTimeoutError
from datetime import datetime

def get_page_info(url):
    with sync_playwright() as p:
        browser = p.firefox.launch(headless=False)

        page = browser.new_page()
        page.goto(url, timeout=10000)
        if page.locator("h1", has_text = "Access Denied").is_visible():
            write_log("oo","Bot got detected")
            exit()
        try:
            size_dropdown = page.locator("div[role='combobox'][aria-labelledby='size-input-label']")
            size_dropdown.click(timeout = 10000)
        except PTimeoutError:
            write_log("oo","TimeoutError")
            browser.close()
        try:
            size_options = page.locator("li[role='option'][data-value = '28']")
            size_options.first.wait_for(state="visible", timeout=8000)
        except PTimeoutError:
            write_log("oo","TimeoutError")
            browser.close()


        my_size = size_options.text_content().split()
        browser.close()

        size_availability =[my_size[0], my_size[-1] if my_size else None]

        return size_availability

def write_log(size_availability , type_):
    width = 11
    date = datetime.now().strftime("%Y-%m-%d-%H-%M")
    log_file = "/Users/johndoe/PycharmProjects/baby_jacket_checker/web_scraping_baby_jacket/main.log"
    with open(log_file, "a") as logger:
        logger.write(f"{date}: {type_:^{width}} - {size_availability[0]} : {size_availability[-1]}\n")


if __name__ == "__main__":
    result = get_page_info("https://www.nextdirect.com/hu/en/style/su148815/av0999")
    write_log(result, "crocodile")
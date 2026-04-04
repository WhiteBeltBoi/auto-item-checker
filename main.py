from overall_availability_playwright import write_log, get_page_info
from send_text import send_text

crocodile_url = "https://www.nextdirect.com/hu/en/style/su148815/av0999"
fox_url = "https://www.nextdirect.com/hu/en/style/su148815/g12753"

crocodile_size_available = get_page_info(crocodile_url)
write_log(crocodile_size_available, "crocodile")
if crocodile_size_available and "unavailable" not in crocodile_size_available:
    send_text( crocodile_size_available[0],"crocodile")

fox_size_available = get_page_info(fox_url)
write_log(fox_size_available, "fox")
if fox_size_available and "unavailable"  not in fox_size_available:
    send_text( fox_size_available[0], "fox")

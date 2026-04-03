from crocodile_overall_availability import write_to_file, get_availability
from send_text import send_text

crocodile_url = "https://www.nextdirect.com/hu/en/style/su148815/av0999"
fox_url = "https://www.nextdirect.com/hu/en/style/su148815/g12753"

crocodile_size_available = get_availability(crocodile_url)
write_to_file(crocodile_size_available, "crocodile")
if crocodile_size_available and crocodile_size_available.split()[-1].lower() != "unavailable":
    send_text( "crocodile")

fox_size_available = get_availability(fox_url)
write_to_file(fox_size_available, "fox")
if fox_size_available and fox_size_available.split()[-1].lower() != "unavailable":
    send_text( "fox")
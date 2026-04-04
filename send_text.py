import subprocess

def send_text(size: str,type_:str):
    with open("/Users/johndoe/PycharmProjects/baby_jacket_checker/web_scraping_baby_jacket/phone_number.txt") as f:
        phone_number = f.read()
    message = f"The {type_} baby jacket in size {size} is available."
    script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone_number}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''

    subprocess.run(["osascript", "-e", script], check=True)


if __name__ == "__main__":
    send_text("80", "croc")
import subprocess

def send_text(type_:str):
    phone_number = "+36309507721"
    message = f"The {type_} baby jacket is available."
    script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone_number}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''

    subprocess.run(["osascript", "-e", script], check=True)


if __name__ == "__main__":
    send_text("/Users/johndoe/PycharmProjects/baby_jacket_checker/web_scraping_baby_jacket/av0999_log.txt")
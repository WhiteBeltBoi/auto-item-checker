import subprocess

with open("log.txt", "r") as f:
    info = f.read().split()

if info and info[-1] != "unavailable":
    print("Great success!")
    phone_number = "+36309507721"
    message = "The baby jacket is available."
    script = f'''
    tell application "Messages"
        set targetService to 1st service whose service type = iMessage
        set targetBuddy to buddy "{phone_number}" of targetService
        send "{message}" to targetBuddy
    end tell
    '''

    subprocess.run(["osascript", "-e", script], check=True)
else:
    exit(1)

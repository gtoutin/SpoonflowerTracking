import requests
import re
import os
import sys


OS = "mac"
FAIL_MESSAGE = "Uh oh! Something's up with your Spoonflower shop! Go check it out."
APP_TITLE = "Daily Spoonflower Shop Check"

def main():
    page_data = str(requests.get(f"https://www.spoonflower.com/profiles/{SHOP_NAME}").content)
    if (re.search(rf"by {SHOP_NAME}", page_data) is None):
        notify(APP_TITLE, FAIL_MESSAGE, OS) # SOMETHING IS WRONG


def notify(title, message, opsys):
    """Notify the macOS user their shop is messed up"""
    if (opsys == "mac"):
        os.system(f"""
        osascript -e 'display notification "{message}" with title "{title}"'
        """)
    elif (opsys == "linux"):
        os.system(f"""zenity --info --text="{message}" """)


if __name__ == '__main__':
    try:
        SHOP_NAME = sys.argv[1]
    except:
        print("Expecting a command line argument SHOP_NAME")
        exit
    if (len(sys.argv) == 3):
        OS = sys.argv[2]
    main()
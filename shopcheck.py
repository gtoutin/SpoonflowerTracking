import requests
import re
import os
import sys



FAIL_MESSAGE = "Uh oh! Something's up with your Spoonflower shop! Go check it out."
APP_TITLE = "Daily Spoonflower Shop Check"

def main():
    page_data = str(requests.get(f"https://www.spoonflower.com/profiles/{SHOP_NAME}").content)
    if (re.search(rf"by {SHOP_NAME}", page_data) is None):
        notify(APP_TITLE, FAIL_MESSAGE) # SOMETHING IS WRONG


def notify(title, message):
    """Notify the macOS user their shop is messed up"""
    os.system(f"""
    osascript -e 'display notification "{message}" with title "{title}"'
    """)


if __name__ == '__main__':
    SHOP_NAME = sys.argv[1]
    main()
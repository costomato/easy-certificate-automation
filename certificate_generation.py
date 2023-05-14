from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import csv
import os
import json

from dotenv import load_dotenv
load_dotenv()

with open('sorted.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    students = list(reader)

chrome_options = Options()
chrome_options.add_argument('--kiosk-printing')
chrome_options.add_argument('--disable-extensions')
chrome_options.add_argument('--no-margins')
chrome_options.add_argument('--enable-background-graphics')
chrome_options.add_argument('--print-to-pdf')
chrome_options.add_argument('--landscape')

settings = {
    "recentDestinations": [{
        "id": "Save as PDF",
        "origin": "local",
        "account": ""
    }],
    "selectedDestinationId": "Save as PDF",
    "version": 2,
    "isHeaderFooterEnabled": False,
    "customMargins": {
        "marginTop": 0,
        "marginBottom": 0,
        "marginLeft": 0,
        "marginRight": 0
    },
    "customMargins": {},
    "marginsType": 1,
    "scalingType": 3,
    "scaling": 128,
    "isCssBackgroundEnabled": True,
    "isLandscapeEnabled": True,
    "isMarginsEnabled": False,
    "isScalingEnabled": True,
    "isSelectionOnly": False,
    "isBackgroundGraphicsEnabled": True,
    "isCloudPrint": False,
    "deviceName": "Local Destination",
}

chrome_options.add_argument('--enable-print-browser')
# chrome_options.add_argument('--headless')

prefs = {
    'printing.print_preview_sticky_settings.appState': json.dumps(settings),
    'savefile.default_directory': os.getcwd() + '/certificates'
}
chrome_options.add_experimental_option('prefs', prefs)

browser = webdriver.Chrome(options=chrome_options)

browser.get(os.getenv('CERTIFICATE_URL'))

time.sleep(1)

# Replace the span tag with the student name
span = browser.find_element('xpath', '/html/body/div[1]/div/main/div/div/div/div[2]/div/div/div/div[1]/div/div/div[18]/div/div/p/span')

# Iterate through the list of students and save the PDF for each
for student_name in students:
    student_mail = student_name["UNIVERSITY MAIL ID:"]
    student_name = student_name["NAME"]

    browser.execute_script(f"arguments[0].innerHTML = \"{student_name}\"", span)

    # save as pdf
    pdf_file = f'certificates/{student_mail}.pdf'
    browser.execute_script('return window.print();')
    os.rename('certificates/Certificate designs.pdf', pdf_file)

browser.quit()

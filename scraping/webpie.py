#!/usr/bin/python3
"""
Usage: ./webpie.py <URL> <DIRECTORY>

Scrapes websites for images by echoing network requests
"""

from seleniumwire import webdriver  # Import from seleniumwire
from selenium.webdriver.firefox.options import Options
import requests
import os, sys

S_THRESHOLD = 90000

print("Started application")

# Create a new headless instance of the Firefox driver
options = Options()
options.headless = True
driver = webdriver.Firefox(options=options)

# Go to the URL
filepath = f"images/{sys.argv[2]}"
driver.get(sys.argv[1])

# Make directory from arg2
try: 
    os.mkdir(filepath) 
except OSError as error: 
    print(error)

headers = {"Accept-Encoding": 'identity'}

# Naming images
img_num = 1


# Access requests via the `requests` attribute
for request in driver.requests:
    # split header into initator and type
    header = str(request.response.headers['Content-Type'])
    initator, _ = header.split('/')

    # Filters out unwanted requests
    if request.response and initator == "image":
        r = requests.get(request.url, headers=headers)
        # Check sufficient image size (avoid thumbnails)
        if len(r.content) > S_THRESHOLD: 
            with open(f"{filepath}/{img_num}.jpg", 'wb') as f:
                f.write(r.content)
        
        img_num += 1
        print(f"Downloaded image from {request.url} to {filepath}\n")


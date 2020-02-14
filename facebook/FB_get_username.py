from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import csv, re
import time

def get_username():
    options = Options()
    options.add_argument('--headless')
    base = open('facebook/FB_available_account.csv')
    a = csv.reader(base)

    driver = webdriver.Firefox(executable_path='facebook/geckodriver', options=options)

    with open('facebook/fb_account.csv', 'w') as f:
        w = csv.writer(f)
        w.writerow(['user_id', 'username'])
        for row in a:
            driver.get("https://fb.com/{}".format(row[0]))
            print(row[0])
            time.sleep(2)
            url = driver.current_url
            print(url)
            re1 = re.sub('^.*.com\/', '', str(url))
            re2 = re.sub('\/', '', re1)
            print(re2)
            w.writerow([row[0], re2])


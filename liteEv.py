import time
from collections import Counter
from selenium import webdriver
from tqdm import tqdm
import random
from rich.console import Console

console = Console()
browser = webdriver.Chrome('/home/rajath/Downloads/chromedriver_linux64/chromedriver')
browser.maximize_window()
browser.get('https://op.hooah.us/admin.php?s=/admin/public/login.html')
console.print('[INFO....] Logging in with credentials ***********', style='bold green')
username = browser.find_element_by_name('username')
username.click()
username.send_keys('Ritesh')
passwd = browser.find_element_by_name('password')
passwd.click()
passwd.click()
passwd.send_keys('Ritesh40@guruji')
passwd.submit()
time.sleep(0.5)
browser.get('https://op.hooah.us/admin.php?s=/guruji/userlogininfo/index.html')
uid = browser.find_elements_by_xpath('//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr')

vals = []
console.print('[INFO....] Fetching UIDs', style='blue')
for pageNo in tqdm(range(1, 30), unit='uids'):
    for i in range(1, len(uid) + 1):
        vals.append(browser.find_element_by_xpath(
            f'//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[{i}]/td[2]').text)
    browser.get(f'https://op.hooah.us/admin.php?s=/guruji/userlogininfo/index/p/{pageNo}.html')

console.print(f'[INFO....] UIDs Fetched totally were {len(vals)} of which {len(set(vals))} are unique', style='bold blue')
vals = set(vals)
console.print('[INFO....] Sending Coupons to Fetched UIDs', style='green')

for i in tqdm(vals, unit='coupons'):
    browser.get(
        f'https://op.hooah.us/admin.php?s=/Guruji/Couponusersend/choose_coupon_batch/user_id/{i}/country/1.html')
    time.sleep(0.5)
    tw20 = browser.find_element_by_xpath(
        '//*[@id="main"]/div[1]/div/div/div/div/form/div/div[2]/div/div[2]/label/span[2]')
    tw20.click()
    save = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[4]/button[2]')
    save.click()
    console.print(f'UID --> {i} Sent Once (200Rs)', style="bold green")
    time.sleep(1.0)
    browser.get(
        f'https://op.hooah.us/admin.php?s=/Guruji/Couponusersend/choose_coupon_batch/user_id/{i}/country/1.html')
    tw20percent = browser.find_element_by_xpath(
        '//*[@id="main"]/div[1]/div/div/div/div/form/div/div[2]/div/div[8]/label/span[2]')
    tw20percent.click()
    save = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[4]/button[2]')
    save.click()
    console.print(f'UID --> {i} Sent Twice (20%)', style="bold green")
    time.sleep(1.0)

console.print(f'Done sending coupons enjoy!', style="bold green")
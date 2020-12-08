import time
from collections import Counter
from selenium import webdriver
from tqdm import tqdm
import random

browser = webdriver.Chrome('/home/rajath/Downloads/chromedriver_linux64/chromedriver')
browser.get('https://op.hooah.us/admin.php?s=/guruji/orderserviceevaluation/index/p/1.html')
username = browser.find_element_by_name('username')
username.click()
username.send_keys('Ritesh')
passwd = browser.find_element_by_name('password')
passwd.click()
passwd.click()
passwd.send_keys('Ritesh40@guruji')
passwd.submit()
browser.get('https://op.hooah.us/admin.php?s=/guruji/orderserviceevaluation/index.html')
browser.get('https://op.hooah.us/admin.php?s=/guruji/orderserviceevaluation/index.html')
uid = browser.find_elements_by_xpath("//*[@id='main']/div[1]/div/div[2]/div/div/div/div/table/thead/tr/th")
uid = browser.find_elements_by_xpath("//*[@id='main']/div[1]/div/div[2]/div/div/div/div/table/thead/tr")

uid = browser.find_elements_by_xpath("//*[@id='main']/div[1]/div/div[2]/div/div/div/div/table/thead/tr/th")
cols = browser.find_elements_by_xpath('//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/thead/tr/th')
uid = browser.find_elements_by_xpath("//*[@id='main']/div[1]/div/div[2]/div/div/div/div/table/tbody/tr")
uuid = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/thead/tr/th[4]')

vals = []

for pageNo in tqdm(range(3, 5), ):
    for i in range(1, len(uid) + 1):
        vals.append(browser.find_element_by_xpath(
            f'//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[{i}]/td[4]').text)
    browser.get(f'https://op.hooah.us/admin.php?s=/guruji/orderserviceevaluation/index/p/{pageNo}.html')

d = {}

for i in range(len(vals)):
    d[vals[i]] = vals.count(vals[i])
print(d)
time.sleep(1.5)
browser.get('https://op.hooah.us/admin.php?s=/guruji/rechargepaymentorderlist/index.html')

idAmt = {}
for keys in tqdm(d.keys()):
    browser.get(f'https://op.hooah.us/admin.php?s=/guruji/rechargepaymentorderlist/index.html&keyword={keys}')
    time.sleep(0.5)
    amtLen = len(browser.find_elements_by_xpath('//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr'))
    lst = []
    for i in range(1, amtLen + 1):
        try:
            lst.append(browser.find_element_by_xpath(
                f'//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[{i}]/td[7]').text)
        except Exception as e:
            print(e)
            continue
    idAmt[keys] = lst

for idv in idAmt.keys():
    browser.get(
        f'https://op.hooah.us/admin.php?s=/Guruji/Couponusersend/choose_coupon_batch/user_id/{idv}/country/1.html')
    _200Off = browser.find_element_by_css_selector(
        '#main > div.tab-content.ct-tab-content > div > div > div > div > form > div > div.form-group.item_batch_id > div > div:nth-child(2)')
    _500Off = browser.find_element_by_css_selector(
        '#main > div.tab-content.ct-tab-content > div > div > div > div > form > div > div.form-group.item_batch_id > div > div:nth-child(3)')
    _800Off = browser.find_element_by_css_selector(
        '#main > div.tab-content.ct-tab-content > div > div > div > div > form > div > div.form-group.item_batch_id > div > div:nth-child(4)')
    _1000Off = browser.find_element_by_css_selector(
        '#main > div.tab-content.ct-tab-content > div > div > div > div > form > div > div.form-group.item_batch_id > div > div:nth-child(5)')
    _2000Off = browser.find_element_by_css_selector(
        '#main > div.tab-content.ct-tab-content > div > div > div > div > form > div > div.form-group.item_batch_id > div > div:nth-child(6)')
    _10perOff = browser.find_element_by_css_selector(
        '#main > div.tab-content.ct-tab-content > div > div > div > div > form > div > div.form-group.item_batch_id > div > div:nth-child(7)')
    _20perOff = browser.find_element_by_css_selector(
        '#main > div.tab-content.ct-tab-content > div > div > div > div > form > div > div.form-group.item_batch_id > div > div:nth-child(8)')
    _25perOff = browser.find_element_by_css_selector(
        '#main > div.tab-content.ct-tab-content > div > div > div > div > form > div > div.form-group.item_batch_id > div > div:nth-child(9)')

    val = max(Counter(idAmt[idv]).most_common(3))[0]
    if int(val) < 1000:
        if int(val) == 200:
            r = [_200Off, _20perOff]
            lr = random.choice(r)
            lr.click()
            save = browser.find_element_by_xpath('//button[@class="btn btn-primary submit ajax-post visible-md-inline visible-lg-inline"]') # save
            save.click()
            print(f'{idv} ---> {lr}')

            time.sleep(0.5)
        elif int(val) == 500:
            r = [_500Off, _20perOff]
            lr = random.choice(r)
            lr.click()
            save = browser.find_element_by_xpath('//button[@class="btn btn-primary submit ajax-post visible-md-inline visible-lg-inline"]')
            save.click()
            print(f'{idv} ---> {lr}')

            time.sleep(0.5)
        elif int(val) == 800:
            r = [_200Off, _20perOff]
            lr = random.choice(r)
            lr.click()
            save = browser.find_element_by_xpath('//button[@class="btn btn-primary submit ajax-post visible-md-inline visible-lg-inline"]')
            save.click()
            print(f'{idv} ---> {lr}')

            time.sleep(0.5)
        elif int(val) == 1000:
            r = [_1000Off, _20perOff]
            lr = random.choice(r)
            lr.click()
            save = browser.find_element_by_xpath('//button[@class="btn btn-primary submit ajax-post visible-md-inline visible-lg-inline"]')
            save.click()
            print(f'{idv} ---> {lr}')
    else:
        r = [_2000Off, _25perOff]
        lr = random.choice(r)
        lr.click()
        save = browser.find_element_by_xpath('//button[@class="btn btn-primary submit ajax-post visible-md-inline visible-lg-inline"]')
        save.click()
        print(f'{idv} ---> {lr}')
        time.sleep(0.5)
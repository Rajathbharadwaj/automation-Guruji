
import time
from collections import Counter
from selenium import webdriver
from tqdm import tqdm
import random

browser = webdriver.Chrome('/home/rajath/Downloads/chromedriver_linux64/chromedriver')
browser.maximize_window()
browser.get('https://op.hooah.us/admin.php?s=/guruji/orderserviceevaluation/index/p/1.html')
username = browser.find_element_by_name('username')
username.click()
username.send_keys('Ritesh')
passwd = browser.find_element_by_name('password')
passwd.click()
passwd.click()
passwd.send_keys('Ritesh40@guruji')
passwd.submit()
browser.get('https://op.hooah.us/admin.php?s=/guruji/liveusergiftorder/index.html')
browser.get('https://op.hooah.us/admin.php?s=/guruji/liveusergiftorder/index.html')
uid = browser.find_elements_by_xpath("//*[@id='main']/div[1]/div/div[2]/div/div/div/div/table/thead/tr/th")
uid = browser.find_elements_by_xpath("//*[@id='main']/div[1]/div/div[2]/div/div/div/div/table/thead/tr")

uid = browser.find_elements_by_xpath("//*[@id='main']/div[1]/div/div[2]/div/div/div/div/table/thead/tr/th")
cols = browser.find_elements_by_xpath('//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/thead/tr/th')
uid = browser.find_elements_by_xpath("//*[@id='main']/div[1]/div/div[2]/div/div/div/div/table/tbody/tr")
uuid = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/thead/tr/th[4]')

vals = []

for pageNo in tqdm(range(0,1), ):
    for i in range(1, len(uid) + 1):
        vals.append(browser.find_element_by_xpath(
            f'//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr[{i}]/td[5]').text)
    browser.get(f'https://op.hooah.us/admin.php?s=/guruji/liveusergiftorder/index/p/{pageNo}.html')

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
    try:
        br = browser.get(
            f'https://op.hooah.us/admin.php?s=/guruji/couponusersend/index.html&keyword={idv}')
        time.sleep(0.5)
        sc = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div[2]/div/div/div/div/table/tbody/tr/td[8]/div/a')
        sc.click()
        time.sleep(0.5)
        _200Off = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[2]/div/div[2]/label/span[1]')
        _500Off = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[2]/div/div[3]/label/span[1]')
        _800Off = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[2]/div/div[4]/label/span[1]')
        _1000Off = browser.find_element_by_xpath(
            '//*[@id="main"]/div[1]/div/div/div/div/form/div/div[2]/div/div[5]/label/span[1]')
        _2000Off = browser.find_element_by_xpath(
            '//*[@id="main"]/div[1]/div/div/div/div/form/div/div[2]/div/div[6]/label/span[1]')
        _10perOff = browser.find_element_by_xpath(
            '/html/body/div[2]/div/div/div[2]/div[1]/div/div/div/div/form/div/div[2]/div/div[7]/label/span[1]')
        _20perOff = browser.find_element_by_xpath(
            '//*[@id="main"]/div[1]/div/div/div/div/form/div/div[2]/div/div[8]/label/span[1]')
        _25perOff = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[2]/div/div[10]/label/span[1]')

        val = max(Counter(idAmt[idv]).most_common(3))[0]
        val = int(float(val))
        print(val)
        if int(val) < 1000:
            if int(val) <= 200 or int(val) < 500:
                r = [_200Off, _20perOff]
                lr = random.choice(r)
                lr.click()
                time.sleep(0.5)
                save = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[4]/button[2]') # save
                save.click()
                print(f'{idv} ---> {lr}')

                time.sleep(0.5)
            elif int(val) == 500 or int(val) < 800:
                r = [_500Off, _20perOff]
                lr = random.choice(r)
                lr.click()
                time.sleep(0.5)
                save = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[4]/button[2]')
                save.click()
                print(f'{idv} ---> {lr}')

                time.sleep(0.5)
            elif int(val) == 800 or int(val) < 1000:
                r = [_200Off, _20perOff]
                lr = random.choice(r)
                lr.click()
                time.sleep(0.5)
                save = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[4]/button[2]')
                save.click()
                print(f'{idv} ---> {lr}')

                time.sleep(0.5)
            elif int(val) == 1000:
                r = [_1000Off, _20perOff]
                lr = random.choice(r)
                lr.click()
                time.sleep(0.5)
                save = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[4]/button[2]')
                save.click()
                print(f'{idv} ---> {lr}')
        else:
            r = [_2000Off, _25perOff]
            lr = random.choice(r)
            lr.click()
            time.sleep(0.5)
            save = browser.find_element_by_xpath('//*[@id="main"]/div[1]/div/div/div/div/form/div/div[4]/button[2]')
            save.click()
            print(f'{idv} ---> {lr}')
            time.sleep(0.5)
    except Exception as e:
        print(e)
        continue
from urllib.request import urlopen, Request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
import time
import warnings
from tqdm import tqdm
from selenium.webdriver.common.keys import Keys
import pandas as pd

warnings.filterwarnings(action='ignore')

baseUrl = "https://www.instagram.com/explore/tags/"
plusUrl = input('검색할 태그를 입력하세요 : ')
url = baseUrl + quote_plus(plusUrl)

print("Chrome Driver를 실행합니다.")
driver = webdriver.Chrome()

driver.get(url)
time.sleep(30)

pageString = driver.page_source
bsObj = BeautifulSoup(pageString, 'lxml')
temp_data = bsObj.find_all(name='meta')[-1]
temp_data = str(temp_data)
start = temp_data.find('게시물') + 4
end = temp_data.find('개')
total_data = temp_data[start:end]
print("총 {0}개의 게시물이 검색되었습니다.".format(total_data))

"""태그 크롤링"""
print("게시물을 수집하는 중입니다.")

SCROLL_PAUSE_TIME = 1.0
reallink = []

#페이지 끝까지 보는 코드
while True:
    pageString = driver.page_source
    bsObj = BeautifulSoup(pageString, 'lxml')

    for link1 in bsObj.find_all(name='div', attrs={"class":"Nnq7C weEfm"}):
        for i in range(3):
            title = link1.select('a')[0]
            real = title.attrs['href']
            reallink.append(real)
            title = link1.select('a')[1]
            real = title.attrs['href']
            reallink.append(real)
            title = link1.select('a')[2]
            real = title.attrs['href']
            reallink.append(real)
            
    last_height = driver.execute_script('return document.body.scrollHeight')
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(SCROLL_PAUSE_TIME)
    new_height = driver.execute_script("return document.body.scrollHeight")

    if new_height == last_height:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")

        if new_height == last_height:
            break
        else:
            last_height = new_height
            continue

    # 게시물의 개수가 계속 바뀌거나 전체 게시물을 가져오지 못한다면
    # 아래 time.sleep의 시간(초)을 늘려주세요.
    time.sleep(2)

# 데이터 개수 
num_of_data = len(reallink)

print('총 {0}개의 데이터를 수집합니다.'.format(num_of_data))
csvtext = []

#미완성
for i in tqdm(range(num_of_data)):

    #게시물 마다 해시태그 검색
    csvtext.append([])
    req = Request('https://www.instagram.com/p'+reallink[i], headers={'User-Agent': 'Mozila/5.0'})

    webpage = urlopen(req).read()
    soup = BeautifulSoup(webpage, 'lxml', from_encoding='utf-8')

    # !!고쳐야할 부분 = 아이디 크롤링
    soup1 = soup.select('span.Jv7Aj  MqpiF')
    
    reallink1 = soup1

    if reallink1 == '':
        reallink1 = "Null"
    csvtext[i].append(reallink1)

    # !!고쳐야할 부분 = 해시태그 크롤링
    for reallink2 in soup.find_all(name='a', attrs={'class':"xil3i"}):
        hashtags = reallink2['href'].rstrip('#')
        csvtext[i].append(hashtags)

    # csv로 저장

    data = pd.DataFrame(csvtext)
    data.to_csv('insta.txt', encoding='utf-8')

driver.close()
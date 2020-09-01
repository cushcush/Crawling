from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import pandas as pd
import requests

from urllib.request import urlopen
from urllib.parse import quote_plus
from bs4 import BeautifulSoup

# instagram_tags = []
# instagram_date = []
# instagram_url = []
# instagram_userid = []

# 연결부분1
# URL = 'http://cush.kr:7770/api/add'

Search_Tag = input('검색할 태그를 입력하세요 : ')

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}
# url ='https://www.instagram.com/'
# html = requests.get(url, headers = headers).text

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')

time.sleep(3)
elem = driver.find_element_by_name('username')
elem.send_keys('kuminkyu93@naver.com')
elem = driver.find_element_by_name('password')
elem.send_keys('tkfkd325!')
    
time.sleep(3)

#로그인 클릭 버튼
login_button = driver.find_element_by_xpath('/html/body/div/section/main/article/div[2]/div/div/form/div/div[3]/button')
login_button.click()
time.sleep(3)

#나중에 하기1
later_1 = driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div/div/div/button')
later_1.click()
time.sleep(3)

#나중에 하기2
later_2 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
later_2.click()
time.sleep(3)

#검색
search_1 = driver.find_element_by_xpath('/html/body/div/section/nav/div[2]/div/div/div[2]/input')
search_1.send_keys(Search_Tag)
time.sleep(2)

#검색 엔터1
search_1.send_keys(Keys.ENTER)
time.sleep(2)

#검색 엔터2 (작동)
search_1.send_keys(Keys.ENTER)
time.sleep(3)

driver.find_element_by_css_selector('#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1) > a > div.eLAPa > div._9AhH0').click()
time.sleep(2)

all_data = []

# instagram_url.append(0)
# instagram_tags.append(0)
# instagram_date.append(0)
# instagram_userid.append(0)

# html = driver.page_source
# soup = BeautifulSoup(html,"html.parser")

# insta = soup.select('#react-root > section > main > article > div:nth-child(3) > div > div:nth-child(1) > div:nth-child(1)')

k = 5

# n = 1
# for i in insta:
#     print('https://www.instagram.com' + i.a['href'])
#     imgUrl = i.select_one('.KL4Bh').img['src']
#     with urlopen(imgUrl) as f:
#         with open('./img/' + Search_Tag + str(n) + '.jpg','wb') as h:
#             img = f.read()
#             h.write(img)
#     n += 1
    
#     if i == k:
#         break
    

#크롤링 범위설정
for i in range(k):
    time.sleep(1)
    try:
        
        # print(int(i/3)+1, str((i%3)+1))

        element = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div['+str(int(i/3)+1)+']/div['+str((i%3)+1)+']/a')
        url = element.get_attribute('href')
        
        print(url)

        element2 = driver.find_element_by_xpath('/html/body/div[1]/section/main/article/div[2]/div/div['+str(int(i/3)+1)+']/div['+str((i%3)+1)+']/a/div[1]/div[1]/img')
        imgUrl = element2.get_attribute('src')

        print(imgUrl)

        i = i+1

        with urlopen(imgUrl) as f:
            with open('./img/' + Search_Tag + str(i) + '.jpg','wb') as h:
                img = f.read()
                h.write(img)

        data = driver.find_element_by_css_selector('.C7I1f.X7jCj')  # C7I1f X7jCj  # 글이 있는 구역
        tag_raw = data.text
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)

        # print(tags)
        
        # body 안에 있는 태그 요소는 .text 로 추출할 수 있습니다. 
        # https://www.fun-coding.org/crawl_advance5.html

        # date 출력
        # date = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/div[2]/a/time')
        # print(date.text)
        # instagram_date.append(data.text)

        # User_ID 출력
        userid = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/article/div[3]/div[1]/ul/div/li/div/div/div[2]/h2/div/span/a')
        
        # print(userid.text)
        
        # 리스트에 값 넣기

        # 연결부분2
        # tmp_dict = {
        #     'url': url,
        #     'imgUrl': imgUrl, 
        #     'hashtag': tags,
        #     'userID': userid.text, 
        # }

        # res = requests.post(URL, data=tmp_dict)


    except:
        # instagram_tags.append("error")
        print('error')

    try:
        WebDriverWait(driver, 100).until( #값을 불러올때까지 기다려줌 
            EC.presence_of_element_located((By.CSS_SELECTOR, '.C7I1f.X7jCj'))
        )
        driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div '
                                            '> a._65Bje.coreSpriteRightPaginationArrow').click() # 다음 버튼
    except:
        driver.close()

    time.sleep(2)

# print(instagram_tags)

#.txt파일로 저장
# data_tags = pd.DataFrame(instagram_tags)
# data_tags.to_csv('insta_tags.txt', encoding='utf-8')

# data_date = pd.DataFrame(instagram_date)
# data_date.to_csv('insta_date.txt', encoding='utf-8')

# data_userid = pd.DataFrame(instagram_userid)
# data_userid.to_csv('insta_userid.txt', encoding='utf-8')

# data_url = pd.DataFrame(instagram_url)
# data_url.to_csv('insta_url.txt', encoding='utf-8')

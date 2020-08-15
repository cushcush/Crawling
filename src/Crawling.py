from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
import pandas as pd

instagram_tags = []
instagram_tag_dates = []

plusUrl = input('검색할 태그를 입력하세요 : ')

driver = webdriver.Chrome()

driver.get('https://www.instagram.com/')
time.sleep(5)
elem = driver.find_element_by_name('username')
elem.send_keys('아이디입력')
elem = driver.find_element_by_name('password')
elem.send_keys('')
    
time.sleep(5)

#로그인 클릭 버튼
login_button = driver.find_element_by_xpath('/html/body/div/section/main/article/div[2]/div/div/form/div/div[3]/button')
login_button.click()
time.sleep(5)

#나중에 하기1
later_1 = driver.find_element_by_css_selector('#react-root > section > main > div > div > div > div > button')
later_1.click()
time.sleep(5)

#나중에 하기2
later_2 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
later_2.click()
time.sleep(5)

#검색
search_1 = driver.find_element_by_xpath('/html/body/div/section/nav/div[2]/div/div/div[2]/input')
search_1.send_keys(plusUrl)
time.sleep(2)

#검색 엔터1
search_1.send_keys(Keys.ENTER)
time.sleep(2)

#검색 엔터2 (작동)
search_1.send_keys(Keys.ENTER)
time.sleep(2)

driver.find_element_by_css_selector('#react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1)'
                                    ' > div:nth-child(1) > a > div > div._9AhH0').click()
time.sleep(2)

#크롤링 범위설정
for i in range(10):
    time.sleep(1)
    try:
        data = driver.find_element_by_css_selector('.C7I1f.X7jCj')  # C7I1f X7jCj  # 글이 있는 구역
        tag_raw = data.text
        
        tags = re.findall('#[A-Za-z0-9가-힣]+', tag_raw)
        tag = ''.join(tags).replace("#", " ")  # "#" 제거

        tag_data = tag.split()

        for tag_one in tag_data:
            instagram_tags.append(tag_one)
            
    #print(instagram_tags)
   
    except:
        instagram_tags.append("error")
        instagram_tag_dates.append('error')

    try:
        WebDriverWait(driver, 100).until( #값을 불러올때까지 기다려줌 
            EC.presence_of_element_located((By.CSS_SELECTOR, '.C7I1f.X7jCj'))
        )
        driver.find_element_by_css_selector('body > div._2dDPU.CkGkG > div.EfHg9 > div > div '
                                            '> a._65Bje.coreSpriteRightPaginationArrow').click() # 다음 버튼
    except:
        driver.close()

    time.sleep(2)

print(instagram_tags)

#.txt파일로 저장
data = pd.DataFrame(instagram_tags)
data.to_csv('insta.txt', encoding='utf-8')

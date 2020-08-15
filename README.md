# Crawling

### 크롤링 순서
1. 로그인 (id,pw미리 입력해놓은것으로 로그인)
1. 나중에 하기 버튼 클릭
1. 나중에 하기 한번더 클릭
1. 검색창 클릭
1. 입력한 텍스트 검색
1. 입력된 해시태그 중 가장 위에 있는 해시태그 검색
1. 검색된 해시태그 중 가장 먼저 있는 게시물 클릭
1. <반복구간>
    1. 게시물에 해시태그 검색
    1. 다음 페이지 넘어가기
    1. 크롤링한 데이터 .txt파일로 저장

### 롤링 위치
- 로그인: /html/body/div/section/main/article/div[2]/div/div/form/div/div[3]/button
- 나중에하기1: /html/body/div/section/main/div/div/div/section/div/button
- 나중에하기2: /html/body/div[4]/div/div/div/div[3]/button[2]
- 검색: /html/body/div/section/nav/div[2]/div/div/div[2]/input
- 텍스트: /html/body/div[3]/div[2]/div/article/div[3]/div/ul/div/li/div/div
- 다음버튼: /html/body/div[3]/div/div/div/a[2]
- 첫 게시물: #react-root > section > main > article > div.EZdmt > div > div > div:nth-child(1) > div:nth-child(1) > a > div > div._9AhH0
- 다음버튼: body > div._2dDPU.CkGkG > div.EfHg9 > div > div > a._65Bje.coreSpriteRightPaginationArrow

### 환경 설정
1. python 다운로드 & 환경변수 설정 (버전 맞추기!)
1. git 다운로드 & 환경변수 설정
1. VSCODE 에 GIT 설치
    VSCODE에서 Ctrl + Shift + X 확장 검색창에서 실행
    githistory, gitlens 를 설치해준다.
1. chromedriver.exe 버전 맞추기
1. vscode에서 필요한 pip install 해주기 (selenium,pandas등)

## 버튼 위치 찾는 방법
1. copy selector
#react-root > section > main > div > div > div > div > button

1. copy Xpath => """ 앞뒤로 따움표 3개 입력 필요 """
//*[@id="react-root"]/section/main/div/div/div/div/button
https://coding-0830.tistory.com/9

1. copy full Xpath
/html/body/div[1]/section/main/div/div/div/div/button

/html/body/div[1]/section/main/div/div/div/div/button

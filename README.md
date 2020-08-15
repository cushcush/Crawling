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
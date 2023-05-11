#프로젝트에 필요한 패키지를 불러온다
import requests # requests 패키지 가져오기
from bs4 import BeautifulSoup as bs # BeautifulSoup 패키지 불러오기, bs로 이름을 간단히 바꿈

#검색할 키워드를 받아 url 생성
query = input('검색할 키워드를 입력하세요: ')
url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+'%s'%query

# requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
response = requests.get(url)    

# 얻고자 하는 html 문서가 여기에 담기게 됨
html_text = response.text

# bs4 패키지의 함수를 이용해서 html 문서를 파싱
soup = bs(html_text, 'html.parser')

#bs4 패키지의 select 함수와 선택자 개념을 이용해서 뉴스기사 제목을 10개 가져온다.
titles = soup.select('a.news_tit')[:10]

#10개의 뉴스 기사 제목을 출력
for i, t in enumerate(titles):
    title = t.get_text()
    print('%d: %s' %(i+1,title))

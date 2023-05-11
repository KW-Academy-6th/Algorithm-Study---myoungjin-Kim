#프로젝트에 필요한 패키지를 불러온다
import requests # requests 패키지 가져오기
from bs4 import BeautifulSoup as bs # BeautifulSoup 패키지 불러오기, bs로 이름을 간단히 바꿈
import urllib.request  #urltrieve 사용을 위해

url = "https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4"

#requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
response = requests.get(url)

# 얻고자 하는 html 문서가 여기에 담기게 됨
html_text = response.text

# bs4 패키지의 함수를 이용해서 html 문서를 파싱
soup = bs(html_text, 'html.parser')

#bs4 패키지의 select 함수와 선택자 개념을 이용해서 고양이 사진을 10개 가져온다.
imgs = soup.select('img')[:10]

#urlretrieve 명령어를 사용해 저장한다.
for i, t in enumerate(imgs):
    img_url = t['src']
    urllib.request.urlretrieve(img_url, "cat" + str(i+1) + ".png")

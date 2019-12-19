import requests
import bs4

html = requests.get('https://music.naver.com/')
soup = bs4.BeautifulSoup(html.text,'html.parser')

keywords =soup.select('뭔지모르겠다_tracklist_move _track_dsc list1 on')

#for keyword in keywords:
#    print(keyword.text)

#배열[0:n] -> 배열의 0번째 인덱스부터 n-1번째
#인덱스들의 요소를 가져와서 배열로 만든다.
real_keywords = keywords[0:20] #검색어가 반복되서 20번까지만 
real_real_keywords = [keyword.text for keyword in real_keywords] #스팬태그도 같이 와서 검색어만 불러오기


#뭐가 1등이지 모르게 가나다 정렬
problem = sorted(real_real_keywords)

print('아래의 보기중에서 1위를 고르세요.')
print(problem)
answer = input('당신이 입력한 답: ')
#배열 [0]: 배열의 첫번째 요소
if answer == real_real_keywords[0]:
    print('정답입니다.')
else:
    print('오답입니다.')

##[1,2,3,4,...,100]
#numbers = [i*2 for i in range(0,101)]
#print(numbers)

#numbers =[]
#for i in range(0,101):
#    numbers.appenpython popular.pyd(i)
#    print(numbers)
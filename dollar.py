import bs4
import requests

#환율가져오기
html = requests.get('https://finance.naver.com/marketindex')
soup = bs4.BeautifulSoup(html.text,'html.parser')
dollar = soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')

print(dollar.text)

ttmmii = f'현재 달러 환율은 {dollar.text}입니다.'
print(ttmmii)
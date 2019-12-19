# 명단에서 이름을 뽑아서 영어소개와 한글소개
import random

name = ['정진영','신동우','이정환','차선우','공찬식']
eng_name = {
    '정진영':'jinyoung',
    '신동우':'cnu',
    '이정환':'sandeul',
    '차선우':'baro',
    '공찬식':'gongchan'
}
지목된사람 = random.choice(name)
지목된영어이름 = eng_name[지목된사람]

#저는 홍길동입니다. My name is houg 문자열을 만들고 싶다.
intro = '저는 ' + 지목된사람 + '입니다. ' + 'My name is ' + 지목된영어이름
intro2 = '저는 {}입니다. My name is {}'.format(지목된사람,지목된영어이름)
intro3 =f'저는 {지목된사람}입니다. My name is {지목된영어이름}'
#print(intro)
#print(intro2)
#print(intro3)

year = range(2021,2030)
comeback = random.choice(year)
dream = f'안녕하세요. 저는 {지목된사람}{지목된영어이름}입니다. 컴백은 아마도 {comeback}년 입니다.'
print(dream)
#로또번호를 랜덤으로 뽑아주는 프로그램
import random

numbers = range(1,46)
# 마치[1,2,3,...,45]와 비슷하다.

#6개의 숫자를 뽑아 출력해주는 프로그램

#alt + shift + 위 or 아래 방향키 =복사
#alt + 위 or 아래 방향키 =통채로 이동
lotto = random.sample (numbers, 6)
print(sorted(lotto))



# 자료형
print(5)
print('아이스크림🍦'*3)
print(5>10)
print(57>10)


# 변수
animal = "강아지"
name = "연탄이"
age = 4
hobby="산책"
is_adult = age >=3


print('우리집', animal ,'의 이름은 ', name,'입니다')
print(name,'이는 ', age,'살이며, ', hobby,'을 아주 좋아해요')

hobby = '공놀이'
print(name,'이는 ', age,'살이며, ', hobby,'을 아주 좋아해요')
print(name ,'이는 어른일까요? ', is_adult )


# 주석
''' 여러문장 
주석처리하기 
그런데 색이 너무 안이쁘다 ㅜㅜ'''


#계산
print(2**3)
print(5%3) # 나머지
print(5//3) #몫
print(3==3) # = =
print(3!=3) # ! =
print(not(1 != 3))
print((3>0) & (3<5)) # and
print((3>0) | (3<5)) #or
print(abs(-5))
print(pow(4,2)) # 4의 2승
print(max(5,12))
print(min(5,12))
print(round(3.14)) # 반올림



from math import *
print(floor(4.99))
print(ceil(4.01))
print(sqrt(16)) #제곱근
# 거의 자바스크립트랑 비슷하다. from math import *를 제외하면



# number += 2 : 자기수에 2 더하기


#random함수
from random import *
print(random()) # 0~1중 랜덤 숫자
print(int(random() *10)) # int는 정수
print(int(random() *10) +1) # int는 정수

print(randrange(1,46)) # 1~ 46미만의 임의의 값
print(randint(1,46)) # 1~ 46이하의 임의의 값 (양 값 다 포함)



#quiz
studyDay = randint(4,28)
print('오프라인 스터디 모임 날짜는 매월 ',studyDay,' 일로 선정되었습니다')



#문자
# 여러줄에 걸쳐 작성
sentence3 = """
내이름은주현
이따3시에 운동가야지🏃‍♀️
"""
print(sentence3)



jumin = "980313-2234567"
print('성별: ' + jumin[7])
print('탄생연도: ' + jumin[0:2]) #처음 값 포함, 마지막 값 불포함 
print('탄생월: ' + jumin[2:4]) #처음 값 포함, 마지막 값 불포함 
print('탄생일: ' + jumin[4:6]) #처음 값 포함, 마지막 값 불포함 
print('생년월일: ' + jumin[:6]) #처음부터 할때는 앞 0을 제외해도 된다
print('생년월일: ' + jumin[7:]) #끝 값까지 가져올 때는 마지막 자리를 생략해도 된다
print('뒤 7자리 (뒤에서부터): ' + jumin[-7:]) 



#문자열 처리함수
python = "Python is Amazing"
print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index('n')
print(index)
index = python.index('n', index + 1)
print(index)

# index = python.index('juhyun') # error!!
print(python.find('juhyun')) # -1

print(python.count('n'))


# 문자열 포멧
print("문자열 포멧📔"*6)

# %를 이용하기

print('나는 %d살입니다.' % 25) # %d는 정수를 의미함. 항상 정수만 넣을 수 있다
print('나는 %s를 좋아해요' %"파이썬") # %s는 문자를 의미함
print('Apple은 %c로 시작해요.' % "A") # %c는 한 글자만 받겠다는 의미

# 참고로 %s로만 사용하면 숫자도 들어감
print('나는 %s살입니다.' % 25) # %d는 정수를 의미함. 항상 정수만 넣을 수 있다

print('나는 %s색과 %s색을 좋아해요.' %('파란', '빨간'))



# {}를 이용하기
print('나는 {}살입니다.' .format(25))
print('나는 {}색과 {}색을 좋아해요.' .format('파란', '빨간'))
print('나는 {1}색과 {2}색을 좋아해요.' .format('파란', '빨간', '분홍'))
print('나는 {age}살이며, {color}색을 좋아해요' .format(age = 25, color="하늘"))


#변수를 이용하기
age = 25
color="하늘"
print(f'나는 {age}살이며, {color}색을 좋아해요.')

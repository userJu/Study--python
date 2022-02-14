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


# 탈출 문자
# \n : 줄바꿈
print('백문이 불여일견\n백견이 불여일타')
# \' \" " 문장 안에서 따옴표 쓰기
print("저는 \"임주현\" 입니다")
# 역슬러시가 필요할때는 \\넣어주면 됨
# \r : 커서를 맨 앞으로 이동
print('Red Apple\rPine')
# \b : 한 글자 삭제 
print('Redd\b Apple')
# \t : 탭
print('red\tApple')




# Quiz
link = 'http://naver.com'
aim = link.index('.')
print(link[7:aim])
link[:3] 
len(link)
link.count('e')

print(link[7:aim] + str(len(link[7:aim])) +str(link.count('e')) + '!')


my_str = link.replace("http://","")
my_str = my_str[:my_str.index('.')]


# 리스트 [] : 순서를 가지는 객체의 집합

subway = [10,20,30]
print(subway)
subway=["유재석","조세호","박명수"]
print(subway)

# 조세호가 탄 칸은?
print(subway.index('조세호'))

# 뒤에 추가
subway.append('뒤')
print(subway)

# 앞에 추가
subway.insert(1,'위치설정')
print(subway)

# 뒤에서부터 빼기
print(subway.pop())
print(subway)

# 같은 이름의 사람이 총 몇 명 있는지 확인하기
subway.append('유재석')
print(subway)
print(subway.count('유재석'))

# 정렬
num_list = [5,2,4,3,1]
num_list.sort()
print(num_list)

# 정렬 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# list는 다양한 자료형을 함께 사용할 수 있다

num_list = [1,2,3,4,5]
mix_list = ['조세호',20,True]
print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)





# 사전
cabinet = {3:'유재석', "100":"김태호"}
print(cabinet[3])
print(cabinet["100"])

print(cabinet.get(3))
# 대괄호로 값을 가져올 때 값이 없는 경우 : 오류, 종료
# get으로 가져올때는 none으로 출력 되고 다음 값을 읽는다

# 기본값을 쓰고 싶을 때 
print(cabinet.get(5, "기본값"))

# 키 확인하는 법
print(3 in cabinet)
print(5 in cabinet)

# 새로운 값 추가하기
cabinet['C-20'] = "조세호"
print(cabinet)
# 만약 key가 진작 있다면 key의 value가 업데이트된다

# 값 삭제하기
del cabinet[3]
print(cabinet)

# key의 정보 출력
print(cabinet.keys())

# value의 정보 출력
print(cabinet.values())

#쌍으로 출력
print(cabinet.items())

#모든 값 지우기
cabinet.clear()
print(cabinet)




# 튜플
# 내용을 변경하거나 추가할 수는 없는데 속도가 list보다 빠름
# 변경되지 않는 내용에 활용

menu=('돈까스',"치즈까스") # 이렇게 작성
print(menu[0])
print(menu[1])

name ="임주현"
age = 25
hobby="코딩"
print(name, age, hobby)

# 튜플 방식으로
(name,age,hobby) = ("임주현", 25, "코딩")
print(name, age, hobby)





# 집합
# 중복이 안되고, 순서가 없다
my_set = {1,2,3,3,3}
print(my_set) # {1,2,3}

java ={"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합
print(java & python)
print(java.intersection(python))

# 합집합
print( java | python)
print(java.union(python))

# 차집합
print(java-python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add('김태호')
print(python)

# java를 까먹었다
java.remove('김태호')
print(java)





# 자료구조의 변경
menu = {'커피','우유','주스'} 
print(menu,type(menu)) # {'주스', '커피', '우유'} <class 'set'>

menu = list(menu)
print(menu,type(menu)) # ['커피', '주스', '우유'] <class 'list'>

menu = tuple(menu)
print(menu, type(menu)) # ('주스', '우유', '커피') <class 'tuple'>

menu = set(menu)
print(menu, type(menu)) # {'주스', '커피', '우유'} <class 'set'>



# shuffle / sample
lists = [1,2,3,4,5]
shuffle(lists)
print(lists)
print(sample(lists,1))
# shuffle : 섞기, sample : list중에서 n개 무작위로 뽑기





#Quiz
users = range(1,21) # 1부터 21 직전까지 숫자 생성 type는 range
users = list(users)
shuffle(users)
top4 = (sample(users,4))
print("-- 당첨자 발표 -- \n 치킨 당첨자 : {0}\n 커피 당첨자 : {1}\n-- 축하합니다 --" .format(top4[0],top4[1:4]))









# # if 
# weather = input('오늘 날씨는 어때요?')
weather= '비'
if weather == '비' or weather =='눈': print('우산을 챙기세요')
elif weather =="미세먼지" : print('마스크를 챙기세요')
else : print('준비물은 필요 없어요')

# temp = int(input('기온은 어때요?'))
temp = 15
if temp >=30 : print('너무 더워요. 나가지 마세요')
elif 15<= temp <30 : print('아주 좋은 날씨!')
elif 0< temp <15 : print('외투를 챙기세요')
else: print('너무 추워요, 나가지 마세요')

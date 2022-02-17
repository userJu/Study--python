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



from encodings import utf_8
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






# for
# for waiting_no in [0,1,2,3,4]:
# for waiting_no in range(3,9):
  # print('대기번호 : {0}'.format(waiting_no))

starbucks = ["주현","주주","공주"]
for customer in starbucks: print("{0}, 커피가 준비되었습니다".format(customer))
# 와 위에 있는 starbucks와  for의 거리가 벌어지면 안되는구나




# while
# customer = '토르'
# index = 5
# # while(조건)
# while index >=1:
#   print('{0}, 커피가 준비 되었습니다. {1} 번 남았어요.' .format(customer, index))
#   index -=1
#   if index == 0:
#     print('커피는 폐기처분되었습니다.')


# customer = '아이언맨'
# index = 1 
# while False: 
#    print('{0}, 커피가 준비 되었습니다. 호출 {1} 회' .format(customer, index))
#    index += 1
#    if index == 345 :
#     print('이건 에바지')

# customer = "주현"
# person = "Unknown"

# while person != customer :
#   print('{0}, 커피가 준비 되었습니다' .format(customer))
#   person = input('이름이 어떻게 되세요? ')







  # continue와 break

absent =[2,5] #결석
no_book = [7]
for student in range(1,11):
  if student in absent:
    continue # 아래 문장 실행 안하고 넘어감
  elif student in no_book:
    print('오늘 수업 여기까지. {0} 다음에는 가져와라' .format(student))
    break # 그 뒤에 있는 것들과는 상관없이 끝내버림
  print('{0}야, 책 읽어봐' .format(student))





# 한 줄 for
students = [1,2,3,4,5]
students = [i+100 for i in students]
print(students)

hero = ['Iron man','Thor','I am groot']
hero = [len(i) for i in hero]
print(hero)

hero = ['Iron man','Thor','I am groot']
hero = [i.upper() for i in hero]
print(hero)






#Quiz

# from random import *

# cnt = 0
# for i in range(1,51):
#   time = randrange(5,51)
#   if 5<= time <=15 :
#     print('[O] {0}번째 손님 (소요시간 : {1}분' .format(i, time))
#     cnt +=1
#   else:
#     print('[] {0}번째 손님 (소요시간 : {1}분' .format(i, time))
# print('총 탑승 승객 :{0}분' .format(cnt))











# 함수
def open_account():
  print('새로운 계좌가 생성되었습니다.')

open_account()



# 전달값과 반환값
def deposit(balance, money):
  print('입금이 완료되었습니다. 잔액은 {0}원 입니다' .format(balance + money))
  return balance + money

# balance = 0
# balance = deposit(balance, 1000)
# print(balance)

def withdraw(balance, money):
  if balance > money :
    print('출금이 완료되었습니다. 잔액은 {0}원 입니다' .format(balance-money))
    return balance - money
  else:
    print('출금이 완료되지 않았습니다. 잔액은 {0} 원입니다' .format(balance))
    return balance

balance = 0
balance = deposit(balance, 1000)
balance = withdraw(balance, 2000)




# 기본값
def profile(name, age=17, main_lang ="파이썬"):
  print('이름 : {0}\t나이 : {1}\t주 사용 언어 : {2}' .format(name, age, main_lang))
  
profile('임주현')
profile('임주현', 25, '파이썬')
profile('임주현', 23, "js")





# 키워드값
def profile(name, age, main_lang):
  print(name,age,main_lang)

profile(name='유재석',main_lang="파이썬",age=20)





# 가변 인자
def profile(name,age,lang1,lang2,lang3,lang4,lang5):
  print('이름: {0}\t나이: {1}\t'.format(name,age),end="")
  print(lang1,lang2,lang3,lang4,lang5)
# end=""를 써주면 출력하고 나서 줄바꿈 처리가 되지 않는다

profile('캐슈', 25,"Kotlin", "Swift", "","","")


def profile(name,age,*language):
  print('이름: {0}\t나이: {1}\t'.format(name,age),end="")
  for lang in language:
    print(lang, end="")
  print()
# 줄바꿈을 막기 위해서 end를 쓰고 마지막 부분에서는 줄바꿈을 위해서 print()로 끝냄

profile('임주현', 25,"Python", "Javascript", "React","Typescript","React-Native","TDD")
profile('캐슈', 25,"Kotlin", "Swift")



# 지역변수와 전역변수
# 지역변수 : 함수 내에서만 쓸 수 있는 것.
# 전역변수 : 모든 공간에서 쓸 수 있는 것.

gun = 10

def checkpoint(soldiers): #경계근무
  global gun # 전역 공간에 있는 gun 사용
  gun=gun-soldiers
  print('[함수 내] 남은 총 : {0}'.format(gun))

def checkpoint_ret(gun, soldiers):
  gun=gun - soldiers
  print('[함수 내] 남은 총 : {0}'.format(gun))
  return gun # return해줌으로써 바뀐 gun의 값을 외부로 던져줄 수 있음.


print('전체 총 : {0}'.format(gun))
# checkpoint(2) # 2명이 경계 근무 나감
gun = checkpoint_ret(gun,2)
print('남은 총 : {0}' .format(gun))



# Quiz

def std_weight(height, gender):
  if gender == '남자':
    G_value = 22
  elif gender =='여자':
    G_value = 21
  value = round(height * height * G_value /10000,2) #반올림 : round
  print('키 {0}cm {1}의 표준 체중은 {2}kg 입니다.' .format(height, gender, value))

std_weight(170, '여자')







# 표준입출력
print('Python'+ "Java") # 붙어서 나온다
print('Python', "Java") # 띄어져서 나온다
print('Python', "Java", sep=" , ") # seperate(sep)를 이용해서 다양하게 출력할 수 있다
print('Python', "Java", sep=" vs ") 
# 함수 두개에 의해서 출력된 문장이 한 줄로 나온다
# Python,Java?무엇이 더 재밌을까요?
print('Python', "Java", sep=",", end="?") 
print('무엇이 더 재밌을까요?')
# end의 의미 : 끝을 물음표로 바꿔달라

import sys
print('Python', "Java", file=sys.stdout) # 표준 출력으로 문장이 찍힘
print('Python', "Java", file=sys.stderr) # 표준 에러로 문장이 찍힘


scores = {'수학':0, '영어':50, "코딩":100}
for subject, score in scores.items(): # key와 value가 페어로 나온다. 쌍으로 튜플로 나옴
  # print(subject, score) # 정렬이 안되어서 나옴

  # 수학이라는 글자가 있으면 8개의 공간을 만들고 왼쪽 정렬을 해라
  # score는 4칸을 확보하고 오른쪽 정렬해라
  print(subject.ljust(8), str(score).rjust(4), sep=":") 


# 은행 대기순번표 001
# 0으로 채우기 : zfill
for num in range(1,21):
  print('대기번호 : ' + str(num).zfill(3))



# answer = input('아무 값이나 입력하세요 : ')
# print('입력하신 값은 {0} 입니다' .format(answer))









# 다양한 출력포멧


# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print('{0: > 10}' .format(500))
# => 0:   // 0(빈 자리)는 빈 공간으로 두고
# => > 오른쪽 정렬을 하되
# => 10 : 총 10자리 공간을 확보

# 양수일 땐 +로, 음수일 땐 -로 표시
print('{0: >+10}' .format(500)) 
print('{0: >-10}' .format(-500)) 
# 첫 문장에서도 -500을 찍으면 자동으로 -가 찍히기는 하지만 양수일 때는 + 없이 그냥 찍힌다

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 콤마를 찍어주기
print('{0:,}' .format(10000000000))

# 3자리마다 콤마를 찍어주기 + 부호
print('{0:+,}' .format(10000000000))
print('{0:-,}' .format(-10000000000))

# 3자리마다 콤마를 찍어주기 + 부호 + 자릿수 확보 + 돈이 많으면 행복하니까 빈 자리는 ^
print('{0:^<+30,}' .format(1000000000000))

# 소수점 출력
print("{0:f}" .format(5/3))
# 소수점 특정 자리수까지만 표시
print("{0:.2f}" .format(5/3))
# => 소수점 3째자리에서 반올림






# 파일 입출력
score_file = open('score.txt','w',encoding="utf8")
print('수학: 0', file=score_file)
print('영어: 50', file=score_file)
score_file.close()

# w(wirte)를 이용할 경우 덮어쓰기가 된다
# 이어서 쓰고 싶으면 a(append)를 쓰면 된다
score_file = open('score.txt','a',encoding='utf8')
score_file.write('과학: 80')
score_file.write('\n코딩: 100')
score_file.close()
# print로 쓸 때는 줄바꿈이 자동으로 처리됐는데
# write로 쓸 때는 줄바꿈이 되지 않는다 그래서 줄바꿈을 위한 \n을 이용

# 파일 내용 읽어오기 r(read)
score_file = open('score.txt','r', encoding="utf_8")
print(score_file.read())
score_file.close()

# 파일 내용 한 줄 씩만 읽어오기
score_file = open('score.txt','r', encoding="utf_8")
print(score_file.readline(), end="") # 줄 별로 읽기. 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") 
print(score_file.readline(), end="") 
score_file.close()


# 몇 줄인지 모를 때 내용 가져오기

# 1
score_file = open('score.txt','r', encoding="utf_8")
while True:
  line=score_file.readline()
  if not line:
    break
  print(line)
score_file.close()

# 2
score_file = open('score.txt','r', encoding="utf_8")
lines = score_file.readlines() # list 형태로 저장
for line in lines:
  print(line)
score_file.close()






# pickle
# 프로그램 상에서 사용하는 데이터를 파일 형태로 저장하는 것

import pickle
profile_file = open('profile.pickle','wb') # 쓰기 목적의 w와 바이너리 타입의 b
# pickle에서는 따로 인코딩을 설정해줄 필요가 없다
profile= {'이름':'임주현', '나이': 25, '취미':['코딩', '쇼핑','카페']}
print(profile)
pickle.dump(profile,profile_file) # profile에 있는 정보를 file에 저장한다.
profile_file.close()

# pickle에서 가져오기
profile_file = open('profile.pickle', 'rb')
profile = pickle.load(profile_file) # file에 있는 정보를 profile에 불러오기
print(profile)
profile_file.close()







# with
import pickle

# with와 pickle
with open('profile.pickle', 'rb') as profile_file:
  print(pickle.load(profile_file))
# with라는 글자를 쓰고 파일을 연다. 이 파일 정보를 profile_file이라는 변수에 저장.
# 그리고 나서 pickle.load(profile_file)을 통해서 파일을 읽을 수 있다
# => 따로 close라는걸 나타낼 필요 없이 with가 알아서 해준다

# with와 txt
with open('study.txt','w', encoding="utf8") as study_file:
  study_file.write('파이썬을 열심히 공부하고 있어요')

# with로 파일 불러오기
with open('study.txt', 'r', encoding="utf8") as study_file:
  print(study_file.read())




  #Quiz
  # for week in range(1,51):
  #   with open(str(week)+'주차.txt', 'w', encoding="utf8") as report_file:
  #     report_file.write('- {0} 주차 주간보고 - \n부서 : \n이름 : \n업무 요약 : ' .format(week))









#클래스

# name = "마린"
# hp = 40
# damage = 5

# print("{0} 유닛이 생성되었습니다." .format(name))
# print("체력 {0} 공격력 {1}\n" .format(hp, damage))


# tank_name = "탱크"
# tank_hp = 150
# tank_damage = 35

# print("{0} 유닛이 생성되었습니다." .format(tank_name))
# print("체력 {0} 공격력 {1}\n" .format(tank_hp, tank_damage))

# tank2_name = "탱크"
# tank2_hp = 150
# tank2_damage = 35

# print("{0} 유닛이 생성되었습니다." .format(tank2_name))
# print("체력 {0} 공격력 {1}\n" .format(tank2_hp, tank_damage))

# def attack(name, location, damage):
#   print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]" .format(name, location, damage))

# attack(name, "1시", damage)
# attack(tank_name, "1시", tank_damage)
# attack(tank_name, "1시", tank2_damage)

# 이렇게 두세개씩 써야하는 것은 너무 불편하다 => class사용

# 위에있는 주석을 class로 다시 만들기

class Unit:
  def __init__(self,name,hp,speed):
    self.name = name
    self.hp = hp
    self.speed=speed
    print('{0} 유닛이 생성되었습니다' .format(name))

  def move(self, location):
    print("[지상 유닛 이동")
    print("{0} : {1} 방향으로 이동합니다. [속도 {2}]"\
      .format(self.name,location,self.speed))

  def damaged(self,damage):
    print("{0} : {1} 데미지를 잃었습니다." .format(self.name, damage))
    self.hp -=damage
    print('{0} : 현재 체력은 {1} 입니다.' .format(self.name, self.hp))
    if self.hp <= 0:
      print("{0} : 파괴되었습니다" .format(self.name))

# marine1 = Unit('마린',40,5)
# marine2 = Unit('마린',40,5)
# tank = Unit('탱크',150,35)




# __init__
# 파이썬에서 쓰이는 생성자
# 마린이나 탱크같이 클래스로부터 만들어지는 애들을 객체라고 한다
# 이 때 '마린'과 '탱크' 는 Unit class의 instance라고 표현한다





# 멤버 변수
# class안에 있는 self.어쩌고 이걸 멤버 변수라고 한다
# class 내에서 정의된 변수고 이걸 이용해 사용할 수 있다

# wraith1 = Unit('레이스',80,5)
# print('유닛 이름 : {0}, 공격력 : {1}' .format(wraith1.name, wraith1.damage))


# wraith2 = Unit('빼앗은 레이스',80,5)
# wraith2.clocking = True

# 외부에서 변수를 추가로 할당하여 True라는 값을 집어넣음
# if wraith2.clocking ==True:
#   print('{0}은 현재 클로킹 상태입니다' .format(wraith2.name))







# 메소드
class AttackUnit(Unit):
  def __init__(self, name, hp,speed, damage):
    Unit.__init__(self,name,hp,speed)
    self.damage=damage

  def attack(self, location):
    print("{0} : {1} 방향으로 적군을 공격 합니다. [공격력 {2}]"\
      .format(self.name, location, self.damage))




class Marine(AttackUnit):
  def __init__(self):
    AttackUnit.__init__(self, "마린",40,1,5)
  
  def stimpack(self):
    if self.hp>10:
      self.hp -=10
      print('{0} : 스팀팩을 사용합니다. (HP 10 감소)' .format(self.name))
    else:
      print('{0} : 체력이 부족하여 스팀팩을 사용하지 않습니다. '.format(self.name))



  class Tank(AttackUnit):
    seize_developed = False

    def __init__(self):
      AttackUnit.__init__(self, '탱크', 150, 1, 35)
      self.seize_mode  = False

    def set_seize_mode(self):
      if Tank.seize_developed ==False:
        return

      if self.seize_mode == False:
        print("{0} : 시즈모드로 전환합니다." .format(self.name))
        self.damage *=2
        self.seize_mode = True
      else:
        print("{0} : 시즈모드를 해제합니다." .format(self.name))
        self.damage /=2
        self.seize_mode = False






# 상속
# class AttackUnit(Unit):
#   def __init__(self, name, hp, damage):
#     Unit.__init__(self,name,hp)
#     self.damage=damage




# 다중 상속
class Flyable:
  def __init__(self,flying_speed):
    self.flying_speed = flying_speed

  def fly(self, name, location):
    print("{0} : {1} 방향으로 날아갑니다. [속도 {2}]" .format(name,location, self.flying_speed))


class FlyableAttackUnit(AttackUnit, Flyable):
  def __init__(self, name, hp, damage, flying_speed):
    AttackUnit.__init__(self, name, hp,0, damage)
    Flyable.__init__(self, flying_speed)

  def move(self, location):
    print('[공중 유닛 이동')
    self.fly(self.name, location)


valkyrie = FlyableAttackUnit('발키리', 200, 6, 5)
valkyrie.fly(valkyrie.name,'3시')

class Wraith(FlyableAttackUnit):
  def __init__(self):
    FlyableAttackUnit.__init__('레이스',80,20,5)
    self.clocked = False

  def clocking(self):
    if self.clocked ==True:
      print('{0} : 클로킹 모드 해제합니다' .format(self.name))
      self.clocked = False
    else:
      print('{0} : 클로킹 모드 설정합니다' .format(self.name))
      self.clocked = True





# 메소드 오버라이딩
vulture =AttackUnit('벌쳐',80,10,20)
battlecruiser = FlyableAttackUnit('배틀크루저',500,25,3)

# vulture.move("11시")
# battlecruiser.fly(battlecruiser.name,'9시')
# 그런데 이렇게 move나 fly를 찾아서 작성해주는게 너무 귀찮다
# 그럴 때 이용하는 것이 메소드 오버라이딩

vulture.move("11시")
battlecruiser.move('9시')
# 똑같은 move함수인데 FlyableAttackUnit에서 move를 재정의해서 이걸로 쓸 수 있음





# pass
class BuildingUnit(Unit):
  def __init__(self,name,hp,location):
    pass # 의미 아무것도 안하고 그냥 이 함수를 완성된 것 처럼 보이게하기.


supply_depot = BuildingUnit('서플라이 디폿',500, '7시')




# super
# 1. 이렇게 쓸 수도 있고
# class SuperBuildingUnit(Unit):
#   def __init__(self, name, hp, location):
#     Unit.__init__(self, name,hp,0)
#     self.location = location

# 2. super을 사용할 수도 있다
class SuperBuildingUnit(Unit):
  def __init__(self, name, hp, location):
    # Unit.__init__(self, name,hp,0)
    super().__init__(name,hp,0) # super을 통해 초기화 할 때는 self는 보내면 안된다
    self.location = location


    # root : practice_class.py






print("안녕하세요")
print('저는 파이썬을 무척 좋아합니다')
print('9*8은',9*8 ,'입니다')
print('안녕히 계세요')
#
print('숫자게임에 오신 것을 환영합니다')
number = 62
s = input('1부터 100 사이에 숫자를 추측해보세요: ')
guess = int(s)
if guess == number:
    print("맞았습니다")
else:
    print("틀렸습니다")
print('게임이 종료되었습니다')
#파티 준비
number = int(input("참석자의 수를 입력하시오: "))
chikcens = number
beers = number*2
cakes = number*4
print("지킨의 수: ", chikcens)
print("맥주의 수: ",beers)
print("케잌의 수: ",cakes)
#
x = 2.0
y = 3.0 * x **2 + 7.0 * x + 9.0
print(y)
# 거북이
import turtle
t = turtle.Turtle()
t.shape("turtle")

size = 20

for i in range(30):
    size = size +3
    t.forward(size)
    t.right(24)
# 숫자 츠축 게임
print("숫자게임에 오신 것을 환영합니다")
number = 77
s = input("1부터 100 사이의 숫자를 추측해보세요: ")
guess = int(s)
if guess == number:
    print("맞았습니다")
else:
    print("게임이 종료 되었습니다")
#2차 함수 계산
x = 2.0
y = 3.0* x**2 + 7.0 *x +9.0
print(y)
#감자 재배
a = 100-10+51*(40-10) - 52*(3*7)
print(a)
#복리 계산
b = 24*(1+0.06)**382
print(b)
#등산 시간 계산
from math import *

time1 = 10/20
length = sqrt(3**2+4**2)
time2 = length/10
time3 = length/30
time4 = 8/20
total = time1+time2+time3+time4
print(total)
#구의 부피 계산하기
r = 5.0
volume = 4.0/3.0 *3.141592 * r**3
print(volume)
#별까지 거래 계산하기
speed = 300000
distance = 40000000000000
secs = distance/speed
light_year = secs/(60.0*60.0*24.0*365.0)
print(light_year)
#대화하는 프로그램 만들기
name = input("이름 입력해주세요: ")
print(name,"님 만나서 반갑습니다.")
age = input("나이를 입력해주세요: ")
print("10년 후면",int(age)+10,"살이 되시는군요!")
#자동 판매기 프로그램
itemPrice = int(input("물건 값을 입력하시오: "))
note = int(input("1000원 지폐 개수: "))
coin500 = int(input("500원 동전 개수: "))
coin100 = int(input("100원 동전 개수: "))
change = note+1000 + coin500+500 + coin100+100 - itemPrice

ncoin500 = change//500
change = change%500

ncoin100 = change//100
change = change%100

ncoin10 = change//10
change = change%10

ncoin1 = change
print("500원=",ncoin500,"100원=",ncoin100,"10원=",ncoin10,"1원=",ncoin1)
#숫자 추측 게임
word1 = input("첫 번째 단어를 입력해주세요: ")
word2 = input("두 번째 단어를 입력해주세요: ")
word3 = input("세 번째 단어를 입력해주세요: ")
acronym = word1[:2]+word2[:2]+word3[:2]
print(acronym)
#터틀 그래픽
import turtle
t = turtle.pen()
while True:
    direction = input("왼쪽->left, 오른쪽->right: ")
    if direction == "left":
        t.left(60)
        t.forwad(50)
    if direction == "right":
        t.left(60)
        t.forward(50)
# 수하물 비용 계산

weight = float(input("짐의 무게는 얼마입니까: "))

if weight > 20:
    print("무거운 짐은 20.000원을 내셔야 합니다")
else:
    print("짐의 대한 수수료는 없습니다")
print("감사합니다")
#옷차름 추천
temperatura = float(input('현재 기온을 입력하세요: '))
if temperatura >30:
    print('반바지를 입으세요')
else:
    print("긴바지를 입으세요")
print('감사합니다')
#홀수 짝수 구별하기
number = int(input("정수를 입력하시오: "))
if ((number%2)==0):
    print("입력된 정수는 짝수 입니다"  )
else:
    print("입력된 정수는 홀수 입니다")
#두수 중 큰 수 출력
x = int(input("첫 번째 정수: "))
y = int(input("두 번째 정수: "))
if (x > y ):
    max = x
else:
    max = y
print("큰 수는",max)
#물건 값 계산
total_sales = int(input("구입 금액을 입력 하시오: "))
if total_sales > 100000:
    discount = total_sales *0.05
    sales = total_sales -discount
print("지불할 금액은 ",sales,"입니다(")
#문자열의 중앙문자
str = input("문자열을 입력하시오: ")
lenght = len(str)
if lenght%2==1:
    ch1 =str[lenght//2]
    print("중앙글자는 ",ch1)
else:
    ch1 = str[lenght//2-1]
    ch2 = str[lenght//2]
    print("중앙글자는 ",ch1,ch2)
#임금 계산
hours = float(input("근무 시간을 입력하시오: "))
wage = float(input("시간당 임금을 입력하시오: "))
if hours <= 40:
    totalWages = wage*hours
else:
    overtime = hours - 40
    totalWages = wage*40 +(1.5*wage)*overtime
print("총임금은",totalWages)
#졸업 학점 검사하기
credits = float(input('이수한 학점수를 입력하시오: '))
gpa = float(input("평점을 입력하시오: "))
if credits >= 140 and gpa >= 2.0:
    print("졸업 가능합니다")
else:
    print("졸업이 힘듭니다")
#음수,0,양수 구별하기
number = int(input("정수를 입력하시오: "))
if number <0:
    print("입력된 정수는 음수 입니다")
elif number == 0:
    print("입력된 정수는 0입니다")
else:
    print("입력된 정수는 양수 입니다")
#음수,0,양수 구별하기
num = float(input("정수를 입력하시오: "))
if num >=0:
    if num ==0:
        print("0입니다")
    else:
        print("양수입니다")
else:
    print("음수 입니다")
#아이디 검사
user_list =["김철수","홍길동","김영희"]
name = input("아이디: ")
if name in user_list:
    password = input("패스워드를 입력하시오: ")
    if password == '12345678':
        print("환영합니다.")
    else:
        print("잘못된 패스워드입니다")
else:
    print("알수 없는 사용자입니다!")
#숫자 한글
number = int(input("숫자를 입력하시오: "))
if (number==1):
    print("하나")
elif (number==2):
    print("둘")
elif (number==3):
    print("셋")
elif (number==4):
    print("넷")
else:
    print("많음")
#달의 일수 출력
month = int(input("월을 입력하시오: "))
if (month==2):
    print("월의 날수는 29일")
elif (month == 4 or month==6 or month==10):
    print("월의 날수 30일")
else:
    print("월의 날수 31일")
#인사말 출력하기
import time
now = time.localtime()
print("현재시간은",time.asctime())
if (now.tm_hour <11):
    print("Good morning")
elif (now.tm_hour <15):
    print("Good afternoon")
elif (now.tm_hour <20):
    print("Good evening")
else:
    print("Good night")
#윤년 판단
year = int(input("연도를 입력하시오: "))
if ( (year % 4 ==0 and year % 100 != 0)or year % 400 == 0):
    print(year,"년 윤년 입니다.")
else:
    print(year,"년이 윤년이 아닙니다")
#이자 방정식
import math
a = float(input("A = "))
b = float(input("B = "))
c = float(input("C = "))
d = b * b - 4 * a * c
if a == 0:
    print("x=",-c/b)
if d == 0:
    print("x=",-b/(2.0*a))
elif d>0:
    print("x1=",(-b + math.sqrt(d))/(2.0*a))
    print("x=",(-b - math.sqrt(d)) / (2.0*a))
else:
    print("실근이 존재하지 않음")
#면적 계산기
choice = int(input('도형을 입력하시오(1: 사각형, 2: 삼각형, 3: 원: '))
if(choice==1):
    w = int(input("가로: "))
    h = int(input(("세로: ")))
    area = w*h
elif (choice==2):
    b = int(input("밑면: "))
    h = int(input("높이: "))
    area = 0.5*b*h
else:
    r = int(input("반지름: "))
    area = 3.141592*r*r
print("면적=",area)
#직선 방정식 구하기
x1 = int(input('첫 번째 점의 x좌표: '))
y1 = int(input('첫 번째 점의 y좌표: '))
x2 = int(input('두 번째 점의 x좌표: '))
y2 = int(input('두 번째 점의 y좌표: '))
if ( (x2-x1)!=0):
    m = (y2-y1)/(x2-x1)
    q = y1-m*x1
    print("직선의 방정식은",m, 'x+',q)
else:
    print('직선의 방정식은 x=',x1)
#숫자 맞추기 게임
answer = 5
print("숫자 게임에 오신 것을 환영합니다.")
g = input("숫자를 맞춰 보세요: ")
guess = int(g)
if guess == answer:
    print("사용자가 이겼습니다")
elif guess > answer:
    print("너무 큼")
else:
    print("너무 작음")
print("게임 종료")
#가위 바위 보
player = input("(가위, 바,위 보)중에서 하나를 선택하세요: ");
computer = "바위";
print("사용자:",player,"컴퓨터",computer)
if (player == computer):
    print("비겼음")
elif (player == "바위"):
    if (computer == "보"):
        print("컴퓨터가 이겼음!")
    else:
        print("사용자가 이겼음")
elif (player == "보"):
    if (computer == "바위"):
        print("사용자가 이겼음")
    else:
        print("컴퓨터가 이겼음")
elif (player == "가위"):
    if (computer == "바위"):
        print("컴퓨터가 이겼음!")
    else:
        print("사용자가 이겼음")
#사각형 충돌 조사
p1x = int(input("첫번째 사각형의 p1.x= "))
p1y = int(input("첫번째 사각형의 p1.y= "))
p2x = int(input("첫번째 사각형의 p2.x= "))
p2y = int(input("첫번째 사각형의 p2.y= "))

p3x = int(input("두번째 사각형의 p3.x= "))
p3y = int(input("두번째 사각형의 p3.y= "))
p4x = int(input("두번째 사각형의 p4.x= "))
p4y = int(input("두번째 사각형의 p4.y= "))
overlapped = not(p4x < p2x or
                p3x > p2x or
                p2y < p3y or
                p1y > p4y)
if overlapped:
    print("두 개의 사각형이 겹침!")
else:
    print("두 개의 사각형이 겹치지 않음!")
#정수들의 합
sum = 0
limit = int(input("어디까지 계산할까요: "))
for i in range(1,limit+1):
    sum += i
print("1부터 ",limit,"까지의 겅수의 합= ",sum)
#팩토리얼 계산하기
fact = 1.0
n = int(input('정수를 입력하시오:  '))
for i in range(1,n+1):
    fact = fact*1;
print(n,"!은",fact,"이다")
#카운트 다운 프로그램
count = int(input("초기 숫자를 입력하시오: "))
for x in range(count,0,-1):
    print(x, end=" ")
print("발사")
#온도 변환 테이블 출력
for t in range(0,100+1,10):
    c = (t- 32.0) *0.5 / 9.0
    print(t, " ->",round(c,2));
#화면에 별 그리기
import turtle
star = turtle.Turtle()
for i in range(5):
    star.forward(50)
    star.right(144)
#화면에 육각형 그리기
import turtle
polygon = turtle.Turtle()
num_sides = 6
side_length = 70
angle = 360.0 / num_sides
for i in range(num_sides):
    polygon.forward(side_length)
    polygon.right(angle)
#화면에 컬러 다각형 그리기
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
colors = ["yellow","red","purple","blue"]
for c in colors:
    t.color(c)
    t.forward(200)
    t.left(90)
#화면에 사각형 그리기
import turtle
for i in range(3):
    turtle.left(20)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
#화면에 거북이 그리기
import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
t = turtle.Turtle()
t.shape("turtle")
t.color("blue")
size = 20
for i in range(30):
    t.stamp()
    size = size +3
    t.forward(size)
    t.right(24)
#함수 그래프 그리기
import math
import turtle
t = turtle.Turtle()
t.pendown()
for angle in range(360):
    y = math.sin(math.radians(angle))
    scaledX = angle
    scaledY = y * 100
    t.goto(scaledX,scaledY)
#0부터 9까지 출력하기
i = 0
while i < 10:
    print(i,end=(" "))
    i = i + 1
#1+2+3+4+5+6+7+8+9+10 계산하기
i = 1
sum = 0;
while i <= 10:
    sum = sum + i
    i = i + 1
print("합계=",sum)
#팩토리얼 계산하기
i = 1
factorial = 1
while (i <= 10):
    factorial = factorial * i
    i = i +1
print("10!은 %d입니다"%factorial)
#구구단 출력
i = 1
while i <= 9:
    print("3*%d = %d" % (i,3*i))
    i = i +1
#투자 금액 계산하기
year = 0
balance = 1000
while balance < 2000:
    year = year + 1
    interest = balance*0.05
    balance = balance + interest
print("기간: ",year)
print("총액: ",balance)
#자리수의 합
number = 1234
sum = 0;
while number > 0:
    digit = number % 10
    sum = sum + digit
    number = number // 10
print("자리수의 합은 %d입니다."%sum)
#최대 공약수 계산하기
x = int(input("정수를 입력하시오(큰수): "))
y = int(input("정수를 입력하시오(작은수): "))
while (y != 0):
    r = x % y
    x,y = y,r
print("최대 공약수는 %d입니다" %x)
#숫자 맞추기 게임
import random
tries = 0
number = random.randint(1,100)
print("1부터 100 사이의 숫자를 맞추시오")
while tries < 10:
    guess = int(input("숫자를 입력하시오: "))
    tries = tries +1
    if guess < number:
        print("낮음")
    elif guess > number:
        print("높음")
    else:
        break
if guess == number:
    print("축하합니다.시도횟수=",tries)
else:
    print("정답은",number)
#피타고라스 삼각형 찾기
for a in range(1,101,1):
    for b in range(1,101,1):
        for c in range(1,101,1):
            if ( (a*a+b*b)==c*c ):
                print(a,b,c)
#제곱값 출력
for y in range(1,6):
    print("x**",y," ", end="");
print()
for x in range(1,11):
    for y in range(1,6):
        print(x**y," ", end="")
    print()
#알파벳,숫자,스페이스의 처리
statement = input("문자열을 입력하시오: ")
alphas = 0
digits = 0
spaces = 0
for c in statement:
    if c.isalpha():
        alphas = alphas + 1
    if c.isdigit():
        digits += 1
    if c.isspace():
        spaces += 1
print("알파벳 문자의 개수=",alphas)
print("숫자 문자의 개수=",digits)
print("스페이스 문자의 개수=",spaces)
#계좌번호 처리
raw = input("계좌번호를 입력하시오: ")
processed = ""
for c  in raw:
    if c != "-":
        processed = processed +c
print(processed)
#주사위 합 확률
from random import randint
count = int(input("주사 위 실험 반복횟수: "))
rollCount = [0,0,0,0,0,0,0,0,0,0,0,0,0]
for i in range(count):
    die1 = randint(1,6)
    die2 = randint(1,6)
    rollCount[die1+die2] += 1
for i in range(2,13):
        print(i,rollCount[i])
#파이 계산
from random import *
from math import sqrt
n = int(input("반복 횟수를 입력하시오: "))
inside = 0
for i in range(0,n):
    x = random()
    y = random()
    if sqrt(x*x+y*y) <= 1:
        inside += 1
Pi = 4*inside/n
print(Pi)
#생일 축하 함수
def happyBrirhday():
    print("생일축하 합니다")
    print("생일축하 합니다")
    print("사랑하는 친구의", end=(" "))
    print("생일축하 합니다")
happyBrirhday()
#온도 변환 함수
def FtoC(temp_f):
    temp_c=(5.0 *(temp_f -32.0)) /9.0
    return temp_c
temp_f = float(input("화씨 온도를 입력하시오: "))
print(FtoC(temp_f))
#소수 찾기
def is_prime(n):
    for i in range(2, n):
        if (n%i == 0):
            return False
        return True
n = int(input("정수를 입력하시오: "))
print(is_prime(n))
#소수 찾기
import math
def sphereVolume(radius):
    volume = (4.0 /3.0) * math.pi * radius * radius *radius
    return volume
radius = float(input('구의 반지름을 입력하시오: '))
print(sphereVolume(radius))
#패스워드 생성기
import random
def genPass():
    alphabet = "abcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(6):
        index = random.randrange(len(alphabet))
        password = password + alphabet[index]
    return password
print(genPass())
print(genPass())
print(genPass())
#키워드 인수 연습
def add(a,b):
    return a + b
def subtract(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b
r1 = multiply(a=20, b=30)
r2 = add(a=10, b=r1)
print(r2)
#온도 변환기
def printOptions():
    print("'c' 섭씨온도에서 화씨 온도로 변환")
    print("'f' 화씨온도에서 섭씨 온도로 변환")
    print("'q' 종료")
def C2F(c_temp):
    return 9.0 / 5.0 * c_temp +32
def F2C(f_temp):
    return (f_temp - 32.0) * 5.0 / 9.0
printOptions()
choice = input("메뉴에서 선택하세요: ")
while choice != "q":
    if choice == "c":
        temp = float(input("섭씨 온도:" ))
        print("화씨 온도:",C2F(temp))
    elif choice =="f":
        temp = float(input("화씨 온도: "))
        print("섭씨 온도:",F2C(temp))
    printOptions()
    choice = input("메뉴에서 선택하세요: ")
#입력검증
def area(w,h):
    return w*h
def input_pos(msg):
    value = int(input(msg))
    while value <= 0:
        value = int(input('양수를 입력하시오: '))
    return value
width = input_pos('사각형의 가로: ')
height = input_pos("사각형의 세로: ")
print('면적=',area(width,height))
#전역변수와 지역변수
PI = 3.14159265358979
def main():
    radius = float(input('원의 반지름을 입력하시오: '))
    print('원의 면적:', circleArea(radius))
    print('원의 둘레:', circleCircumference(radius))
def circleArea(radius):
    return PI*radius*radius
def circleCircumference(radius):
    return 2*PI*radius
main()
#여러 개의 값 반환
def get_line(x1,y1,x2,y2):
    if (x1 == x2):
        return 0,0
    else:
        slope = (float)(y2-y1) / (float)(x2-x1)
        yintercept = y1 - slope*x1
        return slope,yintercept
x1 = int(input("x1="))
y1= int(input("y1="))
x2 = int(input("x2="))
y2 = int(input("y2="))
slope,yintercept = get_line(x1,y1,x2,y2)
print("기울기=",slope,"y절편=",yintercept)
#성적 처리 프로그램
STUDENTS = 5
scores = []
scoreSum = 0
for i in range(STUDENTS):
    valume = int(input("성적을 입력하시오: "))
    scores.append(valume)
    scoreSum += valume
scoreAvg = scoreSum / len(scores)
highScoreStudents = 0
for i in range(len(scores)):
    if scores[i]>=80:
        highScoreStudents +=1
print("성적 평균은",scoreAvg,"입니다")
print("80점 이상 성적을 받은 학생은",highScoreStudents,"명입니다")
#문자열 처리 프로그램
dogNames = []
while True:
    name = input("강아지의 이름을 입력하시오(종료시에 엔터키: ")
    if name == "":
        break
    dogNames.append(name)
print('강아지들의 이름: ')
for name in dogNames:
    print(name,end=", ")
#피타고라스 삼각형
new_list = []
for x in range(1,30):
    for y in range(x,30):
        for z in range(y,30):
            if x**2+y**2 == z**2:
                new_list.append((x,y,z))
print(new_list)
#연락처 관리 프로그램
menu = 0
friends = []
while menu !=9:
    print("-----------------------------")
    print("1. 친구 리스트 출력")
    print("2. 친가 추가")
    print("3. 친구 삭제")
    print("4. 이름 변경")
    print("9. 종료")
    menu = int(input("메뉴를 선택하시오: "))
    if menu == 1:
        print(friends)
    elif menu == 2:
        name = input("이름을 입력하시오: ")
        friends.append(name)
    elif menu == 3:
        del_name = input("삭제하고 싶은 이름을 입력하시오: ")
        if del_name in friends:
            friends.remove(del_name)
        else:
            print("이름이 발견되지 않았음")
    elif menu == 4:
        old_name = input("변경하고 싶은 이름을 입력하시오: ")
        if old_name in friends:
            index = friends.index(old_name)
            new_name = input("새로운 이름을 입력하시오")
            friends[index] = new_name
        else:
            print("이름이 발견되기 않았음")
#2개의 즈사위
rows = 6
cols = 6
table = []
for row in range(rows):
    table += [[0]*cols]
for row in range(rows):
        for col in range(cols):
            table[row][col] = (row+1+col+1)
print(table)
#TIC-TAC-TOE 게임
board = [[' 'for x in range(3)] for y in range(3)]
while True:
    for r in range(3):
        print("  "+ board[r][0]+"|   "+ board[r][1]+"|  " + board[r][2])
        if(r !=2):
            print("---|---|---")
    x = int(input("다임 수의 x좌표를 입력하시오: "))
    y = int(input("다임 수의 y좌표를 입력하시오: "))
    if board[x][y] != ' ':
        print("잘못된 위치 입니다")
        continue
    else:
        board[x][y] = "X"
    done = False
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' 'and not done:
                board[i][j] = '0'
                done =True
                break;
#함수의 튜플 반환 예지
import math
def calCircle(r):
    area = math.pi * r * r
    circum =  2 * math.pi * r
    return (area,circum)
radius = float(input("원의 반지름을 입력하시오:"))
(a, c) = calCircle(radius)
print("원의 넓이는 "+str(a)+"이고 원의 둘레는"+str(c)+"이다.")
#타티 동시 참석사 알아내기
partyA = set(["Park","Kim","Lee"])
partyB = set(["Park","Choi"])
print("2개의 파티에 모두 참석한 사람은 다음과 같습니다.")
print(partyA.intersection(partyB))
#파일에서 중복되지 않은 단어의 개수 세기
def process(w):
    output =""
    for ch in w:
        if(ch.isalpha() ):
            output += ch
    return output.lower()
words = set()
fname = input("입력 파일 이름: ")
file = open(fname,"r")
for line in file:
    lineWords = line.split()
    for word in lineWords:
        words.add(process(word))
print("사용된 단어의 개수=",len(words))
print(words)
#영한 사전 만들기
english_dict = dict()
english_dict['one'] = '하나'
english_dict['two'] =  '둘'
english_dict['three'] = '셋'
word = input("단어를 입력 하시오: ")
print(english_dict.get(word,"없음"))
#단어 카운터
fname = input("파일 이름: ")
file = open(fname,"r")
table = dict()
for line in file:
    words = line.split()
    for word in words:
        if word not in table:
            table[word] = 1
        else:
            table[word] += 1
print(table)
#축약어 풀어쓰기
table = {"B4":"Before",
        "TX": "Thanks",
        "BBL": "Be Back Later",
        "BCNU": "Be Seeing You",
        "HAND": "Have A Nice Day"}
massage = input('번역할 문장을 입력하시오: ')
words = massage.split()
result = ""
for word in words:
    if word in table:
        result += table[word] + " "
    else:
        result += word
print(result)
#글자 빈도수 세기
string = input("문자열을 입력하시오: ")
countTable = {}
for letter in string:
    countTable[letter] = countTable.get(letter, 0) +1
print(countTable)
#이전값 기억시키기
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print(fib(20))
#희소 행렬 표현
matrix = {(1,2): 1, (2,2):2,(3,2):3}
for y in range(5):
    for x in range(5):
        print(matrix.get((y,x),0),end=" ")
    print()
#회문 검사하기
def chek_pal(s):
    low = 0
    high = len(s) -1
    while True:
        if low > high:
            return True
        a = s[low]
        b = s[high]
        if a !=b:
            return False
        low += 1
        high -=1
s = input("문자열을 입력하시오: ")
s = s.replace(" ","")
if(chek_pal(s)==True):
    print("회문 입니다.")
else:
    print("회문이 아닙니다")
#머리 글자어 만들기
phrase = input("문자열을 입력하시오: ")
acronym = ""
for word in phrase.upper().split():
    acronym +=word[0]
print(acronym)
#이메일 주소 분석
addres = input('이메일 주소를 입력하시오: ')
(id, domain) = addres.split("@")
print(addres)
print('     '+id)
print('     '+domain)
#문자열 분석
sentence = input("문자열을 입력하시오: ")
table = {"alphas":0,"digits":0,"spaces":0}
for i in sentence:
    if i.isalpha():
        table["alphas"] +=1
    if i.isdigit():
        table["digits"] +=1
    if i.isspace():
        table["spaces"] +=1
print(table)
#원을 클래스로 표현
import math
class Circle:
    def __init__(self,radius = 1.0):
        self.__radius = radius
    def setRadius(self,r):
        self.__radius = r
    def getRadius(self):
        return self.__radius
    def carcArea(self):
        area = math.pi*self.__radius*self.__radius
        return area
    def calcCircum(self):
        circumference = 2.0*math.pi*self.__radius
        return circumference
c1 = Circle(10)
print("원의 반지름=",c1.getRadius())
print("원의 넓이",c1.calcCircum())
print("원의 둘레=",c1.calcCircum())
#은행 계좌
class BankAccount:
    def __init__(self):
        self.__balance = 0
    def withdraw(self,amount):
        self.__balance -=amount
        print("통장에 ",amount,"가 입금 되었음")
        return self.__balance
    def deposit(self,amount):
        self.__balance += amount
        print("통장에서 ",amount,"가 출금 되었음")
        return self.__balance
a = BankAccount()
a.deposit(100)
a.withdraw(10)
#자동차 클래스 작성 #오류 나옴
class Car:
    def __init__(self,speed=0,gear=1,color="white"):
        self.__speed=speed
        self.__gear=gear
        self.__color=color
    def setColor(self,speed):
        self.__speed = speed
    def serGear(self,gear):
        self.__gear = gear
    def setColor(self,color):
        self.__color = color
    def __str__(self):
        return '(%d,%d,%s)'%(self.__speed,self.__gear,self.__color)
myCar = Car()
myCar.setGear(3);
myCar.setSpeed(100);
print(myCar)
#계산기
from tkinter import *
from math import *
def calculate(event):
    label.configure(text = "결과:" + str(eval(entry.get())))
Window=Tk()
Label(window,text="파이썬 수식 입력:").pack()
entry = Entry(window)
entry.bind("<Return>",calculate)
entry.pack()
label = Label(window,text = "결과:")
label.pack()
w.mainloop()
#랜덤한 사각형 그리기  # 오류 나옴
import random
from tkinter import *
window = Tk()
canvas = Canvas(window ,width=500 ,heigth=400);
canvas.pack()
color = ["red","orange","yellow","green","blue","violet"]
def draw_rect():
    x = random.randint(0.500)
    y = random.randint(0,400)
    w = random.randint(100)
    h = random.randint(100)
    canvas.create_rectangle(x,y,w,h, fill = random.choice(color))
for i in range(10):
    draw_rect()
window.mainloop()
#마우스로 그림 그리기
from tkinter import *
w = 500
h = 300
def drawDot(event):
    x1,y1 = (event.x - 1),(event.y - 1)
    x2,y2 = (event.x + 1),(event.y + 1)
    canvas.create_oval(x1,y1,x2,y2, fill = "red")
window = Tk
canvas = Canvas(window, width=w, heigth=h)
canvas.pack(expand = YES, fill = BOTH)
canvas.bind("<B1-Motion>",drawDot)
message = Label(window,text = "마우스를 드래그하면 점들이 그려집니다.")
message.pack(side = BOTTOM)
window.mainloop()
#배치 관리자 사용하기
from tkinter import *
window = Tk()
colors = ["green","red","orange","white","yellow","blue"]
r = 0
for c in colors:
    Label (window,text=c, relief=RIDGE,width=15).grid(row=r,column=0)
    r = r = 1
window.mainloop()
#스톱워치 만들기
import tkinter as tk
def startTimer():
    if (running):
        global timer
        timer += 1
        timeText.configure(text=str(timer))
    window.after(10,startTimer)
def start():
    global running
    running = False
running = False
window = tk.Tk()
timer = 0
timeText = tk.Label(window,text="0",font=("Helvetica",80))
timeText.pack()
startButton = tk.Button(window,text='시작',bg="yellow",command=start)
startButton.pack(fill=tk.BOTH)
stopButton = tk.Button(window,text='중지',bg="yellow",command=stop)
stopButton.pack(fill=tk.BOTH)
startTimer()
window.mainloop()
#계산기 만들기
from tkinter import *
def click(key):
    if key == "=":
        try:
            result = eval(entry.get())
            entry.delete(0,END)
            entry.insert(END,str(result))
        except:
            entry.insert(END,"오류!")
    elif key == ("C"):
        entry.delete(0,END)
    else:
        entry.insert(END,key)
window = Tk()
window.title("간단한 계산기")
buttons = [
'7',  '8',  '9',  '+',  'C',
'4',  '5',  '6',  '-',  '  ',
'1',  '2',  '3',  '*',  '  ',
'0',  '.',  '=',  '/',  '   ']
i = 0
for b in buttons:
    cmd = lambda x=b: click(x)
    but = Button(window,text=b,width=5,relief='ridge',command=cmd)
    but.grid(row=i//5+1,column=i%5)
    i += 1
entry = Entry(window,width=33,bg="yellow")
entry.grid(row=0, column=0, columnspan=5)
window.mainloop()
#숫자 추칙 게임    (오류 원인을 못 찾았음)
from tkinter import *
import random
answer = random.randint(1,100)
def guessing():
    guess = int(guessField.get())
    if guess > answer:
        msg = "높음!"
    elif guess < answer:
        msg = "낮음!"
    else:
        msg = '정답!'
    resultLabel["text"]=msg
    guessField.delete(0,5)
def reset():
    global answer
    answer = random.randint(1,100)
    resultLabel["text"] = "다시 한번 하세요!"
window = Tk()
window.configure(bg="white")
window.title("숫자를 맞춰보세요!")
window.geometry("500*80")
titleLabel = Label(window, text="숫자 게임에 오신것을 환영합니다!",
                   bg="white")
titleLabel.pack()
guessField = Entry(window)
guessField.pack(side="left")
tryButton = Button(window,text="시도",fg="green",bg="while",
                   command=guessing)
tryButton.pack(side="left")
resetButton = Button(window,text="조기화",fg="red",bg="white",
                     command=reset)
resetButton.pack(side="left")
resetLabel = Label(window,text="1부터 100사이의 숫자를 입력하시오.",
                   bg="while")
resultLabel.pack(side="left")
window.mainloop()
#패스워드 시스템
from tkinter import *
def print_fields():
    print("아이디: %s"%(e1.get(),e2.get()))
window = Tk()
Label(window,text="아이디").grid(row=0)
Label(window,text="패스워드").grid(row=1)
e1 = Entry(window)
e2 = Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=2, column=1)
Button(window,text='로그인',command=print_fields).grid(row=3,
                                                    column=0,sticky=W,pady=4)
Button(window,text="쥐소 ",command=window.quit).grid(row=3,
                                                   column=1,sticky=W,pady=4)
window.mainloop()
#키를 이용한 정렬 예제
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __repr__(self):
        return "<이름: %s,나이: %s>" %(self.name,self.age)
def keyAge(person):
    return person.age
people = [Person("홍길동",20),Person("김철수",35),Person("최자영",38)]
print(sorted(people,key=keyAge))
#피보나치 이터레이터     (오류 원인을 못 찾았음)
class FibIterator:
    def __init__(self,a=1,b=0,maxValue=50):
        self.a=a
        self.b=b
        self.maxValue=maxValue

    def __init__(self):
        return self
    def __init__(self):
        n = self.a + self.b
        if n > self.maxValue:
            raise StopIteration()
        self.a = self.b
        self.b=n
        return n
for i in FibIterator():
    print(i,end=" ")
#book 클래스
class book:
    title = ''
    pages = 0
    def __init__(self,title='',pages=0):
        self.title = title
        self.pages = pages
    def __str__(self):
        return self.title
    def __add__(self, other):
        return self.pages + other
#동전 던지기 게임
import random
myList = ["head","tail"]
while (True):
    response = input("동전 던지기를 계속하시겠습니까?(yes,no) ");
    if response == "yes":
        coin = random.choice(myList)
        print(coin)
    else:
        break
#sportscar 클래스
class Car:
    def __init__(self,speed):
        self.speed = speed
    def setSpeed(self,speed):
        self.speed = speed
    def getDesc(self):
        return "차량 =("+str(self.speed) +")"
class SportsCar(Car):
    def __init__(self,speed,turbo):
        super().__init__(speed)
        self.turbo=turbo
    def setTurbo(self,turbo):
        self.turbo=turbo
obj = SportsCar(100,True)
print(obj.getDesc())
obj.setTurbo(False)
#도형
class Shape:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def area(self):
        print("계산할수 없음!")
    def perimeter(self):
        print("계산할수 없음!")
class Rectangle(Shape):
    def __init__(self,x,y,w,h):
        self.w=w
        self.h=h
    def area(self):
        return self.w*self.h
    def perimeter(self):
        return 2*(self.w+self.h)
r = Rectangle(0,0,100,200)
print("사각형의 면적",r.area())
print("사각형의 둘레",r.perimeter())
#학생과 강사
class Person:
    def __init__(self,name,number):
        self.name = name
        self.number = number
class Student(Person):
    UNDERGRADUATE = 0
    POSTGRAdUATE = 1
    def __init__(self,name,number,studentType):
        super().__init__(name,number)
        self.studentType = studentType
        self.gpa=0
        self.classes = []
    def enrollCourse(self,course):
        self.classes.append(course)
    def __str__(self):
        return "\n수강과목="+str(self.classes)+"\n평점="+str(self.gpa)
class Teacher(Person):
    def __init__(self,name,number):
        super().__init__(name,number)
        self.courses = []
        self.salary=3000000
    def assignTeacher(self,course):
        self.courses.append(course)
    def __str__(self):
        return "\n이름="+self.name+ "\n주민번호="+self.number+"\n강의과목="+str(self.courses
            )+"\n월급="+str(self.salary)
hong = Student("홍길동","12345678",Student.UNDERGRADUATE )
hong.enrollCourse("자료구조")
print(hong)
kim = Teacher("김철수","123456790")
kim.assignTeacher("Python")
print(kim)
#은행계좌
class BankAccount:
    def __init__(self,name,number,balance):
        self.balance = balance
        self.name = name
        self.number = number
    def withdraw(self,amount):
        self.balance-= amount
        return self.balance
    def deposit(self,amount):
        self.balance += amount
        return self.balance
class SavingsAccoint(BankAccount):
    def __init__(self,name,number,balance,interest_rate):
        super().__init__(name,number,balance)
        self.interest_rate = interest_rate
    def set_interest_rate(self,interest_rate):
        self.interest_rate = interest_rate
    def get_interest_rate(self):
        return self.interest_rate
    def add_interest(self):
        self.balance ++ self.balance*self.interest_rate
class ChekingAccount(BankAccount):
    def __init__(self,name,number,balance):
        super().__init__(name,number,balance)
        self.withdraw_charge =10000
    def withdraw(self,amount):
        return BankAccount.withdraw(self,amount + self.withdraw_charge)
a1 = SavingsAccoint("홍길동",123456,10000,0.05)
a1.add_interest()
print("저죽예금의 잔액=",a1.balance)
a2 = ChekingAccount("김철수",123457,2000000)
a2.withdraw(100000)
print("저죽예금의 잔액=",a2.balance)
#직원과 매니저
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def getSalary(self):
        return salary
class Manager(Employee):
    def __init__(self,name,salary,bonus):
        super().__init__(name,salary)
        self.bonus = bonus
    def getSalary(self):
        salary = super().getSalary()
        return salary +self.bonus
    def __repr__(self):
        return "이름: "+self.name+ "; 월급: "+str(self.salary)+";보너스: "+str(self.bonus)
kim = Manager("김철수",2000000,1000000)
print(kim)
#vehicle과 car,Truck
class Book:
    def __init__(self,title,isbn):
        self.__title = title
        self.__isbd = isbn
    def __repr__(self):
        return "ISBN: "+self.__isbd+ ";TITLE:"+self.__title
book = Book("The Python Tutorial","0123456")
print(book)
#Card와 Deck
class Card:
    suitNames = ['클럽','다이아먼드','하트','스페이트']
    raknNamen = [None,'에이스','2','3','4','5','6','7','8','9','10','잭','퀸','킹']
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return Card.suitNames[self.suit]+" "+\
               Card.rankNames[self.rank]
class Deck:
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1,14):
                card = Card(suit,rank)
                self.cards.append(card)
    def __str__(self):
        lst = [str(card)for card in self.cards]
        return str(lst)
deck = Deck()
print(deck)
#매출 파일 처리
infilename = input("입력 파일 이름: ")
outfilename = input("출력 파일 이름: ")
infile = open(infilename,"r")
outfile = open(outfilename,"w")
sum = 0
count = 0
for line in infile:
    dailySale = int(line)
    sum = sum + dailySale
    count = count + 1
outfile.write("총매출 = "+str(sum)+"\n")
outfile.write("평균 일매출 = "+str(sum/count))
infile.close()
outfile.close()
#스페이스 세기
def parse_file(path):
    infile = open(path)
    spaces = 0
    tabs = 0
    for line in infile:
        spaces += line.count(' ')
        tabs += line.count('\t')
    infile.close()
    return spaces, tabs
filename = input("파일 이름을 입력하시오: ")
spaces,tabs = parse_file(filename)
print("스페이스 수 = %d,탭의 수 = %d")
#줄앞에 번호 붙이기
infile = open("proverbs.txt")
outfile = open("outfile.txt","w")
i = 1
for line in infile:
    outfile.write(str(i)+": "+ line)
    i = i + 1
infile.close()
outfile.close()
#각 문자 횟수 세기
filename = input("파일명을 입력하시오: ").strip()
infile = open(filename, "r")
freqs = {}
for line in infile:
    for char in line.strip():
        if char in freqs:
            freqs[char]+= 1
        else:
            freqs[char] = 1
print(freqs)
infile.close()
#CSV 파일 읽기
f = open("C:\\test.csv", "r")
for line in f.readlines():
    line = line.strip
    print(line)
    parts = line.split(",")
    for part in parts:
        print("  ",part)
#파일 암호화
key = 'abcdefghigklmnopqrstuvwxyz'
def encrypt(n,plaintext):
    result = ''
    for l in plaintext.lower():
        try:
            i  = (key.index(l)+n)%26
            result +=key[i]
        except ValueError:
            result +=l
    return result.lower()
def decrypt(n,ciphertext):
    result = ''
    for l in ciphertext:
        try:
            i = (key.index(l)-n)%26
            result += key[i]
        except ValueError:
            result += l
    return result
n = 3
encrypted = encrypt(n, 'text')
text='the language of truth is simple.'
decrypted = decrypt(n,encrypted)
print("평문: ",text)
print("암호문: ",encrypted)
print("복호문: ",decrypted)
#이미지 파일 복사하기
filename1 = input("원본 파일 이름을 입력하시오: ")
filename2 = input("복사 파일 이름을 입력하시오: ")
infile = open(filename1, "rb")
outfile = open(filename2, "wb")
while True:
    copy_buffer = infile.read(1024)
    if not copy_buffer:
        break
    outfile.write(copy_buffer)
infile.close()
outfile.close()
print(filename1+"를 "+filename2+"로 복사 하였습니다.")
#에라스토스의 체
def eratosthenes(n):
    multiples = set()
    for i in range(2, n + 1):
        if i not in multiples:
            yield i
            multiples.update(range(i * i, n + 1, i))


print(list(eratosthenes(100)))
#프랙탈 그래픽
import turtle
def drawTree(branch,t):
    if branch>5:
        t.forward(branch)
        t.right(20)
        drawTree(branch-15,t)
        t.left(40)
        drawTree(branch-15,t)
        t.left(20)
        t.backward(branch)
def main():
    t = turtle.Turtle()
    window = turtle.Screen()
    t.left(90)
    t.up()
    t.backward(200)
    t.down()
    t.color("green")
    drawTree(100,t)
    window.exitonclick()
main()
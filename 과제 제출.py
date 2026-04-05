# 1. 2부터 100사이의 모든 짝수를 출력하는 반복문을 작성해 보세요.
print('2부터 100사이의 모든 짝수를 출력하기')
for i in range(1,101):
    if i%2==0:
        print(i)

#125+262의 값은 얼마일가?
import random
n = random.randint(1,100)
m = random.randint(1,100)
num = n+m

num1 = 125 + 262
print(num)
for i in range(100):
    answar = int(input("125+262의 값은 얼마일가:"))
    if answar == num1:
        print("맞았습니다")
        break
else:
    print("틀렸습니다")

print("'0'누르시면 반복이 끝납니다")
total = 0
while True:
    number = int(input("정수 입력하세요:"))
    if number == 0:
        total = total + number
        print(f"합은 {total} 입니다")
        break
else:
    print("문자열 불가 숫자만 가능")

#다음의 for 루프를 while 루프로 변환해보기
i = 1
while i < 101 :
    print(i)
    i = i + 1

#구구단표를 출력하기
for i in range(1,10):
    for n in range(1,10):
        print(i * n, end="\t")
    print("\n")

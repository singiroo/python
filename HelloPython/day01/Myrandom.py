from random import *


i = randint(1,2)
com=""
if(i==2):
    com = "짝"
else:
    com = "홀"



mine = input("홀/짝을 입력하세요")
print("당신의 선택 : "+mine)

if (com == mine):
    print("이겼습니다")
else:
    print("졌습니다")

print("정답  :",com)
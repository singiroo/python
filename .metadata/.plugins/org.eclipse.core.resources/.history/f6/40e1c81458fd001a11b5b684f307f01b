from random import *
gawi = ["가위","바위","보"]

com=""
mine = ""
res = ""

# 컴퓨터와 플레이어의 선택
i = randint(0,2)
com = gawi[i]
mine = input("가위, 바위, 보중에 하나를 입력하세요")
# 가위 바위 보 이외의 것을 쓰면 반복

while(mine not in gawi):
    print("다시 입력해주세요")
    mine = input("가위, 바위, 보중에 하나를 입력하세요")

# 가위 바위 보의 승패 판정
if(com == "가위" and mine =="보") or (com=="바위" and mine =="가위" ) or(com == "보"and mine =="바위"):
    res = "졌습니다"
elif(com == mine):
    res = "비겼습니다"
else:
    res = "이겼습니다"
#결과
print(res)
print("나 : {}   컴 : {}".format(mine,com))
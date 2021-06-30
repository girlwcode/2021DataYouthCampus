# """
# DIY6 : 리스트
# """
# student = [100,65, 70, 80, 90]
# print("총점 : ", sum(student))
# print("평균 : ", sum(student)/len(student))
#
# """
# DIY7 : 리스트
# """
# score = [100,65,70,80,30]
# weight = [.1,.3,.2,.2,.2]
# sum = 0
#
# for i in range (len(score)) :
#     sum += score[i] * weight[i]
#
# print("총점 : ", sum)
#
#
# """
# DIY8 : 소수 출력
# """
# num = int(input("숫자 입력 : "))
#
# for i in range (2, num) :
#     if (num % i == 0) :
#         print("소수가 아님")
#         break
#     else: print(num, "은 소수입니다.")
#     break
#
# """
# DIY9 : 숫자 맞추기
# """
# print("숫자 맞추기")
# import random as rd
# target = rd.randint(0,99)
# print("target :", target)
# ip = int(input("숫자를 입력하세요 : "))
#
# while (ip != target) :
#     ip = int(input("틀렸습니다. 숫자를 입력하세요 : "))
#     if (ip < target) :
#         print("hint : UP")
#     else: print("hint : DOWN")
#
#
# print("정답입니다.")
#
# """
# DIY10 : 가위 바위 보
# """
# print("가위 바위 보")
# ip = input("가위 바위 보 중 입력하세요 (한글만) : ")
# com = rd.randint(1,3)
#
# if (ip == "가위") :
#     ip = 2
#     if (ip < com) :
#         print("졌습니다. com : 주먹")
#     if (ip > com) :
#         print("이겼습니다. com : 보")
#     if (ip == com):
#         print("비겼습니다. com : 가위")
#
# elif (ip == "바위") :
#     ip = 2
#     if (ip < com) :
#         print("졌습니다. com : 보")
#     if (ip > com) :
#         print("이겼습니다. com : 가위")
#     if (ip == com):
#         print("비겼습니다. com : 바위")
#
# elif (ip == "보") :
#     ip = 2
#     if (ip < com) :
#         print("졌습니다. com : 가위")
#     if (ip > com) :
#         print("이겼습니다. com : 주먹")
#     if (ip == com):
#         print("비겼습니다. com : 보")

import random as rd
"""
DIY11 : 숫자야구
1. 4자리 숫자 랜덤 할당 (0 안됨)
2. 4s면 게임 종료
"""
answer = []

for i in range(4):
    a = rd.randint(1,9)
    while a in answer :              # a가 이미 뽑은 리스트에 있을 때까지 다시 뽑자
        a = rd.randint(1,9)
    answer.append(a)


a,b,c,d =map(int, input("숫자 4개 입력").split())
user = [a,b,c,d]

while (True) :
    a, b, c, d = map(int, input("숫자 4개 입력").split())
    user = [a, b, c, d]
    strike = 0
    ball = 0
    for i in range (len(answer)):
        if answer[i] in user :
            if answer[i] == user[i]:
                strike += 1
            else:
                ball += 1
    print(strike,"strike", ball, "ball")
    if (strike == 4) :
        print("정답")
        break
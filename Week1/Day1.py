"""
DIY1 : Convert Celsius to Fahrenheit
"""
c = int(input("Enter the Celsius : "))
f = c * 1.8 + 32
print("Converted Celsius ",c, " to Fahrenheit is ", f)

"""
newString = str.replace(a,b) : b를 a로 바꾸고 새로운 문자열(newString)을 만듦
strip() :  앞뒤 공백을 제거하는 함수 

DIY2 
1. 앞뒤 공백을 제거
2. "공백" 이라는 문자열로 분리를 하고 난 결과의 index가 1인 문자열
3. index가 3인 문자는?
"""
diyString = "처음에는 글이 있고 중간에는             공백이 길고, 끝 부분에는 공백이 짧아요 "
#1
print(diyString.strip())
#2
print(diyString.split("공백")[1])
#3
print(diyString[3])

"""
DIY3 : 총점을 입력하면 A~F의 학점을 출력하는 계산기
"""

score = int(input("총점을 입력하세요 : "))

if score >= 90 : print("score is A")
elif score >= 80 : print("score is B")
elif score >= 70 : print("score is C")
elif score >= 60 : print("score is D")
else : print("F")


"""
DIY4 : 별 만들기
"""

def printStar (num) :
    num = int(num)
    if num == 1 :
        for i in range(6) :
            print("*" * i)
        print("\n")

    elif num == 2 :
        for i in range(6):
            print("*" * (i * 2 - 1))
        print("\n")

    elif num == 3 :
        for i in range (5,0,-1):
            print("*" * i)
        print("\n")

    elif num == 4 :
        for i in range (6) :
            print(" " * (5-i) , "*" * (i * 2 - 1))
        print("\n")

    elif num == 5 :
        for j in range (6,0,-1):
            for i in range (1,j) :
                print(i, end="")
            print()
        print("\n")

    elif num == 6 :
        for j in range(5, 0, -1):
            print(" " * (5-j), end="")
            for i in range(1, j):
                print(i, end="")
            for k in range(j, 0, -1):
                print(k, end="")
            print()
        print("\n")


"""
DIY5 : 구구단 함수 만들기
"""
def printDan (dan) :
    dan = int(dan)
    print(dan,"단 구구단 시작")
    for i in range (1,11) :
        print(dan," * ",i," = ", dan * i)

num = input("단 입력 : ")
printDan(num)


for i in range (7) :
    printStar(i)



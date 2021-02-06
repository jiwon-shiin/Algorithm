# 백준 2577 숫자의 개수 (신지원)

A = int(input())
B = int(input())
C = int(input())

mul = str(A*B*C) #곱한 값을 문자열로 변환하여 변수에 저장
for i in range(10): #0부터 9까지 수를
    print(mul.count(str(i))) #곱한 값에서 문자형으로 개수를 세서 출력
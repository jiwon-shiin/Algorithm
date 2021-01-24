# 백준 1629 곱셈 (신지원)

def power(a,n): #거듭제곱을 더 빨리 할 수 있도록 함수 작성
    if n == 0: #a^0 = 1임
        return 1
    x = power(a,n//2)%C #수행시간을 줄이기 위해 x값에 power(a,n//2) 값을 C로 나눈 나머지를 저장
    if n%2 == 0: #짝수번이라면
        return x*x #power(a,n//2)를 제곱하는 방법
    else: #홀수번이라면
        return x*x*a #거기에 a를 한번 더 곱하는 방법
    
A,B,C = map(int,input().split()) #A,B,C를 입력받고
print(power(A,B)%C) #최종값에서 C로 나눈 나머지를 출력

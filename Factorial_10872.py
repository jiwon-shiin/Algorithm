# 백준 10872 팩토리얼 (신지원)

def factorial(n):
    if n <= 1: return 1 #base case
    return n * factorial(n-1) #재귀적으로 실행

n = int(input())
print(factorial(n)) #결과를 출력
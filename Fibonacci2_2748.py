# 백준 2748 피보나치 수 2 (신지원)

n = int(input())
Fib = [0,1] #DP 테이블에 저장할 것임
for i in range(2,n+1):
    Fib.append(Fib[i-1]+Fib[i-2]) #전 수와 전전 수를 더하여 리스트에 추가
print(Fib[-1]) #마지막 원소를 출력하면 됨
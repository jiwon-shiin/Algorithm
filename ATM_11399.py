# 백준 11399 ATM (신지원)

N = int(input())
time = list(map(int,input().split()))
time.sort()
total = 0
for i in range(len(time)): 
    total += sum(time[:i+1])
print(total)
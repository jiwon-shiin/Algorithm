# 백준 11047

N, K = map(int, input().split())
money= []
for i in range(N):
    money.append(int(input()))

total = 0
for i in range(N-1,-1,-1):
    coins = K//money[i]
    total += coins
    K -= coins*money[i]
    if K == 0:
        break
print(total)

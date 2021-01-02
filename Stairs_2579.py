# 백준 2579

def stairs(S):
    DP = [0]*len(S)
    if len(S) == 2: return S[1]
    if len(S) == 3: return S[1]+S[2]
    DP[1] = S[1]
    DP[2] = S[2]+S[1]
    for i in range(3,len(S)):
        DP[i] = max(DP[i-2]+S[i], DP[i-3]+S[i-1]+S[i])
                
    return DP[-1]

N = int(input())
S = [0]
for i in range(N):
    score = int(input())
    S.append(score)
print(stairs(S))
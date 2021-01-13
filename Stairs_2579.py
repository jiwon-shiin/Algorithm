# 백준 2579 계단 오르기 (신지원)

def stairs(S):
    if len(S) == 2: return S[1] #계단의 수가 1이라면 리스트의 크기가 2일 것
    if len(S) == 3: return S[1]+S[2] #계단의 수가 2라면 리스트의 크기가 3일 것
    DP = [0]*len(S) #DP 테이블을 만들어줌
    DP[1] = S[1] #DP[1]은 한 가지 방법으로 한 칸 올라가는 방법 뿐
    DP[2] = S[2]+S[1] #DP[2]의 최댓값은 1번을 밟고 올라가는 방법 뿐
    for i in range(3,len(S)):
        DP[i] = max(DP[i-2]+S[i], DP[i-3]+S[i-1]+S[i]) #전칸+전전전칸 or 전전칸 비교하여 큰 값 DP에 저장
                
    return DP[-1] #마지막 칸의 점수 반환 

N = int(input())
S = [0] #시작점도 0으로 따질 것임. 계단 수와 인덱스 맞추기 위해
for i in range(N):
    score = int(input())
    S.append(score) #각 계단의 점수를 넣음
print(stairs(S)) #반환된 값을 출력
# 백준 1149 RGB거리 (신지원)

N = int(input()) #집의 수
RGB = [] #각 집을 빨강, 초록, 파랑으로 칠하는 비용을 저장할 리스트
DP = [[] for i in range(N)] #모든 집을 칠하는 경우를 저장할 DP테이블
for i in range(N):
    RGB.append(list(map(int,input().split()))) #집을 칠하는 비용을 입력받아 저장

for i in range(N): #모든 집에 대하여
    for j in range(3): #빨,초,파에 대하여
        if i == 0: #첫번째 집의 경우
            DP[i].append(RGB[i][j]) #그냥 비용 저장
        else: #두번째부터는
            DP[i].append(min(DP[i-1][(j+1)%3],DP[i-1][(j+2)%3])+RGB[i][j]) #현재 집과 직전 집을 다른색으로 칠하도록 할 때 더 비용이 적은 값을 저장(2가지 경우 중에)
    
print(min(DP[-1][0],DP[-1][1],DP[-1][2])) #마지막 집까지 구했을 때 세 가지 색 중에 가장 적은 비용을 갖는 값 출력
# 백준 13305 주유소 (신지원)

N = int(input()) #도시의 개수
length = list(map(int, input().split())) #두 도시 사이의 거리
gas = list(map(int, input().split())) #왼쪽 도시부터 순서대로 리터당 기름의 가격

min_gas = 0 #최소비용(정답)을 저장할 변수
before = gas[0] #더 적은 돈을 저장할 변수
for i in range(N-1): #N개의 도시 사이의 N-1개의 도로가 있음
    if length[i]*gas[i] >= length[i]*before: #해당 도시의 기름값*길이가 더 비쌀 경우
        min_gas += length[i]*before #전 도시에서의 기름값
    else: #전 도시의 기름값*길이가 더 비쌀 경우
        min_gas += length[i]*gas[i] #현재 도시의 기름값
    before = min(before,gas[i]) #현재도시와 직전 도시 중 더 싼 기름 값을 저장

print(min_gas) #최솟값 출력
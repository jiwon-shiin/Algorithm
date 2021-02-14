# 백준 2156 포도주 시식 (신지원)

def drink_wine(n): #최대 포도주 양을 구할 함수
    wines = [0] #각 포도주 양을 저장할 리스트(인덱스를 번호와 맞추기 위해 0을 넣음)
    for i in range(n):
        wines.append(int(input())) #포도주 양을 입력받아 저장
    if n < 2: #n이 1이라면
        return wines[-1] #포도주 양 바로 반환
    DP = [0,wines[1],wines[1]+wines[2]]+[0]*(n-2) #각 포도주의 위치에서의 최댓값을 저장할 리스트. 인덱스 맞추기 위해 0, 첫번째 두번째는 바로 값을 넣고 나머지는 0으로 초기화
    for i in range(3,n+1): #3번째부터 n번째까지
        wine = max(DP[i-3]+wines[i-1]+wines[i],DP[i-2]+wines[i],DP[i-1]) #1. 전전전포도주와 전포도주와 현재포도주를 마신다 2. 전전포도주와 현재포도주를 마신다 3. 현재 포도주를 마시지 않는다
        DP[i] = wine #중 최댓값을 DP[i]에 저장
    return DP[-1] #마지막 포도주에 도달했을 때의 값을 반환

n = int(input()) #포도주의 수 입력받음
print(drink_wine(n)) #최대 포도주 양을 구해 출력
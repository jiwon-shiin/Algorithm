# 백준 1932 정수 삼각형 (신지원)

n = int(input()) #삼각형의 크기
triangle = [] #삼각형 모양을 저장할 리스트
for i in range(n):
    triangle.append(list(map(int,input().split()))) #삼각형 모양이 주어지고 이중배열 형태로 한 줄씩 저장

DP = [triangle[-1]] #가장 아래에서부터 위로 올라가도록 DP를 작성할 것임. 맨 마지막 줄은 원래 형태대로 DP에 넣음
for i in range(n-2,-1,-1): #밑에서 두번째부터는
    row = [] #각 줄의 최댓값을 구하여 저장할 리스트. 한 줄이 끝나면 초기화됨
    for j in range(i+1):
        row.append(max(triangle[i][j]+DP[n-2-i][j], triangle[i][j]+DP[n-2-i][j+1])) #아래 층의 두 가지 경우 중 큰 값을 더하여 DP애 저장할 것
    DP.append(row) #DP에 한 줄 저장
print(DP[-1][-1]) #최종 맨 윗층 값은 맨 뒤에 저장되어 있을 것이므로 출력
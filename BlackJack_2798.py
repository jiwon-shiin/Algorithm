# 백준 2798 블랙잭 (신지원)

N,M = map(int,input().split()) #N과 M을 각각 입력 받음(카드의 수와 최대합)

cards = list(map(int,input().split())) #각 카드의 값을 정수형으로 바꾸어 리스트로 만들어줌
cards.sort(reverse = True) #카드를 내림차순으로 정렬

answer = 0 #정답을 저장할 변수
for i in range(N): #i,j,k의 범위를 지정하는데 모든 경우를 탐색할 수 있도록 j는 i+1부터 N까지, k는 j+1부터 N까지
    for j in range(i+1,N):
        for k in range(j+1,N):
            sum_these = cards[i]+cards[j]+cards[k] #이 세개의 카드의 합을 구했을 때
            if sum_these <= M: #M보다 작거나 같고
                if answer < sum_these: #현재 저장된 answer보다 크다면
                    answer = sum_these #answer를 현재 값으로 수정한다
    
print(answer) #최종 구해진 M을 넘지 않는 최대값을 출력
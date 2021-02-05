# 백준 2217 로프 (신지원)

N = int(input()) #로프의 수

ropes = [] #로프들이 버틸 수 있는 최대 중량 리스트
for i in range(N):
    ropes.append(int(input())) #리스트에 넣음
ropes.sort(reverse = True) #내림차순으로 정렬
max_w = 0 #최대 중량을 저장할 변수
for i in range(N): #최종적으로 구하고자 하는 것 = 로프가 최대로 버틸 수 있는 무게 * 로프들의 개수가 최대가 되는 지점
    if ropes[i]*(i+1) > max_w: #현재 로프의 중량 * 현재까지 있는 로프들(가장 큰 것부터 차례로)이 최댓값보다 크다면
        max_w = ropes[i]*(i+1) #최댓값 수정
print(max_w) #최댓값 출력
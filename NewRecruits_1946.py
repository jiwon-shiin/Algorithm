# 백준 1946 신입 사원 (신지원)

import sys

T = int(sys.stdin.readline()) #테스트케이스의 수
for i in range(T):
    N = int(sys.stdin.readline()) #지원자의 수
    a = [] #지원자들을 저장할 리스트
    for i in range(N):
        a.append(tuple(map(int,sys.stdin.readline().split()))) #지원자들의 (서류 순위, 면접 순위)를 튜플형태로 저장
    sorted_a = sorted(a,key=lambda x:x[0]) #서류순위를 기준으로 정렬
    first = sorted_a[0][1] #합격된 사람 중 면접 등수가 가장 높은 사람을 저장할 변수. 서류 순위를 기준으로 정렬하였으므로 일단 서류 순위 1등의 면접 순위를 저장
    answer = 1 #서류 순위 1등은 합격. 최대 인원을 저장할 변수
    for i in range(1,N): #1등 제외 2등부터 순차적으로 돌며
        if sorted_a[i][1]<first: #현재 가장 좋은 면접 점수보다 면접 점수가 좋다면
            first = sorted_a[i][1] #가장 좋은 면접 점수를 수정한 후
            answer +=1 #합격인원에 포함시킴
    print(answer) #각 테스트케이스마다 정답 출력
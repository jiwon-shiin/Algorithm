# 백준 15656 N과 M (7) (신지원)

def findAll(count): #백트랙킹을 이용해 모두 구할 함수
    if count == M: #count가 M을 도달하면
        print(" ".join(map(str,answer))) #answer에 있는 것들을 문자열로 변환하여 공백을 사이에 두고 연결하여 출력한다
        return #종료
    for i in range(N): #0부터 N-1까지의 인덱스를 활용해
        answer.append(A[i]) #answer에 넣고
        findAll(count+1) #count를 하나 늘린 상태로 재귀적으로 호출하고
        answer.pop() #모두 찾은 후에는 최근에 넣은 것을 다시 뺀다
N, M = map(int,input().split()) #N과 M을 입력받아 정수형으로 변환
A = list(map(int,input().split())) #N개의 수를 입력받아 A 리스트에 저장
A.sort() #오름차순으로 A를 정렬해준다
answer = [] #정답을 저장할 빈 배열
findAll(0) #count를 0으로 하여 시작
# 백준 15655 N과 M (6) (신지원)

def findAll(count,index): #모든 경우를 백트랙킹을 이용해 구할 것
    if count == M: #count가 M을 도달하면
        print(" ".join(map(str,answer))) #문자열로 변환하여 공백을 사이에 두고 출력
        return #종료
    for i in range(index,N): #현재 인덱스부터 N-1까지 인덱스 이용
        answer.append(A[i]) #정답 배열에 수 추가하고
        findAll(count+1,i+1) #count와 인덱스를 1씩 올려 재귀적으로 답을 모두 구한 후
        answer.pop() #가장 최근에 넣은 값 제거
        
N,M = map(int,input().split()) #N과 M을 입력받아 정수형으로 변환
A = list(map(int,input().split())) #N개의 수를 입력받아 정수형으로 변환하여 리스트에 저장
A.sort() #오름차순으로 정렬
answer = [] #정답을 저장할 리스트
findAll(0,0) #count와 index를 0으로 시작
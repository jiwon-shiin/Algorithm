# 백준 15657 N과 M (8) (신지원)

def getAll(count,i): #모든 수열을 구할 함수 (백트랙킹 이용)
    if count == M: #M개를 모두 골랐다면
        print(" ".join(answer)) #정답을 출력하고
        return #종료함
    for j in range(i,N):
        answer.append(str(numbers[j])) #순서에 맞는 수를 넣고
        getAll(count+1,j) #다음을 모두 구하도록 재귀적으로 호출
        answer.pop() #이용이 끝난 숫자 다시 제거

N,M = map(int,input().split()) #N과 M을 입력받음
numbers = list(map(int,input().split())) #N개의 수를 입력받아 배열로 저장
numbers.sort() #오름차순으로 정렬
answer = [] #정답을 저장할 배열
getAll(0,0) #count와 index를 모두 0으로 하여 시작함
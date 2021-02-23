# 백준 15649 N과 M (1) (신지원)

def getAll(count,index): 
    if count == M: #count가 M을 도달했다면
        print(" ".join(map(str,ans))) #정답 출력 후
        return #종료
    for i in range(N): #0부터 n-1까지 n번
        if i+1 in ans: #중복이 있다면
            continue #넘어감
        ans.append(i+1) #없다면 정답 리스트에 i+1 값을 추가하고
        getAll(count+1,i) #재귀적으로 함수를 호출하여 모든 경우를 구한 후
        ans.pop() #제일 최근에 넣었던 값을 제거한다
   
N,M = map(int,input().split()) #N,M 값 입력받음
ans = [] #정답을 저장할 리스트
getAll(0,0) #처음에는 count와 index를 0으로 하여 시작
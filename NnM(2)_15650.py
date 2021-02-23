# 백준 15650 N과 M (2) (신지원)

def getAll(count,index): #모든 수열을 구하기 위한 함수
    global N,M #N과 M은 전역변수로 이용할 것임
    if count == M: #지금까지의 개수가 M과 같다면
        if count != len(set(ans)): #중복이 있다면
            return #종료
        print(" ".join(map(str,ans))) #없다면 현재까지 나온 정답을 출력
        return #종료
    for i in range(index,N): #현재 인덱스부터 N이하의 수
        ans.append(i+1) #정답에 i+1값을 추가한다 (인덱스는 0부터 시작, 수는 1부터 시작하기 때문)
        getAll(count+1,i) #재귀적으로 호출하여 count가 M을 도달할 때까지 진행된 후 끝나면 이 위치로 돌아올 것이다 (순차적으로 찾게 됨)
        ans.pop() #추가했던 값을 이용해서 답을 찾았으므로 제거한다
   
N,M = map(int,input().split())
ans = [] #정답을 저장할 리스트
getAll(0,0) #처음에는 count와 index를 0으로 하여 시작
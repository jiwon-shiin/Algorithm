# 백준 15651 N과 M(3) (신지원)

def getAll(count,index): #수열을 하나하나 구하기 위한 함수
    if count == M: #count가 M을 도달하면(M개를 모두 골랐을 때)
        print(" ".join(answer)) #answer에 있는 수들 사이에 빈칸으로 연결하여 출력
        return #종료
    for i in range(N): #1부터 N까지 수를 모두 돌 것인데 인덱스는 1씩 차이남
        answer.append(str(i+1)) #인덱스와 수는 1씩 차이나기 때문에 i+1을 문자열로 변환하여 넣어줌
        getAll(count+1,i) #재귀적으로 호출. count가 M까지 갔다가 돌아올 것임
        answer.pop() #추가했던 수를 다시 뺀다
   
N,M = map(int,input().split())
answer = [] #정답을 저장할 리스트. 매 정답을 구한 후에는 빈 상태가 될 것임
getAll(0,0) #처음에는 count도 0, index도 0으로 시작함
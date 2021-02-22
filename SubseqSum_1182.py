# 백준 1182 부분수열의 합

def find(k,current_sum): #백트랙킹을 이용할 것. 함수를 재귀적으로 호출. k가 인덱스, current_sum은 현재까지 선택된 것의 합
    global count #count가 답을 저장할 변수이므로 전역변수로 이용함
    if k == N: #k가 N을 도달하면
        return #종료
    current_sum += A[k] #현재 합에 현재 값을 더함
    if current_sum == S: #더하여 S가 되었다면
        count += 1 #count로 세어줌
    find(k+1,current_sum) #k번째를 포함하도록 재귀적으로 호출
    find(k+1,current_sum-A[k]) #k번째를 포함하지 않도록 호출
        
N,S = map(int,input().split()) #N과 S를 입력받음
A = list(map(int,input().split())) #N개의 수를 입력받아 정수형으로 변환시켜 A 리스트에 저장
count = 0 #정답을 저장할 변수(전역으로 할 것임)
find(0,0) #find함수를 처음 호출
print(count) #최종적으로 구해진 count 출력
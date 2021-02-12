# 백준 9095 1,2,3 더하기 (신지원)

T = int(input()) #테스트 케이스의 개수
testcase = [] #테스트 케이스 저장할 리스트
max_num = 0 #최대 수를 구할 변수
for i in range(T):
    num = int(input()) #테스트 케이스를 입력받아
    testcase.append(num) #리스트에 추가하고
    if max_num < num: #현재 최대 수보다 크다면
        max_num = num #최대 업데이트
DP = [1,2,4] #DP를 만들어 각각의 방법 수를 저장할 것임 (1은 (1), 2는 (2),(1,1), 3은 (3),(1,2),(2,1),(1,1,1))
for i in range(3,max_num): #4부터
    DP.append(DP[i-1]+DP[i-2]+DP[i-3]) #이 전 방법 수들에 각각 1,2,3을 더하면 방법 수를 구할 수 있음
for i in testcase: #각 테스트 케이스에 대하여
    print(DP[i-1]) #정답 출력 (인덱스는 0부터이므로 -1씩)
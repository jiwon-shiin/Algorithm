# 백준 1003 피보나치 함수 (신지원)

T = int(input()) #테스트 케이스의 수
testcase = [] #테스트 케이스들을 저장할 리스트
max_num = 0 #최대 수를 저장할 변수
DP = [(1,0),(0,1)] #0은 fibonacci(0)을 호출, 1은 fibonacci(1)을 호출하므로 기본으로 튜플형태로 저장
for i in range(T):
    num = int(input()) #테스트 케이스를 입력받음
    testcase.append(num)
    if max_num < num: #현재 최댓값보다 입력받은 수가 크다면
        max_num = num #최댓값 업데이트
for i in range(2,max_num+1): #2부터 max_num까지
    DP.append((DP[i-1][0]+DP[i-2][0],DP[i-1][1]+DP[i-2][1])) #피보나치 함수에서 fibonacci(n-1) + fibonacci(n-2)를 호출하므로 전값과 전전값을 더해 0과 1의 호출 횟수를 튜플 형태로 넣어준다
for i in testcase: #테스트 케이스에 대하여
    print(DP[i][0], DP[i][1]) #각각의 횟수를 공백으로 구분하여 출력
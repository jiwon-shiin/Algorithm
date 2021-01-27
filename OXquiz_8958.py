# 백준 8958 OX퀴즈 (신지원)

N = int(input()) #테스트 케이스의 개수

for i in range(N):
    total = 0 #각 문제의 총합을 저장할 변수
    answer = 1 #연속된 정답일 경우 점수가 올라감
    quiz = input() #테스트케이스 입력받고
    for j in quiz:
        if j=="O": #정답이라면
            total+=answer #총합에 현재 점수를 더하고
            answer += 1 #현재 점수를 1점 올림
        else:
            answer = 1 #점수를 1점으로 리셋
    print(total) #각 테스트케이스마다 점수 출력
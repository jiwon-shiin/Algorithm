# 백준 2231 분해합 (신지원)

N = int(input()) #자연수 N이 주어짐

answer = 0 #정답을 저장할 변수 (없다면 0 출력할 것)
for i in range(N): #순차적으로 모두 탐색하며 가장 작은 생성자를 출력하도록 할 것이다
    num = i #num이라는 변수에 해당 수를 저장하고
    for j in range(len(str(i))): #해당 수의 각 자리 수를 더하여
        num+=int(str(i)[j])
    if num == N: #생성자인지 확인하고
        answer = i #맞다면 answer에 i를 저장하고
        break #반복문을 종료한다

print(answer) #답이 있다면 해당 답을 출력, 없다면 초기에 설정한 0을 출력할 것이다
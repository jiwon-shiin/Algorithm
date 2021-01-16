# 백준 10773 제로 (신지원)

K = int(input()) #정수 몇개가 주어질 지

stack = [] #스택을 이용할 것
for i in range(K):
    num= int(input())
    if num == 0: #입력받은 정수가 0이라면
        stack.pop() #가장 마지막에 들어온 수를 지우고
    else: #아니라면
        stack.append(num) #수를 스택에 추가한다
        
print(sum(stack)) #스택에 남은 수들의 합을 출력
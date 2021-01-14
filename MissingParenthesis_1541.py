# 백준 1541 잃어버린 괄호 (신지원)

eq = input().split("-") #입력된 식을 -기준으로 나누어 저장
answer = 0 #최종 값을 저장
for i in range(len(eq)): 
    if i==0: #-가 나오기 전까지는 모두 더해야 함
        for j in eq[0].split("+"):
            answer += int(j) #최종값에 더함
    else: #-가 나온 이후에는 뒤를 모두 뺀다
        for j in eq[i].split("+"):
            answer -= int(j) #최종값에서 뺌
print(answer) #최종값 출력

# 백준 2750 수 정렬하기 (신지원)

#Selection sort
N = int(input())

numbers = []
for i in range(N): #각 수를 입력받아 리스트에 저장
    number = int(input())
    numbers.append(number)

for i in range(N-1,0,-1): #가장 큰 수를 고른 뒤 맨 뒤와 바꿈(뒤에서 하나씩 줄여가며)
    index = numbers[:i+1].index(max(numbers[:i+1]))
    numbers[index],numbers[i] = numbers[i],numbers[index]

for i in numbers: #하나씩 출력
    print(i)
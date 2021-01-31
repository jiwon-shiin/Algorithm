# 백준 1026 보물 (신지원)

N = int(input()) #배열의 크기
A = list(map(int,input().split())) #A에 있는 N개의 수를 정수형으로 배열에 저장
B = list(map(int,input().split())) #B에 있는 N개의 수를 정수형으로 배열에 저장
#B는 재배열하지 않지만 A와B는 반대 순서이면 되므로 A는 오름차순, B는 내림차순으로 정렬한 후 순서대로 곱하면 됨
A.sort() #A 오름차순 정렬
B.sort(reverse= True) #B 내림차순 정렬

total = 0 #최솟값을 저장할 변수
for i in range(N):
    total += A[i]*B[i] #각 배열의 최소/최대부터 순차적으로 곱함.
print(total) #정답 출력
# 백준 10814 나이순 정렬 (신지원)

N = int(input()) #회원 수

members = [] #멤버들을 저장할 리스트
for i in range(N):
    age,name = input().split() #나이와 이름을 입력받아 하나의 튜플로 저장할 것
    members.append((int(age),name)) #정수형으로 바꾸지 않으면 '15'가 '5'보다 작다고 판단될 수 있는 문제점
members = sorted(members, key = lambda x:x[0]) #나이순으로 정렬. 이미 가입 순서대로 정렬되어 있음

for i in range(N):
    print(members[i][0], members[i][1]) #순서대로 나이와 이름 출력
# 백준 11399 ATM (신지원)

N = int(input()) #사람 수
time = list(map(int,input().split())) #각 사람이 걸리는 시간을 입력받아 리스트로 저장
time.sort() #오름차순으로 정렬
total = 0 #모두의 시간을 더해서 저장할 최종 시간 값
for i in range(len(time)): 
    total += sum(time[:i+1]) #앞의 사람들이 걸리는 시간 모두 더하여 최종 값에 더함
print(total) #최종 시간 출력
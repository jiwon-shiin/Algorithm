# 백준 2810 컵홀더 (신지원)

N = int(input()) #좌석의 수
seats = input() #좌석의 정보
if seats.count('LL') > 0: #커플석이 있다면
    seats = seats.replace('LL','S')
    print(len(seats)+1)
else: #없다면
    print(N)
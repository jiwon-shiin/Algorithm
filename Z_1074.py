# 백준 1074 Z (신지원)

def getZ(N,r,c): #r행 c열을 몇번째로 방문했는지 구하기 위한 함수
    if r==0 and c==0: #0,0은 0이므로 0을 반환
        return 0
    if r%2 == 0: #(짝,짝)->0, (짝,홀)->1이므로
        if c%2 == 0:
            answer = 0
        elif c%2 == 1:
            answer = 1
    elif r%2 == 1: #(홀,짝)->2, (홀,홀)->3이므로
        if c%2 == 0:
            answer = 2
        elif c%2 == 1:
            answer = 3
    return answer + (4*getZ(N-1,r//2,c//2)) #분할하여 N-1씩 앞을 먼저 계산한 후 4를 곱한 값을 더함

N,r,c = map(int,input().split()) #N,r,c를 입력받음
print(getZ(N,r,c))
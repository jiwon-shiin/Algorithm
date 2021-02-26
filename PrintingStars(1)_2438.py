# 백준 2438 별 찍기 - 1 (신지원)

N = int(input()) #N을 입력받아 정수형으로 변환

for i in range(N): #N번
    print("*"*(i+1)) #인덱스는 0부터 N-1이므로 i+1만큼 별 출력
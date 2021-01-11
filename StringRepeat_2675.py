# 백준 2675 문자열 반복 (신지원)

T = int(input())

for i in range(T):
    string = ""
    R, S = input().split()
    for i in range(len(S)):
        string += int(R)*S[i]
    print(string)

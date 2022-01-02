def findA(list,num):
    right = len(list)-1
    left = 0
    while left <= right:
        mid = (right + left) // 2
        if list[mid] > num:
            right = mid - 1
        elif list[mid] < num:
            left = mid + 1
        else:
            return True
    return False


N = int(input())
A = list(map(int,input().split()))
A.sort()

M = int(input())
B = list(map(int,input().split()))
for i in range(M):
    if findA(A,B[i]):
        print(1)
    else:
        print(0)

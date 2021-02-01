# 백준 10815 숫자 카드 (신지원)

N = int(input()) #가지고 있는 카드의 수
cards = list(map(int,input().split())) #가지고 있는 카드의 리스트
cards.sort() #오름차순으로 정렬
M = int(input()) #판별할 카드의 수
check_cards = list(map(int,input().split())) #판별할 카드의 리스트

def binary_search(n): #이진 탐색
    left, right = 0, N-1
    while left<=right:
        m = (left+right)//2
        if cards[m] == n: #일치하는 카드가 있다면
            return 1 #1 반환
        elif cards[m] > n: #찾는 카드보다 크다면 반으로 줄여 왼쪽을 탐색
            right = m - 1
        else: #찾는 카드보다 작다면 반으로 줄여 오른쪽을 탐색
            left = m + 1
    return 0 #일치하는 카드가 없다면 0 반환

for i in check_cards:
    print(binary_search(i), end = " ") #각각을 이진탐색으로 찾아 출력
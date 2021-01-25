# 백준 10809 알파벳 찾기 (신지원)

alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

text= input()
# find 함수를 쓸 경우
for i in alpha: #모든 알파벳에 대해
    print(text.find(i), end = ' ') #있으면 처음 등장하는 위치를, 없으면 -1을. find 함수는 없으면 알아서 -1을 반환함.

# index 함수를 쓸 경우
# for i in alpha:
#     try:
#         print(text.index(i),end = ' ') #index 함수는 없으면 ValueError을 일으킴
#     except ValueError: #ValueError일 경우
#         print(-1, end=' ') #-1을 출력
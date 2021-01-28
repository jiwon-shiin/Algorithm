# 백준 1427 소트인사이드 (신지원)

N = input() #정렬하고자 하는 수 N
nums = [] #수들을 저장할 리스트(문자열 형태로 저장될 것)
for i in N:
    nums.append(i) #리스트에 수들을 모두 넣고
nums.sort(reverse=True) #내림차순으로 정렬
print("".join(nums)) #합쳐서 출력
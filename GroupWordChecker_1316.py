N = int(input())
group = 0
for i in range(N):
    is_group = True
    text = input()
    if len(text) == 1:
        group += 1
        continue
    letters = [text[0]]
    for j in range(1,len(text)):
        if text[j] in letters:
            if text[j] == text[j-1]:
                continue
            else:
                is_group = False
                break
        if text[j] not in letters:
            letters.append(text[j])
    if is_group:
        group += 1
        
print(group)

# 백준 18238

text = input()

total = 0
p = ord("A")

for i in range(len(text)):
    n = ord(text[i])
    if abs(n - p) <= 13:
        total += abs(n-p)
    else:
        total += 26-abs(n-p)
    p = n

print(total)
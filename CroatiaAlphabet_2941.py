croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
croatia.sort(key = len, reverse = True)
text = input()
alph = 0
for i in croatia:
    while i in text:
        text = text.replace(i, " ", 1)
        alph += 1
text = text.replace(" ", "")
alph += len(text)
print(alph)

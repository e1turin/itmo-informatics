import re

text = []
temp = input("Write list of students: ")
while temp:
    text.append(tuple(temp.strip().split()))
    temp=input()

# print(text)

for i in range(len(text)):
    _, F, S, _ = re.split(r"(\w).(\w).", text[i][1])
    if F==S:
        continue
    print(" ".join(text[i]))


#EX6.1
s = input().split()
tem = " ".join(s)
print(tem.title())

#EX6.2
name = input().split(".")
ex = name[1]
if ex.lower() == "py":
    print("Python file")

#EX7.1
s = input()
s = s.strip()
s = s.lower()
if '@' in s:
    print(f"{s} - Valid")
else: 
    print("Invalid")

#EX7.2
s = input().split()
lenword = 0
word = ''
for i in s:
    if len(i) > lenword:
        word = i
        lenword = len(i)
print(word)
#RV5
'''
I enjoy studying. computer science because it challenges me to solve problems creatively and helps me understand how technology shapes our world.
'''
p = input()
s = p.split()
count = 0
sen = 0
char = 0
upper = 0
lower = 0
digit = 0
for i in p:
    if i.isalpha():
        char += 1
for i in p:
    if i == '.' or i == '!' or i == '?':
        sen += 1
    elif i.isupper():
        upper += 1
    elif i.islower():
        lower += 1
    elif i.isdigit():
        digit += 1
print(f"Char: {char:<7} | Words: {len(s):<7} | Sentences: {sen}")
print(f"Upper: {upper:<6} | Lower: {lower:<7} | Digits  : {digit}")
d = dict()
for i in s:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
topword = ""
topval = 0
for i in d:
    if d[i] > topval:
        topword = i
        topval = d[i]
print(f"Top word: \"{topword}\" ({topval} times)")
print(f"Avg word length: {float(char)/float(len(s)):.1f}")

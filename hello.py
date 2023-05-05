from random import randint
s =[randint(160, 196) for x in range(25)]
print (s)
max = max(s)
for i in range(len(s)):
    for g in range (0,len(s)-i-1);
    if s[i] < s[i+1]:
    s[i], s[i+1] = s[i+1], s[i]
    print (s)
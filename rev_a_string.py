word=input()
l=len(word)
str=""
revstr=""
for i in range(l-1,0,-1):
    if i==l-1:
        str=str+word[i]
    if i==l-2:
        str=str+word[i]
        break
for i in str:
    if i!=" ":
        revstr=revstr+i
    else:
        revstr=revstr+" "
print(revstr)
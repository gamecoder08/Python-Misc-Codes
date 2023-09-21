a=input("Enter your number: ")
l=list(a)
n=len(l)
rev_num=""
for i in range(n-1,0-1,-1):
    rev_num=rev_num+l[i]
print("Reversed number is: ",rev_num)
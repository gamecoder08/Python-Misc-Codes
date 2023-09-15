l=[]
n=int(input("Enter length of List: "))
print("Enter thr values: ")
for i in range(n):
    ai=int(input())
    l.append(ai)
high_num=0
for i in range(n):
    if high_num<l[i]:
        high_num=l[i]
print("The highest number is: ",high_num)
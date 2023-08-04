dim=int(input("How many numbers do you want to enter:"))
list=[]
for i in range(dim):
    a=float(input("Enter the number:"))
    list.append(a)
#Mean
mean=sum(list)/len(list)
print("Mean=",mean)  
#Median
if(dim%2==0):
    median=(list[(int)(dim/2-1)]+list[(int)(dim/2)])/2
else:
    median=list[(int)((dim+1)/2)]
print("Median=",median)
#Mode
frequency = {} #dict
for i in list:
    frequency.setdefault(i, 0)
    frequency[i]+=1

frequent = max(frequency.values())
for i, j in frequency.items():
    if j == frequent:
        mode = i
        print("Mode=",mode)


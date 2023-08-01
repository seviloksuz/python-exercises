dim=int(input("How many numbers do you want to enter:"))
list=[]
for i in range(dim):
    a=float(input("Enter the number:"))
    list.append(a)
#Mean
mean=sum(list)/len(list)  
#Median
if(dim%2==0):
    median=(list[dim/2]+list[dim/2+1])/2
else:
    mediam=list[(dim+1)/2]
#Mode


from array import *

arr=array('i',[])
n=int(input("Enter how many values in array:"))

for i in range(n):
    x=int(input("Enter values:"))
    arr.append(x)

print(arr)

val=int(input("Enter value to search:"))

k=0
for e in arr:
    if e==val:
        print(k)
        break
    k+=1


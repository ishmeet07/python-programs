# this program is made by ishmeet (binary search in python using array)
import array as arr
x=[]
y=int(input(("enter the no of elements")))
for i in range(0,y):
    a= int(input(f"enter the element {i+1}  "))
    x.append(a)
x.sort()   
a=arr.array('i',x)
for i in range(0,y):
    print(a[i],end=" ")
k=int(input("\nenter the element you want to search  "))
start=0
end=y-1
mid=(int((start+end)/2))
count=0
while(start<=end):
    mid=(int((start+end)/2))
    if(a[mid]<k):
        start=mid+1 

    elif(a[mid]>k):
        end=mid-1   
    elif(a[mid]==k):
        print(f"element found at location {mid+1}") 
        count+=1
        break

if(count ==0):
    print("no element found")    

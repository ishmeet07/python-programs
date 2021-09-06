#this is made by ishmeet singh(bubble sort)
import array as arr
x=[]

l=int(input("enter the no of elements"))
for i in range(0,l):
    k=int(input(f"enter the no of elements{i+1} "))
    x.append(k)
a=arr.array('i',x)

for i in range(0,l-1):
    print(f"\nPASS {i+1}")
    for d in range(0,l-i-1):
        if(a[d]>a[d+1]):
            temp=a[d+1]
            a[d+1]=a[d]
            a[d]=temp
    for k in range(0,l):        
        print(a[k],end=" ")  
print("\n")              
print("the resultant array is \n")
for k in range(0,l):        
        print(a[k],end=" ")       

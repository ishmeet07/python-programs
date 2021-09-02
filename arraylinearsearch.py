import array as arr
x=[]
y=int(input(("enter the no of elements")))
for i in range(0,y):
    a= int(input(f"enter the element {i}"))
    x.append(a)
a=arr.array('i',x)
for i in range(0,y):
    print(a[i],end=" ")
k=int(input("\nenter the element you want to search"))
for i in range(0,y):
    if(a[i]==k):
        print(f"element found at loc{i}")

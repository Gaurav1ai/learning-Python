a=[1,2,3,4,5,6,7,8,9,0]
target = int(input("Enter the number to find : "))
l = len(a)
isFound = False
j =0

for i in range(l):
    if (a[i]==target):
        print(i+1)
        # isFound = True
        # j=i
        break
    if(a[i]!=target):
        print(isFound)
        

    
       
        
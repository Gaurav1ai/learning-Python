i = int(input("Enter Your Cholice 1 or 0=  "))
if(i==1):
    x = 2
    def myfun():
        x= 100
        print(x)
    myfun()
    print(x)
else:
    #global veriables
    x = 4
    print(x)
    def myfun():
       global x
       x=10
       print(x)
    myfun()
    print(x)
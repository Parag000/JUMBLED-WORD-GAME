a=input('\n TYPE ADD \n TYPE SUB \n TYPE MUL \n TYPE DIV \n')

if a=='ADD' or a=='add':
    def add(x,y):
        return x+y
    res1=add(x=int(input("ENTER 1ST NO \t")),y=int(input("ENTER 2ND NO \t")))
    print(res1)

elif a=='SUB' or a=='sub':
    def sub(x,y):
        return x-y
    res2=sub(x=int(input("ENTER 1ST NO \t" )),y=int(input("ENTER 2ND NO \t")))
    print(res2)

elif a=='MUL' or a=='mul':
    def mul(x,y):
        return x*y
    res3=mul(x=int(input("ENTER 1ST NO \t")),y=int(input("ENTER 2ND NO \t")))
    print(res3)

else:
    def div(x,y):
        return x/y
    res4=div(x=int(input("ENTER 1ST NO \t")),y=int(input("ENTER 2ND NO \t")))
    print(res4)

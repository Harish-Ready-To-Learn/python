    --------------------
      PRIME NUMBERS 
    -------------------- 
n=int (input("enter num1 : "))
m=int (input("enter num2 : "))
for num in range(n,m+1):
    if num>1:
        for i in range(2,num):
            if(num%i==0):
                break
        else:
                print(num)
-----------------------------------------
OUTPUT:
enter num1 : 10
enter num2 : 20
11
13
17
19
23
29

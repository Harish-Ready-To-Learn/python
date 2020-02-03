name1=input("enter boy name : ")
name2=input("enter girl name : ")
name1=name1.replace(" ","")
name2=name2.replace(" ","")
print(name1)
print(name2)
for i in name1:
    for j in name2:
        if i==j:
            name1 = name1.replace(i,"",1)
            name2 = name2.replace(j,"",1)
            break

count=len(name1+name2)
print("flames number is : ",count)
if count>0:
    list=["friends","love","affectionate","marriage","enemy","siblings"]
    while len(list)>1:
        c=count%len(list)
        num=c-1
        if num>=0:
            left=list[:num]
            right=list[num+1:]
            list=left+right
        else:
            list=list[:len(list)-1]
    print("relation is : ",list[0])
else:
    print("enter another names....")

q1="""1.independence day?
        a.1948
        b.1950
        c.1947
        d.1946"""
q2="""2.valentines day?
        a.feb 14
        b.mar 3
        c.feb 13
        d.may 1"""
ques={q1:"c",q2:"a"}
score=0
for i in ques:
    print(i)
    ans=input("select the correct answer a/b/c/d: ")
    if ans==ques[i]:
        print("u r answer is correct...!")
        score=score+1
    else:
        print("wrong answer...!")
print("ur score is : ",score)
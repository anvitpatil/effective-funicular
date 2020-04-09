l=list(input("enter the string"))
cc=sc=dc=vc=0
vol=["a",'e','i','o','u',"A","E",'I','O','U']
d=[str(i) for i in range(0,10)]

for i in l:
    if(i in vol ):
        vc+=1
    elif(i in d):
        dc+=1
    elif(i == " "):
        sc+=1
    else:
        cc+=1
print("Vol count "+str(vc)+"    Cont count:"+str(cc)+"    Digits count:"+str(dc)+"      Space"+str(sc))
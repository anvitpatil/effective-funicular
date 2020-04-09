t=int(input(""))
for tt in range (1,t+1):
    n=int(input(""))
    l=[]
    rowc=0
    colc=0
    su=(n*(n+1))//2
    for i in range(n):
        c2=[int(x) for x in input("").split(" ")]
        l.append(c2)
        if(sum(c2)!=su):
            rowc+=1
    for i in range(n):
        lc=sum(l[:][i])
        if(sum(c2)!=su):
            colc+=1
    i=0
    lc=0
    for i in range(n):
        lc=l[i][i]+lc
    print("Case #"+str(tt)+": " +str(lc)+" "+str(rowc) +" "+str(colc))




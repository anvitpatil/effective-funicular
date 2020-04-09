
import numpy as np
t=int(input(""))
for yy in range(1,t+1):
    n,k=[int(x) for x in (input("").split(" "))]
    l=[[]]
    ss=0

    def printLatin(n):
        k = n + 1
        for i in range(1, n + 1, 1):
            temp = k 
            l1=[]
            while (temp <= n) :
                l1.append(temp)
                temp += 1
            l.extend(l1)
            l1=[]
            for j in range(1, k): 
                l1.append(j)
            l.extend(l1)
            k -= 1
        
    def finds():
        so=0
        for i in range(0,n):
            so+=l[i][i]
        
        
        if(so==k):
            print("Case "+str(yy)+": " +"POSSIBLE")
            
            for i in range(0,n):
                for j in range(0,n):
                    print(l[i][j],end=' ')
                print()
            return 1
        else:
            return 0
            

    def swp():
        for _ in range(10000):
            for i in range(0,n):
                for j in range(0,n):
                    l[[i,j]]=l[[j,i]]
                    
                    if(finds()==1):
                        return 0

        return 1
    
    printLatin(n) 
    del l[0]
    l=np.array(l)
    l=np.resize(l,(n,n))
    
    if(swp()==1):
        print("Case "+str(yy)+": " +"IMPOSSIBLE")

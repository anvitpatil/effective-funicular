l=list(input("").split(" "))
ma=0
for i in l:
    s=len(i)
    if(s>ma):
        ma=s
        wo=i
print("The Word "+wo+" has the max letters:"+str(ma))



s=input("Enter the string")
su=input("enter the subString")

for i in range(len(s)):
    j=0
    while(True):
        if(s[i]==su[j]):
            j+=1
            i+=1
        else:
            break
        if(j==len(su)):
            print("Word is found")
            exit()
print("Word Not Found")      
    
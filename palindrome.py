l=list(input(""))
n=len(l)
for i in range(n):
    j=n-i-1
    if(l[i]!=l[j]):
        print("Not a palindrome")
        break
    if(i>=j):
        print("Is a palindrome")
        break
  

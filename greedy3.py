n,k=map(int,input().split())

num=0
while n!=1:
    num+=1
    if n%k == 0 :
        n//=k
    else:
        n-=1

print(num)

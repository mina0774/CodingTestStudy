# 구현 - 백준 18406

n=int(input())
n_str=str(n)

cnt=0
a=0
b=0
for x in n_str:
    cnt+=1
    if cnt<=len(n_str)/2:
        a+=int(x)
    else:
        b+=int(x)

if a==b:
    print("LUCKY")
else:
    print("READY")

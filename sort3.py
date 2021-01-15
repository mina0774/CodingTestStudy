n,k=map(int,input().split())
# a는 오름차순 정렬
a=list(map(int,input().split()))
# b는 내림차순 정렬
b=list(map(int,input().split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i]<b[i]:
        a[i],b[i]=b[i],a[i]

print(sum(a))
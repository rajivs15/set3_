N=int(input())
s=list(map(int,input().split()))
if len(s)==N:
	a=sorted(s)

for i in range(0,len(a)):
	print (a[i],end=" ")

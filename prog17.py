n=int(input())
a=[]
s=0
for i in range(n):
  b=int(input())
  a.append(b)
print(a)
for i in range(n):
  s=s+a[i]
print(s)

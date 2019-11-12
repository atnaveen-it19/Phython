a=str(input())
b=len(a)
c=[]
d=[]
s=0
print(b)
for i in range(b):
  print(ord(a[i]))
  c.append(a[i])
  d.append(ord(a[i]))
  s=s+d[i]
print(c)
print(d)
print(s)


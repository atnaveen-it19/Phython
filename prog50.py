sum=0
for j in range(100,1000,1):
  i=j
  sum=0
  while(i>0):
    digit=i%10
    sum+=digit**3
    i//=10
  if j==sum:
    print(sum)


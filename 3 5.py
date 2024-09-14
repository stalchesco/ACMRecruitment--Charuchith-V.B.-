n=3
prime_num=[2]
while n<2000000:
    for i in range(2,n):
        if n%i==0:
            break
        elif i==n-1:
            prime_num.append(n)
    n+=1
s=0
for j in prime_num:
    s=s+j
print(s)
 
        
    

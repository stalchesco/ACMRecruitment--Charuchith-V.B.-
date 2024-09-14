a=0
b=1
g=0
for i in range(10000):
    s=a+b
    if s%2==0:
        if s<4000000:
            g=g+s
    a=b
    b=s
print('sum=',g)

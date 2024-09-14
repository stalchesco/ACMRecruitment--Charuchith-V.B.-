n=int(input('Enter an integer: '))
r=0
while n>0:
    r=(r*10)+(n%10)
    n=n//10
print(r)

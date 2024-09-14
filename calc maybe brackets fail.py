
def calculation(n):
    a=n.split()
    w=0
    k=len(a)-1
    for i in range(k,-1,-1):
        if a[i]=='^':
            p=1
            for j in range(int(a[i+1])):
                p=p*int(a[i-1])
            a[i-1]=p
            a[i]=' '
            a[i+1]=' '
    for m in range(len(a)-1):
        if (a[m]==' '):
            w+=1
    for e in range(w):
        a.remove(' ')
    print(a)
    w=0
    s=0
    d=1
    f=1
    c=1
    for l in range(len(a)-1):
        if(a[l]=="*"):
            d=(int(a[l-1]))*(int(a[l+1]))
            a[l-1]=' '
            a[l]=' '
            a[l+1]=d
        elif (a[l]=='/'):
            f=(int(a[l-1]))/(int(a[l+1]))
            a[l-1]=' '
            a[l]=' '
            a[l+1]=f
        elif (a[l]=='//'):
            c=(int(a[l-1]))//(int(a[l+1]))
            a[l-1]=' '
            a[l]=' '
            a[l+1]=c
    for m in range(len(a)-1):
        if (a[m]==' '):
            w+=1
    for e in range(w):
        a.remove(' ')
    print(a)
    w=0
    for y in range(len(a)-1):
        if a[y]=="+":
            z=(int(a[y-1]))+(int(a[y+1]))
            a[y-1]=" "
            a[y]=' '
            a[y+1]=z
        elif a[y]=='-':
            di=(int(a[y-1]))-(int(a[y+1]))
            a[y-1]=" "
            a[y]=' '
            a[y+1]=di
    for m in range(len(a)-1):
        if (a[m]==' '):
            w+=1
    for e in range(w):
        a.remove(' ')     
    print(a[0])

    
def brac(n):
    a=n.split()
    p=len(a)-1
    for i in range(p,-1,-1):
        if a[i]=='(':
            s=''
            a.remove(a[i])
            for j in range(i+1,len(a)-1):
                if a[j]==(')'):
                    a.remove(a[j])
                    break
                else:
                    s=s+a[j]
                    calculation(s)

                    
n=input('Enter each digit with space for every operation and digit: ')
brac(n)

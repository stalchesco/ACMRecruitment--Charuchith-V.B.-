import math 
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
    w=0
    for j in range(len(a)-1):
        if a[j]=='sqrt':
            h=math.sqrt(float(a[j+2]))
            a[j+1]=' '
            a[j+3]=' '
            a[j+2]=h
            a[j]=' '
    for m in range(len(a)-1):
        if (a[m]==' '):
            w+=1
    for e in range(w):
        a.remove(' ')
    w=0
    s=0
    d=1
    f=1
    c=1
    for l in range(len(a)-1):
        if(a[l]=="*"):
            d=(float(a[l-1]))*(float(a[l+1]))
            a[l-1]=' '
            a[l]=' '
            a[l+1]=d
        elif (a[l]=='/'):
             if (float(a[l+1]))==0:
                print('Zero Division is not permitted')
             f=(float(a[l-1]))/(float(a[l+1]))
             a[l-1]=' '
             a[l]=' '
             a[l+1]=f
        elif (a[l]=='//'):
            c=(float(a[l-1]))//(float(a[l+1]))
            a[l-1]=' '
            a[l]=' '
            a[l+1]=c
    for m in range(len(a)-1):
        if (a[m]==' '):
            w+=1
    for e in range(w):
        a.remove(' ')
    w=0
    for y in range(len(a)-1):
        if a[y]=="+":
            z=(float(a[y-1]))+(float(a[y+1]))
            a[y-1]=" "
            a[y]=' '
            a[y+1]=z
        elif a[y]=='-':
            di=(float(a[y-1]))-(float(a[y+1]))
            a[y-1]=" "
            a[y]=' '
            a[y+1]=di
    for m in range(len(a)-1):
        if (a[m]==' '):
            w+=1
    for e in range(w):
        a.remove(' ')     
    print(a[0])
                    
n=input('Enter each digit with space for every operation and digit: ')
calculation(n)


#I tried to do so many times without brackets seniors, but i wasnt able to, I gave my best but couldnt hence i am uploading both the without brackets file which works well with precedence without any brackets and the file which i tried to do with brackets but utterly failed in trying to do so.
# after every word or number must leave space in order for it to work

def password(pas):
    was=list(pas)
    ju=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    qu=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    oo=['!','"','#','$','@','%','^','&','*','/','.',':','=','+','_','-']
    pp=['A1b#cD3e','Xy4$Zz7!','P@ssw0rd','M!n3r4L^','T7r$eN8f']
    c=0
    l=0
    k=0
    i=0
    for wrd in was:
        c+=1
    if c==8:
        for jij in ju:
            for wrd in was:
                if wrd==jij:
                    l+=1
        for kik in qu:
            for qrd in was:
                if qrd==kik:
                    k+=1
        if k>0 and l>0:
            for lik in oo:
                for wrt in was:
                    if wrt==lik:
                        i+=1
            if i>0:
                for ull in pp:
                    if ull!=pas:
                        continue
                        
                    else:
                        print('out of all u chose this? tsk tsk tsk do Another one!')
                        break
            else:
                print('enter at least one special character')
        else:
            print('enter at least one small letter or a capital letter')
    else:
        print('Please enter 8 characters')

pas=input('enter a strong password: ')
password(pas)
   

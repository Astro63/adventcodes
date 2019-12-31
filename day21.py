if __name__=="__main__":
    b=list()
    a=input()
    a=a.split(",")
    n9=0
    i=0
    f=0
    s=0
    while n9 != 99:
        if i < len(a):
            if int(a[i])== 1:
                f=int(a[i+1])
                s=int(a[i+2])
                p=int(a[i+3])
                a[p]=int(a[f])+int(a[s])
                print("#1",f,s,p,a[f],a[s],a[p])
            if int(a[i]) == 2:
                f=int(a[i+1])
                s=int(a[i+2])
                p=int(a[i+3])
                a[p]=int(a[s])*int(a[f])
                print("#2",f,s,p,a[f],a[s],a[p])
        i=i+4

        n9=int(a[i])
    print(a[0])


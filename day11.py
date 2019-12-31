if __name__=="__main__":
    a=list()
    n=100
    for i in range(n):
        d=input()
        a.append(int(d))

    c=0

    for i in range(0,len(a)):
        b=0
        b=(a[i]//3)
        b-=2
        while b >=0:
            c=int(c+b)
            b=int(b//3)
            b-=2

        print(b)

    print("###")
    print(c)



"""punctula"""
def suma(a,b):
    s=a+b
    return print("Suma numerelor ",a," si ",b," = ",s)


"""punctulb"""
def produsul(a,b):
    p=a*b
    return print(" Produsul numerelor ",a," si ",b," = ",p)


"""punctulc"""
def media(a,b):
    m=(a+b)/2
    return print(" media aritmetica a numerelor ",a," si ",b," = ",m)


"""punctuld"""
def celmaimarediv(a,b):
    t=[]
    u=[]
    for i in range (1,a+1):
        if (a%i==0):
            t.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            u.append(j)
    c=set(t).intersection(u)
    h=max(c)
    return print(" Cel mai mare divizor comun al numerelor ",a," si ",b," = ",h)


"""punctule"""
def celmaimicmlt(a,b):
    if a>b:
        mlt=a
    elif b>a:
        mlt=b
    else:
        mlt=a
    while True:
        if ((mlt%a==0)and(mlt%b==0)):
            cm=mlt
            break
        mlt +=1
    return print("Cel mai mic multiplu comun al numerelor ",a," si ",b," = ",cm)


"""punctulf"""
def nmin(a,b):
    if a<b:
        return print(" Numarul minim =",a)
    else:
        return print(" Numarul minim =",b)


"""punctulg"""
def nmax(a,b):
    if a>b:
        return print("Numarul maxim = ",a)
    else:
        return print("Numarul maxim =",b)


"""punctulh"""
def suma2():
    a= int(input('Dati primul numar: '))
    b= int(input('Dati al doilea numar: '))
    c=a+b
    return print("suma= ",a," + ",b," = ",c)


"""punctuli"""
def produs2():
    a= int(input('Dati un nr='))
    b= int(input('Dati al doilea nr='))
    c=a*b
    return print(" produs= ",a," x ",b," = ",c)
    

"""punctulj"""
def div(a,b):
    k=[]
    l=[]
    for i in range (1,a+1):
        if (a%i==0):
            k.append(i)
    for j in range (1,b+1):
        if (b%j==0):
            l.append(j)
    c=set(k).intersection(l)
    br=list(c)
    return print("divizorii comuni ai numerelor ",a," si ",b," = ",br)

"""punctulk"""
def cincimlt(a,b):
    c=[]
    if a>b:
        mlt=a
    elif b>a:
        mlt=b
    else:
        multiplu=a
    while len(c)<5:
        if ((mlt%a==0)and(mlt%b==0)):
            c.append(mlt)
            mlt +=1
        else:
            mlt+=1
    return print("5 multipli comuni ale numerelor ",a," si ",b," sunt=",c)


"""punctull"""
def cifrecom(a,b):
    p=[]
    t=[]
    for i in str(a):
        p.append(int(i))
    for n in str(b):
        t.append(int(n))
    c=set(p).intersection(t)
    r=list(c)
    if len(r)!=0:
        return print("Cifrele comune  din numerele ",a," si ",b," sunt= ",r)
    else:
        return print(" nu au cifre comune")


"""punctulm"""
def cifrediferite(a,b):
    u=[]
    r=[]
    for i in str(a):
        u.append(int(i))
    for n in str(b):
        r.append(int(n))
    c=set(u).difference(r)
    y=list(c)
    return print("cifrele care se contin in numarul ",a," si nu se contin in numarul ",b," = ",y)

"""punctuln"""
def acelasinrdiv(a,b):
    l1=[]
    l2=[]
    for i in range (1,a+1):
        if (a%i==0):
            l1.append(i)
    for n in range (1,b+1):
        if (b%n==0):
            l2.append(n)
    if len(l1)==len(l2):
        return print("nr sunt PRIETENE")
    else:
        return print("nr nu sunt PRIETENE") 


nr1= int(input('dati nr1='))
nr2= int(input('dati nr2='))
#1)
suma(nr1,nr2)
#2)
produsul(nr1,nr2)
#3)
media(nr1,nr2)
#4)
celmaimarediv(nr1,nr2)
#5)
celmaimicmlt(nr1,nr2)
#6)
nmin(nr1,nr2)
#7)
nmax(nr1,nr2)
#10)
div(nr1,nr2)
#11)
cincimlt(nr1,nr2)
#12)
cifrecom(nr1,nr2)
#13)
cifrediferite(nr1,nr2)
#14)
acelasinrdiv(nr1,nr2)
#8)
suma2()
#9)
produs2()
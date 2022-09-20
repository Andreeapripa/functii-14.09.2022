n=int(input('n: '))
m=int(input('m: '))
def suma(x,y):
    a=x+y
    return a
def produs(x,y):
    a=x*y
    return a
def ma(x,y):
    a=(x+y)/2
    return a
def div(x,y):
    l_max=[]
    for i in range(1,x+1):
        if x%i==0 and y%i==0:
            l_max.append(i)
    a=max(l_max)
    return a
def mult(x,y):
    for i in range(1,x):
        for j in range(1,x):
            if x*i==y*j: 
                a=x*i
                return a
def minim(x,y):
    if x<y:
        return x
    else:
        return y
def maxim(x,y):
    if x>y:
        return x
    else:
        return y
def snc():
    a=int(input('a: '))
    b=int(input('b: '))
    c=a+b
    return c
def dc(x,y):
    l_max=[]
    for i in range(1,x+1):
        if x%i==0 and y%i==0:
            l_max.append(i)
    return l_max
def mc(x,y):
    multipli=[]
    for i in range(1,x):
        for j in range(1,y):
            if x*i==y*j:
                multipli.append(x*i)
            if len(multipli)==5:
                return multipli
def cc(x,y):
    a1=[]
    a2=[]
    a3=[]
    for j in str(x):
        a1.append(int(j))
    for j in str(y):
        a2.append(int(j))
    for i in a1:
        for k in a2:
            if i==k:
                a3.append(i)
    return a3
def cdp(x,y):
    a1=[]
    a2=[]
    a3=[]
    for i in str(x):
        a1.append(int(i))
    for i in str(y):
        a2.append(int(i))
    for i in a1:
        if i not in a2:
            a3.append(i)
    return a3
def prietenie(x,y):
    l1=[]
    l2=[]
    for i in range(1,x+1):
        if x%i==0:
            l1.append(i)
    for i in range(1,y+1):
        if y%i==0:
            l2.append(i)
            
    if len(l2)==(len(l1)):
        return 'Sunt prieteni'


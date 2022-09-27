import math 
n=int(input('n: '))
m=int(input('m: '))
f=int(input('f: '))
def div(x,y,z):
    l_max=[]
    for i in range(1,x):
        if x%i==0 and y%i==0 and z%i==0:
            l_max.append(i)
    a=max(l_max)
    return a
def mult(x,y,z):
    for i in range(1,x):
        for j in range(1,y):
            for k in range(1,z):
             if x*i==y*j and y*j==k*z: 
                a=x*i
                return a
def minim(x,y,z):
    if x<y:
        if x<z:
            return x
        else:
            return z
    else:
        if y<z: 
            return y
        else:
            return z
def maxim(x,y,z):
    if x>y:
        if x>z:
            return x
        else:
            return z
    else:
        if y>z: 
            return y
        else:
            return z
def dc(x,y,z):
    l_max=[]
    for i in range(1,x):
        if x%i==0 and y%i==0 and z%i==0:
            l_max.append(i)
    return l_max
def mc(x,y,z):
    multipli=[]
    for i in range(1,x):
        for j in range(1,y):
            for k in range(1,z):
                if x*i==y*j and y*j==z*k:
                    multipli.append(x*i)
            if len(multipli)==3:
                return multipli
def triunghi(x,y,z):
    if x+y>=z and x+z>=y and y+z>=x:
        sp=(x+y+z)/2
        aria=math.sqrt(sp*(sp-x)*(sp-y)*(sp-x))
        return 'perimetru= ', x+y+z,\
            'aria= ',aria  
def det(x,y,z):
    if y**2+4*x*z>=0:
        x1=(-y+math.sqrt(y**2+4*x*z))/(2*x)
        x2=(-y-math.sqrt(y**2+4*x*z))/(2*x)
        return'zerourile functiei sunt', x1,x2
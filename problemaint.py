


n=int(input("n="))
def subp(x):
    s=0
    for i in range(x):
        s+=1/(i+1)
    return s
print(subp(n))

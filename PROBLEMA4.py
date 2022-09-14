def factorial(x):
    s=1
    for i in range(1,x):
        s=s*i
def combinatii():
    n=int(input())
    m=int(input())
    if n>m:
        c=factorial(n)/factorial(m)*factorial(n-m)
        return c
print(combinatii())
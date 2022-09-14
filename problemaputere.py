def suma():
    s=1
    for i in range(2,9):
        if i%2==0:
            s+=0.5**i
    return s
print(suma())
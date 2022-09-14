def create_lista():
    n=int(input('Numarul de elemente=?'))
    lista_locala=[]
    for i in range(n):
        elem=input('Elementul '+str(i)+'este:')
        lista_locala.append(elem)
    return lista_locala
lista1=create_lista()
print(lista1)
import random

def busqueda_binaria(lista, comienzo, final, objetivo, iter_cuenta = 0):
    iter_cuenta += 1
    print(f'buscando {objetivo} entre {lista[comienzo]} y  {lista[final]}')

    if comienzo > final:
        return (False, iter_cuenta)
    
    medio = (comienzo + final) // 2

    if lista[medio] == objetivo:
        return (True, iter_cuenta)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, iter_cuenta=iter_cuenta)
    elif lista[medio] > objetivo:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, iter_cuenta=iter_cuenta)
    else:
        print('No deberia imprimirse')



if __name__ == '__main__':
    tamamo_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar '))

    lista = sorted([random.randint(0, 100) for i in range(tamamo_de_lista)])

    (encontrado, iter_cuenta) = busqueda_binaria(lista, 0, len(lista) - 1, objetivo)
    print(lista)
    print(
        f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'Número de iteraiones: {iter_cuenta}')

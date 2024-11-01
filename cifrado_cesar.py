import string

import GUI

def abecedario():
    abecedario_unido = string.ascii_lowercase
    abecedario_separado=[]
    for i in abecedario_unido:
        abecedario_separado.append(i)

    return abecedario_separado
def palabra_cifrar(palabra):
    # palabra_dividida=[]
    # for i in  palabra:
    #     palabra_dividida.append(i)
    # return palabra_dividida
    return list(palabra)



def cifrado_cesar(palabra):
        palabra_cifrada_lista=[]
        palabra_nueva=list(enumerate(palabra_cifrar(palabra)))
        abecedario_nuevo=abecedario()

        lista_a= list(enumerate(abecedario_nuevo))

        for i,letra_palabra in palabra_nueva:
                for j, letra_abecedario in lista_a:
                    if   letra_palabra ==letra_abecedario:

                        indice_nuevo_abecedario=lista_a[(j+3)%len(lista_a)]

                        palabra_cifrada_lista.append(indice_nuevo_abecedario)

        palabra_cifrada=''.join(str(sublista[1])for sublista in palabra_cifrada_lista)
        print(palabra_cifrada)


cifrado_cesar("holaz")
#abecedario()

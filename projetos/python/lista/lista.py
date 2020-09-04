#Listas são estruturas de dados capazes de armazenar múltiplos elementos
#Para a criação de uma lista, basta colocar os elementos separados por vírgulas dentro de colchetes []
#A lista pode conter elementos de tipos diferentes: string, float, boolean e inteiro

lista_frutas = ["uva", "abacaxi", "melancia", "manga"]
print(lista_frutas)


#INDICES
    #Assim como nas strings, é possível acessar separadamente cada item de uma lista a partir de seu índice

lista_numeros = [100, 200, 300, 400, 500]
print(lista_numeros[0]) #retorna o item na posição 0
print(lista_numeros[3]) #retona o item na posição 3

    #Pode-se acessar através de slices (fatias), como nas strings:

print(lista_numeros[2:4])  # da posição 2 até a 4 (não inclusa). Deverá retornar [300, 400]
print(lista_numeros[:3])   # até a posição 3 (não incluso). Deverá retornar [100, 200, 300]
print(lista_numeros[2:])   # da posição 2 até o final. Deverá retornar [300, 400, 500]
print(lista_numeros[:])    # do começo até o final. Deverá retornar [100, 200, 300, 400, 500]

    #Podemos avaliar se os elementos estão na lista com a palavra "in": O retorno sempre será em boolean
lista_estranha = ['duas palavras', 42, True, ['batman', 'robin'], -0.84, 'hipófise']
print(42 in lista_estranha) #deverá retornar True
print('hipófise' in lista_estranha) #deverá retornar True
print('abacate' in lista_estranha) #deverá retornar False

    #É possível obter o tamanho da lista (quantidade de itens) utilizando o método len()
print(len(lista_frutas))
print(len(lista_estranha))
print(len(lista_numeros))

    #Devido à lista ser uma estrutura mutável, é possível remover seus elementos utilizando o comando del:
lista_coisa = ['criança', 456, 'morcego', 56, False, 'bola']
del lista_coisa[2] #Aqui, ele vai deletar o item na posição 2
print(lista_coisa) #Deverá retornar ['criança', 456, 56, False, 'bola']

#O método append() adiciona um elemento ao final da lista
lista_animais = ['cachorro', 'gato', 'abelha', 'pato', 'rinoceronte']
lista_animais.append('coelho') #Deverá retornar ['cachorro', 'gato', 'abelha', 'pato', 'rinoceronte', 'coelho']
print(lista_animais)

#Temos também o insert(), que insere um elemento na posição especificada e move os demais elementos para direita
lista_funcionarios = ['Joana', 'Marcos', 'Silvana', 'Leila']
lista_funcionarios.insert(2, 'Jorge') #Na posição 2, será inserido o item Jorge
print(lista_funcionarios)
#Strings são tipos que armazenam uma sequência de caracteres
#Índices:
    #Como visto anteriormente, o método len() pode ser utilizado para obter o tamanho de estruturas, sejam elas strings, listas, etc. Esse tamanho representa a quantidade de elementos na estrutura.
    #Para obter somente um caractere de dentro dessas estruturas, deve-se utilizar o acesso por índices, no qual o índice entre colchetes [] representa a posição do elemento que se deseja acessar.

#Também é possível fazer algumas operações com strings
nome = "Carol é linda"
print(nome * 3)

nome1 = "Carol é maravilhosa,"
nome2 = "-lhosa, -lhosa"
print(nome1 + "  " + nome2)

#Contar quantos caracteres tem numa string

a = "Carol"
b = "Santos"
nome = a + b

#A função embutida len() nos permite, entre outras coisas, saber o tamanho de uma string:
tamanho = len(nome)
print(tamanho)

print(a[2])
print(a[0:3])

print(nome.lower()) #letras em minusculo
print(nome.upper()) #letras em maiusculo

#FATIAS
#Se, ao invés de obter apenas um elemento de uma estrutura (string, lista, …), deseja-se obter múltiplos elementos, deve-se utilizar slicing (fatiamento). No lugar de colocar o índice do elemento entre chaves, deve-se colocar o índice do primeiro elemento, dois pontos (:) e o próximo índice do último elemento desejado, tudo entre colchetes

frase = "Aprender Python é muito legal"
print(frase[:]) #retorna a frase completa
print(frase[0:6]) #retorna do item 0 ATÉ o item 6
print(frase[6:]) #retorna a partir do item 6 até o final
print(frase[6:10]) #retorna do item 6 até o item 10

#É possível controlar o passo que a fatia usa. Para isso, coloca-se mais um dois pontos (:) depois do segundo índice e o tamanho do passo
fatia = "Python é show de bola"
print(fatia[::2]) #Aqui ele retorna a quantidade de itens de 2 em 2

#SEPARAÇÃO DE STRINGS
#Podemos usar a função split()

frase = "Vamos separar a string"
print(frase.split())
type(frase) #busca qual é o tipo da variável
print(type(frase))

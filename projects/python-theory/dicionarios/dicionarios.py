#Dicionário é uma coleção de itens (chamados chaves) e seus respectivos significados (chamados de valores):
#{chave: valor}
#Cada chave do dicionário deve ser única! Ao contrário de listas, dicionários, não podem ter chaves repetidas.


#DECLARAÇÃO
# Declaramos um dicionário colocando entre chaves {} cada chave e o seu respectivo valor

musicas = {"Rihanna": "We Found Love", "The Weeknd": "The Hills", "Maroon 5": "Telephone"}
print(musicas)

#Diferente das listas, os dicionários não possuem índices 
#Para encontrar um valor dentro do dicionário, é preciso informar sua chave
print(musicas["Rihanna"]) #deve retornar o valor atribuído a chave "Rihanna". Neste caso, "We Founde Love"


#É possível navegar entre o dicionário usando a estrutura de controle "for"
#for chave in musicas:
    #print(chave) #aqui, ele retornará as chaves


#FUNÇÃO DICT
    #A função dict() constrói um dicionário. Existem algumas formas de usá-la
        #Com uma lista de listas:
lista1 = ["brigadeiro", "leite condesado, achocolatado"]
lista2 = ["omelete", "ovos, azeite, condimentos a gosto"]
lista3 = ["ovo frito", "ovo, óleo, condimentos a gosto"]
lista_receitas = [lista1, lista2, lista3]
print(lista_receitas)
#[['brigadeiro', 'leite condesado, achocolatado'], ['omelete', 'ovos, azeite, condimentos a gosto'], ['ovo frito', 'ovo, óleo, condimentos a gosto']]
receitas = dict(lista_receitas)
print(receitas)
#{'brigadeiro': 'leite condesado, achocolatado', 'omelete': 'ovos, azeite, condimentos a gosto', 'ovo frito': 'ovo, óleo, condimentos a gosto'}

    #Usando as chaves {}:

numeros = dict({"um": 1, "dois": 2, "três": 3})
print(numeros)
#{'um': 1, 'dois': 2, 'três': 3}

#Podemos colocar todo tipo de coisa dentro dos dicionários, incluindo listas e até mesmo outros dicionários
numeros5 = {"primos": [2, 3, 5], "pares": [0, 2, 4], "ímpares": [1, 3, 5]}
#print(numeros5["ímpares"]
    #[1, 3, 5]


#Adicionando e removendo elementos
    #Podemos alterar o valor relacionado a uma chave

dados_pessoa = {"nome": "Carlos Almeida", "idade": 25, "familiares": {"mãe", "pai", "irmão", "avó"}}
#print(dados_pessoa["idade"]) #deverá retornar 25
dados_pessoa["idade"] = 48 #agora o chave idade passa a ter o valor 48
print(dados_pessoa["idade"])
print(dados_pessoa)

#Para adicionar um elemento novo à um dicionário, podemos simplesmente fazer o seguinte
estacoes = {1 : "Azul", 2 : "Verde", 3: "Vermelha", 4 : "Amarela"}
estacoes[5] = "Lilás" #retorna o seguinte: {1: 'Azul', 2: 'Verde', 3: 'Vermelha', 4: 'Amarela', 5: 'Lilás'}
print(estacoes)

#Removemos um conjunto chave-elemento de um dicionário com o comando "del":
meses = {1 : "Janeiro", 2: "Fevereiro", 3 : "Março", 4 : "Abril"}
del(meses[4])
print(meses)

#Para apagar todos os elementos de um dicionário, usamos o método "clear":

dias_semana = {1: "Segunda", 2: "Terça", 3: "Quarta", 4: "Quinta", 5: "Sexta"}
dias_semana.clear()
print(dias_semana)





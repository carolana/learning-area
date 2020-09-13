#É possível ler do teclado as informações digitadas pelo usuário.
#A função input() «termina» de ser executada quando pressionamos enter.
# Tudo o que for digitado no teclado, até pressionar a tecla enter, será capturado pela função input(). Isso significa que podemos ler palavras separadas por um espaço, ou seja, uma frase inteira
#O retorno do comando input é sempre uma string
#Se quiser que seja inputado um número real, inteiro é preciso declarar antes do input. Ex: int(input("Coloque um número: "))


numero = input("Digite um numero: ")
print("Você digitou o numero " + str(numero))

print(
"""
+================================+
| Bem-vindo ao meu jogo, trouxa! |
| Coloque um número inteiro      |
| e adivinhe qual número         |
| eu escolhi para você.          |
| Então, qual o número secreto?  |
+================================+
""")

numero_digitado = int(input("Digite seu número: "))

while numero_digitado != 777:
    print("Ha ha! Você ainda preso no meu loop!")
    numero_digitado = int(input("Digite seu número: "))
        
if numero_digitado == 777 :
    print("Muito bem! Você está livre agora.")
        
        

    
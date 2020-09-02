secret_number = 777
print(
"""
+================================+
| Welcome to my game, muggle!    |
| Enter an integer number        |
| and guess what number I've     |
| picked for you.                |
| So, what is the secret number? |
+================================+
""")

numero_digitado = int(input("Digite seu número: "))

while numero_digitado != 777:
    print("Ha ha! You're stuck in my loop!")
    numero_digitado = int(input("Digite seu número: "))
        
if numero_digitado == 777 :
    print("Well done, muggle! You are free now.")
        
        

    
#Também é possível checar mais de uma condição com o elif. É a abreviatura para else if. Ou seja, se o if for falso, testa outra condição antes do else


x = 1
y = 2

#if x == y:
    #print("números iguais")
#elif y > x:
    #print("y é maior que x")
#else:
    #print("números diferentes")

if x == y:
    print("numeros iguais")
elif x < y:
    print("x é maior que y")
elif y > x:
    print("y é maior que x")
else:
    print("numeros diferentes")
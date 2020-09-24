#Para inserir cores no Python de uma forma simples, podemos usar o padrão ANSI, que é compatível com a linguagem
#Para colocar uma cor, vai precisar informar: style, text e back
#O formato para inserir é: \033[m
#Um exemplo utilizando estilo, texto e back: \033[0;33;44m - Aqui estou informando que quero a fonte no estilo none, texto com cor amarelo e background azul


#TIPOS DE ESTILOS
    #Os formatos são em números
    # 0 = none/ 1 = bold/ 4 = underline/ 7 = negative

#TIPOS DE TEXTO
    #Os formatos também são em números (vai do 30 ao 37)
        #30,31,32,33,34,35,36,37
        #branco, vermelho, verde, azul, magente, ciano e cinza

#TIPOS DE BACK
    #Segue o mesmo raciocinio para os tipos de texto, porém os números vão do 40 ao 47.

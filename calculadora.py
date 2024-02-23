import re

#Perguntar o nome do arquivo
arquivo = str (input("Digite o nome do arquivo: "))

def resultado(linha_comandoresultado,calculos):
                
    #Verificando digitos
    if linha_comandoresultado.isdigit():  # Check if the string is a digit

        #convertando a linha de str para int

        line = int(linha_comandoresultado)

        #pegar valores do expressao
        valores = re.findall(r'\d+',calculos[line-1])

        #convertando os valores de str para int 

        int_linha_comandoresultado = [int(num) for num in valores]

        operador_matematico = re.findall(r'[+\-*/|%^]', calculos[line-1])        
        
        #realizar a operação de soma  
        if (operador_matematico[0] == "+"):
 
            resultado = int_linha_comandoresultado[0] + int_linha_comandoresultado[1]
            
            print(resultado)


        #realiza a operação de subtração    
        elif (operador_matematico[0] == "-"):

            resultado = int_linha_comandoresultado[0] - int_linha_comandoresultado[1]

            print(resultado)    

       #realiza a operação de multiplicação
            
        elif (operador_matematico[0] == "*"):

            resultado = int_linha_comandoresultado[0] * int_linha_comandoresultado[1]
        
            print(resultado)        
        
        # realiza a operaçao de divisão real
        
        elif (operador_matematico[0] == "|"):

            resultado = int_linha_comandoresultado[0] / int_linha_comandoresultado[1]

            print(resultado)

       # realiza a operação de divisão inteira
            
        elif (operador_matematico[0] == "/"):
           
           resultado = int_linha_comandoresultado[0] // int_linha_comandoresultado[1]
           
           print(resultado)   

        
        elif (operador_matematico[0] == "%"):

            resultado = int_linha_comandoresultado[0] % int_linha_comandoresultado[1]

            print(resultado)

        elif (operador_matematico[0] == "^"):

            resultado = int_linha_comandoresultado[0] ** int_linha_comandoresultado[1]

            print(resultado)   



def memoria(linha_comando_de_memoria,calculos):
                
    #Verificando digitos
    if linha_comando_de_memoria.isdigit():  # Check if the string is a digit

        #convertando a linha de str para int

        line = int(linha_comando_de_memoria)

        #pegar valores do expressao
        valores = re.findall(r'\d+',calculos[line-1])

        #convertando os valores de str para int 

        int_linha_comando_memoria = [int(num) for num in valores]


def calculadora(arquivo):
    
    with open(arquivo+".txt", "r") as arquivo:

        #ler o arquivo
        calculos = arquivo.readlines()


        # separar os valores do parenteses
        for linha in calculos:

            #remover os parenteses

            linha.replace("(","").replace(")","")
                
            #pegar a lista do comando do resultado
            comandoresultado = re.findall(r'\d+ RES', linha)

            comandoresultado = ", ".join(comandoresultado)

            comandoresultado = comandoresultado.replace(" ", ",")

            #linha do comando do resultado
            linha_comandoresultado = comandoresultado[0:1].replace(" ","")
 
            #pegar o nome do comando do resultado
            nome_do_comando_de_resultado= comandoresultado[2:]

            #pegar comando da memoria

            comando_de_memoria = "MEM"

            comando_de_memoria = ", ".join(comando_de_memoria)
            
            comando_de_memoria = comando_de_memoria.replace(" ", ",")

            #linha do comando do resultado
            linha_comando_de_memoria = comando_de_memoria[0:1].replace(" ","")
 
            #pegar o nome do comando do resultado
            nome_do_comando_de_memoria= comando_de_memoria[2:]


            if(nome_do_comando_de_resultado):
                resultado(linha_comandoresultado,calculos)

            elif(nome_do_comando_de_memoria):
                memoria(linha_comando_de_memoria,calculos)


calculadora(arquivo)                               

        
       

    


     
    
        
      
        
        
            
            
            
                         
              

   
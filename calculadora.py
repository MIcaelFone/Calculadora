import re
arquivo = str (input("Digite o nome do arquivo: "))
with open(arquivo+".txt", "r") as arquivo:
    #ler o arquivo
    calculos = arquivo.readlines()

   # separar os valores do parenteses
    
    for linha in calculos:

        #remover os parenteses
        expressao_parenteses=linha.replace("(","").replace(")","")
           
         # pegar valores do expressao 
        valores = re.findall(r'\d+', linha)

        #convertando os valores
        int_list = [int(num) for num in valores]


        
        #pegar operador 

        operador_matematico = re.findall(r'[+\-*/|%^]', linha)
        
           
        #realizar a operação de soma  
        if (operador_matematico[0] == "+"):
            
            resultado = int_list[0] + int_list[1]
            
            print(resultado)

        #realiza a operação de subtração    

        elif (operador_matematico[0] == "-"):

            resultado = int_list[0] - int_list[1]

            print(resultado)    

       #realiza a operação de multiplicação
            
        elif (operador_matematico[0] == "*"):

            resultado = int_list[0] * int_list[1]
        
            print(resultado)        
        
        # realiza a operaçao de divisão real
        
        elif (operador_matematico[0] == "|"):

            resultado = int_list[0] / int_list[1]

            print(resultado)

       # realiza a operação de divisão inteira
            
        elif (operador_matematico[0] == "/"):
           
           resultado = int_list[0] // int_list[1]
           
           print(resultado)   

        
        elif (operador_matematico[0] == "%"):

            resultado = int_list[0] % int_list[1]

            print(resultado)

        elif (operador_matematico[0] == "^"):

            resultado = int_list[0] ** int_list[1]

            print(resultado)   

#Criar uma funçao para ler os três comandos especiais (N RES), (V MEM) e (MEM)
        #1.N res traz o valor do resultado da operação
            
            
           
       
        
        

            
        
             
            


        #separar os valores e operadores
        
        

        
       

    


     
    
        
      
        
        
            
            
            
                         
              

   
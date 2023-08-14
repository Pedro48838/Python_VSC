nome = str(input("Qual é o seu nome?: "))

if nome == 'Pedro':
    print("Que nome maravilhoso você tem!!")
else:
    print("Seu nome é bem normal") #Posso manter ou retirar o ELSE 
print(f"Tenha um bom dia {nome}!")

#####

nome= str(input("Qual é o seu nome?: "))

if nome == 'Pedro':
    print("Que nome maravilhoso!")
elif nome == 'Roberto' or nome == 'Claudia' or nome == 'Paulo':
    print("Seu nome é bem populare!!")
else:
    print("Não sabia mais oq escrever!")
print(f"Tenha um bom dia {nome}!")

###

nome = str(input("Qual é o seu nome?: "))

if nome == 'Pedro':
    print("Que nome maravilhoso!")
elif nome == 'Gustavo' or nome == 'Claudia' or nome == 'João':
    print("Seu nome é bem comum!!")
elif nome in 'Ana Creusa Jessica Juliana':
    print("Belo nome feminino!")
else:
    print("Seu nome é bem normal --__--") #O ELSE poderia ser retirado sem nenhum problema
print(f"Tenha um bom dia {nome}")





#Primeiros passos com Python

nome = input("Qual o seu nome:  ")
estuda = input("Qual sua formação:  ")
profissão = input("Qual a sua profissão:  ")
idade = input("Qual a sua idade:  ")
linguagem = input("Qual linguagem estuda:  ")

print(" Olá, meu nome é " + nome.upper() + ", sou estudante de " + estuda + " e trabalho na área " + profissão )
print(" Tenho " + str(idade)+ " anos.")

print(" Estou amando estudar " + linguagem)

Ano_de_formação = input(" Em que ano terminará seu curso: ")

formação = int(Ano_de_formação) - 2023
print( "Concluo o curso daqui " + str(formação) + " anos ")


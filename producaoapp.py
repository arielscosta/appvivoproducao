print ("Registro de produção")
print ("Preencha com seus dados")

while True:
    name = input ('Digite seu nome: ')
    if all(c.isalpha() or c.isspace() for c in name):
        break
    else:
        print('Por favor, digite um nome válido')
while True: #Enquanto verdadeiro
    id = input ('RE: ') #interação com usuário
    if all(num.isnumeric() for num in id): #Se resposta for numerica ok
        break #parar
    else: #se nao
        print('Por favor, digite apenas numeros') #informação ao usuário
while True:
    atv = input ("Quantidade de serviços: ")
    if all(qtd.isnumeric () for qtd in atv):
        break
    else:
       print('Por favor, digite apenas numeros') 
atv_num = int or float(atv)
resultado = 0
tabela = input ('Deseja ver tabela de serviços e seus respectivos valores? Responda S ou N ' )
print ("Serviços disponiveis")
print (" Banda Avulsa (1)")
print ("Banda mais linha (2)")
print ("Triploplay (3)")
print ("ME (4)")
for i in range(0,atv_num):
    valor = input("Serviço: ")
    if valor== '1':
        resultado = resultado +1
    elif valor =="2":
        resultado = resultado +2
    elif valor=="3":
        resultado = resultado +3
    elif valor =="4":
        resultado = resultado +4    
final = str (resultado)
print ("Total de pontos barenos: "+ final)

dia = resultado

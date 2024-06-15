print ("Registro de produção")
print ("Preencha com seus dados")



nome = input ("Nome: ")
id = input ("RE: ")
atv = input ("Quantidade de serviços: ")
atv_num = int(atv)
resultado = 0
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
lado = input("Digite o valor correspondente ao lado de um quadrado: ")
if(lado.isdigit()):
   ladoInt = int(lado)
   perimetro = ladoInt * 4
   area = ladoInt * ladoInt
   print("perímetro:", perimetro, "- área:", area)
else:
    print("nao e um digito")
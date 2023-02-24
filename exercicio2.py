primeiraNota = input("Digite a primeira nota: ")
segundaNota = input("Digite a segunda nota: ")
terceiraNota = input("Digite a terceira nota: ")
quartaNota = input("Digite a quarta nota: ")
if(primeiraNota.isdigit() and segundaNota.isdigit() and terceiraNota.isdigit() and quartaNota.isdigit()):
    primeiraNotaInt = int(primeiraNota)
    segundaNotaInt = int(segundaNota)
    terceiraNotaInt = int(terceiraNota)
    quartaNotaInt = int(quartaNota)
    mediaAritmetica = (primeiraNotaInt + segundaNotaInt + terceiraNotaInt + quartaNotaInt) / 4
    print("A média aritmética é", mediaAritmetica)
else:
    print("Alguns inputs nao sao digitos")
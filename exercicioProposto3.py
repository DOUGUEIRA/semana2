numeroUsuario = int(input("Digite um numero inteiro: "))

eliminaUnidade = numeroUsuario // 10
resultadoDezena = eliminaUnidade % 10

print("O digito das dezenas e", resultadoDezena)

# Variavel do tipo string (texto) e representado
# por meio de valor entra aspas (simples ou duplas)
meu_nome = input("Digite seu nome: ")
meu_sobrenome = input("Digite seu sobrenome: ")
nome_completo = f"{meu_nome} {meu_sobrenome}"

# Variavel numerica (inteiro)
minha_data_nasc = int(input("Digite sua data nasc.: "))
minha_idade = 2021 - minha_data_nasc

# como vem do input()
#minha_data_nasc = "1985"
# como fica depois do int()
#minha_data_nasc = 1985

# Variavel numerica (ponto flutuante)
meu_salario = float(input("Digite seu salario: "))

# Variavel booleana (True/False) 
sou_professor = True

mensagem = f"Ola {nome_completo}, voce tem {minha_idade} anos. Voce e professor? R: {sou_professor} e ganha R${meu_salario}."

print(mensagem)

import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    while True:
        nome_completo = input("Digite seu nome completo: ")
        
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (entre 1922 e 2021): "))
            if 1922 <= ano_nascimento <= 2021:
                break
            else:
                print("Erro: Ano de nascimento fora do intervalo permitido.")
        except ValueError:
            print("Erro: Insira um valor numérico para o ano de nascimento.")

    idade = calcular_idade(ano_nascimento)
    print(f"Nome: {nome_completo}")
    print(f"Idade em 2022: {idade} anos")

if __name__ == "__main__":
    main()
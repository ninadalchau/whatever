cpf = input("Digite o CPF:")
regiao = input("Digite sua região:")

cpf = cpf.replace('.', '')
cpf = cpf.replace('-', '')

regiao = cpf.replace("á", "a")
regiao = cpf.replace("ã", "a")
regiao = cpf.replace("í", "i")
regiao = cpf.replace("ô", "o")

def somador(cpf):
    soma = 0
    for num in cpf:
        soma += int(num)
    soma = str(soma)
    if soma[0] == soma[1]:
            print("CPF válido")

if cpf.isdigit():
    if len(cpf) == 11:
        if cpf[8] == 0 and regiao.lower() == "rio grande do sul" or "rs":
            somador(cpf)
        elif cpf[8] == 1 and regiao.lower() == "distrito federal" or "goias" or "mato grosso" or "mato grosso do sul" or "tocantins" or "df" or "go" or "mt" or "ms" or "to":
            somador(cpf)
        elif cpf[8] == 2 and regiao.lower() == "para" or "amazonas" or "acre" or "amapa" or "rondonia" or "roraima" or "am" or "ac" or "ap" or "ro" or "rr" or "pa":
            somador(cpf)
        elif cpf[8] == 3 and regiao.lower() == "ceara" or "maranhao" or "piaui" or "pi" or "ma" or "ce":
            somador(cpf)
        elif cpf[8] == 4 and regiao.lower() == "pernambuco" or "rio grande do norte" or "paraiba" or "alagoas" or "pe" or "rn" or "pb" or "al":
            somador(cpf)
        elif cpf[8] == 5 and regiao.lower() == "bahia" or "ba" or "sergipe" or "se":
            somador(cpf)
        elif cpf[8] == 6 and regiao.lower() == "minas gerais" or "mg":
            somador(cpf)
        elif cpf[8] == 7 and regiao.lower() == "rio de janeiro" or "rj" or "espirito santo" or "es":
            somador(cpf)
        elif cpf[8] == 8 and regiao.lower() == "sao paulo" or "sp":
            somador(cpf)
        elif cpf[8] == 9 and regiao.lower() == "parana" or "pr" or "santa catarina" or "sc":
            somador(cpf)
        else:
            print("CPF inválido")
    else:
        print("CPF inválido")
else:
    print("CPF inválido")
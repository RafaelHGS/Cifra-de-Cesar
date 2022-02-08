from random import randint as rd

discoExterno = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]

discoInterno = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
                "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", ]


def novoDiscoInterno(key):
    novoDisco = discoInterno[key:]
    novoDisco.extend(discoInterno[:key])
    return novoDisco


def criptografar_descriptografar(key=0, frase="", C_or_D=1):
    nKey = key.split(" ")
    nova_frase = ""
    do_nKey = 0

    for x in range(0, len(nKey)):
        try:
            nKey[x] = int(nKey[x]) * C_or_D
        except:
            return "Key inválida"
        if nKey[x] >= 26 or nKey[x] <= -26:
            return "Key inválida"

    for letra in frase:
        novo_disco = list(zip(discoExterno, novoDiscoInterno(nKey[do_nKey])))
        do_nKey += 1
        if do_nKey > len(nKey)-1:
            do_nKey = 0

        if letra not in discoExterno:
            nova_frase += letra
        else:
            for x, y in novo_disco:
                if letra == x:
                    nova_letra = letra.replace(x, y)
                    nova_frase += nova_letra
                    break

    print("\nNovo Texto Gerado:")
    return nova_frase.title()


def gera_key():
    try:
        opcao = int(input("\nDeseja gerar uma quantidade de keys definida, ou uma key por caractere ?\n[1]Quantidade de keys\n[2]Por caractere no texto\n"))
        if opcao <=0 or opcao >=3:
            print("Erro ao Gerar Key, tente Novamente")
            return
    except:
        print("Erro ao Gerar Key, tente Novamente")
        return

    if opcao == 1:
        try:
            nKeys = int(input("\nDigite a quantidade de keys para serem geradas (OBS: em um numero inteiro positivo): "))
            if nKeys <0:
                print("Erro ao Gerar Key, tente Novamente")
                return
        except:
            print("Erro ao Gerar Key, tente Novamente")
            return
            
        keys_em_frase = ""
        for x in range(0, nKeys):
            numero_randomico = str(rd(-25, 25))
            if x == nKeys-1:
                keys_em_frase += numero_randomico
            else:
                keys_em_frase += numero_randomico + ","

        keys_em_frase = " ".join(keys_em_frase.split(","))

        with open('key.txt', 'w') as key:
            key.write("{a}".format(a= keys_em_frase))
            key.close
        print("\nO arquivo .txt com a sua key de caracteres foi gerado com sucesso!\n")

    elif opcao == 2:
        frase = input("\nDigite uma frase: ")
        keys_em_frase = ""

        for x in range(len(frase)):
            numero_randomico = str(rd(-25, 25))
            if x == len(frase)-1:
                keys_em_frase += numero_randomico
            else:
                keys_em_frase += numero_randomico + ","

        keys_em_frase = " ".join(keys_em_frase.split(","))

        with open('key.txt', 'w') as key:
            key.write("{a}".format(a= keys_em_frase))
            key.close
        print("\nO arquivo .txt com a sua key de caracteres foi gerado com sucesso!\n")
    else:
        print("Erro de Gera Key")

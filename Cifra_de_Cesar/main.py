from Módulos import funcoes

def main():
    while True:
        try:
            toDo = int(
                input("\nO que deseja Fazer ?: \n[1]Criptografar\n[2]Descriptografar\n[3]Gerar Key\n"))
            if toDo <= 0 or toDo >= 4:
                print("Erro de opção")
                break

            if toDo == 1:
                key = input(
                    "\nInforme a Key (>= -25 E <= 25) no formato 'x y z...' (ex: 2 25 -7 ...): ")
                frase = input("Insira a frase: ").lower()
                print(funcoes.criptografar_descriptografar(key, frase,))
            elif toDo == 2:
                frase = input("\nInsira a frase: ").lower()
                key = input(
                    "\nInforme a Key (>= -25 E <= 25) no formato 'x y z...' (ex: 2 25 -7 ...): ")
                print(funcoes.criptografar_descriptografar(key, frase, -1))
            elif toDo == 3:
                funcoes.gera_key()
            print()
            break
        except:
            print("Erro")
            break


if __name__ == "__main__":
    main()

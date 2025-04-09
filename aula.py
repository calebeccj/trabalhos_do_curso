def main():
    Nome = ""
    Idade = 0
    Email = ""
    Cidade = ""
    Profissao = ""
    Opcao = 0
    while True:
        print("\nMenu\n")
        print("[1].Cadastrar Usuário")
        print("[2].Ver cadastro")
        print("[3].Sair do sistema")
        Opcao = int(input("\nDigite uma opção: "))
        if Opcao == 1:
            Nome = input("\nDigite seu nome: ")
            Idade = int(input("\nDigite a sua idade: "))
            while True:
                Email = input("\nDigite seu e-mail: ")
                if "@gmail.com" in Email:
                    break
                else:
                    print("\nAdicione o '@gmail.com' em seu e-mail.")
            Cidade = input("\nDigite a sua cidade: ")
            Profissao = input("\nDigite a sua profissão: ")
        elif Opcao == 2:
            if Nome == "" and Idade == 0 and Email == "" and Cidade == "" and Profissao == "":
                print("\nVocê preencheu algum dado incorretamente.")
            else:
                print(f"Nome: {Nome} \nIdade: {Idade} \nE-mail: {Email} \nCidade: {Cidade} \nProfissão: {Profissao}")
        if Opcao == 3:
            print("\nEncerrando o sistema...")
            break
        elif Opcao > 3:
            print("Opção inválida, tente novamente.")
if __name__ == "__main__":
    main()            

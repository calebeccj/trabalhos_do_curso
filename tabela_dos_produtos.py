def main():
    opcao = 0
    produto = " "

    while True:
        print("\n=======MENU=======\n")
        print("1.Cadastrar produto")
        print("2.Ver produto cadastrado")
        print("3.Sair do sistema\n")
        print("=====================")
        opcao = int(input("Digite uma opção: "))
        
        if opcao == 1:
            produto = input("\nDigite o nome do produto: ")
            quantidade = int(input("DIgite a quantidade do produto: "))
            print("\n=====Produto cadastrado com sucesso!=====\n")
        
        elif opcao == 2:
             if produto == " " or quantidade == 0:
              print("\n=====Nenhum produto cadastrado.=====\n")
             else:
              print("\nPreoduto cadastrado: ", produto)
              print("Unidade(s): ", quantidade)
        

        
        if opcao == 3:
            print("\n=====Encerrando o sistema...=====")
            break

        elif opcao > 3:
            print("\n=====Opção inexistente!=====\n")
            
if __name__ == "__main__":
    main()

            
        
            
            

            
        



 
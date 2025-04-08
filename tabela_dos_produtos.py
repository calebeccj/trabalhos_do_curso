def main():
    opcao = 0
    produto = []

    while True:
        print("\n=======MENU=======\n")
        print("1.Cadastrar produto")
        print("2.Ver produto cadastrado")
        print("3.Sair do sistema\n")
        print("=====================")
        opcao = int(input("Digite uma opção: "))
        
        if opcao == 1:
            nome = input("\nDigite o nome do produto: ")
            try:
               quantidade = int(input("DIgite a quantidade do produto: "))
               produto.append({"Produto": nome, "Unidade(s)": quantidade})
               print(f"\n=====Produto '{nome}' cadastrado com sucesso!=====\n")
            except ValueError:
               print("\nNenhum produto foi cadastrado.")   
        
        elif opcao == 2:
             print("\nLista de Produtos:")
             for i, produto in enumerate(produto):
                print(f"{i + 1}. Nome: {produto['Produto']}, Unidade(s): {produto['Unidade(s)']}")
    
        if opcao == 3:
            print("\n=====Encerrando o sistema...=====")
            break

        elif opcao > 3:
            print("\n=====Opção inexistente!=====\n")
            
if __name__ == "__main__":
    main()

            
        
            
            

            
        



 

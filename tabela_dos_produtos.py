def main():
    opcao = 0
    produto = [] #Os colchetes fazem dicionarios

    while True:
        print("\n=======MENU=======\n")
        print("1.Cadastrar produto")
        print("2.Ver produto cadastrado")
        print("3.Sair do sistema\n")
        print("=====================")
        opcao = int(input("Digite uma opção: "))
        
        if opcao == 1:
            nome = input("\nDigite o nome do produto: ")
            try: #O try vai tentar exceutar o meu código e caso der erro o programa não vai fechar, pois except está programado à exibir uma mensagem de erro caso ocorra um erro especifico 
               quantidade = int(input("DIgite a quantidade do produto: "))
               produto.append({"Produto": nome, "Unidade(s)": quantidade}) #Append adiciona um item no dicionario/lista
               print(f"\n=====Produto '{nome}' cadastrado com sucesso!=====\n") #Me deixa colocar variaveis no meio da string de forma mais clean
            except ValueError:
               print("\nNenhum produto foi cadastrado.")   
        
        elif opcao == 2:
             print("\nLista de Produtos:")
             for i, produto in enumerate(produto): #O for vai ficar passando por cada item da lista e o enumerate vai dar um indice para eles
                print(f"{i + 1}. Nome: {produto['Produto']}, Unidade(s): {produto['Unidade(s)']}")#O i indica o indice da lista (ou numero do item) e sempre vai começar no 0
    
        if opcao == 3:
            print("\n=====Encerrando o sistema...=====")
            break

        elif opcao > 3:
            print("\n=====Opção inexistente!=====\n")
            
if __name__ == "__main__":
    main()

            
        
            
            

            
        



 

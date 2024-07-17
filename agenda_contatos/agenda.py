
### Agenda de contatos ###

def adicionar_contato(agenda, nome_contato, numero_contato, email_contato):
    Nao = False 
    contato = {"nome": nome_contato, "numero": numero_contato, "email": email_contato, "favorito": Nao} 
    agenda.append(contato)
    print(f"\nContato {nome_contato} foi adicionada com sucesso!")
    return

def remover_contato(agenda):
    nome_contato = input("\nDigite o nome do contato que deseja remover: ")
    for contato in agenda:
        if contato["nome"] == nome_contato:
            agenda.remove(contato)
            print(f"\nContato {nome_contato} foi removido com sucesso!")
        if not contato["nome"] == nome_contato:
            print(f"\nContato não encontrado.")
        else:
            print("Erro desconhecido...")
        return

def listar_contatos(agenda):
    print("\nLista de Contatos: ")
    for indice, contato in enumerate(agenda, start=1):
        status = "♥" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        numero_contato = contato["numero"]
        email_contato = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} / {numero_contato} / {email_contato}")
    return

def editar_contato(agenda):
    listar_contatos(agenda)
    for contato in agenda:
        nome_contato = input("\nDigite o nome do contato que deseja editar: ")
        if contato["nome"] == nome_contato:
            print(f"\nEditar contato {nome_contato}: ")
            contato["nome"] = input("Novo nome: ")
            contato["numero"] = input("Novo número: ")
            contato["email"] = input("Novo e-mail: ")
            print(f"\nContato {nome_contato} editado com sucesso!")
            print(f"\nContato Atualizado: {", ".join(str(valor) for valor in contato.values())}")
        else:
            print("Contato não encontrado...")
        return     

def marcar_favorito(agenda, nome_contato):
    for contato in agenda:
            Sim = True
            if contato["nome"] == nome_contato:
                contato["favorito"] = Sim
                print(f"\nContato {nome_contato} marcado como favorito!")
            else:
                print("Contato não encontrado...")
            return

def listar_favoritos(agenda):
    print("\nLista de Contatos Favoritos: ")
    for indice, contato in enumerate([contato for contato in agenda if contato["favorito"]], start=1):
        status = "♥" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        numero_contato = contato["numero"]
        email_contato = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} / {numero_contato} / {email_contato}")
    return

agenda = []
while True:
    print("\nMenu da Agenda de contatos:")
    print("1 - Adicionar Contato")
    print("2 - Remover Contato")
    print("3 - Listar Contatos")
    print("4 - Editar um Contato")
    print("5 - Marcar Contato como Favorito")
    print("6 - Ver Lista de Contatos Favoritos")
    print("7 - Sair")

    option = input("\nDigite a sua escolha: ")
     
    if option == "1":
        nome_contato = input("\nDigite o nome do contato que deseja adicionar: ")
        numero_contato = input("\nDigite o número do contato: ")
        email_contato = input("\nDigite o e-mail do contato: ")
        adicionar_contato(agenda, nome_contato, numero_contato, email_contato)
        
    elif option == "2":
        remover_contato(agenda)
        listar_contatos(agenda)
        
    elif option == "3":
        listar_contatos(agenda)
        
    elif option == "4":
        editar_contato(agenda)
        
    elif option == "5":
        listar_contatos(agenda)
        nome_contato = input("\nDigite o nome do contato que deseja marcar como favorito: ")
        marcar_favorito(agenda, nome_contato)
        listar_favoritos(agenda)
        
    elif option == "6": 
        listar_favoritos(agenda)       
        
    elif option == "7":
        break
    
print("Fechando Agenda de Contatos...")   



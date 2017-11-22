import sqlite3
conn = sqlite3.connect('bancodedados.db')
cursor = conn.cursor()

#variaveis gerais
usuario_logado = ""

#cria tabelas
def modularTable():#Victor
    clear()
    tabela = int(input('\nBem vindo ao sistema Meditech\nPrimeiramente adicione os modulos com que deseja trabalhar\n\n1 - funcionarios\n2 - Veiculos\n3 - Agendamentos\n4 - Equipamentos\n5 - Paciente\n6 - login\n7 - anamnese\n8 - leito\n9 - finalizar.\n\nQuais sao as tabelas de dados que deseja utilizar?'))
    if tabela == 1:
        tabela_funcionarios()
        modularTable()
    elif tabela == 2:
        tabela_veiculos()
        modularTable()
    elif tabela == 3:
        tabela_agendamentos()
        modularTable()
    elif tabela == 4:
        tabela_equipamento()
        modularTable()
    elif tabela == 5:
        tabela_paciente()
        modularTable()
    elif tabela == 6:
        tabela_login()
        cadastro_login('admin', '123', 'gerente')
        modularTable()
    elif tabela == 7:
        tabela_anamnese()
        modularTable()
    elif tabela == 8:
        tabela_leito()
        modularTable()
    elif tabela == 9:
        firstAccess()
    else:
        print('Opcao invalida')
        modularTable()

def firstAccess():
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")

    if len(cursor.fetchall()):
        fazerlogin()
    else:
        modularTable()

def fazerlogin():
    clear()
    print('\nBem vindo ao sistema de gerencimento Meditech:\n')
    login = input('Digite o seu login:\n')
    senha = input('Digite sua senha:\n')
    cursor.execute('SELECT * FROM login WHERE nome_usuario = ? and senha = ?', (login, senha))
    if len(cursor.fetchall()) >= 1:
        cursor.execute('SELECT * FROM login WHERE nome_usuario = ? and senha = ?', (login, senha))
        for linha in cursor.fetchall():
            global usuario_logado
            usuario_logado = linha[1]
            area = linha[3]
            if area == 'medico':
                menu_medico()
            if area == 'engenheiro biomedico':
                menu_engbio()
            if area == 'atendente':
                menu_atendente()
            if area == 'gerente':
                menu_manager()
    else:
        input('\nLogin ou senha incorretos, pressione qualquer tecla')
        fazerlogin()

def tabela_funcionarios():#marianne
    cursor.execute('CREATE TABLE funcionarios(nome TEXT NOT NULL, profissao TEXT NOT NULL, matricula VARCHAR(25) NOT NULL, id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT);')

def tabela_veiculos():#marianne
    cursor.execute('CREATE TABLE veiculos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, placa VARCHAR(8) NOT NULL, status TEXT NOT NULL, motorista TEXT NOT NULL, paramedico TEXT NOT NULL, paciente TEXT NOT NULL);')

def tabela_agendamentos():#marianne
    cursor.execute('CREATE TABLE agendamentos(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, id_paciente INTEGER NOT NULL, id_medico INTEGER NOT NULL, data VARCHAR(10) NOT NULL, horario VARCHAR(5));')

def tabela_equipamento():# Luiz Eduardo
    cursor.execute('CREATE TABLE equipamento(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, funcao TEXT NOT NULL, preco INTEGER, status TEXT NOT NULL, data DATE NOT NULL);')

def tabela_paciente():# Luiz Eduardo
    cursor.execute('CREATE TABLE paciente(id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, idade INTEGER, sexo TEXT NOT NULL, peso INTEGER);')

def tabela_leito(): #luiz henrique
    cursor.execute('CREATE TABLE dadosleito( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome TEXT NOT NULL, num_leito INTEGER NOT NULL)')

def tabela_login(): #luiz henrique
    cursor.execute('CREATE TABLE login( id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, nome_usuario TEXT NOT NULL, senha VARCHAR(10) NOT NULL, area TEXT NOT NULL)')

def tabela_anamnese(): #luiz henrique
    cursor.execute('CREATE TABLE anamnese (id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, id_paciente INTEGER NOT NULL, o_que_sente TEXT NOT NULL, onde_doi TEXT NOT NULL, quando_comecou INTEGER NOT NULL)')
def clear():#marianne
    print("\n" * 100)

# funçoes

def lista_equipamento():
    verifica = cursor.execute('SELECT * FROM equipamento')
    for linha in verifica.fetchall():
        print(linha)
def insere_equipamento(nome, funcao, preco, status, data):  # Luiz Eduardo
    cursor.execute('INSERT INTO equipamento(nome,funcao,preco,status,data)VALUES(?,?,?,?,?)',
                   (nome, funcao, preco, status, data))
    conn.commit()

def remove_equipamento(id_equipamento):  # Luiz Eduardo
    cursor.execute('DELETE FROM equipamento WHERE id =?', id_equipamento)
    conn.commit()

def alterar_equipamento(novo_nome, nova_funcao, novo_preco, novo_status, nova_data, id_equipamento):  # Luiz Eduardo
    cursor.execute('UPDATE equipamento SET nome = ?, funcao= ?, preco = ?,status = ?, data = ? WHERE id = ?',
                   (novo_nome, nova_funcao, novo_preco, novo_status, nova_data, id_equipamento))
    conn.commit()

def insere_funcionarios (nome, profissao, matricula):#marianne
    cursor.execute('INSERT INTO funcionarios(nome, profissao, matricula) VALUES (?,?,?)', (nome, profissao, matricula))
    conn.commit()

def remove_funcionarios (id_funcionario):#marianne
    cursor.execute("DELETE FROM funcionarios WHERE id = ?", (id_funcionario))
    conn.commit()

def altera_funcionarios(alteracao_campo, alteracao, id_funcionario):#marianne
    if alteracao_campo == 'nome':
        cursor.execute("UPDATE funcionarios SET nome = ? WHERE id = ?", (alteracao, id_funcionario))
    if alteracao_campo == 'profissao':
        cursor.execute("UPDATE funcionarios SET profissao = ? WHERE id = ?", (alteracao, id_funcionario))
    if alteracao_campo == 'matricula':
        cursor.execute("UPDATE funcionarios SET matricula = ? WHERE id = ?", (alteracao, id_funcionario))
    conn.commit()

def insere_veiculos(placa, status, motorista, paramedico, paciente):#marianne
    cursor.execute("INSERT INTO veiculos(placa, status, motorista, paramedico, paciente) VALUES (?,?,?,?,?)", (placa, status, motorista, paramedico, paciente))
    conn.commit()

def remove_veiculos(id_veiculo):#marianne
    cursor.execute("DELETE FROM veiculos WHERE id = ?", (id_veiculo))
    conn.commit()

def altera_veiculos(alteracao_campo, alteracao, id_veiculo):#marianne
    if alteracao_campo == 'placa':
        cursor.execute("UPDATE veiculos SET placa = ? WHERE id = ?", (alteracao, id_veiculo))
    if alteracao_campo == 'status':
        cursor.execute("UPDATE veiculos SET status = ? WHERE id = ?", (alteracao, id_veiculo))
    if alteracao_campo == 'motorista':
        cursor.execute("UPDATE veiculos SET motorista = ? WHERE id = ?", (alteracao, id_veiculo))
    if alteracao_campo == 'paramedico':
        cursor.execute("UPDATE veiculos SET paramedico = ? WHERE id = ?", (alteracao, id_veiculo))
    if alteracao_campo == 'paciente':
        cursor.execute("UPDATE veiculos SET paciente = ? WHERE id = ?", (alteracao, id_veiculo))
    conn.commit()

def insere_agendamentos(id_paciente, id_medico, data, horario):#marianne
    cursor.execute("INSERT INTO agendamentos(id_paciente, id_medico, data, horario) VALUES (?,?,?,?)", (id_paciente, id_medico, data, horario))
    conn.commit()

def remove_agendamentos(id_paciente):#marianne
    cursor.execute("DELETE FROM agendamentos WHERE id = ?", (id_paciente))
    conn.commit()

def altera_agendamentos(alteracao_campo, alteracao, id_agendamentos):#marianne
    if alteracao_campo == 'id_paciente':
        cursor.execute("UPDATE agendamentos SET id_paciente = ? WHERE id = ?", (alteracao, id_agendamentos))
    if alteracao_campo == 'id_medico':
        cursor.execute("UPDATE agendamentos SET id_medico = ? WHERE id = ?", (alteracao, id_agendamentos))
    if alteracao_campo == 'data':
        cursor.execute("UPDATE agendamentos SET data = ? WHERE id = ?", (alteracao, id_agendamentos))
    if alteracao_campo == 'horario':
        cursor.execute("UPDATE agendamentos SET horario = ? WHERE id = ?", (alteracao, id_agendamentos))
    conn.commit()

def cadastro_login(nome_usuario, senha, area):
    cursor.execute('INSERT INTO login(nome_usuario, senha, area) VALUES (?, ?, ?)', (nome_usuario, senha, area))
    conn.commit()

def remove_login(id_usuario):
    mostrar = cursor.execute('SELECT * FROM login')
    for linha in mostrar.fetchall():
        print(linha)
    cursor.execute('DELETE FROM login WHERE id = ?', (id_usuario))
    conn.commit()

def altera_login():
    login = input('Digite seu login:\n')
    novo_login = input('Digite o novo login:\n')
    cursor.execute('UPDATE login SET nome_usuario = ? WHERE nome_usuario = ?', (novo_login, login))
    senha = input('Digite a senha:')
    nova_senha = input('Digite a nova senha:\n')
    cursor.execute('UPDATE login SET senha = ? WHERE senha = ?', (nova_senha, senha))
    conn.commit()

def insere_paciente(nome, idade, sexo, peso):# Luiz Eduardo
    cursor.execute('INSERT INTO paciente(nome,idade,sexo,peso)VALUES(?,?,?,?)',(nome,idade,sexo,peso))
    conn.commit()

def remove_paciente(id_paciente):# Luiz Eduardo
    cursor.execute('DELETE FROM paciente WHERE id=?', id_paciente)
    conn.commit()

def cadastra_leito(nome, numero): #luiz h
    cursor.execute('INSERT INTO dadosleito(nome, num_leito) VALUES (?, ?)', (nome, numero))
    conn.commit()

def remove_leito(id_paciente): #luiz h
    cursor.execute("DELETE FROM dadosleito WHERE id = ?", (id_paciente))
    conn.commit()

def insere_anamnese(id_paciente, onde_doi, o_que_sente, quando_comecou): #luiz h
    cursor.execute('INSERT INTO anamnese(id_paciente, onde_doi, o_que_sente, quando_comecou) VALUES (?,?,?,?)',
                       (id_paciente, onde_doi, o_que_sente, quando_comecou))
    conn.commit()

#menus
def menu_atendente():#marianne
    clear()
    print('\nBem vindo '+usuario_logado+'!\n1- Agendar consulta.\n2- Cancelar agendamento.\n3- Alterar agendamento.\n4- Ver agendamentos.\n5- Cadastrar paciente. \n6-Sair.')
    opcao = int(input('Digite a opcao desejada: '))
    if opcao == 1:
        clear()
        id_paciente = input("Digite o ID do paciente: ")
        id_medico = input("Digite o ID do medico: ")
        data = input("Digite a data da consulta: ")
        horario = input("Digite o horario da consulta: ")
        insere_agendamentos(id_paciente, id_medico, data, horario)
        menu_atendente()
    if opcao == 2:
        clear()
        print('Consultas cadastradas (ID, ID paciente, ID medico, data, horario): ')
        mostrar = cursor.execute('SELECT * FROM agendamentos')
        for linha in mostrar.fetchall():
            print(linha)
        id_paciente_r = input("Digite o ID do paciente que deseja remover: ")
        remove_agendamentos(id_paciente_r)
        menu_atendente()
    if opcao == 3:
        clear()
        print('Consultas cadastradas (ID, ID paciente, ID medico, data, horario): ')
        mostrar = cursor.execute('SELECT * FROM agendamentos')
        for linha in mostrar.fetchall():
            print(linha)
        id_agendamentos = input('\nID agendamento: ')
        alteracao_campo = input('Digite o campo de alteracao (id_paciente, id_medico, data, horario): ')
        alteracao = input('Digite a alteracao: ')
        altera_agendamentos(alteracao_campo, alteracao, id_agendamentos)
        menu_atendente()
    if opcao == 4:
        clear()
        print('Consultas cadastradas (ID, ID paciente, ID medico, data, horario): ')
        mostrar = cursor.execute('SELECT * FROM agendamentos')
        for linha in mostrar.fetchall():
            paciente_id = linha[1]
            medico_id = linha[2]
            paciente_nome = ''
            medico_nome = ''
            medico_profissao = ''
            novo_mostrar = cursor.execute('SELECT * FROM paciente WHERE id = ? OR id = ?', (paciente_id, paciente_id))
            for nova_linha in novo_mostrar.fetchall():
                paciente_nome = nova_linha[1]
            novo_mostrar = cursor.execute('SELECT * FROM funcionarios WHERE id = ? OR id = ?', (medico_id, medico_id))
            for nova_linha in novo_mostrar.fetchall():
                medico_nome = nova_linha[0]
                medico_profissao = nova_linha[1]
            print(linha[3], 'as', linha[4], paciente_nome, 'tem um consulta agendada com', medico_nome, '(', medico_profissao, ')')

        input('Pressione qualquer tecla para continuar')
        menu_atendente()
    if opcao == 5:
        clear()
        nome = input('Digite o nome do paciente: ')
        idade = input('Digite a idade do paciente: ')
        sexo = input('Digite o sexo do paciente: ')
        peso = input('Digite o peso do paciente: ')
        insere_paciente(nome, idade, sexo, peso)
        menu_atendente()
    if opcao == 6:
        fazerlogin()

    else:
        clear(), print("Invalido, entre com outro valor\n"), menu_atendente()

def menu_manager():
    clear()
    print('\nBem vindo '+usuario_logado+'!\n1- Cadastrar funcionario.\n2- Remover funcionario.\n3- Alterar funcionario.\n4- Ver funcionarios cadastrados.\n5- Cadastrar veiculo.\n6- Remover veiculo.\n7- Alterar veiculo.\n8- Ver veiculos cadastrados.\n9- Cadastrar login.\n10- Remover login.\n11- Alterar login\n12- Listar logins\n13- Sair!')
    opc = int(input('Digite a opcao desejada: '))
    if opc == 1:
        nome = input('Digite o nome do funcionario: ')
        profissao = input('Digite a profissao do funcionario: ')
        matricula =  input('Digite a matricula do funcionario: ')
        insere_funcionarios(nome, profissao, matricula)
        voltar_manager()
        return 0
    if opc == 2:
        print('Funcionarios cadastrados (nome, profissao, matricula, ID): ')
        mostrar = cursor.execute('SELECT * FROM funcionarios')
        for linha in mostrar.fetchall():
            print(linha)
        id_funcionario_r = input("\nDigite o ID do funcionario que deseja remover: ")
        remove_funcionarios(id_funcionario_r)
        voltar_manager()
        return 0
    if opc == 3:
        print('Funcionarios cadastrados (nome, profissao, matricula, ID): ')
        mostrar = cursor.execute('SELECT * FROM funcionarios')
        for linha in mostrar.fetchall():
            print(linha)
        id_funcionario = int(input('\nID do funcionario que deseja alterar: '))
        alteracao_campo = input('Digite o campo de alteracao (nome, profissao, matricula): ')
        alteracao = input('Digite a alteracao: ')
        altera_funcionarios(alteracao_campo, alteracao, id_funcionario)
        voltar_manager()
        return 0
    if opc == 4:
        print('Funcionarios cadastrados (nome, profissao, matricula, ID): ')
        mostrar = cursor.execute('SELECT * FROM funcionarios')
        for linha in mostrar.fetchall():
            print(linha)
        voltar_manager()
        return 0
    if opc == 5:
        placa = input('Digite a placa do veiculo: ')
        status = input('Digite o status do veiculo: ')
        motorista = input('Digite o motorista do veiculo: ')
        paramedico = input('Digite o paramedico que esta no veiculo: ')
        paciente = input('Digite o paciente que será atendido: ')
        insere_veiculos(placa, status, motorista, paramedico, paciente)
        voltar_manager()
        return 0
    if opc == 6:
        print('Veiculos cadastrados (ID, placa, status, motorista, paramedico, paciente): ')
        mostrar = cursor.execute('SELECT * FROM veiculos')
        for linha in mostrar.fetchall():
            print(linha)
        id_veiculo_r = input("\nDigite o ID do veiculo que deseja remover: ")
        remove_veiculos(id_veiculo_r)
        voltar_manager()
        return 0
    if opc == 7:
        print('Veiculos cadastrados (ID, placa, status, motorista, paramedico, paciente): ')
        mostrar = cursor.execute('SELECT * FROM veiculos')
        for linha in mostrar.fetchall():
            print(linha)
        id_veiculo = input('\nID do veiculo que deseja alterar: ')
        alteracao_campo = input('Digite o campo de alteracao (placa, status, motorista, paramedico, paciente): ')
        alteracao = input('Digite a alteracao: ')
        altera_veiculos(alteracao_campo, alteracao, id_veiculo)
        voltar_manager()
        return 0
    if opc == 8:
        print('Veiculos cadastrados (ID, placa, status, motorista, paramedico, paciente): ')
        mostrar = cursor.execute('SELECT * FROM veiculos')
        for linha in mostrar.fetchall():
            print(linha)
        voltar_manager()
        return 0
    if opc == 9:
        nome_usuario = input('\nDigite o login a ser cadastrado:')
        senha = input('\nDigite sua senha:')
        area = input('\nDigite sua profissao:')
        cadastro_login(nome_usuario, senha, area)
        voltar_manager()
        return 0
    if opc == 10:
        mostrar = cursor.execute('SELECT * FROM login')
        for linha in mostrar.fetchall():
            print(linha)
        id_usuario = input('digite o id do usuario a ser removido: ou "cancelar" para voltar\n')
        if(id_usuario != "cancelar"):
            remove_login(id_usuario)
        voltar_manager()
        return 0
    if opc == 11:
        altera_login()
        voltar_manager()
        return 0
    if opc == 12:
        mostrar = cursor.execute('SELECT * FROM login')
        for linha in mostrar.fetchall():
            print(linha)
        voltar_manager()
        return 0
    if opc == 13:
        fazerlogin()
    else:
        clear(), print("Invalido, entre com outro valor\n"), menu_manager()
def voltar_manager():# Luiz Eduardo
    volta = input('\nDeseja voltar(sim ou nao)?:')
    if volta == 'sim':
        clear()
        menu_manager()
    else:
        return 0

def menu_medico():
    clear()
    opcao = int(input('\nBem vindo '+usuario_logado+'\nDigite\n1-Para fazer anamnese\n2-Para cadastrar ou remover um leito \n3-Para mudar senha ou login\n4-Para sair\n'))
    if opcao == 1:
        mostrar = cursor.execute('SELECT * FROM paciente')
        for linha in mostrar.fetchall():
            print(linha)
        id_paciente = input('\nDigite o ID do paciente:\n')
        onde_doi = input('\nDigite o local da dor:\n')
        o_que_sente = input('\nDigite o que o paciente sente:\n')
        quando_comecou = input('\nDigite a data de quando começou:\n')
        insere_anamnese(id_paciente, onde_doi, o_que_sente, quando_comecou)
        voltar_medico()
        return 0
    if opcao == 2:
        op = int(input('\n1-Cadastrar\n2-Remover\n:'))
        if op == 1:
            nome = input('Digite o nome do paciente:')
            numero = input('Digite o numero do leito:')
            cadastra_leito(nome, numero)
            voltar_medico()
            return 0
        if op == 2:
            mostrar = cursor.execute('SELECT * FROM dadosleito')
            for linha in mostrar.fetchall():
                print(linha)
            id_paciente = input('id do leito a ser removido:')
            remove_leito(id_paciente)
            voltar_medico()
            return 0
    if opcao == 3:
        altera_login()
        voltar_medico()
        return 0
    if opcao == 4:
        fazerlogin()
    else:
        print('Numero invalido, digite novamente!\n')
def voltar_medico():# Luiz Eduardo
    volta = input('\nDeseja voltar(sim ou nao)?:')
    if volta == 'sim':
        clear()
        menu_medico()
    else:
        return 0

def menu_engbio():# Luiz Eduardo
    clear()
    print("Bem vindo "+usuario_logado+"!\n\n1-Calibragem de equipamentos.\n2-Cadastrar/Remover equipamento.\n3-Listar/Alterar equipamentos.\n4-Sair!")
    opcao = int(input('Digite o numero da opcao desejada=>'))
    if opcao == 1:
        print("\nQual equipamento deseja calibrar ?")
        voltar_engbio()
        return 0
    if opcao == 2:
        print("1-Cadastrar\n2-Remover")
        cr = int(input('Digite o numero da opcao desejada=>'))
        if cr == 1:
            nome = input('Nome:')
            funcao = input('Funcao:')
            preco = input('Preço:')
            status = input('Status:')
            data = input('Data de insersao:')
            insere_equipamento(nome, funcao, preco, status, data)
            print('Cadastrado com sucesso !')
            voltar_engbio()
            return 0
        if cr == 2:
            lista_equipamento()
            id_equipamento = input('id=')
            remove_equipamento(id_equipamento)
            print("\nEquipamento removido com sucesso!")
            voltar_engbio()
            return 0
        else:
            voltar_engbio()
            return 0
    if opcao == 3:
        lista_equipamento()
        resp = input('\nDeseja alterar(sim ou nao)?')
        if resp == 'sim':
            id_equipamento = input('Id do equipamento:')
            novo_nome = input('Digite o nome:')
            nova_funcao = input('Digite a funcao:')
            novo_preco = input('Digite o preco:')
            novo_status = input('Digite o novo status do equipamento:')
            nova_data = input('Digite a data atual:')
            alterar_equipamento(id_equipamento, novo_nome, nova_funcao, novo_preco, novo_status, nova_data)
            print('Alterado com sucesso !')
            voltar_engbio()
            return 0
        else:
            voltar_engbio()
            return 0
    if opcao == 4:
        fazerlogin()
    else:
        clear()
        menu_engbio()
def voltar_engbio():# Luiz Eduardo
    volta = input('\nDeseja voltar(sim ou nao)?:')
    if volta == 'sim':
        clear()
        menu_engbio()
    else:
        return 0


firstAccess()

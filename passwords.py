import sqlite3

MASTER_PASSWORD = "senha1"

senha = input("Insira sua senha master:")
if senha != MASTER_PASSWORD:
    print("Senha Inválida! Encerrando ...")
    exit() 

conn = sqlite3.connect('passwords.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    service  TEXT NOT NULL,
    usernamer TEXT NOT NULL,
    password  TEXT NOT NULL
);
''')

def menu():
    print("******************************")
    print("* i : inserir nova senha     *")
    print("* l : listar serviços salvos *")
    print("* r : recuperar uma senha    *")
    print("* s : sair                   *")
    print("******************************")

def get_password(service):
    cursor.execute(f'''
        SELECT username, password FROM users
        WHERE service = '{service}'
    ''')

    if cursor.rowcount ==0:
        print("Serviço não cadastrado (use 'l' para verificar os serviços).")
    else:
        for user in cursor.fetchall():
            print(user)

def insert_password(cursor,service, username, password):
    cursor.execute('''
    INSERT INTO users (service, username, password) 
    VALUES ('{service}', '{username}', '{password}' )
    ''')
    conn.commit()

def show_services(cursor):
    cursor.execute('''
    SELECT service FROM users;
    ''')
    for service in cursor.fetchalll():
        print(service)
    

while True:
    menu()
    op = input("o que deseja fazer? ")
    if op not in ['l', 'i', 'r']:
        print("Opção Inválida!")
        continue

    if op == 's':
        break

    if op == 'i':
        service = input('Qual o nome do serviço?  ')
        username = input('Qual o nome de usuario? ')
        password = input('Qual a senha')
        insert_password(service, username, password)

    if op == 'l':
        show_passwords()

    if op == 'r':
        service = input('Qual o serviço para o qual quer a senha? ')
        get_password(service)



conn.close()
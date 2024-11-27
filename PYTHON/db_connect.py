
# coding: UTF-8

# db_connect.py

import mysql.connector
import os

connect = mysql.connector.connect (

    host = '127.0.0.1',
    user = 'root',
    password = 'toorroot',
    database = 'my_database'    

)

if connect.is_connected ():

    pass

else:

    print ('not connected!')
    exit ()

cursor = connect.cursor ()

verify_database = f'SHOW DATABASES LIKE {database};'

cursor.execute (verify_database)

verify_database = cursor.fetchone ()

if verify_database:

    pass

else:

    pwd = os.getcwd ()

    file_my_database = f'{pwd}\\my_database.sql'

    with open (file_my_database, 'r', encoding = 'UTF-8') as file:

        import_query_sql = file.read ()

    for jump in import_query_sql.split (';'):

        if jump.strips ():
   
            cursor.execute (jump)
        
    cursor.commit ()

while True:

    os.system ('cls')
    
    print ("""
    =============================
   *                             * 
   *       CRUD in the Python    *
   *                             *   
   *     1) CREATE | CRIAR       *
   *     2) READ | LER           *
   *     3) UPDATE | ATUALIZAR   *
   *     4) DELETE | DELETAR     *
   *                             *
    =============================
    """)
    
    crud = int (input ('Type the option: '))
    
    if crud == 1:
        os.system ('cls')
        break
    elif crud == 2:
        os.system ('cls')
        break
    elif crud == 3:
        os.system ('cls')
        break
    elif crud == 4:
        os.system ('cls')
        break
    else:
        os.system ('cls')
        continue

tables = ['users', 'address']

def show_tables_command ():

    command_show_tables = f"SHOW TABLES;"
    
    cursor.execute (command_show_tables)
    
    results = cursor.fetchall ()
    
    for result in results:
    
        print (result [0])

show_tables_command ()

print ('\n')
table_name = input ('table_name or e/E to exit: ')
os.system ('cls')

def show_columns_command ():

    if table_name in tables and table_name == 'users':

        command_show_columns = f"DESCRIBE users;"
        
        cursor.execute (command_show_columns)
        
        results = cursor.fetchall ()
        
        for result in results:
        
            print (result [0])
        
    elif table_name in tables and table_name == 'address':

        command_show_columns = f"DESCRIBE address;"
        
        cursor.execute (command_show_columns)
        
        results = cursor.fetchall ()
        
        for result in results:
        
            print (result [0])
            
show_columns_command ()

print ('\n')
quantity_columns = int (input ('quantity_columns: '))

"""def select_command ():

    if table_name in tables and table_name == 'users':

        command_select = f"SELECT * FROM users;"

        cursor.execute (command_select)
        
        result = cursor.fetchall ()
        
        print (result)
        
    elif table_name in tables and table_name == 'users':
    
        command_select = f"SELECT * FROM address;"
        
        cursor.execute (command_select)
        
        result = cursor.fetchall ()
        
        print (result)
        
    else:
    
        print ('column not found!')

select_command ()"""

if crud == 1:

    while True:
        
        if table_name in tables:
        
            if table_name == 'users':
            
                should_break = False
            
                while True:
                
                    columns_users = []
                    data_users = []

                    print ('\n')
                    
                    for quantity_column in range (quantity_columns):
                    
                        column_user = input ('column_name{}: '.format (quantity_column+1))
                        columns_users.append (column_user)
                        
                    print ('\n')

                    for zero, column_user in enumerate (columns_users):
                    
                        data_for_column = input ('data_for_column_{}: '.format (column_user))
                        data_users.append (data_for_column)
                        
                    columns_join = ", ".join (columns_users)
                    values = []    
                        
                    for column, data_column in zip (columns_users, data_users):
                    
                        values.append (f"'{data_column}'" if isinstance (data_column, str) else str (data_column))
                    
                    data_join = ", ".join (values)
                    
                    command_insert = f"INSERT INTO {table_name} ({columns_join}) VALUES ({data_join})"
                    
                    cursor.execute (command_insert)
                    connect.commit ()
                    should_break = True
                    break
                
                if should_break == True:
                
                    break
                    
                else:
                
                    continue
                    
            elif table_name == 'address':
            
                should_break = False
                
                while True:
                
                    columns_address = []
                    data_address = []
                    
                    for quantity_column in range (quantity_columns):
                    
                        column_address = input ('column_name{}: '.format (quantity_column+1))
                        columns_address.append (column_address)
                        
                    print ('\n')
                        
                    for zero, column_address in enumerate (columns_address):
                    
                        address_data = input ('data_for_column_{}: '.format (column_address))
                        data_address.append (address_data)
                        
                    columns_join = ", ".join (columns_address)
                    values = []
                    
                    for column, data_column in zip (columns_address, data_address):

                        values.append (f"'{data_column}'" if isinstance (data_column, str) else str (data_column))
                    
                    data_join = ", ".join (values)

                    command_insert = f"INSERT INTO {table_name} ({columns_join}) VALUES ({data_join})"

                    cursor.execute (command_insert)                    
                    cursor.commit ()
                    should_break = True
                    break

                if should_break == True:

                    break

                else:

                    continue                

            else:
            
                print ('table not found!')
                
        elif table_name == 'e' or table_name == 'E':
        
            break
            
        else:
        
            break

elif crud == 2:

    while True:
    
        if table_name in tables:
        
            break
    
        print ('\n')
         
else:

    print ('incorrect')


































def read ():

    command = f'SELECT * from users;'
    return cursor.execute (command)
    result = cursor.fetchall ()
    
    print (result)
    
def insert ():

    command_insert_users = f'INSERT INTO users (full_name, date_of_birth, cpf, email, phone) VALUES ({column_user})';
    command_insert_address = f'INSERT INTO address (road, neighborhood, city, uf, postcode) VALUES ()'

#Criando função de conexão e consulta
import mysql.connector  
import os, queries
from dotenv import load_dotenv; load_dotenv() #carrega segredos no .env

def make_connection():
    """Cria conexão com o banco de dados através do arquivo .env de configuração

    Returns:
        _type_: _mysql.connector.connection_cext.CMySQLConnection_
    """    
    con = mysql.connector.connect(user=os.getenv('USER'),password=os.getenv('PSWD'), \
        host=os.getenv('HOST'), database=os.getenv('DB'))
    return con

def select(query):
    """_Realiza o processo de executar consulta_

    Args:
        query (_type_): _string_

    Returns:
        _type_: _list_
    """    
    con = make_connection()
    cursor = con.cursor()
    cursor.execute(query)
    result = cursor.fetchall()

    if con.is_connected():
        cursor.close()
        con.close()
        
    return result

def pretty_print(result_list, question_number):
    if question_number < 6:
        print(f'q{question_number}\t{result_list[0][0]}\t{result_list[0][1]}')
    else:
        for q in result_list:
            print(f'{q[0]}\t{q[1]}\t{q[2]}')
            
if __name__ == '__main__':
    print('Questao\tV1\tV2')
    pretty_print(select(queries.QUESTAO_1),1)
    pretty_print(select(queries.QUESTAO_2),2)
    pretty_print(select(queries.QUESTAO_3),3)
    pretty_print(select(queries.QUESTAO_4),4)
    pretty_print(select(queries.QUESTAO_5),5)
    print('-'*20)
    pretty_print(select(queries.QUESTAO_6),6)
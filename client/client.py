import socket
import rsa

# recebo do usuário o endereço de ip do servidor e sua chave pública
server_ip = input("Digite o IP do servidor: ")
public_key_path = input("Digite o caminho da chave pública do servidor: ")

# lê a chave pública
with open(public_key_path, 'rb') as key_file:
    public_key_bytes = key_file.read()

# carrega a chave pública
public_key = rsa.PublicKey.load_pkcs1(public_key_bytes, format='PEM')

# inicializa o socket, para que possa se conectar com o servidor através da porta
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, 5002))

while True:
    # recebe a mensagem digitada pelo usuário
    message = input("Digite a mensagem: ").encode('utf-8')
    if message.lower() == 'sair':
        break
    
    # criptografa a mensagem utilizando a chave pública do servidor
    encrypted_message = rsa.encrypt(message, public_key)
    
    # envia a mensagem ao servidor
    client_socket.send(encrypted_message)

client_socket.close() # fecha a conexão

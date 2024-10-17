import socket
import rsa

server_ip = input("Digite o IP do servidor: ")
public_key_path = input("Digite o caminho da chave pública do servidor: ")

with open(public_key_path, 'rb') as key_file:
    public_key_bytes = key_file.read()

public_key = rsa.PublicKey.load_pkcs1(public_key_bytes, format='PEM')

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, 12345))  # Conectar ao IP do servidor

while True:
    message = input("Digite a mensagem (ou 'sair' para encerrar): ")
    if message.lower() == 'sair':
        break
    
    encrypted_message = rsa.encrypt(message, public_key)
    
    client_socket.send(encrypted_message)

client_socket.close()

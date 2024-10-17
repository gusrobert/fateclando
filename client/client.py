import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

server_ip = input("Digite o IP do servidor: ")
public_key_path = input("Digite o caminho da chave pública do servidor (arquivo .pem): ")

with open(public_key_path, 'rb') as key_file:
    public_key_bytes = key_file.read()

public_key = serialization.load_pem_public_key(public_key_bytes, backend=default_backend())

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((server_ip, 12345))  # Conectar ao IP do servidor

while True:
    message = input("Digite a mensagem (ou 'sair' para encerrar): ")
    if message.lower() == 'sair':
        break
    
    encrypted_message = public_key.encrypt(
        message.encode(),
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    client_socket.send(encrypted_message)

client_socket.close()

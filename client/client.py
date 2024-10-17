import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import hashes

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

public_key_bytes = client_socket.recv(1024)
public_key = serialization.load_pem_public_key(public_key_bytes, backend=default_backend())

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

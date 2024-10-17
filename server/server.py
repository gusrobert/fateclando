import socket
import rsa

private_key_path = input('Endereco da chave privada: ')
public_key_path = input('Endereco da chave pública: ')

with open(private_key_path, 'r') as key_file:
    private_key_bytes = key_file.read()

with open(public_key_path, 'r') as key_file:
    public_key_bytes = key_file.read()

private_key = rsa.PrivateKey.load_pkcs1(private_key_bytes, format='PEM')
public_key = rsa.PublicKey.load_pkcs1(public_key_bytes, format='PEM')

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 12345))
server_socket.listen(1)
print("Aguardando conexão...")

conn, addr = server_socket.accept()
print(f"Conectado a {addr}")

conn.send(public_key_bytes)

while True:
    encrypted_message = conn.recv(1024)
    if not encrypted_message:
        break

    decrypted_message = rsa.decrypt(encrypted_message, private_key)

    print(f"Mensagem recebida: {decrypted_message.decode()}")

conn.close()

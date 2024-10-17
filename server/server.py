import socket
import rsa

# Recebo as chaves privada e pública do servidor
private_key_path = input('Endereco da chave privada: ')

# Leio as chaves
with open(private_key_path, 'r') as key_file:
    private_key_bytes = key_file.read().encode()

# Carrega as chaves
private_key = rsa.PrivateKey.load_pkcs1(private_key_bytes, format='PEM')

# Inicializa o socket e configura o ip e a porta
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5002))
server_socket.listen(1)
print("Aguardando conexão...")

# Recebe as conexões
conn, addr = server_socket.accept()
print(f"Conectado a {addr}")

while True:
    # recebe as mensagens encriptadas com a chave pública do servidor
    encrypted_message = conn.recv(1024)
    if not encrypted_message:
        break

    # descriptografa a mensagem utilizando a chave privada
    decrypted_message = rsa.decrypt(encrypted_message, private_key)

    #exibe a mensagem na tela
    print(f"Mensagem recebida: {decrypted_message.decode()}")

conn.close() # fecha a conexão

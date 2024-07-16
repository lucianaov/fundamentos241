import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    question = input("Digite a questão (1a, 1b, 2a, 2b, 3, 4, 5a, 5b, 6a, 6b ou 7): ")
    if question in ['1a', '1b']:
        param1 = input("Digite o parâmetro: ")
        message = f"{question}|{param1}"
    elif question in ['2a', '2b', '3']:
        param1 = input("Digite o primeiro parâmetro binário: ")
        param2 = input("Digite o segundo parâmetro binário: ")
        message = f"{question}|{param1}|{param2}"
    elif question == '4':
        param1 = input("Digite o valor decimal (por exemplo, -750.1875): ")
        message = f"{question}|{param1}"
    elif question == '5a':
        param1 = input("Digite a frase: ")
        message = f"{question}|{param1}"
    elif question == '5b':
        param1 = input("Digite a primeira frase: ")
        param2 = input("Digite a segunda frase: ")
        message = f"{question}|{param1}|{param2}"
    elif question in ['6a', '6b', '7']:
        message = f"{question}|"
    else:
        print("Questão inválida.")
        return
    
    client_socket.send(message.encode('utf-8'))
    
    response = client_socket.recv(1024).decode('utf-8')
    print(f"Resposta do servidor: {response}")

    client_socket.close()

if __name__ == "__main__":
    start_client()


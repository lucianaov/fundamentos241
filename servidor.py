import socket
import struct

def hex_to_dec(hex_num):
    return int(hex_num, 16)

def dec_to_bin(dec_num):
    return bin(int(dec_num))[2:]

def bin_to_dec(bin_str):
    if bin_str[0] == '1':  # Negative number in two's complement
        return -((1 << len(bin_str)) - int(bin_str, 2))
    else:
        return int(bin_str, 2)

def dec_to_bin(dec_num):
    if dec_num < 0:
        dec_num = (1 << 8) + dec_num  # Convert negative number to two's complement
    return bin(dec_num)[2:].zfill(8)

def add_binary(bin1, bin2):
    result = bin_to_dec(bin1) + bin_to_dec(bin2)
    result_bin = dec_to_bin(result)
    overflow = result > 127 or result < -128
    return result_bin, overflow

def sub_binary(bin1, bin2):
    result = bin_to_dec(bin1) - bin_to_dec(bin2)
    result_bin = dec_to_bin(result)
    overflow = result > 127 or result < -128
    return result_bin, overflow

def div_binary(bin1, bin2):
    num1 = bin_to_dec(bin1)
    num2 = bin_to_dec(bin2)
    if num2 == 0:
        return "Erro: Divisão por zero", True
    result = num1 // num2
    result_bin = dec_to_bin(result)
    return result_bin, False

def float_to_ieee754(value):
    packed = struct.pack('>f', value)
    bits = ''.join(f'{c:08b}' for c in packed)
    hex_value = ''.join(f'{c:02X}' for c in packed)
    return bits, hex_value

def utf8_encode(s):
    return s.encode('utf-8').hex()

def compare_utf8_lengths(s1, s2):
    len1 = len(s1.encode('utf-8'))
    len2 = len(s2.encode('utf-8'))
    return len1, len2

def simplify_boolean_expression():
    # Simplificação algébrica da função booleana F(A, B, C, D, E)
    steps = [
        "F(A, B, C, D, E) = A'B'C'D'E' + A'BC'DE' + AB'C'D'E'",
        "Distribuição da negação: A'B'C'D'E' + A'BC'DE' + AB'C'D'E'",
        "Distribuição de A': A'(B'C'D'E' + BC'DE') + AB'C'D'E'",
        "Fatoração de B'C'D'E': A'(B'C'D'E' + DE') + AB'C'D'E'",
        "Distribuição de B'C'D'E': A'(B'C'D'E' + E') + AB'C'D'E'",
        "Simplificação: A'(B'C'D' + D)E' + AB'C'D'E'",
        "Fatoração de E': A'(B'C'D' + D)E' + AB'C'D'E'",
        "Distribuição de A'(B'C'D' + D): A'(B'C'D' + D)E' + AB'C'D'E'",
        "Simplificação final: A'E' + AB'C'D'E'"
    ]
    return steps

def simplify_boolean_expression():
    # Simplificação algébrica da função booleana F(A, B, C)
    steps = [
        "F(A, B, C) = A'B'C' + A'BC + AB'C'",
        "Distribuição da negação: A'B'C' + A'BC + AB'C'",
        "Distribuição de A': A'(B'C' + BC) + AB'C'",
        "Fatoração de B'C': A'(B'C' + C) + AB'C'",
        "Distribuição de B'C': A'(B'C + C) + AB'C'",
        "Simplificação: A'(B' + C) + AB'C'",
    ]
    return steps

def process_request(data):
    try:
        question, *params = data.split('|')
        params = [param.strip() for param in params]

        if question == '1a':
            hex_num = params[0]
            result = hex_to_dec(hex_num)
            return f"Resultado (2AA16 para base 10): {result}"
        
        elif question == '1b':
            dec_num = params[0]
            result = dec_to_bin(dec_num)
            return f"Resultado (356 para base 2): {result}"
        
        elif question == '2a':
            bin1, bin2 = params
            result, overflow = add_binary(bin1, bin2)
            overflow_msg = "com overflow" if overflow else "sem overflow"
            return f"Resultado (11010111 + 11100111): {result} ({overflow_msg})"
        
        elif question == '2b':
            bin1, bin2 = params
            result, overflow = sub_binary(bin1, bin2)
            overflow_msg = "com overflow" if overflow else "sem overflow"
            return f"Resultado (11100100 - 10101111): {result} ({overflow_msg})"
        
        elif question == '3':
            bin1, bin2 = params
            result, error = div_binary(bin1, bin2)
            if error:
                return result
            return f"Resultado (01101001 / 11110101): {result}"
        
        elif question == '4':
            value = float(params[0])
            bits, hex_value = float_to_ieee754(value)
            return f"Resultado (-750.1875 em IEEE 754):\n(a) Sequência de bits: {bits}\n(b) Hexadecimal: {hex_value}"
        
        elif question == '5a':
            phrase = params[0]
            encoded = utf8_encode(phrase)
            return f"Codificação UTF-8 de '{phrase}': {encoded}"
        
        elif question == '5b':
            phrase1 = params[0]
            phrase2 = params[1]
            len1, len2 = compare_utf8_lengths(phrase1, phrase2)
            return f"'{phrase1}' ocupa {len1} bytes, '{phrase2}' ocupa {len2} bytes."
        
        elif question == '6a':
            return "Por favor, desenhe a rede de portas lógicas manualmente."
        
        elif question == '6b':
            steps = simplify_boolean_expression()
            return "\n".join(steps)

        elif question == '7':
            # Implementação da questão 7 aqui
            # Exemplo simples para demonstração
            steps = simplify_boolean_expression()
            return "\n".join(steps)  # Retornando a simplificação da expressão booleana ABC
        
        
        else:
            return "Questão não reconhecida ou não implementada."
        
    except Exception as e:
        return f"Erro ao processar a solicitação: {e}"

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Servidor aguardando conexões...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Conexão de {addr} estabelecida.")
        
        data = client_socket.recv(1024).decode('utf-8')
        if not data:
            break
        
        response = process_request(data)
        client_socket.send(response.encode('utf-8'))
        
        client_socket.close()

if __name__ == "__main__":
    start_server()


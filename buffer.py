import ctypes

# Definição de uma classe para simular um buffer
class Buffer:
    def __init__(self):
        # Simulando um buffer de 64 bytes
        self.buffer = ctypes.create_string_buffer(64)

    def overflow(self, input_data):
        # Método que tenta copiar dados para o buffer
        print(f"Tentando armazenar {len(input_data)} bytes no buffer...")
        # Cuidado: Não deve ser usado em aplicações reais
        ctypes.memmove(self.buffer, input_data.encode('utf-8'), len(input_data))

    def display(self):
        # Mostra o conteúdo do buffer
        print("Conteúdo do buffer:", self.buffer.raw)

# Função principal para simular o ataque
def main():
    # Criando um objeto de buffer
    buffer = Buffer()

    # Dados de entrada grandes para simular o overflow
    attack_data = "A" * 100  # 100 bytes de 'A'

    # Tentando um ataque de buffer overflow
    try:
        buffer.overflow(attack_data)
    except Exception as e:
        print("Ocorreu um erro:", e)

    # Exibindo o conteúdo do buffer
    buffer.display()

if __name__ == "__main__":
    main()
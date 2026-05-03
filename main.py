# Importa as funções que criamos nos outros arquivos
from sniffer import listar_interfaces, capturar_pacotes
from detector import analisar_pacote

def main():
    print("=" * 50)
    print("        🛡️  Simple IDS - Monitor de Rede")
    print("=" * 50)

    # Chama a função do sniffer.py que lista e exibe as interfaces disponíveis
    interfaces = listar_interfaces()

    print("\nDigite o número da interface que deseja monitorar: ", end="")
    
    # int() converte o que o usuário digitou (texto) para número inteiro
    escolha = int(input())

    # Verifica se o número digitado existe na lista
    # ex: se há 10 interfaces, só aceita de 0 a 9
    if escolha < 0 or escolha >= len(interfaces):
        print("❌ Opção inválida!")
        return  # encerra a função se a escolha for inválida

    # Pega o nome da interface pelo índice escolhido
    interface_escolhida = interfaces[escolha]

    # try/except captura erros esperados sem travar o programa
    try:
        # Inicia a captura — para cada pacote capturado,
        # o sniffer chama analisar_pacote automaticamente (callback)
        capturar_pacotes(interface_escolhida, analisar_pacote)
    except KeyboardInterrupt:
        # Ctrl+C dispara o KeyboardInterrupt — tratamos aqui com uma mensagem amigável
        print("\n\n🔴 Monitoramento encerrado pelo usuário.")
        print("📄 Alertas salvos em: alertas.log")

# Garante que main() só roda quando o arquivo é executado diretamente
# Se outro arquivo importar este, o main() não é chamado automaticamente
if __name__ == "__main__":
    main()
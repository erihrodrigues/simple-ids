# Importa as funções do Scapy:
# sniff = captura pacotes da rede
# get_if_list = lista as interfaces de rede disponíveis
from scapy.all import sniff, get_if_list

def listar_interfaces():
    # Pega todas as interfaces de rede do PC (Wi-Fi, Ethernet, Loopback, etc)
    interfaces = get_if_list()
    
    print("\n🔌 Interfaces de rede disponíveis:")
    
    # enumerate() retorna o índice (i) e o valor (interface) ao mesmo tempo
    for i, interface in enumerate(interfaces):
        print(f"  [{i}] {interface}")
    
    # Retorna a lista para ser usada em outro lugar (ex: main.py)
    return interfaces

def capturar_pacotes(interface, callback):
    # interface = qual placa de rede vai monitorar
    # callback = função que será chamada automaticamente para cada pacote capturado

    print(f"\n🟢 Iniciando captura na interface: {interface}")
    print("   Pressione Ctrl+C para parar.\n")

    # sniff() fica em loop infinito escutando a rede
    # iface = qual interface monitorar
    # prn = função chamada a cada pacote (nosso callback)
    # store=False = não guarda pacotes na memória, evita travar o PC
    sniff(iface=interface, prn=callback, store=False)
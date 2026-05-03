# defaultdict é um dicionário que cria automaticamente um valor padrão para chaves novas
from collections import defaultdict
import time                        # usado para pegar o horário atual em segundos
from logger import registrar_alerta  # função que salva e exibe os alertas

# Histórico de atividade por IP — cada IP tem seu próprio registro
historico_portas = defaultdict(set)  # set = conjunto, não permite portas duplicadas
historico_icmp = defaultdict(list)   # list = lista de timestamps de pacotes ICMP
historico_syn = defaultdict(list)    # list = lista de timestamps de pacotes SYN

# Limites que definem quando um comportamento é considerado suspeito
LIMITE_PORT_SCAN = 15   # 15 portas únicas = suspeito
LIMITE_ICMP_FLOOD = 10  # 10 pings em 2 segundos = suspeito
LIMITE_SYN_FLOOD = 20   # 20 pacotes SYN em 3 segundos = suspeito

def analisar_pacote(pacote):
    # Importa as camadas do Scapy que vamos inspecionar
    # IP = camada de rede (contém IPs de origem e destino)
    # TCP = camada de transporte (contém portas e flags)
    # ICMP = protocolo de ping
    from scapy.all import IP, TCP, ICMP

    # Descarta pacotes que não têm camada IP (ex: pacotes ARP)
    if not pacote.haslayer(IP):
        return

    ip_origem = pacote[IP].src   # IP de quem enviou o pacote
    agora = time.time()          # horário atual em segundos (ex: 1746291483.42)

    # --- Detecção 1: Port Scan ---
    # Port Scan = alguém tentando descobrir quais portas estão abertas
    if pacote.haslayer(TCP):
        porta = pacote[TCP].dport          # porta de destino do pacote
        historico_portas[ip_origem].add(porta)  # adiciona ao conjunto desse IP

        # Se o IP já acessou 15 portas diferentes, dispara alerta
        if len(historico_portas[ip_origem]) >= LIMITE_PORT_SCAN:
            registrar_alerta(
                tipo="Port Scan",
                ip_origem=ip_origem,
                detalhes=f"{len(historico_portas[ip_origem])} portas únicas acessadas"
            )
            historico_portas[ip_origem].clear()  # reseta para não gerar alertas repetidos

    # --- Detecção 2: ICMP Flood ---
    # ICMP Flood = enviar muitos pings para sobrecarregar o alvo
    if pacote.haslayer(ICMP):
        historico_icmp[ip_origem].append(agora)  # registra o horário deste ping

        # Filtra a lista mantendo só os pings dos últimos 2 segundos
        # "agora - t <= 2" = o ping aconteceu há menos de 2 segundos
        historico_icmp[ip_origem] = [t for t in historico_icmp[ip_origem] if agora - t <= 2]

        # Se houve 10 ou mais pings em 2 segundos, dispara alerta
        if len(historico_icmp[ip_origem]) >= LIMITE_ICMP_FLOOD:
            registrar_alerta(
                tipo="ICMP Flood",
                ip_origem=ip_origem,
                detalhes=f"{len(historico_icmp[ip_origem])} pacotes ICMP em 2 segundos"
            )
            historico_icmp[ip_origem].clear()

    # --- Detecção 3: SYN Flood ---
    # SYN Flood = enviar muitos pedidos de conexão sem completá-los,
    # deixando o servidor sobrecarregado esperando respostas
    if pacote.haslayer(TCP):
        flags = pacote[TCP].flags
        if flags == "S":  # "S" = flag SYN ativa, sem ACK — pedido de conexão incompleto
            historico_syn[ip_origem].append(agora)

            # Mantém só os SYNs dos últimos 3 segundos
            historico_syn[ip_origem] = [t for t in historico_syn[ip_origem] if agora - t <= 3]

            # Se houve 20 ou mais SYNs em 3 segundos, dispara alerta
            if len(historico_syn[ip_origem]) >= LIMITE_SYN_FLOOD:
                registrar_alerta(
                    tipo="SYN Flood",
                    ip_origem=ip_origem,
                    detalhes=f"{len(historico_syn[ip_origem])} pacotes SYN em 3 segundos"
                )
                historico_syn[ip_origem].clear()
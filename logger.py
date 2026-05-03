# Módulo para trabalhar com datas e horários
import datetime

def registrar_alerta(tipo, ip_origem, detalhes):
    # tipo      = nome do ataque detectado (ex: "Port Scan")
    # ip_origem = IP de quem gerou o tráfego suspeito
    # detalhes  = informações extras sobre o pacote

    # datetime.now() = horário atual
    # strftime() formata a data para ficar legível: "2026-05-03 18:18:03"
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Monta a linha do alerta juntando todas as informações
    mensagem = f"[{agora}] [ALERTA] {tipo} | IP: {ip_origem} | {detalhes}"

    # Exibe o alerta no terminal
    print(mensagem)

    # Salva o alerta no arquivo alertas.log
    # "a" = modo append, adiciona no final sem apagar o que já estava salvo
    # Se o arquivo não existir, Python cria automaticamente
    # "with" garante que o arquivo é fechado corretamente após salvar
    with open("alertas.log", "a") as arquivo:
        arquivo.write(mensagem + "\n")  # "\n" pula linha após cada alerta
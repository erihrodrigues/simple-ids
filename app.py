# Flask = framework web para criar o servidor e as rotas
# render_template = carrega o arquivo HTML da pasta templates/
# jsonify = converte lista Python para formato JSON (usado pelo JavaScript)
from flask import Flask, render_template, jsonify
import threading  # permite rodar o IDS e o Flask ao mesmo tempo
import datetime
from sniffer import listar_interfaces, capturar_pacotes

# Cria a aplicação Flask
app = Flask(__name__)

# Lista global que guarda todos os alertas gerados durante a sessão
# Global = qualquer função do arquivo pode acessar e modificar ela
alertas = []

def registrar_alerta_web(tipo, ip_origem, detalhes):
    # Versão web do registrar_alerta — em vez de salvar em arquivo,
    # salva na lista "alertas" para o JavaScript buscar via /alertas
    agora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Dicionário com os dados do alerta — vira um objeto JSON na página
    alerta = {
        "horario": agora,
        "tipo": tipo,
        "ip": ip_origem,
        "detalhes": detalhes
    }
    alertas.append(alerta)  # adiciona o alerta na lista global
    print(f"[ALERTA WEB] {tipo} | {ip_origem}")  # confirma no terminal

# Rota "/" = página principal — acessada em http://localhost:5000
@app.route("/")
def index():
    return render_template("index.html")  # carrega o dashboard HTML

# Rota "/alertas" = retorna os alertas em JSON para o JavaScript da página
# O JavaScript chama essa rota a cada 2 segundos para atualizar a tabela
@app.route("/alertas")
def get_alertas():
    return jsonify(alertas)

def iniciar_ids(interface):
    import logger
    import detector

    # Substitui a função registrar_alerta dos dois módulos pela versão web
    # Assim quando o detector detectar um ataque, o alerta vai para a lista
    # em vez de só aparecer no terminal
    logger.registrar_alerta = registrar_alerta_web
    detector.registrar_alerta = registrar_alerta_web

    # Inicia a captura de pacotes — bloqueante, roda para sempre até Ctrl+C
    capturar_pacotes(interface, detector.analisar_pacote)

if __name__ == "__main__":
    interfaces = listar_interfaces()
    print("\nDigite o número da interface que deseja monitorar: ", end="")
    escolha = int(input())
    interface_escolhida = interfaces[escolha]

    # Thread = linha de execução paralela
    # daemon=True = a thread para automaticamente quando o programa principal fechar
    thread = threading.Thread(target=iniciar_ids, args=(interface_escolhida,))
    thread.daemon = True
    thread.start()  # inicia o IDS em paralelo

    print("\n🌐 Acesse o dashboard em: http://localhost:5000")

    # Inicia o servidor Flask — fica rodando e escutando requisições
    # host="0.0.0.0" = aceita conexões de qualquer IP da rede local
    # port=5000 = porta onde o servidor vai rodar
    app.run(host="0.0.0.0", port=5000)
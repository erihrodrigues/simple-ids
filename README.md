<div align="center">
root@erica:~/simple-ids$ cat README.md

# 🛡️ Simple IDS — Intrusion Detection System

</div>

---

<div align="center">

![Python](https://img.shields.io/badge/Python-3.x-00ff99?style=for-the-badge&logo=python&logoColor=white&labelColor=0a0a0a)
![Flask](https://img.shields.io/badge/Flask-Web-00ff99?style=for-the-badge&logo=flask&logoColor=white&labelColor=0a0a0a)
![Scapy](https://img.shields.io/badge/Scapy-Packets-00ff99?style=for-the-badge&logoColor=white&labelColor=0a0a0a)
![Status](https://img.shields.io/badge/Status-Active-00ff99?style=for-the-badge&labelColor=0a0a0a)

</div>

---

<pre>
root@erica:~/simple-ids$ ./ids --describe

[ EN ] A lightweight network intrusion detection system built with Python and Scapy.
       Monitors network traffic in real time and detects suspicious patterns
       such as Port Scan, SYN Flood and ICMP Flood — with a terminal-style web dashboard.

[ PT ] Um sistema simples de detecção de intrusão em redes, construído com Python e Scapy.
       Monitora o tráfego de rede em tempo real e detecta padrões suspeitos
       como Port Scan, SYN Flood e ICMP Flood — com dashboard web estilo terminal.
</pre>

---

## ⚡ Features / Funcionalidades

<pre>
root@erica:~/simple-ids$ ls features/

[✓] Real-time packet capture         — Captura de pacotes em tempo real
[✓] Port Scan detection              — Detecção de varredura de portas
[✓] SYN Flood detection              — Detecção de flood de conexões TCP
[✓] ICMP Flood detection             — Detecção de ping flood
[✓] Terminal-style web dashboard     — Dashboard web estilo terminal
[✓] Auto-updating alerts table       — Tabela de alertas atualizada a cada 2s
[✓] Alert logging to file            — Alertas salvos em alertas.log
</pre>

---

## 🖥️ Dashboard

<div align="center">
  <img src="assets/dashboard.png" alt="Simple IDS Dashboard" width="100%"/>
</div>

---

## 🛠️ Tech Stack

<pre>
root@erica:~/simple-ids$ ls stack/

python       — core language
scapy        — packet capture and analysis
flask        — web server and dashboard
threading    — parallel execution (IDS + Flask)
javascript   — real-time dashboard updates
npcap        — windows packet capture driver
</pre>

---

## 📁 Project Structure / Estrutura
simple-ids/
├── app.py          → Flask server + web alert handler
├── sniffer.py      → Network interface listing and packet capture
├── detector.py     → Attack detection logic (Port Scan, SYN Flood, ICMP Flood)
├── logger.py       → Terminal alert logging and .log file writing
├── alertas.log     → Generated alert log file
└── templates/
└── index.html  → Terminal-style web dashboard

---

## 🚀 Installation / Instalação

**1. Clone the repository**
```bash
git clone https://github.com/erihrodrigues/simple-ids.git
cd simple-ids
```

**2. Install dependencies**
```bash
pip install scapy flask
```

**3. Install Npcap** *(Windows only)*

Download and install from: https://npcap.com/#download

> ⚠️ During installation, check **"Install Npcap in WinPcap API-compatible Mode"**

---

## ▶️ Usage / Como usar

<pre>
root@erica:~/simple-ids$ python app.py

# Run as administrator / Execute como administrador!
# Choose your network interface / Escolha a interface de rede
# Open your browser / Abra o navegador:

→ http://localhost:5000
</pre>

> ⚠️ **Must be run as administrator** — packet capture requires elevated privileges.
> **Execute como administrador** — a captura de pacotes requer privilégios elevados.

---

## 🔍 How it works / Como funciona

<pre>
root@erica:~/simple-ids$ cat how_it_works.txt

Packet arrives on network interface
             ↓
      sniffer.py captures it
             ↓
    detector.py analyzes it
             ↓
   Suspicious? → logger.py fires alert
             ↓
   alert saved to alertas.log
             ↓
   dashboard updates in real time
</pre>

---

## 📡 Detection Rules / Regras de Detecção

<pre>
root@erica:~/simple-ids$ cat rules.conf

[PORT SCAN]   → 15+ unique ports accessed by same IP
[SYN FLOOD]   → 20+ SYN packets in 3 seconds from same IP
[ICMP FLOOD]  → 10+ ICMP packets in 2 seconds from same IP
</pre>

---

<div align="center">

<pre>
root@erica:~/simple-ids$ exit
Session terminated.
</pre>

Made with 💚 by [Erica Almeida](https://github.com/erihrodrigues)

</div>
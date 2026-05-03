<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NIS - Network Intelligence Suite</title>
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            background: #0a0e1a;
            font-family: 'Courier New', 'Fira Code', monospace;
            color: #00ffcc;
            padding: 30px 20px;
            line-height: 1.5;
        }
        .container {
            max-width: 1000px;
            margin: auto;
            background: #0f1322;
            border: 1px solid #00ffcc30;
            border-radius: 12px;
            padding: 30px;
            box-shadow: 0 0 25px #00ffcc10;
        }
        .header {
            text-align: center;
            border-bottom: 2px solid #00ffcc;
            padding-bottom: 20px;
            margin-bottom: 30px;
        }
        .header h1 {
            font-size: 2.2rem;
            letter-spacing: 3px;
            color: #ff3366;
            text-shadow: 0 0 5px #ff3366;
        }
        .header p {
            color: #88aaff;
            margin-top: 8px;
        }
        .badge {
            display: inline-block;
            background: #1e2a3a;
            padding: 5px 12px;
            border-radius: 30px;
            font-size: 12px;
            color: #00ffcc;
            margin: 5px;
        }
        .section {
            margin: 30px 0;
            border-left: 3px solid #00ffcc;
            padding-left: 20px;
        }
        .section h2 {
            color: #ffaa44;
            margin-bottom: 15px;
            font-size: 1.6rem;
        }
        .cmd {
            background: #00000060;
            border: 1px solid #00ffcc40;
            padding: 12px;
            font-family: monospace;
            border-radius: 8px;
            overflow-x: auto;
            margin: 15px 0;
            color: #bbffdd;
        }
        table {
            width: 100%;
            border-collapse: collapse;
            margin: 15px 0;
        }
        td, th {
            border: 1px solid #00ffcc30;
            padding: 8px;
            text-align: left;
        }
        th {
            background: #00ffcc20;
            color: #ffcc00;
        }
        .footer {
            text-align: center;
            margin-top: 40px;
            padding-top: 20px;
            border-top: 1px solid #00ffcc30;
            font-size: 12px;
            color: #6688aa;
        }
        a {
            color: #ff9966;
            text-decoration: none;
        }
        .ascii {
            font-size: 11px;
            white-space: pre;
            color: #00cc99;
            text-align: center;
        }
    </style>
</head>
<body>
<div class="container">
    <div class="header">
        <div class="ascii">
╔═════════════════════════════════════════════════════╗
║   NETWORK INTELLIGENCE SUITE (NIS) v1.0            ║
║   Professional Security Toolkit                    ║
╚═════════════════════════════════════════════════════╝
        </div>
        <h1>🛡️ NIS</h1>
        <p>developed by <strong style="color:#ff7777">Abhishek</strong> | greyhat · ethical · powerful</p>
        <div>
            <span class="badge">🔍 network scanner</span>
            <span class="badge">🚪 port scanner</span>
            <span class="badge">⚙️ service detect</span>
            <span class="badge">🖥️ OS fingerprint</span>
            <span class="badge">🐞 vuln checker</span>
            <span class="badge">📡 packet monitor</span>
        </div>
    </div>

    <div class="section">
        <h2>📌 what is nis ?</h2>
        <p>Network Intelligence Suite – complete network recon + vulnerability assessment tool.<br>
        <span style="color:#88aaff">✔️ legal for authorized testing</span> &nbsp;|&nbsp; 
        <span style="color:#88aaff">✔️ termux + linux + kali ready</span></p>
    </div>

    <div class="section">
        <h2>⚡ features</h2>
        <table>
            <tr><th>module</th><th>function</th></tr>
            <tr><td>network scanner</td><td>find all devices on your network</td></tr>
            <tr><td>port scanner</td><td>detect open ports (1-65535)</td></tr>
            <tr><td>service detector</td><td>grab banners & identify services</td></tr>
            <tr><td>os fingerprinting</td><td>guess linux / windows / cisco</td></tr>
            <tr><td>vulnerability checker</td><td>weak configs, default ports, poor auth</td></tr>
            <tr><td>packet monitor</td><td>live traffic capture (src/dst/proto)</td></tr>
            <tr><td>report generator</td><td>json + html pretty output</td></tr>
        </table>
    </div>

    <div class="section">
        <h2>🚀 install & run (termux/linux)</h2>
        <div class="cmd">
            git clone https://github.com/abhieexploits/NIS.git<br>
            cd NIS<br>
            chmod +x setup.sh && ./setup.sh<br>
            python nis.py
        </div>
        <p>📦 dependencies: scapy · requests · whois · dnspython + nmap, arp-scan, tcpdump</p>
    </div>

    <div class="section">
        <h2>🎮 menu preview</h2>
        <div class="cmd">
[1] network scanner<br>
[2] port scanner<br>
[3] service detector<br>
[4] os fingerprinting<br>
[5] vulnerability check<br>
[6] packet monitor<br>
[7] 🔥 full scan (all modules)<br>
[8] generate report<br>
[9] view last report<br>
[0] exit
        </div>
    </div>

    <div class="section">
        <h2>📸 example output</h2>
        <div class="cmd">
nis@tool:~$ 2<br>
target ip: 192.168.1.100<br>
port range: 1-1000<br>
<br>
[+] port 22 - OPEN (ssh)<br>
[+] port 80 - OPEN (http)<br>
[+] port 443 - OPEN (https)<br>
[+] port 3306 - OPEN (mysql)<br>
<br>
=> 4 open ports found
        </div>
    </div>

    <div class="section">
        <h2>📁 project structure</h2>
        <div class="cmd">
NIS/<br>
├── nis.py<br>
├── modules/   (scanner, ports, services, os, vuln, packet, report)<br>
├── utils/     (colors, validators)<br>
├── wordlists/<br>
├── output/    (reports .json / .html)<br>
├── setup.sh<br>
└── README.html
        </div>
    </div>

    <div class="section">
        <h2>⚠️ legal disclaimer</h2>
        <p style="color:#ffaa88">educational & authorized testing ONLY. do not scan without permission.<br>
        misuse = illegal. developer not responsible. you are warned.</p>
    </div>

    <div class="footer">
        🔥 network intelligence suite | abhishek | greyhat since 2026<br>
        <a href="#">github.com/abhieexploits/NIS</a> &nbsp;|&nbsp; 🕯️ use for good, break nothing without permission
    </div>
</div>
</body>
</html>

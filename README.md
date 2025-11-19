# 🛡️ Python Network Scanner

A simple automated network scanner built in Python using `nmap` and the `python-nmap` library.  
This project is part of my cybersecurity learning journey, focusing on practical tooling, network analysis, and Python automation.

---

## 🚀 Features

- Runs an Nmap scan directly from Python
- Shows open ports and detected services
- CLI arguments for flexible usage (`--target`, `--ports`)
- Works on local and remote targets
- Beginner-friendly, clean code structure

---

## 📦 Requirements

Before running the scanner, make sure you have:

- **Python 3+**
- **Nmap** installed and added to your system PATH  
  Download here: https://nmap.org/download.html  
- Python dependency:


---

## ⚙️ Installation

Create and activate a virtual environment:

```bash
python -m venv venv
venv\Scripts\activate        # Windows
# or
source venv/bin/activate     # macOS / Linux

pip install -r requirements.txt

🕹️ Usage
🔍 Basic scan (localhost)
python -m scanner.scanner

🎯 Scan a specific target
python -m scanner.scanner --target 192.168.1.10

🔧 Scan a custom port range
python -m scanner.scanner --target 192.168.1.10 --ports 1-65535

Short version
python -m scanner.scanner -t 127.0.0.1 -p 80,443

⚠️ Legal Notice

This tool is intended for educational and authorized use only.
Never scan networks or systems you do not own or have explicit permission to test.

📚 Roadmap (Future Improvements)

Save scan results to JSON/CSV

Add basic vulnerability indicators (e.g., “Port 22 open → SSH service”)

Faster scanning (multiple threads)

Exportable scan reports (HTML/PDF)

Web dashboard or GUI

Scheduled recurring scans

✨ About This Project

This tool is part of my personal learning project in cybersecurity.
It helps me practice:

Network scanning

Python automation

Security tooling

Git & GitHub workflow

Building real tools from scratch

Feel free to explore, fork, or contribute!


---

# 🎉 Ferdig!

Denne README-en er:

✔ Ryddig  
✔ Fullstendig  
✔ Uten feil formatering  
✔ Perfekt for GitHub  

---

## Vil du gjøre neste steg?

**Leksjon 3:** Lagre scan-resultater til JSON eller CSV  
(veldig nyttig for security analysis)

Bare skriv:

👉 **“klar for neste”**
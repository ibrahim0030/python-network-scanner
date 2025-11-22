# Python Nettverksskanner

En enkel og praktisk nettverksskanner skrevet i Python, bygget for læring innen cybersikkerhet.
Prosjektet demonstrerer hvordan man bruker Python sammen med `nmap` til å skanne både egen PC og andre enheter på hjemmenettverket.

---

## Funksjoner

* Skanner mål-IP for åpne porter og tjenester
* Bruker `python-nmap` for integrasjon med Nmap
* CLI-argumenter: `--target`, `--ports`
* Kan skanne deg selv (localhost) eller valgfri enhet
* Lett å utvide med flere sikkerhetsfunksjoner

---

## Krav

For å bruke verktøyet trenger du:

* **Python 3**
* **Nmap installert** (må ligge i PATH)
  Last ned her: [https://nmap.org/download.html](https://nmap.org/download.html)
* Avhengigheter installert via `requirements.txt`

---

## Installering og oppstart

### Klon prosjektet

```bash
git clone https://github.com/<brukernavn>/<repo-navn>.git
cd <repo-navn>
```

### Opprett og aktiver virtuelt miljø

```bash
python -m venv venv
```

**Windows:**

```bash
venv\Scripts\activate
```

**Mac/Linux:**

```bash
source venv/bin/activate
```

### Installer avhengigheter

```bash
pip install -r requirements.txt
```

### Start scanneren

#### Standard skanning (localhost)

```bash
python -m scanner.scanner
```

Dette skanner din egen PC (127.0.0.1).

#### Skann en annen enhet

```bash
python -m scanner.scanner --target 192.168.4.186
```

#### Skann tilpasset portområde

```bash
python -m scanner.scanner --target 192.168.4.186 --ports 1-65535
```

---

## Eksempler på resultater

### Eksempel: Skanning av egen PC

```
[+] Starting scan against 127.0.0.1 on ports 1-1024

Host: 127.0.0.1 (localhost)
State: up

Protocol: tcp
  Port: 135     State: open     Service: msrpc
  Port: 137     State: filtered Service: netbios-ns
  Port: 445     State: open     Service: microsoft-ds
```

### Eksempel: Skanning av en IoT-enhet

```
Host is up (0.010s latency)

PORT     STATE SERVICE         VERSION
80/tcp   open  http            nginx
8008/tcp open  http
8009/tcp open  ajp13
8443/tcp open  https-alt
9000/tcp open  cslistener
9080/tcp open  glrpc
```

---

## Om prosjektet

Dette er et læringsprosjekt i cybersikkerhet, med fokus på:

* Nettverksanalyse
* Python-automatisering
* Git/GitHub-workflow
* Forståelse av lavnivå sikkerhetsverktøy

Prosjektet er perfekt for portefølje og videre utvikling!

Det er viktig at dette prosjektet kun  blir brukt til lovlige tester. Uautorisert portskanning kan være ulovlig!
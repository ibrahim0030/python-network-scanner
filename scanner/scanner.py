import nmap

def scan_target(target: str, ports: str = "1-1024"):
    nm = nmap.PortScanner()
    print(f"[+] Starting scan against {target} on ports {ports}")
    nm.scan(target, ports)

    for host in nm.all_hosts():
        print(f"\nHost: {host} ({nm[host].hostname()})")
        print(f"State: {nm[host].state()}")

        for proto in nm[host].all_protocols():
            print(f"\nProtocol: {proto}")
            lport = nm[host][proto].keys()
            for port in sorted(lport):
                state = nm[host][proto][port]['state']
                service = nm[host][proto][port].get('name', 'unknown')
                print(f"  Port: {port}\tState: {state}\tService: {service}")

if __name__ == "__main__":
    # midlertidig: scanner localhost (din egen maskin)
    scan_target("127.0.0.1")

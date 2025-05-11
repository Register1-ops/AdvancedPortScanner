import nmap

def nmap_scan(ip, ports):
    """Scans given ports using Nmap."""
    scanner = nmap.PortScanner()
    scanner.scan(ip, ports)
    
    # Check if the scan was successful
    if ip not in scanner.all_hosts():
        print(f"Scan failed for {ip} or no open ports found.")
        return
    
    # Now safely access the results
    for port in scanner[ip]['tcp']:
        state = scanner[ip]['tcp'][port]['state']
        print(f"Port {port}: {state}")

# User Input
target_ip = input("Enter target IP: ")
port_range = input("Enter port range (e.g., 1-1024): ")

nmap_scan(target_ip, port_range)

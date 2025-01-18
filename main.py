from modules.subdomain import subdomain_enumeration
from modules.whois import whois_lookup
from modules.dns import dns_lookup

def main():
    domain = input("Enter the target domain (e.g., example.com): ").strip()
    wordlist = "subdomains.txt"

    print("\n[+] Starting Subdomain Enumeration...")
    subdomains = subdomain_enumeration(domain, wordlist)
    print(f"[+] Found {len(subdomains)} subdomains.")

    print("\n[+] Performing WHOIS Lookup...")
    whois_lookup(domain)

    print("\n[+] Performing DNS Lookup...")
    dns_lookup(domain)

if __name__ == "__main__":
    main()

import whois
import dns.resolver
import requests

def subdomain_enumeration(domain, wordlist):
    """Brute-force subdomains using a wordlist."""
    subdomains = []
    with open(wordlist, 'r') as file:
        for line in file:
            subdomain = line.strip()
            full_domain = f"{subdomain}.{domain}"
            try:
                # Resolve the subdomain
                dns.resolver.resolve(full_domain, 'A')
                subdomains.append(full_domain)
                print(f"[+] Found subdomain: {full_domain}")
            except dns.resolver.NXDOMAIN:
                continue
            except Exception as e:
                print(f"[-] Error resolving {full_domain}: {e}")
    return subdomains

def whois_lookup(domain):
    """Perform a WHOIS lookup for the domain."""
    try:
        w = whois.whois(domain)
        print(f"[+] WHOIS Information for {domain}:")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
    except Exception as e:
        print(f"[-] Error performing WHOIS lookup: {e}")

def dns_lookup(domain):
    """Perform a DNS lookup for common records."""
    record_types = ['A', 'MX', 'NS', 'TXT']
    for record in record_types:
        try:
            answers = dns.resolver.resolve(domain, record)
            print(f"[+] {record} Records for {domain}:")
            for rdata in answers:
                print(rdata)
        except dns.resolver.NoAnswer:
            print(f"[-] No {record} records found for {domain}")
        except Exception as e:
            print(f"[-] Error resolving {record} records: {e}")

def main():
    domain = input("Enter the target domain (e.g., example.com): ").strip()
    wordlist = "subdomains.txt"  # Path to your subdomain wordlist

    print("\n[+] Starting Subdomain Enumeration...")
    subdomains = subdomain_enumeration(domain, wordlist)
    print(f"[+] Found {len(subdomains)} subdomains.")

    print("\n[+] Performing WHOIS Lookup...")
    whois_lookup(domain)

    print("\n[+] Performing DNS Lookup...")
    dns_lookup(domain)

if __name__ == "__main__":
    main()

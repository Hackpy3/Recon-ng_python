import whois

def whois_lookup(domain):
    try:
        w = whois.whois(domain)
        print(f"[+] WHOIS Information for {domain}:")
        print(f"Registrar: {w.registrar}")
        print(f"Creation Date: {w.creation_date}")
        print(f"Expiration Date: {w.expiration_date}")
        print(f"Name Servers: {w.name_servers}")
    except Exception as e:
        print(f"[-] Error performing WHOIS lookup: {e}")

import dns.resolver

def subdomain_enumeration(domain, wordlist):
    subdomains = []
    with open(wordlist, 'r') as file:
        for line in file:
            subdomain = line.strip()
            full_domain = f"{subdomain}.{domain}"
            try:
                dns.resolver.resolve(full_domain, 'A')
                subdomains.append(full_domain)
                print(f"[+] Found subdomain: {full_domain}")
            except dns.resolver.NXDOMAIN:
                continue
            except Exception as e:
                print(f"[-] Error resolving {full_domain}: {e}")
    return subdomains

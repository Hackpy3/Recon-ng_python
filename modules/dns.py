import dns.resolver

def dns_lookup(domain):
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

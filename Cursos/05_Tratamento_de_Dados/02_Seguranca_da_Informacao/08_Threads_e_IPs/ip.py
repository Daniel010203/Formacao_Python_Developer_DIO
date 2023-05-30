import ipaddress

# ip = '192.168.0.1'
ip = '192.168.0.0/24'  # rede

# endereco = ipaddress.ip_address(ip)
rede = ipaddress.ip_network(ip, strict=False)  # aceita endereços de rede invalidos

# print(endereco)
print(rede)

for ip in rede:
    print(ip)
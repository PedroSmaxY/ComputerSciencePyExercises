import subprocess

while True:
    endereco_ip = "26.180.235.84" # endereço IP que deseja testar o ping

    retorno = subprocess.call(["ping", "-c", "3", endereco_ip]) # envia um ping com 3 pacotes

    if retorno == 0:
        print(f"O endereço IP {endereco_ip} está respondendo aos pings.")
    else:
        print(f"O endereço IP {endereco_ip} não está respondendo aos pings.")


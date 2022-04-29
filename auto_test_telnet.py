import telnetlib

open_hosts = open("hosts.txt", mode="r", encoding="UTF-8")
hosts = open_hosts.readlines()
port = "445"
i = 0
result = open('resultado-hosts.txt', 'w')

while i < 106:
    try:
        connection = telnetlib.Telnet(hosts[i], port)
        response = hosts[i].rstrip("\n")+' ' + port +' - Success'
    
    except:
        response = hosts[i].rstrip("\n")+' ' + port +' - Failed'
                
    finally:
        print(response)
        result.writelines(response + "\n")
        i += 1

open_hosts.close()
result.close()    
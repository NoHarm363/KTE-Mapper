import re
import nmap

ascii_art = '''
  _  _________ ______         __  __          _____  _____  ____________
 | |/ /__   __|  ____|       |  \/  |   /\   |  __ \|  __ \|  ____|  __ \\
 | ' /   | |  | |__          | \  / |  /  \  | |__) | |__) | |__  | |__) |
 |  <    | |  |  __|         | |\/| | / /\ \ |  ___/|  ___/|  __| |  _  /
 | . \   | |  | |____        | |  | |/ ____ \| |    | |    | |____| | \ \\
 |_|\_\  |_|  |______|       |_|  |_/_/    \_\_|    |_|    |______|_|  \_\\
'''

print(ascii_art)

while True:
    try:
        ip_address = input("Please type your IP address: \n")
        ip_address = ip_address.replace(" ", "")

        correct_ipaddr = re.search(r'^([1-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]).([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$', ip_address)

        if correct_ipaddr:
            break
        else:
            print("Incorrect IP address. Please try again. Format: xxx.xxx.xxx.xxx")

    except:
        pass

print("Your IP address is:", ip_address)

while True:
    try:
        port_range = input("Please type the port number range you want to scan, available range (1-65535):\n ")
        port_range = port_range.replace(" ","")
        correct_port_range = re.match(r'^(?:[1-9]\d{0,4}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5]|65535)\-(?:[1-9]\d{0,4}|[1-5]\d{4}|6[0-4]\d{3}|65[0-4]\d{2}|655[0-2]\d|6553[0-5]|65535)$', port_range)
        port_range_list = port_range.split("-")
        start_port = int(port_range_list[0])
        end_port = int(port_range_list[1])

        if 1 <= start_port <= end_port and start_port <= end_port <= 65535:
            print("Start Port:", start_port)
            print("End Port:", end_port)
            break
        
    except:
        pass

print(f"Your port number range is:{start_port}-{end_port}\nYour start port number is:{start_port} \nYour end port number is:{end_port}")

print("-------------------------------------------------------------------------------")
for port in range(start_port, end_port + 1):
    nm_scan = nmap.PortScanner()
    nm_scan.scan(ip_address, str(port))
    all_host = nm_scan.all_hosts()
    hostname = nm_scan[ip_address].hostname()
    state = nm_scan[ip_address].state()
    protocol = nm_scan[ip_address].all_protocols()
    port_status = nm_scan[ip_address]['tcp'][port]['state'] #port
    has_port = nm_scan[ip_address].has_tcp(port) #port
    print(f"port:{port}    status: {port_status}    {has_port}                                             |")
print("-------------------------------------------------------------------------------\n")

print(f"Addtional Information:\n Host: {all_host} ({hostname})\nState: {state}\nProtocol: {protocol}\n")

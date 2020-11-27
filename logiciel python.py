print("""

   _____  .__  .__
  /  _  \ |  | |  | _____    ____\n
 /  /_\  \|  | |  | \__  \  /    \ \n
/    |    \  |_|  |__/ __ \|   |  \ \n
\____|__  /____/____(____  /___|  /\n
        \/               \/     \/\n

""")

def main():
    n = input("1- Scanner le reseau\n2- Detecter les Failles\n3- Exploiter les Failles\n4- Veuiller chosir un Programs")

    if n == '1':
        nmap()
    if n == '2':
        vuln()
    if n == '3':
        os.system('msfconsole')
    else:
        print("Choisi ton Program.")

def nmap():
    print("********************Bienvenue dans le Scanner********************")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    ip = input("\nEntrer une Ip Valide ou un Host")
    sc.scan(ip , '1-1O24')
    print(sc.scaninfo())
    print(sc[ip]('tcp').keys())

def vuln():
    print("********************Bienvenue dans le scanner de Vulnérabiliter********************")
    print("*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
    ip = input("\nEntrer une Ip Valide ou un Host")
    print(os.system('nmap -sV --script=vulscan.nse ' +ip))

if __name__ == "__main__":
    main()

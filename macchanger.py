import argparse
import subprocess #Para ejecutar comandos a nivel de sistema, cambio de MAC
import re

def get_arguments():
    parser = argparse.ArgumentParser(description="Herramienta para cambiar la dirección MAC de una interfaz de red")
    parser.add_argument("-i", "--interface", required=True, dest="interface", help="Nombre de la interfaz de red")
    parser.add_argument("-m", "--mac", required=True, dest="mac_address", help="Nueva dirección MAC para la interfaz de red")
    
    return parser.parse_args()

def is_valid_input(interface, mac_address):
    is_valid_interface = re.match(r'^[e][n|t][s|h]\d{1,2}$', interface) #Aplicamos una expresión regex sobre interface para comprobar que sea una interfaz válida (LINUX)
    is_valid_mac_address = re.match(r'^([A-Fa-f0-9]{2}[:]){5}[A-Fa-f0-9]{2}$', mac_address)

    return is_valid_mac_address and is_valid_interface

def change_mac_address(interface, mac_address):

    if is_valid_input(interface, mac_address):
        subprocess.run(["ifconfig", interface, "down"])
        subprocess.run(["ifconfig", interface, "hw", "ether", mac_address])
        subprocess.run(["ifconfig", interface, "up"])
    else:
        print("Los datos introducidos son incorrectos")

def main():
    args = get_arguments()
    change_mac_address(args, args.interface, args.mac_address)

if __name__ == '__main__':
    main()
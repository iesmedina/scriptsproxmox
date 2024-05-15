#!/usr/bin/python3
########################################################
##                                                    ##
## SCRIPT PARA CREAR LOS BRIDGES NECESARIOS           ##
## PARA QUE LOS ALUMNOS PUEDAN TENER UN CONTENEDOR    ##
## ROUTER                                             ##
##                                                    ##
## PBR: Abrirá el fichero de configuración,           ##
##      con el inicio y final proporcionado compone   ##
##      la línea que se debe añadir al fichero de     ##
##      y modifica dicho fichero.                     ##
##                                                    ##
##  PARÁMETROS DE ENTRADA:                            ##
##            inicio: número del primer vmbr          ##
##                      a añadir                      ##
##            final: número del último vmbr           ##
##                      a añadir                      ##
##                                                    ##
########################################################

import subprocess

#esta función determina si se ha encontrado la línea "source /etc/network/interfaces.d/* porque hay que escribir antes
def ultimalinea(cadena):
    import re
    patron="source"
    if (re.match(patron,cadena)):
        return True
    else:
        return False


def creabridges(inicio,final):
   
    archivo="/etc/network/interfaces" #archivo de configuración network de proxmox
    bridges=[] #creamos una lista vacía para acoger los bridges que queremos añadir
   
    for n in range(int(inicio),int(final)+1): #este bucle añade a la lista los números de los bridges a añadir
        nombre="vmbr"+str(n)
        bridges.append(nombre)

    try:
        f=open(archivo,'r')
    except FileNotFoundError:
        print("Fichero de configuración no encontrado")

    listalineas=f.readlines() #creamos una lista con el contenido del fichero
    f.close

    try:
        f=open(archivo,'w')
    except FileNotFoundError:
        print("Ocurrió un error al crear el fichero de configuración")
 
   #escribimos todas las líneas menos la última
    for linea in listalineas: 
        if not ultimalinea(linea):
            f.write(linea)
      
   #escribimos las líneas de los vmbr a crear
    for bridge in bridges: #este bucle recorre la lista , compone la línea a añadir al fichero de configuración y la añade
        texto="\nauto "+bridge+"\niface "+bridge+"\n      bridge-ports none"+"\n      bridge-stp off"+"\n      bridge-fd 0\n"
        f.write(texto)

   #escribimos la última línea
    f.write("\nsource /etc/network/interfaces.d/*")
    f.close()
    subprocess.run(["ifreload","-a"])
    return 0

def main(args):
    return 0

if __name__=='__main__':
    import sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("inicio",
                        type=int,
                        help="número del primer bridge del rango")
    parser.add_argument("final",
                        type=int,
                        help="número del último bridge del rango")
    args=parser.parse_args()
    creabridges(args.inicio,args.final)
    sys.exit(main(sys.argv))

#!/usr/bin/python3
########################################################
##                                                    ##
## SCRIPT PARA CREAR USUARIOS ALUMNADO                ##
## DE FORMA MASIVA                                    ##
##                                                    ##
## PBR: Recorrerá línea a línea el archivo de texto   ##
##      que contine el listado de usuarios a crear.
##      Creará y asignará los pool para cada usuario. ##
##      Por último añadirá las máquinas a los pools.  ##
##                                                    ##
##  PARÁMETROS DE ENTRADA: 
##            usuarios: nombre del fichero texto      ##
##                      que contine la lista de       ##
##                      usuarios.
##            máquinas: nombre del fichero texto      ##
##                         que contine las máquinas   ##
##                         a crear                    ##
##
########################################################
from Creausuario import creausuario
from Creapool import creapool
from Creamaquina import creamaquina
def main(args):
    archivo="/etc/network/interfaces"
    bridges=[] #creamos una lista vacía para acoger los bridges
    inicio=args[1]
    final=args[2]
    print(type(inicio))
    try:
       f=open(archivo,'a')
    except FileNotFoundError:
        print("Fichero de datos no encontrado")
    for n in range(int(inicio),int(final)+1):
        nombre="vmbr"+str(n)
        bridges.append(nombre)

    for bridge in bridges:
        texto="\nauto "+bridge+"\niface "+bridge+"\n      bridge-ports none"+"\n      bridge-stp off"+"\n      bridge-fd 0"
        f.write(texto)
    f.close()
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
    sys.exit(main(sys.argv))

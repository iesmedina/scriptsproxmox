#!/usr/bin/python3

##########################################################
##          FUNCIÓN QUE BORRA UNA MV                   ###
##                                                     ###
##  PARÁMETROS DE ENTRADA                              ###
##    maquina: id de la máquina a borra                ###

##                                                     ###
##########################################################

import subprocess
def borramaquina(IDmaquina):
    
    #borramos la máquina con el id
    #esto es una chapuza pero no encuentro cómo saber si un id es de una máquina
    #o de un contenedor así que lo intento primero como máquina y luego como contenedor
    
    #orden=subprocess.run(["pct list|grep "+IDmaquina],stdout=subprocess.PIPE)
    #cambiar las dos siguientes líneas a como están en la imagen del móvil
    orden=subprocess.run(["pct","list"],stdout=subprocess.PIPE)
    salida=subprocess(["grep",IDmaquina],stdin=orden.stdout,stdout=subprocess.PIPE)
    #salida=orden.stdout
    #salida=salida.decode('UTF-8')
    if(salida.stdout==""):
        print("es una maquina")
    else:
        print("Es un contenedor")
    #subprocess.run(["qm","stop",IDmaquina])
    #subprocess.run(["pct","stop",IDmaquina])
    #subprocess.run(["qm","destroy",IDmaquina,"--purge"])
    #subprocess.run(["pct","destroy",IDmaquina,"--purge"])
    
    return 0

def main(args):
    return 0

if __name__=='__main__':
    import sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("maquina",
                        type=str,
                        help="ID de la máquina a borrar")
    args=parser.parse_args()
    borramaquina(args.maquina)
    sys.exit(main(sys.argv))


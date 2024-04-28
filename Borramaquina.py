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
    subprocess.run(["qm","destroy",IDmaquina,"--purge"])
    subprocess.run(["pct","destroy",IDmaquina,"--purge"])
    
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


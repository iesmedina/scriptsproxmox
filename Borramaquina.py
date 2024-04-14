#!/usr/bin/python3

##########################################################
##          FUNCIÓN QUE BORRA UNA MV                   ###
##                                                     ###
##  PARÁMETROS DE ENTRADA                              ###
##    usuario: nombre de usuario                       ###
##    maquinas: fichero de texto con el listado de     ###
##              máquinas a crear                       ###
##                                                     ###
##########################################################

import subprocess
def borramaquina(IDmaquina):
    
    #borramos la máquina con el id
    subprocess.run(["qm","destroy",IDmaquina,"--purge"])
    
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


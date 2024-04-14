#!/usr/bin/python3

################################################
##  FUNCIÓN QUE CREA UN USUARIO PVE PROXMOX  ###
##                                           ###
##  PARÁMETROS DE ENTRADA                    ###
##    usuario: nombre de usuario             ###
##    password: contraseña                   ###
##                                           ###
################################################

import subprocess
def borrausuario(nombre):
    nombre=nombre+"@pve"
    orden=subprocess.run(["pveum","userdel",nombre])
    return 0
def main(args):
    return 0

if __name__=='__main__':
    import sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("nombre",
                         type=str,
                         help="Nombre de usuario PVE")
    
    args=parser.parse_args()
    borrausuario(args.nombre)
    sys.exit(main(sys.argv))


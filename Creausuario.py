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
def creausuario(nombre,password,grupo):
    nombre=nombre+"@pve"
    orden=subprocess.run(["pveum","useradd",nombre,"-G",grupo])
    orden=subprocess.run(["pvesh","set","/access/password","--userid",nombre,"--password",password])
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
    parser.add_argument("password",
                         type=str,
                         help="Contraseña del usuario")
    parser.add_argument("grupo",
                        help="Grupo al que pertenece")
    args=parser.parse_args()
    creausuario(args.nombre,args.password,args.grupo)
    sys.exit(main(sys.argv))


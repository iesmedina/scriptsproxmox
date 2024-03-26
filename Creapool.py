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
def creapool(nombre):
    pool="pool_"+nombre
    ruta="/pool/"+nombre
    orden=subprocess.run(["pvesh","create","pools","--poolid",pool])
    orden=subprocess.run(["pvesh","set","/access/acl","--path",ruta,"--roles","PVEAdmin","--users",nombre+"@pve"])
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
    creapool(args.nombre)
    sys.exit(main(sys.argv))


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
def creapool(nombre,rol):
    
    #componenmos el nombre del pool
    pool="pool_"+nombre
    #componemos la ruta del pool
    ruta="/pool/"+nombre
    #creamos el pool
    print("Creación del pool "+pool)
    subprocess.run(["pvesh","create","pools","--poolid",pool])
    #le damos el permiso al usuario sobre el pool
    #subprocess.run(["pvesh","set","/access/acl","--path",ruta,"--roles","PVEAdmin","--users",nombre+"@pve"])
    subprocess.run(["pveum","acl","modify","/pool/"+pool+"/","--users",nombre+"@pve","--roles",rol])
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
    parser.add_argument("rol",
                        type=str,
                        help="Rol a asignar")
    args=parser.parse_args()
    creapool(args.nombre,args.rol)
    sys.exit(main(sys.argv))


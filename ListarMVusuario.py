#!/usr/bin/python3

###############################################################################
##  FUNCIÓN QUE MUESTRA LAS MÁQUINAS DE UN USUARIO PVE PROXMOX              ###
##                                                                          ###
##  PBR: El script recorrerá las líneas del archivo de configuración        ###
##       de proxmox que tiene asociados los usuarios a sus pool y a sus     ###
##       máquinas. Cuando localice la línea del usuario a mostrar, extraerá ###
##       el ID de sus máquinas y las muestra.                               ###
##                                                                          ###
##  PARÁMETROS DE ENTRADA                                                   ###
##    usuario: nombre de usuario                                            ###
##                                                                          ###
##                                                                          ###
###############################################################################

import subprocess

def listarMVusuario(nombre):
    #componenmos el nombre del pool
    pool="pool_"+nombre

    #Abrimos el archivo de configuración y buscamos las líneas donde se almacenan el id
    #de las máquinas del usuario
    try:
        f=open("/etc/pve/user.cfg",'r')
    except FileNotFoundError:
        print("No se ha podido localizar el archivo de configuración")
    for linea in f:
        linea=linea.rstrip()
        if linea!='':# nos saltamos las líneas vacías
            valores=linea.split(":")
            
            if valores[1]==pool : #localizamos el pool de ese usuario
                maquinas=valores[3].split(',') #creamos una lista con las máquinas de este usuario
                print("Máquinas virtuales de "+nombre+"...")
                for maquina in maquinas:
                    print(maquina)
                
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
    listarMVusuario(args.nombre)
    sys.exit(main(sys.argv))


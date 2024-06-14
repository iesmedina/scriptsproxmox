#!/usr/bin/python3

###############################################################################
##  FUNCIÓN QUE MUESTRA LAS MÁQUINAS DE TODOS USUARIO PVE PROXMOX           ###
##                                                                          ###
##  PBR: El script recorrerá las líneas del archivo de configuración        ###
##       de proxmox que tiene asociados los usuarios a sus pool y a sus     ###
##       máquinas. Por cada usuario mostrará sus MV                         ###
##                                                                          ###
##                                                                          ###
##                                                                          ###
###############################################################################

import subprocess

def listaMVtodos():

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
            if valores[0]=='pool':
                maquinas=valores[3].split(',') #creamos una lista con las máquinas de este usuario
                print("Máquinas virtuales de "+valores[1]+"...")
                for maquina in maquinas:
                    print(maquina)

    return 0

def main(args):
    return 0

if __name__=='__main__':
    import sys
    listaMVtodos()
    sys.exit(main(sys.argv))


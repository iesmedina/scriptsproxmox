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
from ListarMVusuario import listarMVusuario
def listarMVgrupo(grupo):

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
            if valores[0]=='group' and valores[1]==grupo: #hemos encontrado el grupo
                miembros=valores[2].split(',') #creamos una lista para los miembros del grupo

                for usuario in miembros:
                    nombre=usuario.split('@')[0] #le quitamos @pve
                    
                    listarMVusuario(nombre)
            
    return 0

def main(args):
    return 0

if __name__=='__main__':
    import sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("grupo",
                        type=str,
                        help="Grupo del cual se quieren mostrar las máquinas")
    args=parser.parse_args()
    listarMVgrupo(args.grupo)
    sys.exit(main(sys.argv))


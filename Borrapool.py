#!/usr/bin/python3

###############################################################################
##  FUNCIÓN QUE BORRA LAS MÁQUINAS Y EL POOL DE UN USUARIO PVE PROXMOX      ###
##                                                                          ###
##  PBR: El script recorrerá las líneas del archivo de configuración        ###
##       de proxmox que tiene asociados los usuarios a sus pool y a sus     ###
##       máquinas. Cuando localice la línea del usuario a borrar extraerá   ###
##       el ID de sus máquinas y las borrará.                               ###
##       Podría ser más eficaz que ya que hace el recorrido borrara a todos ###
##       pero perdemos la posibilidad de usuarlo para borrar solo a un      ###
##       usuario. Creo que si no tarda mucho la ejecución masiva, es mejor  ###
##       dejarlo así.                                                       ###
##                                                                          ###
##  PARÁMETROS DE ENTRADA                                                   ###
##    usuario: nombre de usuario                                            ###
##                                                                          ###
##                                                                          ###
###############################################################################

import subprocess
from Borramaquina import borramaquina
def borrapool(nombre):
    
    
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
                print("Borrando máquinas virtuales de "+nombre+"...")
                for maquina in maquinas:
                    borramaquina(maquina)
                #una vez borradas las máquinas podemos borrar el pool
                print("Borrando el pool /pool/"+pool+"...")
                subprocess.run(["pvesh","delete","/pools/"+pool])
               
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
    borrapool(args.nombre)
    sys.exit(main(sys.argv))


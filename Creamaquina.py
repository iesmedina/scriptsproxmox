#!/usr/bin/python3

##########################################################
##  FUNCIÓN QUE CREA UNA MV BASADA EN UNA PLANTILLA    ###
##                                                     ###
##  PARÁMETROS DE ENTRADA                              ###
##    usuario: nombre de usuario                       ###
##    maquinas: fichero de texto con el listado de     ###
##              máquinas a crear                       ###
##                                                     ###
##########################################################

import subprocess
def creamaquina(usuario,maquinas):
    
    #componenmos el nombre del pool
    pool="pool_"+usuario

    try:
        f=open(maquinas,'r')
    except FileNotFoundError:
        print("Fichero de datos no encontrado")
    for linea in f: #recorremos las líneas del fichero que contiene las máquinas
        linea=linea.rstrip() #eliminamos el salto de línea
        
        #extraemos los datos de la línea: id de la plantilla a clonar y nombre de máquina a crear
        valores=linea.split(',')
        idplantilla=valores[0]
        nombremaquina=valores[1]
        
        #caculamos el próximo id de máquina
        orden=subprocess.run(["pvesh","get","cluster/nextid"],stdout=subprocess.PIPE)
        idmaquina=orden.stdout #recogemos la salida de la orden
        idmaquina=idmaquina.decode('UTF-8') #transformamos la salida a tipo str
        idmaquina=idmaquina.rstrip() #quitamos el salto de línea del final de la cadena
        
        #creamos la máquina
        print("Creando máquina "+nombremaquina+" para "+usuario)
        subprocess.run(["pvesh","create","/nodes/pve/qemu/"+idplantilla+"/clone","--pool="+pool,"--newid",idmaquina,"--name",nombremaquina,"--full"])
    
    return 0

def main(args):
    return 0

if __name__=='__main__':
    import sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("usuario",
                         type=str,
                         help="Nombre de usuario PVE")
    parser.add_argument("maquinas",
                        type=str,
                        help="Fichero con las máquinas a crear")
    args=parser.parse_args()
    creamaquina(args.usuario,args.maquinas)
    sys.exit(main(sys.argv))


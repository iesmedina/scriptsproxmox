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
    for linea in f:
        linea=linea.rstrip() #eliminamos el salto de línea
        #extraemos los datos de la línea: id de la plantilla a clonar y nombre de máquina a crear
        valores=linea.split(',')
        idplantilla=valores[0]
        nombremaquina=valores[1]
        
        #caculamos el próximo id de máquina
        orden=subprocess.run(["pvesh","get","cluster/nextid"],stdout=subprocess.PIPE)
        idmaquina=orden.stdout
        idmaquina=idmaquina.decode('UTF-8')
        idmaquina=idmaquina.rstrip() #quitamos el salto de línea del final de la cadena
        print(type(idplantilla),type(pool),type(idmaquina),type(nombremaquina))
        #creamos la máquina
        #orden="pvesh create /nodes/pve/qemu/"+idplantilla+"/clone --pool="+pool+" --newid "+idmaquina+" --name "+nombremaquina+" --full"
        #print(orden)
        #subprocess.run(orden)
        subprocess.run(["pvesh","create","/nodes/pve/qemu/"+idplantilla+"/clone","--pool="+pool,"--newid "+idmaquina,"--name",nombremaquina,"--full"])
    
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


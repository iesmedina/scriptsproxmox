#!/usr/bin/python3
############################################################
##                                                        ##
## SCRIPT PARA CREAR LO CONTENEDORES-ROUTERS              ##
## DE FORMA MASIVA                                        ##
##                                                        ##
## PBR: Recorrerá línea a línea el archivo de texto       ##
##      que contine el listado de usuarios que            ##
##      necesitan un router. Para cada uno clonará        ##
##      el contenedor router y le pondrá la configuración ##
##      correcta.                                         ##
##      IMPORTANTE: los bridges a asignar a cada router   ##
##                  deben estar creados previamente       ##
##                                                        ##
##  PARÁMETROS DE ENTRADA:                                ##
##                                                        ##
##       id del contenedor a clonar (plantilla router)    ##
##                                                        ##
##       usuarios: nombre del fichero texto               ##
##                      que contine la lista de           ##
##                      usuarios.                         ##
##                                                        ##
##       inicio: primer id del rango de bridges a usar    ##
##                                                        ##
##       fin: último id del rango de bridges a usar       ##
##                                                        ##
##                                                        ##
############################################################


import subprocess

def main(args):
    archivo=args[2] #el segundo parámetro es el archivo donde está el alumnado
    plantilla=args[1] #el primer parámetro es el número de la plantilla a clonar
    inicio=args[3]
    final=args[4]
    alumnos=[] #creamos una lista donde se guardarán el nombre del alumnado
    bridges=[] #creamos una lista donde se guardarán los bridges
    for n in range(int(inicio),int(final)+1):
        bridge="vmbr"+str(n)
        bridges.append(bridge)

    try:
        f=open(archivo,'r')
    except FileNotFoundError:
        print("Fichero de datos no encontrado")
    for linea in f:
        linea=linea.rstrip() #eliminamos el salto de línea
        valores=linea.split(",") #segmentamos la cadena separando por , split devuelve una lista
        nombre="al_"+valores[0] #añadimos al nombre el sufijo al_ que corresponde al alumnado
        alumnos.append(nombre)
    f.close()
    if len(bridges)!=len(alumnos):
        print("El número de alumnos y el número de bridges no coincide")
    else:
        indice=0 #esta variable controlará el bridge que toca asignar
        for alumno in alumnos:

            #calculamos el próximo id de máquina
            orden=subprocess.run(["pvesh","get","cluster/nextid"],stdout=subprocess.PIPE)
            idrouter=orden.stdout #recogemos la salida de la orden
            idrouter=idrouter.decode('UTF-8') #transformamos la salida a str
            idrouter=idrouter.rstrip() #quitamos el salto de línea del final de la cadena

            #clonamos el contenedor en el pool del alumno
            print("Creando el contenedor router para "+alumno)
            subprocess.run(["pct","clone",plantilla,idrouter,"--pool","pool_"+alumno])

            #asignamos el bridge al contenero
            subprocess.run(["pct","set",idrouter,"-net1","name=eth1,bridge="+bridges[indice]+",firewall=1,ip=10.100.100.1/24"])
            #asignamos permiso sobre el bridge
#pveum acl modify /sdn/zones/localnetwork/vmbr2000 --users al_pepito@pve --roles PVESDNAdmin
            subprocess.run(["pveum","acl","modify","/sdn/zones/localnetwork/"+bridges[indice], "--users", alumno+"@pve","--roles","PVESDNAdmin"])
            indice+=1
    return 0

if __name__=='__main__':
    import sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("plantilla",
                        type=str,
                        help="id del contenedor a clonar")
    parser.add_argument("usuarios",
                        type=str,
                        help="Nombre del archivo que contiene el listado de alumnos")
    parser.add_argument("inicio",
                         type=int,
                         help="primer número del bridge a asignar")
    parser.add_argument("final",
                         type=int,
                         help="final del rango de bridges a asignar")

    args=parser.parse_args()
    sys.exit(main(sys.argv))

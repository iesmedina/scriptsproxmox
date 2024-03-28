#!/usr/bin/python3
########################################################
##                                                    ##
## SCRIPT PARA CREAR USUARIOS ALUMNADO                ##
## DE FORMA MASIVA                                    ##
##                                                    ##
## PBR: Recorrerá línea a línea el archivo de texto   ##
##      que contine el listado de usuarios a crear.
##      Creará y asignará los pool para cada usuario. ##
##      Por último añadirá las máquinas a los pools.  ##
##                                                    ##
##  PARÁMETROS DE ENTRADA: 
##            usuarios: nombre del fichero texto      ##
##                      que contine la lista de       ##
##                      usuarios.
##            máquinas: nombre del fichero texto      ##
##                         que contine las máquinas   ##
##                         a crear                    ##
##
########################################################
from Creausuario import creausuario
from Creapool import creapool
from Creamaquina import creamaquina
def main(args):
    archivo=args[1]
    try:
       f=open(archivo,'r')
    except FileNotFoundError:
        print("Fichero de datos no encontrado")
    for linea in f:
        linea=linea.rstrip() #eliminamos el salto de línea
        valores=linea.split(",") #segmentamos la cadena separando por , split devuelve una lista
        nombre="al_"+valores[0] #añadimos al nombre el sufijo al_ para distinguir al alumnado. Esto facilitará el borrado masivo
        password=valores[1]
        grupo=valores[2]
        #CREAMOS EL USUARIO
        print("Creando usuario "+nombre+"@pve...")
        creausuario(nombre,password,grupo)
        #CREAMOS SU POOL
        creapool(nombre)
        print("Creando máquinas virtuales para "+nombre+"@pve...")
        #CREAMOS SUS MÁQUINAS
        maquinas=args[2]
        creamaquina(nombre,maquinas)
    return 0

if __name__=='__main__':
    import sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("nombre",
                        type=str,
                        help="Nombre del archivo que contiene el listado de alumnos")
    parser.add_argument("maquinas",
                        type=str,
                        help="Nombre del archivo que contiene el listado de máquinas")
    args=parser.parse_args()
    sys.exit(main(sys.argv))

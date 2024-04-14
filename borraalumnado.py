#!/usr/bin/python3
##########################################################
##                                                      ##
## SCRIPT PARA BORRAR USUARIOS ALUMNADO                 ##
## DE FORMA MASIVA                                      ##
##                                                      ##
## PBR: Recorrerá línea a línea el archivo de texto     ##
##      que contine el listado de usuarios a borrar.    ##
##      Para cada alumno, borrará sus máquinas, su pool ##
##      y luego borrará el usuario.                     ##
##                                                      ##
##  PARÁMETROS DE ENTRADA:                              ##
##            usuarios: nombre del fichero texto        ##
##                      que contine la lista de         ##
##                      usuarios.                       ##
##                                                      ##
##                                                      ##
##########################################################

from Borrausuario import borrausuario
from Borrapool import borrapool

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
        
        #Borramos las máquinas y el pool
       
        borrapool(nombre)
       
        #Borramos el usuario
        borrausuario(nombre)
        print("Usuario borrado con éxito")
        
    return 0

if __name__=='__main__':
    import sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("nombre",
                        type=str,
                        help="Nombre del archivo que contiene el listado de alumnos")
    parser.add_argument("-- maquinas",
                        type=str,
                        help="Opcional. Nombre del archivo que contiene el listado de máquinas")
    args=parser.parse_args()
    sys.exit(main(sys.argv))

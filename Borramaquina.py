#!/usr/bin/python3

##########################################################
##          FUNCIÓN QUE BORRA UNA MV                   ###
##                                                     ###
##  PARÁMETROS DE ENTRADA                              ###
##    maquina: id de la máquina a borra                ###

##                                                     ###
##########################################################

import subprocess
def borramaquina(IDmaquina):
    
    #borramos la máquina con el id
    #esto es una chapuza pero no encuentro cómo saber si un id es de una máquina
    #o de un contenedor así que lo intento primero como máquina y luego como contenedor
    
    orden=['pct','list']
    pct=subprocess.Popen(orden,stdout=subprocess.PIPE) #ejecutamos la primera orden y capturamos la salida
    orden=['grep',IDmaquina]
    grep=subprocess.Popen(orden,stdin=pct.stdout,stdout=subprocess.PIPE,encoding='utf-8') #ejecutamos grep pasándoloe como entrada la salida anterior
    pct.stdout.close()
    maquina=grep.communicate()[0] #el método communicate de la ejecución anterior es una tupla y el primer elemento es la cadena encontrada
       
   
    if(maquina==""):
        subprocess.run(["qm","stop",IDmaquina])    
        subprocess.run(["qm","destroy",IDmaquina,"--purge"])    
    else:
        subprocess.run(["pct","stop",IDmaquina])
        subprocess.run(["pct","destroy",IDmaquina,"--purge"])
         
    
    
    return 0

def main(args):
    return 0

if __name__=='__main__':
    import sys
    import argparse
    parser=argparse.ArgumentParser()
    parser.add_argument("maquina",
                        type=str,
                        help="ID de la máquina a borrar")
    args=parser.parse_args()
    borramaquina(args.maquina)
    sys.exit(main(sys.argv))


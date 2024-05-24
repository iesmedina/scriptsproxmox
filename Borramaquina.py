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
    
    # El siguiente código determina si el Id es de una máquina o de un contendor
    # Lo hace sacando un listado de los contenedores (pct list) y buscando el
    # Id de la máquina en él (grep IDmaquina) 
    
    orden=['pct','list']
    pct=subprocess.Popen(orden,stdout=subprocess.PIPE) #ejecutamos la primera orden y capturamos la salida
    orden=['grep',IDmaquina]
    grep=subprocess.Popen(orden,stdin=pct.stdout,stdout=subprocess.PIPE,encoding='utf-8') #ejecutamos grep pasándoloe como entrada la salida anterior
    pct.stdout.close()
    maquina=grep.communicate()[0] #el método communicate de la ejecución anterior es una tupla y el primer elemento es la cadena encontrada
       
    #Si la cadena es vacía es que no se ha encontrado en el listado y es una máquina
    #En caso contrario, es un contendor
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


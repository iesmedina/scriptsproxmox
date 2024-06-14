#!/usr/bin/python3

###############################################################################
##  SCRIPT QUE MUESTRA UN MENÚ CON DISTINTAS FUNCIONALIDADES DE LISTADO     ###
##  DE MÁQUINAS                                                             ###                ###
##  PBR: Muestra el menú y según la opción escogida pide los datos y        ###
##       llama a la función que corresponda                                 ###
##                                                                          ###
##                                                                          ###
##                                                                          ###
##                                                                          ###
###############################################################################

from ListarMVusuario import listarMVusuario
from ListarMVtodos import listarMVtodos
from ListarMVgrupo import listarMVgrupo

def menu():
    print("1- Mostrar las máquinas de un usuario")
    print("2- Mostrar las máquinas de los usuarios de un grupo")
    print("3- Mostrar todas las máquinas de todos los usuarios")
    op=input("Acción a realizar (1,2,3): ")
    return(op)

def listarMV():
    op=menu()
    if(op=='1'):
        usuario=input("Introduzca el nombre del usuario ")
        listarMVusuario(usuario)
    elif(op=='2'):
        grupo=input("Introduzca el nombre del grupo ")
        listarMVgrupo(grupo)
    elif(op=='3'):
        listarMVtodos()

    return 0

def main(args):
    return 0

if __name__=='__main__':
    import sys
    listarMV()
    sys.exit(main(sys.argv))


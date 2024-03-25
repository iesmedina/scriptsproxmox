#!/usr/bin/python3
# ASÍ HAY QUE CONSTRUIR CREAUSUARIO PARA QUE SE PUEDA USAR DESDE CONSOLA Y
# TAMBIÉN SE PODRÍA LLAMAR DESDE OTRO PROGRAMA. ver prueba2.py
def cuadrado(num):
    return(num*num)
def main(args):
    return 0

if __name__ == '__main__':
    import sys
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("numero",
                        type=int, 
                        help="Números de los que desea saber su cuadrado",
                        nargs='?')
    args = parser.parse_args()
    print(cuadrado(args.numero))
    sys.exit(main(sys.argv))

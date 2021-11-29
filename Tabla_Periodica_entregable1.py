"""

Programa desarrollado como primer entregable para el proyeto "Tabla Periodica"

FUTURE DEVELOPERS

Batch 2

@autor: Aaron Merlos Hernandez

"""

def MostrarGrupo(grupo):
    DirGrupos = {
        1: ['H', 'Li', 'Na', 'K', 'Rb', 'Cs', 'Fr'],
        2: ['Be', 'Mg', 'Ca', 'Sr', 'Ba', 'Ra'],
        3: ['Sc', 'Y', 'Lu', 'Lr'],
        4: ['Ti', 'Zr', 'Hf', 'Rf'],
        5: ['V', 'Nb', 'Ta', 'Db'],
        6: ['Cr', 'Mo', 'W', 'Sg'],
        7: ['Mn', 'Tc', 'Re', 'Bh'],
        8: ['Fe', 'Ru', 'Os', 'Hs'],
        9: ['Co', 'Rh', 'Ir', 'Mt'],
        10: ['Ni', 'Pd', 'Pt', 'Ds'],
        11: ['Cu', 'Ag', 'Au', 'Rg'],
        12: ['Zn', 'Cd', 'Hg', 'Cn'],
        13: ['B', 'Al', 'Ga', 'In', 'Tl', 'Nh'],
        14: ['C', 'Si', 'Ge', 'Sn', 'Pb', 'Fl'],
        15: ['N', 'P', 'As', 'Sb', 'Bi', 'Mc'], 
        16: ['O', 'S', 'Se', 'Te', 'Po', 'Lv'],
        17: ['F', 'Cl', 'Br', 'I', 'At', 'Ts'],
        18: ['He', 'Ne', 'Ar', 'Kr', 'Xe', 'Rn', 'Og']
        }
    
    
    if (grupo in DirGrupos) == True:
        lista = list(DirGrupos[grupo])
        print('\nLos elementos del grupo {} son: \n\t{}'.format(grupo, DirGrupos[grupo]))
        while(True):
            elemento = input("Introduzca el simbolo del elemento que quiere consultar: ")
            elemento = elemento.capitalize()
            if (elemento in lista) == True:
                print('\n\t---Informacion sobre el elemento [{}]---'.format(elemento))
                GlosarioElementos(elemento)
                break
            else:
                print("\n EL ELEMENTO '{}' NO SE ENCUENTRA EN EL GRUPO {} DE LA TABLA PERIODICA, INTENTE NUEVAMENTE".format(elemento, grupo))
                
        return False
        
    else: 
        print('\n EL GRUPO {} NO SE ENCUENTRA EN LA TABLA PERIODICA, INTENTE NUEVAMENTE'.format(grupo))
        return True
    
    
def GlosarioElementos(elemento):
    
    DicElementos = {
        'H': ['Hidrogeno', 1.008, -259.1, -252.9, 'Gas', '1s^1', '+-1', 1, 1],
        'Li': ['Litio', 6.941, 180.5, 1342, 'Solid', '[He]2s^1', '+1', 1, 3],
        'Na': ['Sodio', 22.99, 97.8, 883, 'Solid', '[Ne]3s^1', '+1', 1, 11],
        'K': ['Potasio', 39.10, 63.25, 760, 'Solid', '[Ar]4s^1', '+1', 1, 19],
        'Rb': ['Rubidio', 85.47, 38.9, 686, 'Solid', '[Kr]5s^1', '1', 1, 37],
        'Cs': ['Cesio', 132.9, 28.4, 669, 'Solid', '[Xe]6s^1', '+1', 1, 55],
        'Fr': ['Francio', 223, 27, 677, 'Solid', '[Rn]7s^1', '+1', 1, 87],
        'Be': ['Berilio', 9.012, 1278, 2970, 'Solid', '[He]2s^2', '2', 2, 4],
        'Mg': ['Magnesio', 24.31, 649, 1090, 'Solid', '[Ne]2s^2', '+2', 2, 12],
        'Ca': ['Calcio', 40.08, 839, 1484, 'Solid', '[Ar]4s^2', '+2', 2, 20],
        'Sr': ['Estroncio', 87.62, 769, 1384, 'GSolid', '[Kr]5s^2', '+2', 2, 38],
        'Ba': ['Bario', 137.3, 725, 1640, 'Solid', '[Xe]6s^2', '+2', 2, 56],
        'Ra': ['Radio', 226, 7000, 1140, 'Solid', '[Rn]7s^2', '+2', 2, 88],
        'Sc': ['Escandio', 44.96, 1541, 2832, 'Solid', '[Ar]3d^1*4s^2', '+3', 3, 21],
        'Y': ['Itrio', 88.91, 1523, 3337, 'Solid', '[Kr]4d^1*5s^2', '+3', 3, 39],
        'Lu': ['Lutecio', 175.00, 1663, 3402, 'Solid', '[Xe]4f^14*5d^1*6^2', '+3', 2, 71],
        'Lr': ['Laurencio', 262, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*7s^2*7p^1', '+3', 3, 103],
        'Ti': ['Titanio', 47.87, 1660, 3287, 'Solid', '[Ar]3d^2*4s^2', '+4,3,2', 4, 22],
        'Zr': ['Circon', 91.22, 1852, 4377, 'Solid', '[Kr]4d^2*5s^2', '+4', 4, 40],
        'Hf': ['Hafnio', 178.5, 2227, 4600, 'Solid', '[Xe]4f^14*5d^2*6s^2', '+4', 4, 72],
        'Rf': ['Rutherfordio', 267, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^2*7s^2', 'N/A', 4, 104],
        'V': ['Vanadio', 50.94, 1890, 3380, 'Solid', '[Ar]3d^3*4s^2', '+5,2,3,4', 5, 23],
        'Nb': ['Niobio', 92.91, 2468, 4742, 'Solid', '[Kr]4d^4*5s^1', '+5,3', 5, 41],
        'Ta': ['Tantalio', 180.9, 2996, 5425, 'Solid', '[Xe]4f^14*5d^3*6s^2', '+5', 5, 73],
        'Db': ['Dubnio', 268, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^3*7s^2', 'N/A', 5, 105],
        'Cr': ['Cromo', 52.00, 1857, 2672, 'Solid', '[Ar]3d^5*4s^1', '+3,2,6', 6, 24],
        'Mo': ['Molibdeno', 95.95, 2617, 4612, 'Solid', '[Kr]ed^5*5s^1', '+6,3,5', 6, 42],
        'W': ['Tungsteno', 183.8, 3410, 5660, 'Solid', '[Xe]4f^14*5d^4*6s^2', '+6,4', 6, 74],
        'Sg': ['Seaborgio', 269, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^4*7s^2', 'N/A', 6, 106],
        'Mn': ['Manganeso', 54.94, 1244, 1962, 'Solid', '[Ar]3d^5*4s^2', '+2,3,4,6,7', 7, 25],
        'Tc': ['Tecnecio', 98.00, 2172, 4877, 'Solid', '[Kr]ed^5*5s^2', '+7,4,6', 7, 43],
        'Re': ['Renio', 186.2, 3180, 5600, 'Solid', '[Xe]4f^14*5d^5*6s^2', '+7,4,6', 7, 75],
        'Bh': ['Bohrio', 270, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^5*7s^2', 'N/A', 7, 107],
        'Fe': ['Hierro', 55.85, 1535, 2750, 'Solid', '[Ar]3d^6*4s^2', '+3,2', 8, 26],
        'Ru': ['Rutenio', 44, 2310, 3900, 'Solid', '[Kr]4d^7*5s^1', '+4,3,6,8', 8, 44],
        'Os': ['Osmio', 190.2, 3045, 5030, 'Solid', '[Xe]4f^14*5d^6*6s^2', '+4,6,8', 8, 76],
        'Hs': ['Hasio', 269, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^6*7s^2', 'N/A', 'N/A', 108],
        'Co': ['Cobalto', 58.93, 1495, 2870, 'Solid', '[Ar]3d^7*4s^2', '+2,3', 9, 27],
        'Rh': ['Rodio', 102.9, 1966, 3727, 'Solid', '[Kr]4d^8*5s^1', '+3,4,6', 9, 45],
        'Ir': ['Iridio', 192.2, 2410, 4130, 'Solid', '[Xe]4f^14*5d^7*6s^2', '+4,3,6', 9, 77],
        'Mt': ['Meitnerio', 278, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^7*7s^2', 'N/A', 'N/A', 109],
        'Ni': ['Niquel', 58.69, 1453, 2730, 'Solid', '[Ar]3d^8*4s^2', '+2,3', 2, 28],
        'Pd': ['Paladio', 106.4, 1554, 3140, 'Solid', '[Kr]4d^10', '+2,4', 10, 46],
        'Pt': ['Platino', 195.1, 1772, 3827, 'Solid', '[Xe]4f^14*5d^9*6s^1', '+4,2', 2, 78],
        'Ds': ['Darmstatio', 'N/A', 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^9*7s^1', 'N/A', 'N/A', 110],
        'Cu': ['Cobre', 63.55, 1083, 2567, 'Solid', '[Ar]3d^10*4s^1', '+2,1', 1, 29],
        'Ag': ['Plata', 107.9, 962, 2212, 'Solid', '[Kr]4d^10*5s^1', '+1', 1, 47],
        'Au': ['Oro', 197.00, 1064, 3080, 'Solid', '[Xe]4f^14*5d^10*6s^1', '+3,1', 1, 79],
        'Rg': ['Roentgenio', 281, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^10*7s^1', 'N/A', 'N/A', 111],
        'Zn': ['Cinc', 65.38, 419.6, 906, 'Solid', '[Ar]3d^2*4s^2', '+2', 2, 30],
        'Cd': ['Cadnio', 112.4, 320.9, 765, 'Solid', '[Kr]4d^10*5s^2', '+2', 2, 48],
        'Hg': ['Mercurio', 200.6, -38.9, 357, 'Liquid', '[Xe]4f^14*5d^10*6s^2', '+2,1', 2, 80],
        'Cn': ['Copernico', 285, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^10*7s^2', 'N/A', 'N/A', 112],
        'B': ['Boro', 10.81, 2079, 2550, 'Solid', '[He]2s^2*2p^1', '+3', 3, 5],
        'Al': ['Aluminio', 26.98, 660, 2467, 'Solid', '[Ne]3s^2*3p^1', '+3', 3, 13],
        'Ga': ['Galio', 69.72, 29.8, 2403, 'Solid', '[Ar]3d^10*4s^2*2p^1', '+3', 3, 31],
        'In': ['Indio', 114.8, 156.6, 2080, 'Solid', '[Kr]4d^10*5s^2*5p^1', '+3', 3, 49],
        'Tl': ['Talio', 204.4, 303, 1457, 'Solid', '[Xe]4f^14*5d^10*6s^2*6p^1', '+1,3', 3, 81],
        'Nh': ['Nihonio', 286, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^10*7s^2*7p^1', 'N/A', 'N/A', 113],
        'C': ['Carbono', 12.01, 3367, 4827, 'Solid', '[He]2s^2*2p^2', '+-4', 4, 6],
        'Si': ['Silicio', 28.09, 1410, 2355, 'Solid', '[Ne]3s^2*3p^2', '+-4', 4, 14],
        'Ge': ['Germanio', 72.63, 947.4, 2830, 'Solid', '[Ar]3d^10*4s^2*4p^2', '+4,2', 4, 32],
        'Sn': ['Estaño', 118.7, 232, 2270, 'Solid', '[Kr]4d^10*5s^2*5p^2', '+4,2', 4, 50],
        'Pb': ['Plomo', 207.2, 327.5, 1740, 'Solid', '[Xe]4f^14*5d^10*6s^2*6p^2', '+2,4', 4, 82],
        'Fl': ['Flerovio', 289, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^10*7s^2*7p^2', 'N/A', 'N/A', 114],
        'N': ['Nitrogeno', 14.01, -209.9, -195.8, 'Gas', '[He]2s^2*2p^3', '-3', 5, 7],
        'P': ['Fosforo', 30.97, 44.1, 280, 'Solid', '[Ne]3s^2*3p^3', '-3', 5, 15],
        'As': ['Arsenico', 74.92, 817, 617, 'Solid', '[Ar]3d^10*4s^2*4p^3', '+-3,+5', 5, 33],
        'Sb': ['Antimonio', 121.8, 631, 1950, 'Solid', '[Kr]4d^10*5s^2*5p^3', '+3,5', 5, 51],
        'Bi': ['Bismuto', 209.00, 271, 1560, 'Solid', '[Xe]4f^14*5d^10*6s^2*6p^3', '+3,5', 5, 83],
        'Mc': ['Moscovio', 289, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^10*7s^2*7p^3', 'N/A', 'N/A', 115],
        'O': ['Oxigeno', 16.00, -218.4, -183, 'Gas', '[He]2s^2*2p^4', '-2', 6, 8],
        'S': ['Azufre', 32.07, 112.8, 444.7, 'Solid', '[Ne]3s^2*3p^4', '-2', 6, 16],
        'Se': ['Selenio', 78.97, 217, 685, 'Solid', '[Ar]3d^10*4s^2*4p^4', '+4,-2,+6', 6, 34],
        'Te': ['Telurio', 127.6, 449.5, 989.8, 'Solid', '[Kr]4d^10*5s^2*25p^4', '+4,6,-2', 6, 52],
        'Po': ['Polonio', 209, 254, 962, 'Solid', '[Xe]4f^14*5d^10*6s^2*6p^4', '+4,2', 6, 84],
        'Lv': ['Livermorio', 293, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^10*7s^2*7p^4', 'N/A', 'N/A', 116],
        'F': ['Fluorita', 19.00, -219.8, -188.1, 'Gas', '[He]2s^2*2p^5', '-1', 7, 9],
        'Cl': ['Cloro', 35.45, -101, -34.6, 'Gas', '[Ne]3s^2*3p^5', '-1', 7, 17],
        'Br': ['Bromo', 79.90, -7.2, 58.8, 'Liquid', '[Ar]3d^10*4s^2*4p^5', '+-1,+5', 7, 35],
        'I': ['Yodo', 126.9, 113.5, 184, 'Solid', '[Kr]4d^10*5s^2*5p^5', '-1,+5,7', 7, 53],
        'At': ['Astato', 210, 302, 337, 'Solid', '[Xe]4f^14*5d^10*6s^2*6p^5', '±1,3,5,7', 7, 85],
        'Ts': ['Teneso', 294, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^10*7s^2*7p^5', 'N/A', 'N/A', 117],
        'He': ['Helio', 4.0026, -272.2, -268.9, 'Gas', '1s^2', '0', 2, 2],
        'Ne': ['Neon', 20.18, -248, -248.7, 'Gas', '[He]2s^2*2p^6', '0', 8, 10],
        'Ar': ['Argon', 39.95, -189.2, -185.7, 'Gas', '[Ne]3s^2*3p^6', '0', 8, 18],
        'Kr': ['Cripton', 83.80, -157, -152, 'Gas', '[Ar]3d^10*4s^2*4p^6', '0', 8, 36],
        'Xe': ['Xenon', 131.3, -111.8, -107.1, 'Gas', '[Kr]4d^10*5s^2*5p^6', '0', 8, 54],
        'Rn': ['Radon', 222, -71, -61.8, 'Gas', '[Xe]4f^14*5d^10*6s^2*6p^6', '0', 8, 86],
        'Og': ['Oganeson', 294, 'N/A', 'N/A', 'N/A', '[Rn]5f^14*6d^10*7s^2*7p^6', 'N/A', 'N/A', 118],
        }
    
    lista_info = list(DicElementos[elemento])
    print('\n\tNombre: {}\n\tPeso atomico: {}\n\tPunto de fusion: {}°C\
          \n\tPunto de ebullicion: {}°C\n\tFase a temperatura y presion estandar: {}\
          \n\tConfiguracion electronica: {}\n\tEstados de oxidacion comunes: {}\
          \n\tNumero de electrones de valencia: {}\n\tNumero atomico: {}'.format(
          lista_info[0], lista_info[1], lista_info[2], lista_info[3], lista_info[4], lista_info[5], 
          lista_info[6], lista_info[7], lista_info[8]))
    return ''
    

if  __name__ ==  '__main__':
    
   print("\n\n\t\t**TABLA PERIODICA INTERACTIVA***\n")
   salida = 'Y'
   
   while(salida.upper() == 'Y'):
       GrupoInvalido = True
       while (GrupoInvalido):

           grupo = input("Introduzca el numero de grupo a consultar de la tabla periodica: ")
           try:
               grupo =int(grupo)
               GrupoInvalido = MostrarGrupo(grupo)
           except Exception: #si falla por alguna causa continua con el flujo
               print("\n '{}' NO ES UN NUMERO, INTENTE NUEVAMENTE ".format(grupo))
           
       salida = input("\nIntroduzca la letra [Y] para realizar otra consulta y cualquier otro caracter para salir del programa:  ")
   print('\nSaliendo...')
   
   

   
   
   
   
   
   
   
   
   
   
   
   
   

#-*- coding:utf-8 -*-
'''
Created on 21 nov. 2020

@author: granl
'''


from Pokemon import *


print('Proyecto sobre pokemon 6vs6')

#Ejercicio 1
r_pokemon=leer_pokemon('../data/Smogon.csv')
print('\nNúmero de registros leídos:', len(r_pokemon))
print('Los tres primeros registros son:', r_pokemon[:3])
print('Los tres últimos registros son:', r_pokemon[-3:])


#Ejercicio 2
print('\nEste es el ejercicio 2, donde vamos a filtrar los pokémon por sus tipos. Los pokemon pueden tener dos o un tipo.')
print('\nLos pokémon tienen estos tipos: bug, dark, dragon, electric, fairy, fighting, fire, flying, ghost, grass, ground, ice, normal, poison, psychic, rock, steel y water.')
tipo1=input('Elige el primer tipo:' )
tipo2=input('Elige el segundo tipo:' )
tipo_1=tipo1.capitalize()
tipo_2=tipo2.capitalize()
poke=filtrar_por_tipos(r_pokemon,tipo_1,tipo_2)
if len(poke) < 1:
    print('No existe ningún Pokémon con esa combinación de tipos.')
else:
    if tipo_2=='': tipo_2 = 'dos no tiene'
    print('\nEl número de pokémon con tipo',tipo_1, 'y el tipo', tipo_2, 'son:', len(poke))
    print('Los tres primeros pokémon con el tipo',tipo_1,'y el tipo', tipo_2,'son:', poke[:3])
    print('Los tres últimos pokémon con el tipo',tipo_1, 'y el tipo', tipo_2,'son:', poke[-3:])


#Ejercicio 3
print('\nEste es el ejercicio 3, aquí te pedimos que nos digas si quieres un pokemon legendario o no y si quieres que sea mego o no. Para indicarlo pon true o false')
legen=input('Pon si quieres que sea legendario:' )
mega=input('Pon si quieres que sea mega:' )
legendario=legen.upper()
megas=mega.upper()
list_poke=obtener_pokemon(r_pokemon,legendario,megas)
print('\nEl número de pokémon con el legendario',legendario, 'y la mega', megas, 'son:', len(list_poke))
print('Los tres primeros pokémon con el legendario',legendario,'y la mega', megas,'son:', list_poke[:3])
print('Los tres últimos pokémon con el legendario',legendario, 'y la mega', megas,'son:', list_poke[-3:])


#Ejercicio 4
print('\nEste es el ejercicio 4, vamos a calcular la media de los puntos de vida, ataque, defensa, ataque especial, defensa especial y velocidad.')
print('Los pokémon tienen estos tipos: bug, dark, dragon, electric, fairy, fighting, fire, flying, ghost, grass, ground, ice, normal, poison, psychic, rock, steel y water.')
tipo1=input('Elige el primer tipo:' )
tipo2=input('Elige el segundo tipo:' )
tipo_1=tipo1.capitalize()
tipo_2=tipo2.capitalize()
media_puntos=media_de_puntos(r_pokemon,tipo_1,tipo_2)
if len(media_puntos) < 1:
    print('No existe ningún Pokémon con esa combinación de tipos.')
else:
    if tipo_2=='': tipo_2 = 'dos no tiene'
    print(f'La media de los puntos de los pokemon de tipo {tipo_1} y de tipo {tipo_2} son: de vida {media_puntos[0]}, de ataque {media_puntos[1]}, \nde defensa {media_puntos[2]}, de ataque especial {media_puntos[3]}, de defensa especial {media_puntos[4]} y de velocidad {media_puntos[5]}.')
    

#Ejercicio 5
print('\nEste es el ejercicio 5, vamos a calcular la media de los puntos totales dependiendo de su tier. Los tiers son: AG, BL, BL2, BL3, BL4, NU, OU, PU, RU, Uber, UU.')
tier=input('Pon el tier del que quieres saber la media de sus puntos totales:' )
media=media_total_de_tiers(r_pokemon,tier)
print('La media de los puntos totales del tier', tier, 'es:', media)
    

#Ejercicio 6
print('\nEste es el ejercicio 6, en este ejercicio te vamos ha decir los pokémon con peor ataque.')
limite=int(input('Pon cuantos pokémon quieres ver: '))
peor=obtener_pokemon_peor_ataque(r_pokemon,limite)
print(f'Los {limite} Pokémon con peor ataque son: {peor}')


#Ejercicio 7
print('\nEste es el ejercicio 7, vamos hacer una lista con los pokemon con mayor puntos totales, dependiendo de su tier. Los tiers son: AG, BL, BL2, BL3, BL4, NU, OU, PU, RU, Uber, UU.')
tier=input('Pon el tier:' )
limite=int(input('Pon cuantos pokémon quieres ver: '))
pokemon_con_mejor_puntos=obtener_pokemon_total(r_pokemon,tier,limite)
if len(pokemon_con_mejor_puntos)<1:
    print('Te has equivocado escribiendo el tier.')
else:
    print(f'Los {limite} Pokémon con los mejores puntos totales del tier {tier} son: {pokemon_con_mejor_puntos}')
    

#Ejercicio 8
print('\nEste es el ejercicio 8, en este ejercicio te vamos hacar un diccionario donde nos diga los Pokémon que hay del cada tipo, solo tomando como referencia el primero, según su generación. Las generaciones solo van del 1 al 6.')
gene=int(input('Pon la generación sobre la que quiere hacer el diccionario: '))
if 6>= gene >=1 :
    dicc_pokemon_por_tipo=obtener_diccionario_por_generacion(r_pokemon,gene)
    print(f'El diccionario de la generación {gene} es: {dicc_pokemon_por_tipo}')
else:
    print('Solo hay 6 generaciones, de la primera a la sexta.')
    

#Ejercicio 9
print('\nEste es el ejercicio 9, vamos hacer un diccionario donde nos diga una tupla con los nombre y la velocidad de los Pokémon, ordenada de mayor a menor por su velocidad. Con la condición de si es legendario o no, para indicarlo hay que poner true o false')
legen=input('Pon si quieres que sea legendario:' )
legendario=legen.upper()
pokemon_con_mejor_velocidad=Obtener_diccionario_por_tier(r_pokemon,legendario)
if len(pokemon_con_mejor_velocidad)<1:
    print('No has escrito bien true o false')
else:
    print(f'Los Pokémon con las mejores velocidades según su tier son: {pokemon_con_mejor_velocidad}')


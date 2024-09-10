#-*- coding:utf-8 -*-
'''
Created on 21 nov. 2020

@author: granl
'''

import csv
from collections import namedtuple
RegistroPokemon = namedtuple('Pokémon', 'n_pokedex,name,type1,type2,total,hp,atk,defe,sp_atk,sp_defe,spe,gene,legen,mega,tier')


def leer_pokemon (fichero):
    res=list()
    with open(fichero, 'rt', encoding='utf-8') as f:
        registros=csv.reader(f)
        next(registros)
        for registro in registros:
            res.append(RegistroPokemon(int(registro[0]),registro[1],registro[2],registro[3],int(registro[4]),int(registro[5]),int(registro[6]),int(registro[7]),int(registro[8]),int(registro[9]),int(registro[10]),int(registro[11]),registro[12],registro[13],registro[14]))
    return res

def filtrar_por_tipos(pokemon,tipo1,tipo2=''):
    return [r for r in pokemon if r.type1==tipo1 and r.type2==tipo2]

def obtener_pokemon(pokemon,legen,mega):
    if legen=='TRUE' and mega=='TRUE':
        return[(r.name,r.gene,r.tier) for r in pokemon if (r.legen==legen and r.mega==mega)]
    elif legen=='TRUE' and mega=='FALSE':
        return[(r.name,r.gene,r.tier) for r in pokemon if (r.legen==legen and r.mega==mega)]
    elif legen=='FALSE' and mega=='FALSE':
        return[(r.name,r.gene,r.tier) for r in pokemon if (r.legen==legen and r.mega==mega)]
    elif legen=='FALSE' and mega=='TRUE':
        return[(r.name,r.gene,r.tier) for r in pokemon if (r.legen==legen and r.mega==mega)]
    else:
        print('Error, solo puedes poner en los campos, true o false')

def media_de_puntos(pokemon,tipo1,tipo2=''):
    puntos=[(p.hp,p.atk,p.defe,p.sp_atk,p.sp_defe,p.spe) for p in pokemon if p.type1==tipo1 and p.type2==tipo2]
    media=len(puntos)
    if media<1:
        res=[]
    else:
        res=list()
        vida=sum([punto[0] for punto in puntos]) 
        res.append(vida/media)
        ataque=sum([punto[1] for punto in puntos])
        res.append(ataque/media)
        defensa=sum([punto[2] for punto in puntos])
        res.append(defensa/media)
        sp_atk=sum([punto[3] for punto in puntos])
        res.append(sp_atk/media)
        sp_defe=sum([punto[4] for punto in puntos])
        res.append(sp_defe/media)
        spe=sum([punto[5] for punto in puntos])
        res.append(spe/media)
    return res     
            
def media_total_de_tiers(pokemon,tier):
    media=0
    aux=[p.total for p in pokemon if p.tier==tier]
    total=len(aux)
    if total < 1:
        return 0
    else:  
        for t in aux:
            media=t+media
    return media/total

def obtener_pokemon_peor_ataque(pokemon,limite):
    aux=[(p.name, p.atk) for p in pokemon]
    return sorted(aux,key=lambda e:e[1])[:limite]
    
def obtener_pokemon_total(pokemon,tier,limite):
    lista_filtrada_por_tier=[(p.name, p.total) for p in pokemon if p.tier==tier]
    if len(lista_filtrada_por_tier)<1:
        return[]
    else:
        return sorted(lista_filtrada_por_tier,key=lambda e:e[1],reverse=True)[:limite]

def obtener_diccionario_por_generacion(pokemon,gene): 
    dicc_pokemon= dict()
    for p in pokemon:
        if p.gene==gene:
            if p.type1 in dicc_pokemon:
                dicc_pokemon[p.type1] += 1
            else:
                dicc_pokemon[p.type1] = 1
    
    return dicc_pokemon

def Obtener_diccionario_por_tier(pokemon,legen):
    aux=[(p.name, p.spe, p.tier) for p in pokemon if p.legen==legen]
    maxima_velocidad= sorted(aux, key=lambda e:e[1], reverse=True)
    dicc_pokemon= dict()
    for m in maxima_velocidad:
        if  m[2] in dicc_pokemon:
            dicc_pokemon[m[2]].append((m[0],m[1]))
        else:
            dicc_pokemon[m[2]] = [(m[0],m[1])]
                
    return dicc_pokemon
    
    

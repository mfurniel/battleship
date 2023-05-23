import creartablero

# Aletario vs Aleatorio

def azar_vs_azar(jugadorIA,jugadorRival):

    while(not jugadorIA.flota_rival_hundida() and not jugadorRival.flota_rival_hundida()):
   
        jugadorIA.aleatoriopero(jugadorRival)

        if(jugadorIA.flota_rival_hundida()):
            print('Gano jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('Perdio jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            break
        elif(jugadorRival.flota_rival_hundida()):
            print('Gano jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('Perdio jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            break
      
        jugadorRival.aleatoriopero(jugadorIA)
     
        if(jugadorIA.flota_rival_hundida()):
            print('Gano jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('Perdio jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            break
        elif(jugadorRival.flota_rival_hundida()):
            print('Gano jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('Perdio jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            break

# Greddy vs Greddy

def greedy_vs_greedy(jugadorIA,jugadorRival):

    while(not jugadorIA.flota_rival_hundida() and not jugadorRival.flota_rival_hundida()):
   
        jugadorIA.greedy(jugadorRival)
        jugadorIA.turnos=jugadorIA.turnos+1
        if(jugadorIA.flota_rival_hundida()):
            print('Gano jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('Perdio jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
        elif(jugadorRival.flota_rival_hundida()):
            print('Gano jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('Perdio jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
      
        jugadorRival.greedy(jugadorIA)
        jugadorRival.turnos=jugadorRival.turnos+1
        if(jugadorIA.flota_rival_hundida()):
            print('Gano jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('Perdio jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
        elif(jugadorRival.flota_rival_hundida()):
            print('Gano jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('Perdio jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break

def greedy_vs_azar(jugadorIA,jugadorRival):

    while(not jugadorIA.flota_rival_hundida() and not jugadorRival.flota_rival_hundida()):
   
        jugadorIA.greedy(jugadorRival)

        if(jugadorIA.flota_rival_hundida()):
            print('Gano jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('Perdio jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
        elif(jugadorRival.flota_rival_hundida()):
            print('Gano jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('Perdio jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
      
        jugadorRival.aleatoriopero(jugadorIA)
     
        if(jugadorIA.flota_rival_hundida()):
            print('Gano jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('Perdio jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
        elif(jugadorRival.flota_rival_hundida()):
            print('Gano jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('Perdio jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break

def huntTarget_vs_huntTarget(jugadorIA,jugadorRival):

    while(not jugadorIA.flota_rival_hundida() and not jugadorRival.flota_rival_hundida()):

        if(jugadorIA.nombre=='IA'):  
            print(jugadorIA.direccion_target) 
            creartablero.imprimirTablero(jugadorIA.tableroBusqueda)
            
        jugadorIA.hunt_target(jugadorRival,'greedy')
        jugadorIA.turnos=jugadorIA.turnos+1

        if(jugadorIA.flota_rival_hundida()):
            print('Gano jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('Perdio jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
        elif(jugadorRival.flota_rival_hundida()):
            print('Gano jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('Perdio jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
      
        jugadorRival.hunt_target(jugadorIA,'greedy')
        jugadorRival.turnos=jugadorRival.turnos+1
     
        if(jugadorIA.flota_rival_hundida()):
            print('Gano jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('Perdio jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
        elif(jugadorRival.flota_rival_hundida()):
            print('Gano jugadorRival en un total de: ',jugadorRival.turnos,' turnos')
            print('Perdio jugadorIA en un total de: ',jugadorIA.turnos,' turnos')
            print('hundidos por IA: ',jugadorIA.cuantos())
            print('hundidos por Rival: ',jugadorRival.cuantos())
            break
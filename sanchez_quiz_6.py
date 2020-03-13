
FILAS = RUR.MAX_X
COLUMNAS = RUR.MAX_Y

"""
Descripción: Reborg gira a la derecha
Pre: Reborg mira hacia el este
Pos: Reborg mira al sur
"""

def turn_right():
    repeat 3:
        turn_left()


"""
Descripción: Reborg gira 180 grados
Pre: Reborg mira hacia el este
Pos: Reborg mira al oeste
"""
        
def turn_180():
    repeat 2:
        turn_left()

"""
Descripción: Reborg sube escalones de forma ascendente a la derecha
Pre: Reborg mira hacia el este (x,y)
Pos: Reborg mira al este (x+1,y+1)
"""        
        
def escalonar():
    agarrar()
    move()
    turn_left()
    move() 
    turn_right()
    agarrar()

"""
Descripción: Reborg agarra objetos
Pre: Reborg no tiene objetos
Pos: Reborg tiene objetos
""" 
    
def agarrar():
    if object_here():
        take()

"""
Descripción: Reborg sube escalones de forma descendente a la derecha
Pre: Reborg mira hacia el sur (x,y)
Pos: Reborg mira al sur (x+1,y-1)
"""         
        
def escalonde():
    agarrar()
    move()
    turn_left()
    move() 
    turn_right()
    agarrar()

"""
Descripción: Reborg sube escalones de forma descendente a la derecha,
tomando objetos, pasa a la esquina izquierda, baja en escalera tomando 
objetos y vuelve a la posicion inicial
Pre: Reborg mira hacia el este (x,y)
Pos: Reborg mira al este (x,y)
"""  
    
def stair():
    cont = 1
    cont2 = 1
    while cont < COLUMNAS:
        escalonar()
        cont += 1
        if wall_in_front():
            turn_180()
    while front_is_clear():
        move()
    turn_left()
    while cont2 < FILAS:
        escalonde()
        cont2 += 1
    turn_right()
    while front_is_clear():
        move()
    turn_180()
    






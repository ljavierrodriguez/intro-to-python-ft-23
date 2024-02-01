""" Loops o Ciclos """

""" 

for value in  collection:
    sentences

"""

for i in range(1, 100, 2): # start = 0, stop = valor a detener, step = 1
    print(i) # 1 3 5 7 9
    
nombres = ["Hugo", "Paco", "Luis"]

for i in range(len(nombres)):
    print(nombres[i])
    
for nombre in nombres:
    print(nombre) # Hugo Paco Luis
    
    
indice = 0
while(indice < len(nombres)):
    print(nombres[indice])
    #indice = indice + 1
    indice += 1
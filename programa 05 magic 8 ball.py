#Programa 05 magic 8 ball
import random
a = input("Haz una pregunta sí o no: ")
lista = ["sí","no","puede que no","seguramente sí","eso está hecho","100% seguro que sí","sinceramente no creo"]
i = random.randint(0,len(lista))
print(lista[i])


x = [1,2,3,4,5,6]
print len(x)

#Dividir las listas
print (x[:3])
# Hasta el 3
#Primeros 3 elementos empezando de 0

print (x[3:])
#Despues del 3
#elementos desde el tercer de la lista hasta el final

print (x[-2:])
#Los ultimos 2 elementos de la lista

x.extend([7,8])
print (x)
#extender la lista agregando otra lista

x.append(9)
print (x)
#agregar valor a la lista

y = [10, 11, 12]
listofList = [x,y]
print (listofList)
#Crear listas con listas dentro de listas

print (y[1])
#imprimir elemnto especifico de la lista

#realizar la funcion de ordenamiento de mayor a menor y luego de menor a myor
z = [3,2,1]
z.sort()
print z

z.sort(reverse=True)
print z

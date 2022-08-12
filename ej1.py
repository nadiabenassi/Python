#1) Ingresar una lista de 10 productos con sus respectivos precios

productos=[] #creamos la lista vacia
precios=[] #creamos la lista vacia
for x in range(10): #pedimos que cargue productos y precios 10 veces
    nom=input("Ingrese el nombre del producto:")
    productos.append(nom) #agrega producto a la lista
    pre=int(input("Ingrese el precio de dicho producto:"))
    precios.append(pre) #agrega precios a la lista
    
#a) Calcular el promedio de todos los precios e imprimirlo por pantalla
suma=0 #contador en 0
x=0
while x<len(precios): 
    suma=suma+precios[x] #la suma será igual a la suma de los elementos de la lista precios
    x=x+1 
    prom=suma/10 #se realiza el promedio entre suma y los 10 elementos de la lista
    

print("El promedio de precios de todos los productos es")   #se imprime el promedio 
print(prom)    


#b) Imprimir el nombre del producto mas caro
mayor=precios[0] #creamos la variable mayor pidiendo que de la lista precios tome el primer elemento 0 suponiendo que es el menor elemento
for x in range(1,11):  
    if precios[x]>mayor: 
        mayor=precios[x] 
        print("Producto mas caro es") #muestra el elemento mayor
        print(mayor) #no me salio mostrar el mayor con el nombre del producto


#c) Imprimir los productos cuyos precios sean mayores a 1000

cantidad=0 #utilizando la misma logica anterior, buscamos si de la lista precios hay elementos que superan el 1000
x=0
while x<len(precios):
    if precios[x]>100:
        cantidad=cantidad+1
    x=x+1
    

print("La cantidad de valores mayores a 1000 en la lista son:") #los mostramos en pantalla
print(cantidad)




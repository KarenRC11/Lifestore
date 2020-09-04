#importacion de las listas de lifestore

from lifestore_file import lifestore_products
from lifestore_file import lifestore_sales
from lifestore_file import lifestore_searches

print("Bienvenido a Lifestore: los mejores productos al mejor precio\n")

#Si eres administrador la contraseña es admin
#Si eres usuario normal la contraseña es user123

#El programa es sensible a mayúsculas y minúsculas, por lo que se debe ingresar todo con minúsculas.

usuario = input("Selecciona una opción: (administrador / usuario) : ")

if usuario == "administrador":
	password = input("Introduce tu contraseña: ")

  #si ingresa su contraseña mas de 2 veces y esta mal, el programa acaba y se debe volver a iniciar 

	if password == "admin":
	  
		print("Puedes acceder")
    #El menú para alguien que es administrador es de 10 opciones y tiene acceso a todo.
		print("Menú ")
		
    #El administrador puede consultar toda la lista de productos: producto, id, categoria, etc.
		print("1: Lista de productos")
		#El administrador puede consultar las ventas realizadas.
		print("2: Lista de ventas")
		#El administrador puede consultar la lista de los productos buscados
		print("3: Lista de búsquedas")
		#El admnistrador puede consultar cuales son los productos que se han vendido mas. Si el producto se ha vendido mas de 5 veces enronces esta considerado entre los mas vendidos. 
		print("4: Productos más vendidos")
		#El administrador puede consultar  que productis son los que se han buscado mas. Si el producto se busco mas de 10 veces entonces esta entre los mas buscados.
		print("5: Productos más buscados")
		#El administrador puede consultar aquellos productos que tuvieron una reseña de 5 (mas alta)
		print("6: Productos con las mejores reseñas")
		#El administrador puede consultar aquellos productos que tuvieron una reseña baja de 1.
		print("7: Productos con las peores reseñas")
	 #El administrador puede consultar aquellos productos que tuvieron ventas menores de 5 veces, por lo que se consideran como los menos vendidos o rezagados.
		print("8: Productos con menos ventas/ rezagados")
		#El administrador puede consultar aquellos productos que fueron comprados pero se devolvieron mas.
		print("9: Productos devueltos")
		#El administrador puede consultar cuales fueron las ventas de cada mes y asi generar analisis de posibles promociones
		print("10: Ventas mensuales")
		#El administrador selecciona la opcion que desea ver del menu. 
		selección = input("Ingresa la opción que deseas ver: ")

		if selección == '1':
		  
		  print("Lista de productos:", lifestore_products)
		  
		  
		elif selección == "2":
		  
		  print("Listado de ventas: ", lifestore_sales)
		  
		  
		elif selección == "3":
		  
		  print("Listado de búsquedas: ", lifestore_searches)

		elif selección == '4':
      #Contador para el id product
			v = 1
      #Se crea una lista para almacenar los productos mas vendidos
			lista_mas_vendidos = []
      #Se crea una sublista para almacenar los id_product y saber cuantas veces se vendio cada uno.
			lista_venta = []
      #Ciclo para almacenar los id product en lista_venta
			for venta in lifestore_sales:
				if venta[1] >= 1 or venta[1] <= 96:
					lista_venta.append(venta[1])
      #Bucle while para contar los productos en lista_venta
			while v < 97: #mientras el id product es menor a 97 se ejecuta
				x = lista_venta.count(v) #se hace el conteo de cada id product
				if x > 5:  #si el producto se vendio mas de 5 veces
					lista_mas_vendidos.append(v) #alamcena el id product en la la lista de los mas vendidos
				v += 1 #id product mas uno
			print("Lista de los más vendidos:", lista_mas_vendidos) #lista de los mas vendidos
			
			#Codigo sin hacer uso de count

			#cuenta_productos
			#numero_de_ventas = []
			
			#for producto in lifestore_products:
			  
			  #for venta in lifestore_sales:
			    
			    #if producto[0] == venta[1]:
			      
			      #cuenta_productos += 1
			      
			   #cuenta = [producto[0], producto[1], cuenta_productos]
			   
			   #numero_de_ventas.append(cuenta)
			   
			   #cuenta_productos = 0
			   
			   #for total in numero_de_ventas:
			     
			     #print("El producto", total[1], "se vendio", total[2]
			     
			   #for índice in range(1, 20):
			     #print("Nombre: ", #numero_de_ventas[indice][1])
			    
		elif selección == '5':

      #id product de busqueda
			producto_buscado = 1
      #lista de los mas buscados
			lista_mas_buscados = []
      #mientras el id product es menor a 97, ya que sabemos que tenemos 96 productos
			while producto_buscado < 97:
         #suma del conteo de las veces que el id product fue buscado en la lista de busquedas
				y = sum(
				    lst.count(producto_buscado) for lst in lifestore_searches)
        #si el producto fue buscado mas de 10 veces es de los mas buscados 
				if (y - 1) > 10: #menos uno para no contar el id search   
					lista_mas_buscados.append(producto_buscado)
				producto_buscado += 1 #contador de id product mas 1

			print("Los productos más buscados son: ", lista_mas_buscados)
			
      #Codigo sin sum y count

			#cuenta_busqueda
			#total_busquedas
			
			#for producto un lifestore_products:
			  #for busqueda in lifestore_searches:
			    #if producto[0] == búsqueda[1]:
			      
			      #cuenta_busqueda += 1
			
			  #formato_busquedas = [producto[0], producto[1], cuenta_busqueda)
			
			  #total_busquedas.append(formato_busquedas)
			  
			#for índice in range(1,20):
			  #print("Nombre", total_busquedas[indice][1])
			
	
		elif selección =="6":
		  #Se crea la lista de mejores reseñas 
		  lista_mejores_resenas = []
		  #Para cada producto con reseña igual a 5 (la mas alta) se almacena en la lista de los productos con las mejores reseñas
		  for resena in lifestore_sales:
		    if resena[2] == 5:
		      lista_mejores_resenas.append(resena[1])
		  
		  print("Los productos con las mejores reseñas son: ", lista_mejores_resenas)
		  
		elif selección == "7":
		  #Se crea la lista de peores reseñas
		  lista_peores_resenas =[]
		  #Para cada producto con reseña igual a 1 (la mas baja) se almacena en la lista de productos con las peorese reseñas.
		  for resena in lifestore_sales:
		    if resena[2] == 1:
		      lista_peores_resenas.append(resena[1])
		  print("Los productos con las peores reseñas son", lista_peores_resenas)
		  
		elif selección == "8":
		  #contador de id product
		  v = 1 
		  #la lista de los menos vendidos
		  lista_menos_vendidos = []
		  #sublista para almacenar los id product de la lista de ventas
		  lista_venta = []
		  #El bucle for es similar al de los mas vendidos
		  for venta in lifestore_sales:
		    if venta[1] >= 1 or venta[1] <= 96:
		      
		      lista_venta.append(venta[1])
		      
		  while v < 97:
		    
		    x = lista_venta.count(v)
		    if x < 5: #si el producto se vendio menos de 5 veces es de los menos vendidos
		      lista_menos_vendidos.append(v)
		      
		    v += 1
		    
		  print("Lista de los menos vendidos", lista_menos_vendidos)
		  
		elif selección == "9":
		  #se crea la lista de los productos devueltos
		  lista_devueltos = []
		  
		  for sale in lifestore_sales:
		    #si el producto fue devuelto se agrega a lista devueltos
		    if sale[4] == 1:
		      
		      lista_devueltos.append(sale[1])
		      
		  print("Los productos que se han devuelto son: ", lista_devueltos)
		  
		elif selección == "10":
		   #Sublista para almacenar solo las fechas de ventas
		   lista_fecha= []
		   
		   for venta in lifestore_sales:
		     
		     lista_fecha.append(venta[3])
		    
		     #print(lista_fecha)

		     #sublista para obtener solo el mes y el año 
		     lista_anos = []
		   
		   for ano in lista_fecha:
		     #slicing del mes y año
		     lista_anos.append([ano[3:5], ano[6:10]])
		    
		   #print(lista_anos)
		    
		   #contar cuantas veces se repite un mes para el número de ventas
		   
		   for venta_mes in lista_anos:
		     
		     enero = lista_anos.count(['01', '2020'])
		     
		   print("Enero: ", enero)
		   
		   for venta_mes in lista_anos: 
		     
		     febrero = lista_anos.count(['02', '2020'])
		     
		   print("Febrero: ", febrero)
		   
		   for venta_mes in lista_anos:
		     
		     marzo = lista_anos.count(['03', '2020'])
		     
		   print("Marzo: ", marzo)
		   
		   for venta_mes in lista_anos:
		     
		     abril = lista_anos.count(['04', '2020'])
		     
		   print("Abril: ", abril)
		   
		   for venta_mes in lista_anos: 
		     
		     mayo = lista_anos.count(['05', '2020'])
		     
		   print("Mayo: ", mayo)
		   
		   for venta_mes in lista_anos:
		     
		     junio = lista_anos.count(['06', '2020'])
		     
		   print("Junio: ", junio)
		   
		   for venta_mes in lista_anos:
		     
		     julio = lista_anos.count(['07', '2020']) 
		     
		   print("Julio: ", julio) 
		   
		   for venta_mes in lista_anos:
		     
		     agosto = lista_anos.count(['08', '2020'])
		     
		   print("Agosto: ", agosto)
		   
		   for venta_mes in lista_anos:
		     
		     septiembre = lista_anos.count(['09', '2020'])
		     
		   print("Septiembre ", septiembre)
		   
		   for venta_mes in lista_anos:
		     
		     octubre = lista_anos.count(['10', '2020'])
		     
		   print("Octubre: ", octubre)
		   
		   for venta_mes in lista_anos:
		     
		     noviembre = lista_anos.count(['11', '2020'])
		     
		   print("Noviembre: ", noviembre)
		   
		   for venta_mes in lista_anos:
		     
		     diciembre = lista_anos.count(['12', '2020'])
		     
		   print("Diciembre: ", diciembre)
	
	else:
	  #Repeticion del codigo de la primera parte si la contraseña esta mal 
		print("Contraseña incorrecta")
		password = input("Vuelve a introducir tu contraseña: ")

		if password == "admin":
			print("Puedes acceder")
			print("Menú ")
			
			print("1: Lista de productos")
			
			print("2: Lista de ventas")
			
			print("3: Lista de búsquedas")
			
			print("4: Productos más vendidos")
			
			print("5: Productos más buscados")
			
			print("6: Productos con las mejores reseñas ")
			
			print("7: Productos con las peores reseñas")
			
			print("8: Productos menos vendidos/ rezagados")
			
			print("9: Productos devueltos")
			
			print("10: Ventas mensuales")
			
			selección = input("Ingresa la opción que deseas ver: ")

			if selección == '1':

				print("Lista de productos: ", lifestore_products)
				
				
			elif selección == "2":
			  
			  print("Listado de ventas: ", lifestore_sales)
			  
			elif selección == "3":
			  
			  print("Listado de búsquedas:", lifestore_searches)
			  
			  
			elif selección == '4':

				v = 1

				lista_mas_vendidos = []

				lista_venta = []

				for venta in lifestore_sales:

					if venta[1] >= 1 and venta[1] <= 96:

						lista_venta.append(venta[1])

				while v < 97:

					x = lista_venta.count(v)

					if x > 5:

						lista_mas_vendidos.append(v)

					v += 1

				print("Lista más vendidos", lista_mas_vendidos)

			elif selección == '5':

				producto_buscado = 1

				lista_mas_buscados = []

				while producto_buscado < 97:

					y = sum(
					    lst.count(producto_buscado)
					    for lst in lifestore_searches)

					if y > 10:

						lista_mas_buscados.append(producto_buscado)

					producto_buscado += 1

				print("Los productos más buscados son:", lista_mas_buscados)
				
			elif selección == "6":
			  
			  lista_mejores_resenas = []
			  
			  for resena in lifestore_sales:
			    if resena[2] == 5:
			      lista_mejores_resenas.append(resena[1])
			      
			  print("Los productos con mejores reseñas son: ", lista_mejores_resenas)
			  
			elif selección == "7":
			  
			  lista_peores_resenas = []
			  
			  for resena in lifestore_sales:
			    if resena[2] == 1:
			      lista_peores_resenas.append(resena[1])
			      
			  print("Lista de los productos con las peores reseñas", lista_peores_resenas)
			
			elif selección == "8":
			   
			   v = 1
			   
			   
			   lista_menos_vendidos = []
			   
			   
			   lista_venta = []
			   
			   
			   for venta in lifestore_sales:
			     
			     if venta[1] >= 1 or venta[1] <= 96:
			       
			       lista_venta.append(venta[1])
			       
			   while v < 97:
			     
			     x = lista_venta.count(v)
			     
			     if x < 5:
			       
			       lista_menos_vendidos.append(v)
			       
			     v += 1 
			       
			   print("Los productos rezagados son: ", lista_menos_vendidos)
			   
			elif selección == "9":
		
			    lista_devueltos = []
			    
			    for sale in lifestore_sales:
			      
			      if sale[4] == 1:
			        
			        lista_devueltos.append(sale[1])
			        
			    print("Los productos que se han devuelto son: ", lista_devueltos)
			    
			elif selección == "10":
			  
			  lista_fecha= []
			  
			  for venta in lifestore_sales:
			    
			    lista_fecha.append(venta[3])
			    
			    lista_anos = []
			    
			  for ano in lista_fecha:
			    
			    lista_anos.append([ano[3:5], ano[6:10]])
			    
			  
			  for venta_mes in lista_anos:
			    
			    enero = lista_anos.count(['01','2020'])
			    
			  print("Enero: ", enero)
			  
			  for venta_mes in lista_anos:
			    
			    febrero = lista_anos.count(['02','2020'])
			    
			  print("Febrero: ", febrero)
			  
			  for venta_mes in lista_anos:
			    
			    marzo = lista_anos.count(['03','2020'])
			    
			  print("Marzo: ", marzo)
			   
			  for venta_mes in lista_anos:
			    
			    abril = lista_anos.count(['04','2020'])
			    
			  print("Abril: ", abril)
			  
			  for venta_mes in lista_anos:
			    
			    mayo = lista_anos.count(['05','2020'])
			    
			  print("Mayo: ", mayo)
			  
			  for venta_mes in lista_anos:
			    
			    junio = lista_anos.count(['06','2020'])
			    
			  print("Junio:  ", junio)
			  
			  for venta_mes in lista_anos:
			    
			    julio = lista_anos.count(['07','2020'])
			    
			  print("Julio: ", julio)
			  
			  for venta_mes in lista_anos:
			    
			    agosto = lista_anos.count(['08','2020'])
			    
			  print("Agosto: ", agosto)
			  
			  for venta_mes in lista_anos:
			    
			    septiembre = lista_anos.count(['09','2020'])
			    
			  print("Septiembre: ", septiembre)
			  
			  for venta_mes in lista_anos:
			    
			    octubre = lista_anos.count(['10','2020'])
			    
			  print("Octubre:  ", octubre)
			  
			  for venta_mes in lista_anos:
			    
			    noviembre = lista_anos.count(['11','2020'])
			    
			  print("Noviembre:  ", noviembre)
			  
			  
			  for venta_mes in lista_anos:
			    
			    diciembre = lista_anos.count(['12','2020'])
			    
			  print("Diciembre: ", diciembre)
			   
  #si el usuario es un usuario cualquiera, la contraseña es user123
elif usuario == "usuario": 
	
	password = input("Introduce tu contraseña: "
)
	if password == "user123":
#este usuario solo podra ver las 3 listas principales sin mas detalles
		print("Puedes acceder")
		print("Menú ")
		print("1: Lista de productos")
		print("2: Listado de ventas")
		print("3: Listado de búsquedas")
		
		selección = input("Ingresa la opción que deseas ver: ")
		
		#Imprime la lista de productos
		if selección == "1":
		  
		  print("Listado de productos:", lifestore_products)
		  #imprime la lista de ventas
		elif selección == "2":
		  
		  print("Listado de ventas: ", lifestore_sales)
		  #imprime la lista de busquedas
		elif selección == "3":
		  
		  print("Listado de búsquedas: ", lifestore_searches)
#Repeticion del codigo de la primera parte de usuario
	else:
		print("Contraseña incorrecta")
		password = input("Vuelve a introducir tu contraseña: ")

		if password == "user123":

			print("Puedes acceder")

			print("Menú ")
			
			print("1: Listado de productos")

			print("2: Listado de ventas")
			
			print("3: Listado de búsquedas")
			
			
			selección = input("Ingresa la opción que deseas ver: ")
			
			
			if selección == "1":
			  
			  print("Listado de productos:", lifestore_products)
			
			
			elif selección == "2":
			  
			  print("Listado de ventas: ", lifestore_sales)
			
			elif selección == "3":
			  
			  print("Listado de búsquedas: ", lifestore_searches)
			  
		else: 
		  #Si ingresa la contraseña 2 veces y es incorrecta el programa acaba.
		  print("Número de intentos alcanzado\nVuelve a intentar  más tarde")
	#Si no es usuario ni administrador acaba el programa.		 
else:
	print("No es un usuario válido")

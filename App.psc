Algoritmo App
	Escribir '�Est�s registrado?'
	Leer a
	si a='no' entonces
		Escribir 'nif,nombre,telefono,email,pais,ciudad,direcci�n'
		Leer cuenta
		Escribir 'contrase�a'
		Leer contrase�a1
		Escribir 'contrase�a'
		Leer contrase�a2
		Mientras  contrase�a1<>contrase�a2 Hacer
			Escribir 'Las contrase�as no coinciden'
		FinMientras
		Escribir 'cuenta creada'
	FinSi
	si a='si' Entonces
		Escribir 'contrase�a'
		Leer contrase�a2
		Mientras  contrase�a1<>contrase�a2 Hacer
			Escribir 'Las contrase�as no coinciden'
		FinMientras
	FinSi
	Escribir'productos'
	Escribir'producto1,8 unidades,17.55'
	Leer p1
	Escribir 'producto2,5 unidades,5.99'
	Leer p2
	Escribir'elije los productos que quieras a�adir al carrito'
	Leer carrito
	Mientras carrito<> z Hacer
		Escribir'cuando quieras dejar de a�adir productos y pasar a pagar pulsa z'
	FinMientras
	Escribir 'Nombre,nif,direcci�n,producto,precio por unidad,fecha,precio real(precio*iva del pais)'
	Leer  fact
	escribir 'Sms(fact.pdf) enviado a telefono x' 
FinAlgoritmo

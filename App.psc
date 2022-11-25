Algoritmo App
	Escribir '¿Estás registrado?'
	Leer a
	si a='no' entonces
		Escribir 'nif,nombre,telefono,email,pais,ciudad,dirección'
		Leer cuenta
		Escribir 'contraseña'
		Leer contraseña1
		Escribir 'contraseña'
		Leer contraseña2
		Mientras  contraseña1<>contraseña2 Hacer
			Escribir 'Las contraseñas no coinciden'
		FinMientras
		Escribir 'cuenta creada'
	FinSi
	si a='si' Entonces
		Escribir 'contraseña'
		Leer contraseña2
		Mientras  contraseña1<>contraseña2 Hacer
			Escribir 'Las contraseñas no coinciden'
		FinMientras
	FinSi
	Escribir'productos'
	Escribir'producto1,8 unidades,17.55'
	Leer p1
	Escribir 'producto2,5 unidades,5.99'
	Leer p2
	Escribir'elije los productos que quieras añadir al carrito'
	Leer carrito
	Mientras carrito<> z Hacer
		Escribir'cuando quieras dejar de añadir productos y pasar a pagar pulsa z'
	FinMientras
	Escribir 'Nombre,nif,dirección,producto,precio por unidad,fecha,precio real(precio*iva del pais)'
	Leer  fact
	escribir 'Sms(fact.pdf) enviado a telefono x' 
FinAlgoritmo

from password_validator import PasswordValidator
import phonenumbers
from phonenumbers.phonenumberutil import region_code_for_country_code
from datetime import date

telefono = None #variable global para llamar a telefono más tarde

def contraseñaValida():
    vale = False
    contrasena = 0
    while not vale: #si no hay contraseña te la pide
        contrasena1 = False
        contrasena = input('Escribe una contraseña: ')

        schema = PasswordValidator()

        # Requisitos de la contraseña entre 8 y 100 caracteres,con una mayuscula, una minuscula, un digito y sin espacios
        schema \
            .min(8) \
            .max(100) \
            .has().uppercase() \
            .has().lowercase() \
            .has().digits() \
            .has().no().spaces() \
            # comprueba que la contraseña valga
        vale = schema.validate(contrasena)
        if not vale:
            print('La contraseña no es valida, debe tener mayusculas, minusculas, numeros,' 
                  'no debe contener espacios y debe tener 8 caracteres como mínimo')
        else:
            contrasena1 = input('vuelve a introducir la contraseña: ')

        if contrasena1 != contrasena:
            print('las contraseñas no coinciden')
            vale = False
    return contrasena

def correoValido():
    cont = False
    while not cont: #te pide el correo
        correo = input('dime el correo: ')
        x = correo.find('@') #busca la @
        if x == -1: #si la encuentra lo guarda y si no te lo pide hasta que este
            print('correo invalido')
        else:
            print('correo valido')
            cont = True

def numeroTelefono():
    cont = False
    i = 0
    while not cont:
        global telefono #trae la variable a la función
        telefono = input('introduce el numero de teléfono: (+xx xxxxxxxxx):') #guarda el tlf

        try:#formatea el telefono y se asegura que este bien
            phoneNumber = phonenumbers.parse(telefono)
            print(phoneNumber)
            i = region_code_for_country_code(phoneNumber.country_code) == 'ES'
            cont = True
        except UnboundLocalError:
            print('introduce un número en el formato mencionado')
            cont = False
        except phonenumbers.NumberParseException:
            cont = False
            print('introduce un número en el formato mencionado')

    return i



class Cliente(): # instancia la clase
    def __init__(self):#constructor
        self.dni=input('Dime tu dni/nif: ')#setters
        self.nombrec=input('Dime tu nombre: ')
        self.tlf =numeroTelefono()
        self.email=correoValido()
        self.pais=input('Dime el pais en el que resides: ')
        self.ciudad=input('Dime la ciudad en la que vives: ')
        self.direccion=input('Dime tu dirección: ')
        self.contraseña=contraseñaValida()

c1=Cliente()#instaciar objeto

class Producto():
    def __init__(self,nombre,precio):
        self.nombre=nombre
        self.precio=precio

p1=Producto('camisa',17.99)#instancio objetos
p2=Producto('pantalon',24.52)
p3=Producto('zapatos',59.99)

print(p1.nombre,p1.precio)
print(p2.nombre,p2.precio)
print(p3.nombre,p3.precio)

total=0#creo una variable y dos listas(vacias) para guardar lo necesario
carrito =[]
precio =[]
try:#si ocurre un error el preograma no se rompe
    producto = input('Pulsa 4 cuando quieras dejar de añadir productos: ')
    while producto <= 3:#el bucle sigue hasta que se pulsa 4 o cualquier otro numero
        producto = int(input('Para añadir un producto presiona 1,2 o 3: '))
        if producto == 1:#dependiendo de que se presione se añade un producto o otro
            carrito.append(p1.nombre)
            precio.append(p1.precio)
        if producto == 2:
            carrito.append(p2.nombre)
            precio.append(p2.precio)
        if producto == 3:
            carrito.append(p3.nombre)
            precio.append(p3.precio)
    for y in precio:
        total += y #suma todos los precios
except:
    print('A ocurrido un error')
if c1.pais != 'españa':#si el cliente no es español paga un bonus por transporte internacinal
    total=total*1.21
print(f'Factura\n{c1.nombrec}----{c1.dni}\n{c1.pais}---{c1.ciudad}---{c1.direccion}\n{carrito}\n{precio}\n{date.today()}----{total}€')
#Dejo el date.today sin formatear por que lo veo innecesario
print(f'Un sms conteniendo factura.pdf a sido enviado a {telefono}')#si pusiera c1.tlf diria True en vez del telefono por eso se usa el global

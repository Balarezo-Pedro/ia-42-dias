# Tipado dinámico
x = 5
x = "ahora soy texto"   # válido, a diferencia de Java

# Listas y diccionarios
tickets = ["red caída", "VPN lenta", "impresora"]
tickets.append("correo")
ticket = {"id": 101, "prioridad": "alta", "equipo": "redes"}
print(ticket["prioridad"], len(tickets))

# For, sin índices
for t in tickets:
    print(f"Ticket: {t}")
for i in range(3):          # 0, 1, 2
    print(i)

# Funciones
def saludar(nombre, saludo="Hola"):
    return f"{saludo}, {nombre}"
print(saludar("Pedro"))

# Comprehensions (el equivalente a stream().filter().map())
mayusculas = [t.upper() for t in tickets]
largos = [t for t in tickets if len(t) > 8]
print(mayusculas, largos)

#diccionario con cuántas veces aparece cada palabra.
texto="todos los peruanos somos los amigos"
def contar_palabras (texto):
    palabras=texto.lower().split()
    contador={}
    for palabra in palabras:
        contador[palabra]=contador.get(palabra,0)+1
    return contador

print (contar_palabras(texto))

#devuelve los tickets de esa prioridad, con una comprehension.
def filtrar_tickets(tickets, prioridad):
    return [boleto for boleto in tickets if boleto["prioridad"]==prioridad]

tickets = [
    {"id": 1, "titulo": "caída de red", "prioridad": "alta"},
    {"id": 2, "titulo": "apagón", "prioridad": "alta"},
    {"id": 3, "titulo": "no autentica", "prioridad": "baja"},
]
print(filtrar_tickets(tickets,"alta"))
print(filtrar_tickets(tickets,"media"))

#devuelve el promedio, o None si la lista está vacía.
def promedio_resolucion(horas):
    if not horas:
        return None

    return sum(horas)/len(horas)

horas=[3,4,6,0]
hor=[]
print (promedio_resolucion(horas))
print (promedio_resolucion(hor))
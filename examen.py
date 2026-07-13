arreglos = {
    'FLO1': ['Ramo Primavera', 'ramo', 'rosado', 'M', True, 'primavera'],
    'FLO2': ['Caja Elegante', 'caja', 'blanco', 'L', True, 'todo año'],
    'FLO3': ['Ramo Solar', 'ramo', 'amarillo', 'S', False, 'verano'],
    'FLO4': ['Centro Mesa', 'centro', 'rojo', 'M', True, 'todo año'],
    'FLO5': ['Ramo Bosque', 'ramo', 'verde', 'L', False, 'otoño'],
    'FLO6': ['Caja Noche', 'caja', 'morado', 'M', True, 'invierno'],
}

bodega = {
    'FLO1': [15990, 8],
    'FLO2': [29990, 3],
    'FLO3': [9990, 12],
    'FLO4': [24990, 5],
    'FLO5': [19990, 0],
    'FLO6': [22990, 6],
    }

def mostrar_menu():
    print("""
========== MENÚ PRINCIPAL ==========
1. Unidades por tipo de arreglo
2. Búsqueda de arreglos por rango de precio
3. Actualizar precio de arreglo
4. Agregar arreglo
5. Eliminar arreglo
6. Salir
=====================================
""")
    
def leer_opcion():
    while True:
        try:
            op=int(input("Ingrese una opcion: "))
        except ValueError:
            print("Error, debe ser un numero entero")
        else:
            if op>=1 and op <=6:
                return op
            
def validar_nombre(nombre):
    if nombre.strip() !="":
        return True
    else:
        return False
    
def validar_tipo(tipo):
    if tipo.strip() !="":
        return True
    else:
        return False
    
def validar_color(color_principal):
    if color_principal.strip() != "":
        return True
    else:
        return False
    
def validar_tamaño(tamaño):
    if tamaño =="S" or tamaño =="M" or tamaño == "L":
        return True
    else:
        return False

def validar_tarjeta(incluye_tarjeta):
    if incluye_tarjeta=="s":
        return True
    else:
        if incluye_tarjeta=="n":
            return False
        
def validar_temporada(temporada):
    if temporada.strip() != "":
        return True
    else:
        return False
    
def validar_precio(precio):
    if precio>0:
        return True
    else:
        return False
    
def validar_unidades(unidades):
    if unidades>=0:
        return True
    else:
        return False
    
def existe_codigo(codigo):
    if arreglos in codigo:
        return True
    else:
        return False
    
def unidades_tipo(tipo):
    tipo=input("Ingrese tipo de arreglo a consultar: ").upper()
    for arreglos in tipo:
        codigo=[bodega][2].upper()==codigo.upper()
        print(f"El total de unidades disponibles es: {arreglos}")
    else:
        print("Tipo de arreglo no encontrado")
    total= 0

def busqueda_precio(p_min, p_max):





def buscar_codigo(codigo):





def actualizar_precio(codigo, nuevo_precio):






def main():
    while True:
        mostrar_menu()
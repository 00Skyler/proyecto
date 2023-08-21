vehiculos = [["Maxus V80", 10, "BCA 321", True,25000,"E-501"], ["Nissan Urvan NV350 Premium", 15, "XYZ 789", True,29000,"R-258"], ["Hyundai Grand Starex", 20, "RST 456", True,32000,"M-789"]]
viajes = []

tarifa_pasajero = 2500




def menu():
    print("\n-------¡¡¡Bienvenido!!!---------\n")
    print("\nHa llegado al sistema de administrasion de viajes")
    print("Seleccione una opcion\n")
    print("\n1. Reservar un viaje.\n 2. Consultar un viaje.\n 3. Editar un viaje. \n4. Salir")
    
def registrar_viaje():

    while True:
        
        pasajeros = int(input("Cuantos pasajeros lleva?: "))
        confirmar_pasajero = input(f"\nUsted ha ingresado una cantidad de pasajeros de {pasajeros} personas, es correcto? [s-n]: ").upper()
        
        
        if confirmar_pasajero == "N":
            print("\nHa respondido que no, por favor ingrese nuevo numero de pasajeros")
            continue
        elif pasajeros <= 1:
            print("\nOpcion invalida")
            print("El minimo de personas que puede reservar es de 2 pasajeros")
            print("\nPor favor intente de nuevo")
            
        
        else:
            vehiculo_seleccionado = False
        
            for vehiculo in vehiculos:
                if pasajeros <= vehiculo[1] and vehiculo[3]:
                    vehiculo_seleccionado = vehiculo
                    break
        
            if vehiculo_seleccionado:
                correo = input("Ingrese una direccion de correo electronico: ")
                print(f"\nInformacion de vehiculo disponible para {pasajeros} personas:")
                print(f"Marca y modelo: {vehiculo_seleccionado[0]}.\nPlaca: {vehiculo_seleccionado[2]}. Costo por uso: ₡{vehiculo_seleccionado[4]}\n")
                monto_total = pasajeros * tarifa_pasajero + vehiculo_seleccionado[4] 
                monto_impuesto = monto_total * 1.13
                
                print(f"IVA: 13%.\nTarifa por pasajero: ₡2500 \n{pasajeros} Pasajeros: ₡{pasajeros*tarifa_pasajero}. \nCosto por uso: ₡{vehiculo_seleccionado[4]}. \nMonto total con IVA: ₡{monto_impuesto:8.2f}")
                confirmar = input("Desea continuar con la compra? [s/n]: ").upper()
                if confirmar == "N":
                        print("Por favor ingrese una nueva cantidad de pasajeros: ")
                        continue
                else: 
                    
                    print(f"La compra ha sido efectuada con exito, le llegara una factura a su correo {correo}")
                    print(f"La identificacion del viaje es: {vehiculo_seleccionado[5]}")
                
                    print("\n********************************************************************************")
                    print("** ** ** ** **Gracias por preferirnos** ** ** ** **\n ")
                    
                    monto_total_reserva = monto_total + vehiculo_seleccionado[4]
                    vehiculo_seleccionado.append(monto_total_reserva)
                    vehiculo_seleccionado.append(correo.upper())
                    vehiculo_seleccionado.append(pasajeros)
                    
                    viajes.append(vehiculo_seleccionado) 
                    
                    
                    
                    
                with open("viajes.txt", "w",encoding="utf-8") as f:
                        for viaje in viajes:
                            texto = ""
                            for i in range(len(viaje)):
                                if i > 0:
                                    texto += ","  
                                texto += str(viaje[i])
                            texto += "\n"  
                            f.write(texto) 
                        break
              
           
            else:
                print("No hay vehiculo disponible para la cantidad de pasajeros ingresada.")
    
 


            
           
    
   
            
def Buscar_en_archivo(archivo, texto_a_buscar):
    resultados = []
    with open(archivo, 'r', encoding="utf-8") as file:
        for linea in file:
            if texto_a_buscar in linea:
                resultados = linea.strip().split(',')
                print(f"Marca y modelo: {resultados[0]}")
                print(f"Placa: {resultados[2]}")
                print(f"ID: {resultados[5]}")
                print(f"Monto total: ₡{resultados[6]}")
                print(f"Correo: {resultados[7]}")
                print(f"Cantidad de personas: {resultados[8]}")
                break  
        else:
            print("No se encontró el viaje con ese correo.")
        


def editar(archivo, texto_a_buscar):
    resultados = []
    with open(archivo, 'r', encoding="utf-8") as file:
        for linea in file:
            if texto_a_buscar in linea:
                resultados = linea.strip().split(',')
                print(f"Marca y modelo: {resultados[0]}")
                print(f"Placa: {resultados[2]}")
                print(f"ID: {resultados[5]}")
                print(f"Monto total: ₡{resultados[6]}")
                print(f"Correo: {resultados[7]}")
                print(f"Cantidad de personas: {resultados[8]}")
                print("\n************************************* ")
                print("\nDesea que desea editar. \n1.Numero de pasajeros. \n2.Correo electronico. \n3.Salir.")
                edit = input("Seleccion: ")
                            
                while edit != "3":
                    if edit == "1":
                        print("Ha seleccionado cambio de pasajeros")
                        print("\nNota: El cambio de pasajeros va a afectar el monto total y los detalles de el vehiculo seleccionado")
                        nueva_cantidad_pasajeros = int(input("\nIngrese nueva cantidad de pasajeros: "))
                        with open(archivo, 'w', encoding="utf-8") as file:
                            for linea in file:
                                resultados[7].replace(nueva_cantidad_pasajeros)
                                print(resultados[7])
        else:
            print("No se encontró el viaje con ese correo.")

                        
                        
                    
            
                

                
                
        
               

            
    
                
    
                   
    #Interfas de uso*****************                
    
while True:
    menu()
    sel = input("Seleccione aqui: ")
    if sel == "4":
        print("Gracias")
        break
    elif sel == "1":
        print( "\nHa seleccionado reservar un viaje")
        print("\n********** Minimo: 2 personas ---- Maximo: 20 Personas *************\n")
        registrar_viaje()
        break
    elif sel == "2":
        
        print("Ha seleccionado consultar un viaje")
        correo = input("\nIngrese el correo electronico usado para reservar el viaje: ").upper()
        Buscar_en_archivo("viajes.txt",correo)
        break
        
       
    
        
    elif sel == "3":
        print("Ha seleccionado editar un viaje")
        correo = input("\nIngrese el correo electronico utilizado para reservar el viaje: ").upper()
        editar("viajes.txt",correo)
        
    
    elif sel != "1" or sel != "2" or sel != "3" or sel != "4":
        print("\n******* Seleccion invalida ******\n")
        print("\nRealize seleccion nuevamente")
        continue

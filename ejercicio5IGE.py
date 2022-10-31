#Teniéndos los siguientes criterios:
#Desaprobado: nota < 11
#Destacado: nota > 16
#Aprobado: para el resto de casos

#Implementar registrar_aprobados como generador y que su único parametro
#de entrada sea alumnos_notas Posteriormente utilizar un bucle y enumerate
#para obtener la siguiente salida.

#1 -> Marcelo : 15 (Aprobado)
#2 -> Jose : 20 (Destacado)
#3 -> Juan : 18 (Destacado)
#4 -> Marco : 11 (Aprobado)
#5 -> María : 4 (Desaprobado)
#6 -> Ricardo : 7 (Desaprobado)
#7 -> Liz : 14 (Aprobado)
#8 -> Diego : 13 (Aprobado)
#9 -> Roberto : 1 (Desaprobado)
#10 -> Martin : 9 (Desaprobado)
#11 -> Álvaro : 10 (Desaprobado)

def registrar_aprobados(l):
    for i in l:
        if i[1] == 0 or i[1] < 11 :
            yield i[0],i[1],"Desaprobado"
        elif i[1] == 11 or i[1] <=16:
            yield i[0],i[1],"Aprobado"
        elif i[1] >16 and i[1] <= 20:
            yield i[0],i[1],"Destacado"# trasforma en una tupla al usar yield

notas = [15, 20,18, 11, 4, 7, 14, 13 ,1 ,9, 10]
alumnos = ["Marcelo", "Jose", "Juan", "Marco", "María", "Ricardo", "Liz", "Diego", "Roberto", "Martin", "Álvaro"]
alumnos_notas = zip(alumnos, notas)


for num , (nom ,nota,estado) in enumerate(registrar_aprobados(alumnos_notas),start=1):
    print(f"#{num} -> {nom} : {nota} ({estado})")
    
print ("hola mundo")

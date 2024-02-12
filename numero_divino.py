from tkinter import *
from tkinter import messagebox

lista = []

def iniciar():
    num = int(label_cantidad.get())
    if num != 0:
        fibonacci(num)
        perfectos(num)
    else:
        messagebox.showinfo(message="Debes ingresar un número diferente a 0.")


def fibonacci(num):
    a = 0
    b = 1
    contador = 0

    while contador < num:
        lista.append(a)
        listbox_serie_fibonacci.insert("end",a)
        suma = a + b
        a = b
        b = suma
        aureo = suma / a
        aureo_inverso = 1 / aureo
        aureo_aureo = aureo * aureo
        listbox_aureo.insert("end",aureo)
        listbox_aureo_inverso.insert("end",aureo_inverso)
        listbox_producto_aureo.insert("end",aureo_aureo)
        print(aureo)
        contador = contador + 1

    print(lista)
    const_aureo = listbox_aureo.get("end")
    label_sumatoria.config(text="Sumatoria: {}".format(suma-1))
    label_aureo.config(text="Nº Aúreo: {}".format(const_aureo))


def perfectos(num):
    def validarPerfecto(n):
        c = 0
        for i in range(1, n):
            if n % i == 0:
                c+= i
        if c == (n):
            return True
        else:
            return False
        
    numeros_perfectos = []
    for i in range(1, num):
        if validarPerfecto(i):
            numeros_perfectos.append(i)
            listbox_perfecto.insert("end",i)
            print("Es Perfecto: ", i)
    return numeros_perfectos


def limpiar():
    #Debemos borrar el contenido de las cajas de texto
    listbox_serie_fibonacci.delete(0,END)
    listbox_aureo.delete(0,END)
    listbox_aureo_inverso.delete(0,END)
    listbox_perfecto.delete(0,END)
    listbox_producto_aureo.delete(0,END)

    label_cantidad.delete(0,END)
    label_sumatoria.config(text="Sumatoria: 0")
    label_aureo.config(text="Nº Aúreo: 0")
    label_cantidad.focus()


ventana = Tk()
ventana.title("Buscador de números")
ventana.geometry("830x520")



Label(text="Buscador",font=("Loto",12)).place(x=140,y=20)

Label(text="Cant. Números: ").place(x=40,y=50)
label_cantidad = Entry(width=15)
label_cantidad.place(x=132,y=50)


Label(text="Serie Fibonacci").place(x=20,y=80)
Label(text="Constante aúrea").place(x=180,y=80)
Label(text="Constante aúrea (inversa)").place(x=340,y=80)
Label(text="Números perfectos").place(x=500,y=80)
Label(text="Productos aúreos").place(x=660,y=80)


Button(text="JUEGA!",command=iniciar).place(x=260,y=45)
Button(text="Limpia",command=limpiar).place(x=330,y=45)

#Listbox
listbox_serie_fibonacci = Listbox(width=25,height=20)
listbox_serie_fibonacci.place(x=20,y=100)

listbox_aureo = Listbox(width=25,height=20)
listbox_aureo.place(x=180,y=100)

listbox_aureo_inverso = Listbox(width=25,height=20)
listbox_aureo_inverso.place(x=340,y=100)

listbox_perfecto = Listbox(width=25,height=20)
listbox_perfecto.place(x=500,y=100)

listbox_producto_aureo = Listbox(width=25,height=20)
listbox_producto_aureo.place(x=660,y=100)





#Etiquetas
label_sumatoria = Label(text="Sumatoria: 0")
label_sumatoria.place(x=20,y=430)

label_aureo = Label(text="Nº Aúreo: 0")
label_aureo.place(x=20,y=450)

Label(text="Phi (Φ) es: 1.618033988749894").place(x=19,y=470)

ventana.mainloop()

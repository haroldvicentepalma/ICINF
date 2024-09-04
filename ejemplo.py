import tkinter as tk

user = 'persona'
password = 'algo123'
correo =''

###

#funcio que cree una ventana donde crear un nuevo usuario
def crear_usuario():
    
    #funcion que cambia el usuario, la contraseña y el correo
    def usuario_creado():
        global user,password,correo

        user = N_usuario.get()
        password = N_contrasena.get()
        correo = correo_electronico.get()
        ventana2.destroy()

    ventana2 = tk.Toplevel()
    
    ventana2.geometry('500x400')

    titulo2 = tk.Label(ventana2,text='Crear Nuevo Usuario',font=('arial',40))
    N_usuario_ = tk.Label(ventana2,text='Nuevo Usuario:')
    N_contrasena_ = tk.Label(ventana2,text='Nueva Contraseña:')
    correo_electronico_ = tk.Label(ventana2,text='Correo Electronico:')

    N_usuario = tk.Entry(ventana2)
    N_contrasena = tk.Entry(ventana2)
    correo_electronico = tk.Entry(ventana2)

    crear = tk.Button(ventana2,text='Crear Usuario',command=usuario_creado)

    titulo2.pack(pady=50)
    N_usuario_.pack()
    N_usuario.pack()
    N_contrasena_.pack()
    N_contrasena.pack()
    correo_electronico_.pack()
    correo_electronico.pack()
    crear.pack(pady=10)

#funcion que compruebe si la contraseña es correcta
def comprovacion():
    texto1 = usuario.get()
    texto2 = contrasena.get()
    if texto2 != password:
        error = tk.Toplevel()

        Error = tk.Label(error,text='Contraseña Incorrecta',font=('arial',15))

        Error.pack()
    elif texto1 == user and texto2 == password:
        
        ventana3 = tk.Tk()

        etiqueta = tk.Label(ventana3,text='Una nueva ventana')
        ventana.destroy()

###

#ventana principal

ventana = tk.Tk()

ventana.geometry('500x400')

label = tk.Label(ventana,text='Ingreso De Usuario',font=('arial',40))
label_ = tk.Label(ventana)
usuario_ = tk.Label(ventana,text='Usuario:')
contrasena_ = tk.Label(ventana,text='Contraseña:')

usuario = tk.Entry(ventana,)
contrasena = tk.Entry(ventana)

ingresar = tk.Button(label_,text='Ingresar',command=comprovacion)
crear_nuevo_usuario = tk.Button(label_,text='Crear Usuario',command=crear_usuario)

label.pack(pady=50)
usuario_.pack()
usuario.pack()
contrasena_.pack()
contrasena.pack()
label_.pack()

ingresar.grid(column=0,row=0,padx=5,pady=10)
crear_nuevo_usuario.grid(column=1,row=0)

ventana.mainloop()
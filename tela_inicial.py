import tkinter
from snake.snake_game import Jogo


def Tela_inicial():
    root_tela_inicial = tkinter.Tk()
    root_tela_inicial.geometry("920x981+0+0")
    root_tela_inicial.resizable(width='False', height=False)
    root_tela_inicial.title('Ebony Sys || JOGOS')

    image = tkinter.PhotoImage(file='img/back.png')
    image = image.subsample(1, 1)

    labelimage = tkinter.Label(image=image)
    labelimage.place(x=0, y=0, relwidth=1.0, relheight=1.0)

    snake = tkinter.Button(root_tela_inicial, text="Snake", bg='light blue', font='Ubuntu 18 italic', bd=2,
                           relief='raised', activebackground='green', width=35, command=Jogo)
    snake.place(x=200, y=400)

    corrida = tkinter.Button(root_tela_inicial, text='Corrida', bg='light blue', font='Ubuntu 18 italic', bd=2,
                             relief='raised', activebackground='blue', width=35)
    corrida.place(x=200, y=450)

    sinuca = tkinter.Button(root_tela_inicial, text='Sinuca', bg='light blue', font='Ubuntu 18 italic', bd=2,
                            relief='raised', activebackground='yellow', width=35)
    sinuca.place(x=200, y=500)

    sair = tkinter.Button(root_tela_inicial, text="Sair", bg='light blue', font='Ubuntu 18 italic', bd=2,
                          relief='raised', activebackground='red', width=35)
    sair.place(x=200, y=550)

    root_tela_inicial.mainloop()


Tela_inicial()

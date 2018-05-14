from tkinter import *

from tkinter import filedialog, messagebox


def sair():
    root.destroy()


def converte():
    legenda(path)
    messagebox.showinfo("legenda amarela", "Conversão concluída")


def abrir():
    global path
    root.file = filedialog.askopenfilename(filetypes=(("legenda", "*.srt"), ("all files", "*.*")))
    path = root.fileName
    e.insert(END, path + "\n")


def legenda(leg):
    """lê o arquivo de origem"""
    arq = open(leg, 'r')
    legenda_amarela = leg + '_legenda amarela.srt'
    arq2 = open(legenda_amarela, 'w')

    line = arq.readline()
    while line != "":
        tex = line.strip()
        if line[0] not in '0123456789' and line[0] != '\n':
            arq2.write('<font color="#dcff15">' + tex + '</font>')
            arq2.write('\n')
        else:

            arq2.write(line)
        line = arq.readline()
    arq.close()
    arq2.close()
    return None


root = Tk()
root.title("CONVERSOR DE LEGENDA AMARELA")
root.geometry("400x400")
root.resizable(0, 0)
# root.configure(bg = "RoyalBlue")

frame = Frame(root, width=300, height=300, bd=2, relief="raise")
frame.place(x=50, y=40)
path = ""

lab = Label(frame, text="BEM VINDO AO CONVERSOR DE LEGENDAS").place(x=25, y=25)
bt1 = Button(frame, width=10, text="Abrir", command=abrir).place(x=200, y=250)
bt2 = Button(frame, width=10, text="Converter", command=converte).place(x=110, y=250)
bt3 = Button(frame, width=10, text="Sair", command=sair).place(x=20, y=250)

e = Text(frame, width=25, height=5)
e.place(x=40, y=50)

root.mainloop()

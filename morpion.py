from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Jeu du morpion')
root.iconbitmap('C:/Users/Mathloss/Desktop/morpion/morpion.ico')

#-----------------------VARIABLES----------------------------------

#compteur
count = 0
#case cliquée
clicked = True

#--------------------- LES FONCTIONS----------------------------------

#fonction clique
def clique(bouton):
    global clicked,count
    if bouton["text"] == " " and clicked == True:
        bouton["text"] = "X"
        clicked = False
        count += 1
        verif_gagnant()
    elif bouton["text"] == " " and clicked == False:
        bouton["text"] = "O"
        clicked = True
        count += 1
        verif_gagnant()
    else:
        messagebox.showerror("Morpion","La case est déjà utilisée\nChoisis-en une autre!!")

# on desactive les boutons si il y a un gagnant
def desactive_bouton():
   b1.config(state=DISABLED)   
   b2.config(state=DISABLED)
   b3.config(state=DISABLED)
   b4.config(state=DISABLED)
   b5.config(state=DISABLED)
   b6.config(state=DISABLED)
   b7.config(state=DISABLED)
   b8.config(state=DISABLED)
   b9.config(state=DISABLED)

# Quelqu'un a gagné
def verif_gagnant():
    global gagnant
    gagnant = False

    # ligne horizontale
    if b1["text"]=="X" and b2["text"]=="X" and b3["text"]=="X":
        b1.config(bg="light green")
        b2.config(bg="light green")
        b3.config(bg="light green")
        gagnant = True
        messagebox.showinfo("x", "Le X a gagné!!")
        desactive_bouton()
    elif b4["text"]=="X" and b5["text"]=="X" and b6["text"]=="X":
        b4.config(bg="light green")
        b5.config(bg="light green")
        b6.config(bg="light green")
        gagnant = True
        messagebox.showinfo("x", "Le X a gagné!!")
        desactive_bouton()
    elif b7["text"]=="X" and b8["text"]=="X"and b9["text"]=="X":
        b7.config(bg="light green")
        b8.config(bg="light green")
        b9.config(bg="light green")
        gagnant = True
        messagebox.showinfo("x", "Le X a gagné!!")
        desactive_bouton()
    elif b1["text"]=="O" and b2["text"]=="O"and b3["text"]=="O":
        b1.config(bg="light green")
        b2.config(bg="light green")
        b3.config(bg="light green")
        gagnant = True
        messagebox.showinfo("O", "Le O a gagné!!")
        desactive_bouton()
    elif b4["text"]=="O" and b5["text"]=="O" and b6["text"]=="O":
        b4.config(bg="light green")
        b5.config(bg="light green")
        b6.config(bg="light green")
        gagnant = True
        messagebox.showinfo("O", "Le O a gagné!!")
        desactive_bouton()
    elif b7["text"]=="O" and b8["text"]=="O" and b9["text"]=="O":
        b7.config(bg="light green")
        b8.config(bg="light green")
        b9.config(bg="light green")
        gagnant = True
        messagebox.showinfo("O", "Le O a gagné!!")
        desactive_bouton()

    # ligne verticale
    elif b1["text"]=="X" and b4["text"]=="X" and b7["text"]=="X":
        b1.config(bg="light green")
        b4.config(bg="light green")
        b7.config(bg="light green")
        gagnant = True
        messagebox.showinfo("x", "Le X a gagné!!")
        desactive_bouton()
    elif b2["text"]=="X" and b5["text"]=="X" and b8["text"]=="X":
        b2.config(bg="light green")
        b5.config(bg="light green")
        b8.config(bg="light green")
        gagnant = True
        messagebox.showinfo("x", "Le X a gagné!!")
        desactive_bouton()
    elif b3["text"]=="X" and b6["text"]=="X" and b9["text"]=="X":
        b3.config(bg="light green")
        b6.config(bg="light green")
        b9.config(bg="light green")
        gagnant = True
        messagebox.showinfo("x", "Le X a gagné!!")
        desactive_bouton()
    elif b1["text"]=="O" and b4["text"]=="O"and b7["text"]=="O":
        b1.config(bg="light green")
        b4.config(bg="light green")
        b7.config(bg="light green")
        gagnant = True
        messagebox.showinfo("O", "Le O a gagné!!")
        desactive_bouton()
    elif b2["text"]=="O" and b5["text"]=="O"and b8["text"]=="O":
        b2.config(bg="light green")
        b5.config(bg="light green")
        b8.config(bg="light green")
        gagnant = True
        messagebox.showinfo("O", "Le O a gagné!!")
        desactive_bouton()
    elif b3["text"]=="O" and b6["text"]=="O" and b9["text"]=="O":
        b3.config(bg="light green")
        b6.config(bg="light green")
        b9.config(bg="light green")
        gagnant = True
        messagebox.showinfo("O", "Le O a gagné!!")
        desactive_bouton()
    
    #gagnant vertical
    elif b1["text"]=="X" and b5["text"]=="X" and b9["text"]=="X":
        b1.config(bg="light green")
        b5.config(bg="light green")
        b9.config(bg="light green")
        gagnant = True
        messagebox.showinfo("X", "Le X a gagné!!")
        desactive_bouton()
    elif b7["text"]=="X" and b5["text"]=="X" and b3["text"]=="X":
        b7.config(bg="light green")
        b5.config(bg="light green")
        b3.config(bg="light green")
        gagnant = True
        messagebox.showinfo("X", "Le X a gagné!!")
        desactive_bouton()
    elif b1["text"]=="O" and b5["text"]=="O" and b9["text"]=="O":
        b1.config(bg="light green")
        b5.config(bg="light green")
        b9.config(bg="light green")
        gagnant = True
        messagebox.showinfo("O", "Le O a gagné!!")
        desactive_bouton()
    elif b7["text"]=="O" and b5["text"]=="O" and b3["text"]=="O":
        b7.config(bg="light green")
        b5.config(bg="light green")
        b3.config(bg="light green")
        gagnant = True
        messagebox.showinfo("O", "Le O a gagné!!")
        desactive_bouton()
    elif gagnant == False and count == 9:
        messagebox.showinfo('Morpion', "Match nul")

def reset():
    global b1,b2,b3,b4,b5,b6,b7,b8,b9 
    global clicked, count
    clicked = True
    count = 0 

    # creation des boutons
    b1 = Button(root, text=" ", font=("Arial",32), height=3, width=6, bg="white", command=lambda:clique(b1))
    b2 = Button(root, text=" ", font=("Arial",32), height=3, width=6, bg="white", command=lambda:clique(b2))
    b3 = Button(root, text=" ", font=("Arial",32), height=3, width=6, bg="white", command=lambda:clique(b3))

    b4 = Button(root, text=" ", font=("Arial",32), height=3, width=6, bg="white", command=lambda:clique(b4))
    b5 = Button(root, text=" ", font=("Arial",32), height=3, width=6, bg="white", command=lambda:clique(b5))
    b6 = Button(root, text=" ", font=("Arial",32), height=3, width=6, bg="white", command=lambda:clique(b6))

    b7 = Button(root, text=" ", font=("Arial",32), height=3, width=6, bg="white", command=lambda:clique(b7))
    b8 = Button(root, text=" ", font=("Arial",32), height=3, width=6, bg="white", command=lambda:clique(b8))
    b9 = Button(root, text=" ", font=("Arial",32), height=3, width=6, bg="white", command=lambda:clique(b9))
    
    #mise en page
    b1.grid(row=0,column=0)
    b2.grid(row=0,column=1)
    b3.grid(row=0,column=2)
    b4.grid(row=1,column=0)
    b5.grid(row=1,column=1)
    b6.grid(row=1,column=2)
    b7.grid(row=2,column=0)
    b8.grid(row=2,column=1)
    b9.grid(row=2,column=2)

# Creation du menu
my_menu = Menu(root)
root.config(menu=my_menu)
# Options du menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Mise à zéro", command=reset) 
options_menu.add_command(label="Quitter", command=quit) 

reset()
root.mainloop()
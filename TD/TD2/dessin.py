import tkinter as tk
import random
root = tk.Tk()
root.title("Dessins random")  
canvas = tk.Canvas(root, width=400, height=300, bg="black", borderwidth=5, relief="ridge")
canvas.grid(row=1, column=1, rowspan=5)  
couleur_b=""

def dessiner_cercle():
    global couleur_b
    couleur_de_base="blue"
    diameter = 100
    x = random.randint(0, 400 - diameter)
    y = random.randint(0, 300 - diameter)
    if couleur_b =="":
        canvas.create_oval(x, y, x + diameter, y + diameter, fill=couleur_de_base)
    else:
        canvas.create_oval(x, y, x + diameter, y + diameter, fill=couleur_b)

def dessiner_carre():
    global couleur_b
    couleur_de_base="red"
    side = 100
    x = random.randint(0, 400-side)
    y = random.randint(0, 300-side)
    if couleur_b =="":
       canvas.create_rectangle(x, y, x + side, y + side, fill=couleur_de_base)
    else:
        canvas.create_rectangle(x, y, x + side, y + side, fill=couleur_b)


def dessiner_croix():
    global couleur_b
    couleur_de_base="yellow"
    side = 100
    x = random.randint(0, 400-side)
    y = random.randint(0, 300-side)
    if couleur_b =="":
       canvas.create_line(x, y, x + side, y + side, fill=couleur_de_base, width=3)
       canvas.create_line(x + side, y, x, y + side, fill=couleur_de_base, width=3)
    else:
        canvas.create_line(x, y, x + side, y + side, fill=couleur_b, width=3)
        canvas.create_line(x + side, y, x, y + side, fill=couleur_b, width=3)

def choisir_couleur():
    global couleur_b
    couleur = input("Entrez une couleur (white, black, red, green, blue, cyan, yellow) : ")
    if couleur in ["white", "black", "red", "green", "blue", "cyan", "yellow"]:
        couleur_b=couleur
    elif couleur not in ["white", "black", "red", "green", "blue", "cyan", "yellow", "normal"]:
            couleur = input("Couleur invalide, entrez une couleur valide (white, black, red, green, blue, cyan, yellow) : ")
            couleur_b=couleur



cercle = tk.Button(root, text="Cercle", command=dessiner_cercle)
carre = tk.Button(root, text="Carré", command=dessiner_carre)
croix = tk.Button(root, text="Croix", command=dessiner_croix)
couleur = tk.Button(root, text="Choisir une couleur", command=choisir_couleur)



cercle.grid(row=1, column=0, pady=5, padx=5)
carre.grid(row=2, column=0, pady=5, padx=5)
croix.grid(row=3, column=0, pady=5, padx=5)
couleur.grid(row=0, column=1)
root.mainloop()
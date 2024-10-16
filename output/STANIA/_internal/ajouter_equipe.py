# ici pour ajouter les equipes
from tkinter import *

from sql import inserer_equipe
from liste_equipes import page_table_equipes


def equipe():
    equipe_fenetre = Tk()
    equipe_fenetre.attributes('-fullscreen', False)
    equipe_fenetre.title("Ajouter Equipe")
    equipe_fenetre.configure(padx=600, pady=150)

    # titre de la page
    title_label = Label(equipe_fenetre, text="Ajouter une nouvelle equipe", font=("Arial", 30))
    title_label.place(x=-350, y=-140)

    # Creqtion de formulaire de creation du compte
    label_nom = Label(equipe_fenetre, text="Nom:")
    label_nom.grid(row=1, column=1)

    input_nom = Entry(equipe_fenetre)
    input_nom.grid(row=1, column=2)

    label_pays = Label(equipe_fenetre, text="Pays:")
    label_pays.grid(row=2, column=1)

    input_pays = Entry(equipe_fenetre)
    input_pays.grid(row=2, column=2, padx=10, pady=10)

    label_j1 = Label(equipe_fenetre, text="Joueur 1:")
    label_j1.grid(row=3, column=1)

    input_j1 = Entry(equipe_fenetre)
    input_j1.grid(row=3, column=2)

    label_j2 = Label(equipe_fenetre, text="Joueur 2:")
    label_j2.grid(row=4, column=1)

    input_j2 = Entry(equipe_fenetre)
    input_j2.grid(row=4, column=2)

    label_j3 = Label(equipe_fenetre, text="Joueur 3:")
    label_j3.grid(row=5, column=1)

    input_j3 = Entry(equipe_fenetre)
    input_j3.grid(row=5, column=2)

    label_j4 = Label(equipe_fenetre, text="Joueur 4:")
    label_j4.grid(row=6, column=1)

    input_j4 = Entry(equipe_fenetre)
    input_j4.grid(row=6, column=2)

    label_j5 = Label(equipe_fenetre, text="Joueur 5:")
    label_j5.grid(row=7, column=1)

    input_j5 = Entry(equipe_fenetre)
    input_j5.grid(row=7, column=2)

    label_j6 = Label(equipe_fenetre, text="Joueur 6:")
    label_j6.grid(row=9, column=1)

    input_j6 = Entry(equipe_fenetre)
    input_j6.grid(row=9, column=2)

    label_j7 = Label(equipe_fenetre, text="Joueur 7:")
    label_j7.grid(row=11, column=1)

    input_j7 = Entry(equipe_fenetre)
    input_j7.grid(row=11, column=2)

    def ajouter_equipe():
        nom = input_nom.get()
        pays = input_pays.get()
        j1 = input_j1.get()
        j2 = input_j2.get()
        j3 = input_j3.get()
        j4 = input_j4.get()
        j5 = input_j5.get()
        j6 = input_j6.get()
        j7 = input_j7.get()

        inserer_equipe(nom, pays, j1, j2, j3, j4, j5, j6, j7)


    boutton1 = Button(equipe_fenetre, text="Submit", command=ajouter_equipe)
    boutton1.grid(row=12, column=2, padx=5, pady=5)


    boutton2 = Button(equipe_fenetre, text="Liste des equipes", command=page_table_equipes)
    boutton2.grid(row=13, column=2, padx=5, pady=5)


    boutton4 = Button(equipe_fenetre, text="Retour")
    boutton4.grid(row=14, column=3, padx=5, pady=35)

    equipe_fenetre.mainloop()
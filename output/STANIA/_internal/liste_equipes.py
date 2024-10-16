# lister les equipes

from tkinter import *
from sql import liste_equipe, supprimer_equipe
from tkinter import ttk


def page_table_equipes():

    fnt_table_joueur = Tk()
    fnt_table_joueur.attributes('-fullscreen', False)
    fnt_table_joueur.title("Table Equipe")
    fnt_table_joueur.configure(padx=30, pady=120)

    title_label = Label(fnt_table_joueur, text="Table Joueurs", font=("Arial", 30))
    title_label.place(x=40, y=-90)

    table_joueur = liste_equipe()

    # creation du tableau tkinter
    tableau_etudiant = ttk.Treeview(fnt_table_joueur)

    # definition des colones
    tableau_etudiant["columns"] = ("Id", "Nom", "Pays", "Joueur 1", "Joueur 2", "Joueur 3", "Joueur 4", "Joueur 5", "Joueur 6", "Joueur 7")

    # En-tete du tableau
    tableau_etudiant.heading("Id", text="Id", anchor=CENTER)
    tableau_etudiant.column("Id", minwidth=0, width=70)

    tableau_etudiant.heading("Nom", text="Nom", anchor=CENTER)
    tableau_etudiant.column("Nom", minwidth=0, width=100)

    tableau_etudiant.heading("Pays", text="Pays", anchor=CENTER)
    tableau_etudiant.column("Pays", minwidth=0, width=100)

    tableau_etudiant.heading("Joueur 1", text="Joueur 1", anchor=CENTER)
    tableau_etudiant.column("Joueur 1", minwidth=0, width=70)

    tableau_etudiant.heading("Joueur 2", text="Joueur 2", anchor=CENTER)
    tableau_etudiant.column("Joueur 2", minwidth=0, width=70)

    tableau_etudiant.heading("Joueur 3", text="Joueur 3", anchor=CENTER)
    tableau_etudiant.column("Joueur 3", minwidth=0, width=70)

    tableau_etudiant.heading("Joueur 4", text="Joueur 4", anchor=CENTER)
    tableau_etudiant.column("Joueur 4", minwidth=0, width=70)

    tableau_etudiant.heading("Joueur 5", text="Joueur 5", anchor=CENTER)
    tableau_etudiant.column("Joueur 5", minwidth=0, width=70)

    tableau_etudiant.heading("Joueur 6", text="Joueur 6", anchor=CENTER)
    tableau_etudiant.column("Joueur 6", minwidth=0, width=70)

    tableau_etudiant.heading("Joueur 7", text="Joueur 7", anchor=CENTER)
    tableau_etudiant.column("Joueur 7", minwidth=0, width=70)

    for i in table_joueur:  # id    #nom   #prenom #age
        tableau_etudiant.insert(parent="", index="end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]))

    tableau_etudiant.grid(row=2, column=2)

    def supprimer():
        id = tableau_etudiant.item(tableau_etudiant.selection())['values'][0]
        supprimer_equipe(id)

    button1 = Button(fnt_table_joueur, text="Supprimer equipe", command=supprimer)
    button1.grid(row=3, column=2, pady=20)

    button1 = Button(fnt_table_joueur, text="Fermer")
    button1.grid(row=5, column=2, pady=20)

    fnt_table_joueur.mainloop()
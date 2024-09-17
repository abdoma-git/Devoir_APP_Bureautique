
from tkinter import *
from PIL import Image, ImageTk
from ajouter_joueur import joueur
from ajouter_equipe import equipe
from matchs import match

def open_dashboard(fenetre):

    fenetre.destroy()

    dashboard = Tk()
    dashboard.attributes('-fullscreen', True)
    dashboard.title("Nouveau Compte")
    dashboard.configure(padx=330, pady=120)


    title_label = Label(dashboard, text="Bonjour A STANIA", font=("Arial", 30))
    title_label.place(x=40, y=-90)

    # Image
    image1 = Image.open("images/tt.png")
    photo1 = ImageTk.PhotoImage(image1)

    image2 = Image.open("images/ajouter.jpg")
    photo2 = ImageTk.PhotoImage(image2)

    # Création d'un widget Label pour afficher l'image
    image_label1 = Label(dashboard, image=photo1, width=800, height=400)
    image_label1.place(x=-100, y=0)

    buttonyy = Button(dashboard, text="Fermer", command=exit)
    buttonyy.grid(row=5, column=8, padx=20, pady=150)

    button = Button(dashboard, text="Ajouter joueur", command=joueur)
    button.grid(row=6, column=1, padx=20, pady=150)

    button2 = Button(dashboard, text="Ajouter Match", command=match)
    button2.grid(row=6, column=2, padx=20, pady=150)

    button3 = Button(dashboard, text="Ajouter Equipe", command=equipe)
    button3.grid(row=6, column=3, padx=20, pady=150)


    dashboard.mainloop()



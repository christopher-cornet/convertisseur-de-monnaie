from tkinter import *

# Créer une fenêtre
root = Tk()

# Titre
root.title("Convertisseur de monnaie")
# Dimensions
root.geometry('400x300')

# Liste des monnaies
options = ["EUR", "USD"]

# Bouton/Menu currency1 = choix de la devise: soit euro ou dollar
chooseCurrency1 = Label(root, text="Choisir la devise:")
chooseCurrency1.grid(row=0, column=0, padx=40, pady=15)

clicked = StringVar()
clicked.set("EUR")
currency1 = OptionMenu(root, clicked, *options)
currency1.grid(row=1, column=0)
currency1.config(bg="#0788D1")

chooseCurrency1 = Label(root, text="Valeur:")
chooseCurrency1.grid(row=2, column=0, pady=10)

nombre_valeur1 = Entry(root, width=20)
nombre_valeur1.grid(row=3, column=0)

# Bouton/Menu currency2 = choix de la devise: soit euro ou dollar
choisirDevise2 = Label(root, text="Choisir la devise:")
choisirDevise2.grid(row=0, column=1, padx=80)

clicked2 = StringVar()
clicked2.set("USD")
currency2 = OptionMenu(root, clicked2, *options)
currency2.grid(row=1, column=1)
currency2.config(bg="#0788D1")

choisirDevise2 = Label(root, text="Valeur convertie:")
choisirDevise2.grid(row=2, column=1)

nombre_valeur2 = Entry(root, width=20)
nombre_valeur2.grid(row=3, column=1)
nombre_valeur2.config(state="disabled")

# Fonction pour faire fonctionner la conversion
def convert():
    if clicked.get() == "EUR" and clicked2.get() == "EUR":
        print("Erreur ! Vous ne pouvez pas convertir EUR vers EUR.")
    elif clicked.get() == "USD" and clicked2.get() == "USD":
        print("Erreur ! Vous ne pouvez pas convertir USD vers USD.")
    elif clicked.get() == "EUR" and clicked2.get() == "USD":
        conversion = float(nombre_valeur1.get()) * 1.08 # Euro vers USD
        round_conversion = round(conversion, 2)
        print(round_conversion)
    elif clicked.get() == "USD" and clicked2.get() == "EUR":
        conversion = float(nombre_valeur1.get()) * 0.92 # USD vers Euro
        round_conversion = round(conversion, 2) # Jusqu'à 2 décimales
        print(round_conversion)
    # Faire une condition en fonction de si j'ai mis euro ou dollar pour multiplier par 1.08 (euro dollar) ou par 0.92 (dollar euro)

# Bouton convertir qui donne le résultat
convert_button = Button(root, text="Convertir", bg="#0788D1", fg="white", command=convert)
convert_button.grid(row=4, column=0, pady=10)

# Rajouter un bouton clear qui reset tout

# Faire un historique des conversions accessibles depuis un bouton qui print l'historique (save)

# Execute Tkinter
root.mainloop()
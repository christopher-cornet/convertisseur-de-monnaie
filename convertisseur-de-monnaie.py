from tkinter import *
from tkinter import messagebox

# Créer une fenêtre
root = Tk()
# Titre
root.title("Convertisseur de monnaie - Christopher CORNET")
# Dimensions
root.geometry('450x300')
# Icône
root.iconbitmap('currency.ico')

# Liste des monnaies
options = ["EUR", "USD"]

# Bouton/Menu currency1 = choix de la devise: soit euro ou dollar
chooseCurrency1 = Label(root, text="Choisir la devise:")
chooseCurrency1.grid(row=0, column=0, padx=60, pady=15)

clicked = StringVar()
clicked.set("EUR")

currency1 = OptionMenu(root, clicked, *options)
currency1.grid(row=1, column=0)
currency1.config(bg="#0788D1")
 
chooseCurrency1 = Label(root, text="Valeur:")
chooseCurrency1.grid(row=2, column=0, pady=10)

nb_value1 = Entry(root, width=20)
nb_value1.grid(row=3, column=0)

# Bouton/Menu currency2 = choix de la devise: soit euro ou dollar
choisirDevise2 = Label(root, text="Choisir la devise:")
choisirDevise2.grid(row=0, column=1, padx=80)

clicked2 = StringVar()
clicked2.set("USD")

currency2 = OptionMenu(root, clicked2, *options)
currency2.grid(row=1, column=1)
currency2.config(bg="#0788D1")

# Fonction pour faire fonctionner la conversion
def convert():
    if clicked.get() == "EUR" and clicked2.get() == "EUR":
        messagebox.showwarning("Erreur de conversion", "Erreur ! Vous ne pouvez pas convertir EUR en EUR.")
    elif clicked.get() == "USD" and clicked2.get() == "USD":
        messagebox.showwarning("Erreur de conversion", "Erreur ! Vous ne pouvez pas convertir USD en USD.")
    elif clicked.get() == "EUR" and clicked2.get() == "USD":
        conversion = float(nb_value1.get()) * 1.08 # Euro vers USD
        round_conversion = round(conversion, 2) # Jusqu'à 2 décimales
        nb_converted.config(state="normal")
        nb_converted.insert(0, round_conversion)
        # Ajout dans une variable qui est ensuite print dans l'historique avec les autres conversions
    elif clicked.get() == "USD" and clicked2.get() == "EUR":
        conversion = float(nb_value1.get()) * 0.92 # USD vers Euro
        round_conversion = round(conversion, 2) 
        nb_converted.config(state="normal")
        nb_converted.insert(0, round_conversion)

def delete():
    nb_converted.delete(0, 'end')

def deleteAll():
    nb_converted.delete(0, 'end')
    nb_value1.delete(0, 'end')
        
# Nombre une fois converti
choisirDevise2 = Label(root, text="Valeur convertie:")
choisirDevise2.grid(row=2, column=1)

nb_converted = Entry(root, width=20)
nb_converted.grid(row=3, column=1)
nb_converted.config(state="disabled")

# Bouton convertir qui affiche le résultat
convert_button = Button(root, text="Convertir", bg="#0788D1", fg="white", command=convert)
convert_button.grid(row=4, column=0, pady=10)

# Bouton qui supprime la valeur convertie
clear_button = Button(root, text="Supprimer", bg="#0788D1", fg="white", command=delete)
clear_button.grid(row=4, column=1, pady=10)

# Bouton qui supprime la valeur à convertir et la valeur convertie
clear_all_button = Button(root, text="Tout supprimer", bg="#0788D1", fg="white", command=deleteAll)
clear_all_button.grid(row=5, column=1, pady=10)

# Faire un historique des conversions accessibles depuis un bouton qui print l'historique (save)

# Lance Tkinter
root.mainloop()
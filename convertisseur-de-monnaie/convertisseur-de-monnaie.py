from tkinter import *
from tkinter import messagebox
import subprocess
import os

root = Tk()
root.title("Convertisseur de monnaie - Christopher CORNET")
root.geometry('450x300')
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

# Effectuer la conversion
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
        file_history = open("historique_conversions.txt", "a") # Ouvre le fichier, écrit la conversion faite et le ferme
        file_history.write("{} {} {} {}\n".format(nb_value1.get(), "EUR en USD =", round_conversion, "$"))
        file_history.close()
    elif clicked.get() == "USD" and clicked2.get() == "EUR":
        conversion = float(nb_value1.get()) * 0.92 # USD vers Euro
        round_conversion = round(conversion, 2) 
        nb_converted.config(state="normal")
        nb_converted.insert(0, round_conversion)
        file_history = open("historique_conversions.txt", "a")
        file_history.write("{} {} {} {}\n".format(nb_value1.get(), "USD en EUR =", round_conversion, "€"))
        file_history.close()

# Effacer la valeur convertie
def delete():
    nb_converted.delete(0, 'end')

# Effacer toutes les valeurs
def deleteValue1AndConverted():
    nb_converted.delete(0, 'end')
    nb_value1.delete(0, 'end')

# Supprime l'historique
def deleteHistory():
    messagebox.askquestion("Confirmation","Voulez-vous supprimer l'historique ?")  
    os.remove("historique_conversions.txt")
        
# Le nombre une fois converti
choisirDevise2 = Label(root, text="Valeur convertie:")
choisirDevise2.grid(row=2, column=1)

nb_converted = Entry(root, width=20)
nb_converted.grid(row=3, column=1)
nb_converted.config(state="disabled")

# Bouton convertir qui affiche le résultat
convert_button = Button(root, text="Convertir", bg="#53D317", fg="white", command=convert)
convert_button.grid(row=4, column=0, pady=10)

# Bouton qui supprime la valeur convertie
clear_button = Button(root, text="Supprimer", bg="#FF1A1A", fg="white", command=delete)
clear_button.grid(row=4, column=1, pady=10)

# Bouton qui supprime la valeur à convertir et la valeur convertie
clear_values_button = Button(root, text="Supprimer les valeurs", bg="#FF1A1A", fg="white", command=deleteValue1AndConverted)
clear_values_button.grid(row=5, column=1, pady=10)

# Bouton qui supprime l'historique des conversions
clear_all_button = Button(root, text="Supprimer l'historique", bg="#FF1A1A", fg="white", command=deleteHistory)
clear_all_button.grid(row=6, column=1, pady=10)

# Historique des conversions faites.
def history():
    file_history = "./historique_conversions.txt"
    if os.path.exists(file_history):
        subprocess.run(r"historique_conversions.txt",shell=True)
    else:
        messagebox.showerror("Erreur","Le fichier auquel vous voulez accéder n'existe pas/plus.")

get_history = Button(root, text="Historique", bg="#FFB413", fg="white", command=history)
get_history.grid(row=5, column=0, pady=10)

# Lance Tkinter
root.mainloop()
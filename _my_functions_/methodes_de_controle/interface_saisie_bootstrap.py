import os
import tkinter as tk
from tkinter import messagebox, filedialog
from ttkbootstrap import Style
from datetime import datetime
import csv
import json
import pandas as pd
from dicttoxml import dicttoxml
from fpdf import FPDF


class SingletonMeta(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        """Crée une nouvelle instance de la classe si elle n'existe pas déjà."""
        if self not in self._instances:
            instance = super().__call__(*args, **kwargs)
            self._instances[self] = instance
        return self._instances[self]


class EnregistreurFichier:
    """Classe pour l'enregistrement des données dans un fichier."""

    def __init__(self, repertoire, nom_fichier, donnees):
        self.chemin = os.path.join(repertoire, nom_fichier)
        self.donnees = donnees
        self.repertoire=repertoire

    def enregistrer(self):
        """Enregistre les données dans un fichier."""
        extension = os.path.splitext(self.chemin)[1]
        sous_repertoire = os.path.join(self.repertoire, extension.lstrip('.'))
        os.makedirs(sous_repertoire, exist_ok=True)
        chemin_complet = os.path.join(sous_repertoire, os.path.basename(self.chemin))

        if extension == '.txt':
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                f.write(self.donnees)
        elif extension == '.csv':
            with open(chemin_complet, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(self.donnees.keys())
                writer.writerow(self.donnees.values())
        elif extension == '.json':
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                json.dump(self.donnees, f, ensure_ascii=False)
        elif extension == '.xml':
            with open(chemin_complet, 'w', encoding='utf-8') as f:
                f.write(dicttoxml(self.donnees).decode())
        elif extension == '.xlsx':
            df = pd.DataFrame([self.donnees])
            df.to_excel(chemin_complet, index=False)
        elif extension == '.pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for i, (key, val) in enumerate(self.donnees.items()):
                pdf.cell(200, 10, txt=f"{key}: {val}", ln=i+1, align='C')
            pdf.output(chemin_complet)
        

class Application(tk.Tk, metaclass=SingletonMeta):
    """Application pour la saisie des informations."""

    def __init__(self):
        super().__init__()
        self.title("Saisie des informations")
        self.style = Style('superhero')
        self.style.theme_use()

        # Centrer la fenêtre et ajouter des marges
        self.geometry("800x800")
        self.configure(bg='white')
        self.pack_propagate(False)

        # Créer un cadre pour contenir tous les widgets
        cadre = tk.Frame(self, bg='white', padx=20, pady=10)
        cadre.pack(fill='both', expand=True)

        # Créer les champs de saisie avec les valeurs par défaut
        self.champs = ['Nom', 'Prénom', 'Adresse', 'Âge', 'Téléphone', 'Email', 'Répertoire par défaut',
                       'Nom de fichier']
        valeurs_par_defaut = ['Dupont', 'Marcel', '12 avenue du roi vert 56212 Montvers', '23 ans',
                              '06 08 52 36 24', 'dupont@free.fr', 'G:\programmation\python\openClassRoomModulePython\datas', f'test_enregistrement-{datetime.now().strftime("%d-%m-%y")}']
        self.entries = {}

        for champ, valeur_par_defaut in zip(self.champs, valeurs_par_defaut):
            frame = tk.Frame(cadre, bg='white')
            # Ajouter une marge verticale entre les champs
            frame.pack(fill='x', pady=10)
            label = tk.Label(frame, text=champ, bg='white')
            label.pack(side='left')
            entry = tk.Entry(frame)
            # Ajouter une valeur par défaut à chaque champ de saisie
            entry.insert(0, valeur_par_defaut)
            entry.pack(side='right', fill='x', expand=True)
            self.entries[champ] = entry

        # Créer la checkbox pour les conditions contractuelles
        self.conditions_var = tk.BooleanVar()
        checkbox = tk.Checkbutton(cadre, text="J'accepte les conditions contractuelles", variable=self.conditions_var,
                                  bg='white')
        checkbox.pack()

        # Créer la liste déroulante pour les extensions à exclure
        frame_extensions_a_exclure = tk.Frame(cadre, bg='white')
        frame_extensions_a_exclure.pack(fill='x', pady=10)
        label_extensions_a_exclure = tk.Label(
            frame_extensions_a_exclure, text="Extensions à exclure", bg='white')
# suite
        label_extensions_a_exclure.pack(side='left')
        self.extensions_a_exclure = tk.Listbox(
            frame_extensions_a_exclure, selectmode='multiple')
        for item in ['.txt', '.py', '.csv', '.xml', '.json', '.xlsx', '.pdf']:
            self.extensions_a_exclure.insert('end', item)
        self.extensions_a_exclure.pack(side='right', fill='x', expand=True)

        # Créer la liste déroulante pour le format du fichier à enregistrer
        frame_format_fichier = tk.Frame(cadre, bg='white')
        frame_format_fichier.pack(fill='x', pady=10)
        label_format_fichier = tk.Label(
            frame_format_fichier, text="Format du fichier", bg='white')
        label_format_fichier.pack(side='left')
        self.format_fichier_var = tk.StringVar()
        liste_deroulante_format_fichier = tk.OptionMenu(frame_format_fichier, self.format_fichier_var,
                                                        '.txt', '.py', '.csv', '.xml', '.json', '.pdf', '.xlsx')
        liste_deroulante_format_fichier.pack(
            side='right', fill='x', expand=True)

        # Créer les boutons OK et Annuler
        frame_boutons = tk.Frame(cadre, bg='white')
        frame_boutons.pack(fill='x', pady=10)
        bouton_ok = tk.Button(frame_boutons, text="OK",
                              command=self.valider, bg='green')
        bouton_ok.pack(side='left')
        bouton_annuler = tk.Button(
            frame_boutons, text="Annuler", command=self.annuler, bg='orange')
        bouton_annuler.pack(side='right')

#
    def valider(self):
        """Valide les entrées de l'utilisateur."""
        if not self.conditions_var.get():
            messagebox.showerror(
                "Erreur", "Vous devez accepter les conditions contractuelles.")
            return
        for champ, entry in self.entries.items():
            if not entry.get():
                messagebox.showerror("Erreur", f"Le champ {
                                     champ} est obligatoire.")
                return
        # Convertir les données en un dictionnaire
        donnees = {champ: entry.get() for champ, entry in self.entries.items()}
        # Enregistrer les données dans un fichier
        repertoire = self.entries['Répertoire par défaut'].get()
        nom_fichier = self.entries['Nom de fichier'].get(
        ) + self.format_fichier_var.get()
        enregistreur = EnregistreurFichier(repertoire, nom_fichier, donnees)
        enregistreur.enregistrer()
        messagebox.showinfo(
            "Succès", "Les données ont été enregistrées avec succès.")
        self.destroy()  # Fermer la fenêtre après l'enregistrement des données

    def annuler(self):
        """Annule les entrées de l'utilisateur et ferme la fenêtre."""
        self.destroy()


if __name__ == "__main__":
    app = Application()
    app.mainloop()

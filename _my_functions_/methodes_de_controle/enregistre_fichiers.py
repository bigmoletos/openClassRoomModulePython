import csv
import json
import pandas as pd
from dicttoxml import dicttoxml
from fpdf import FPDF

class EnregistreurFichier:
    """Classe pour l'enregistrement des données dans un fichier."""

    def __init__(self, repertoire, nom_fichier, donnees):
        self.chemin = os.path.join(repertoire, nom_fichier)
        self.donnees = donnees

    def enregistrer(self):
        """Enregistre les données dans un fichier."""
        extension = os.path.splitext(self.chemin)[1]
        if extension == '.txt':
            with open(self.chemin, 'w') as f:
                f.write(self.donnees)
        elif extension == '.csv':
            with open(self.chemin, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerow(self.donnees.keys())
                writer.writerow(self.donnees.values())
        elif extension == '.json':
            with open(self.chemin, 'w') as f:
                json.dump(self.donnees, f)
        elif extension == '.xml':
            with open(self.chemin, 'w') as f:
                f.write(dicttoxml(self.donnees).decode())
        elif extension == '.xlsx':
            df = pd.DataFrame([self.donnees])
            df.to_excel(self.chemin, index=False)
        elif extension == '.pdf':
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            for i, (key, val) in enumerate(self.donnees.items()):
                pdf.cell(200, 10, txt=f"{key}: {val}", ln=i+1, align='C')
            pdf.output(self.chemin)

from informations_projet import InformationsProjet

def main():
    # Créer une instance de la classe InformationsProjet
    info_projet = InformationsProjet()

    # Tester toutes les fonctions
    print("Informations du nom du projet : ", info_projet.obtenir_info_projet())
    print("Répertoire de travail : ", info_projet.obtenir_repertoire_travail())
    print("Informations du package : ", info_projet.obtenir_info_package())
    print("Liste des répertoires : ", info_projet.obtenir_liste_repertoires())
    print("Fichiers dans le répertoire : ", info_projet.obtenir_fichiers_repertoire())
    print("Dossiers dans le répertoire de travail : ", info_projet.obtenir_dossiers_repertoire_travail())
    print("Fichiers Python sans extension : ", info_projet.obtenir_fichiers_python_sans_ext())

if __name__ == "__main__":
    main()
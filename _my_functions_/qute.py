

# while True:
#     try:
#         borne1=int(input("veuillez entrer le premier chiffre: ").strip())
#         borne2=int(input("veuillez entrer le deuxième chiffre: ").strip())
       
#         print(f"vous avez entré les chiffres suivants: \n Borne1={borne1}\n Borne2={borne2}")
#         borne3=int(input("veuillez entrer le 3éme chiffre: ").strip())
        
       

#         if borne3<borne1 and borne3<borne2:
#             print(f"votre 3éme borne= {borne3} est \n inférieure à la borne1={borne1} ")
#         elif borne3>=borne1 and borne3<=borne2:
#             print(f"votre 3éme borne= {borne3} est \n comprise entre les borne1={borne1} et la borne2={borne2}")
#         else:
#             print(f"votre 3éme borne= {borne3} est \n superieure à la borne2={borne2} ")
        
#     except ValueError:
#         print("Erreur : veuillez saisir uniquement des chiffres entier")
#     message=input("""Vous avez saisi des erreurs voulez-vous arreter le programme ou continuer ?
#                   tapez Oui(o) pour arreter
#                   tapez sur n'importe quelle touche pour continuer:  """)
    
#     if message.lower()  in ['o', 'oui','y','yes']:
#         break
        

# for number in range(4,-1,-2) :
#     print(number)

#table de muliplication de 1 à 10
resultat=0
# boucle de 1 à 10
for table in range (1,11):
    #je place réinitialise le tableau à chaque fois sinon il se rempli de toutes les tables
    table_muliplication=[]
    # print("table multiplication",table_muliplication)
    print(f"la table de multiplication de {table} : ")
    
    # boucle de 1 à  10 ou de 1 à 5 en fonction de la table
    for multiplicateur in range (1,6 if table>=5 else 11):
        resultat=table*multiplicateur
        # j'ajoute à la liste "table_multiplication" le resultat du calcul
        table_muliplication.append(str(resultat))
        #je retire les [] et les '' du tableau en le convertissant en string

        # print(f"{table} * {multiplicateur}  = {resultat}")
    print(table_muliplication)
# print("\n")

# ecrire un programme qui transforme les secondes en mois jour heure seconde
# input en seconde
seconde=int(input("veuillez saisir un chiffre entier de secondes"))
# 1 mois = 30j, 1 années=365 j, 1jour 24h, 1heure 60minute 1 minute 60s

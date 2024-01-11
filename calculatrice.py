
def calculatrice():
    historique = []

    while True:
        try:
            nombre1 = float(input("Entrez le premier chiffre/nombre : "))
            nombre2 = float(input("Entrez le deuxième chiffre/nombre : "))
            operation = input("Entrez l'opération (+, -, *, /) : ")
            if operation == '+':
                resultat = nombre1 + nombre2
            elif operation == '-':
                resultat = nombre1 - nombre2
            elif operation == '*':
                resultat = nombre1 * nombre2
            elif operation == '/':
        
                if nombre2 == 0:
    
                    raise ValueError("Erreur, la division n'existe pas!.")
                resultat = nombre1 / nombre2
            else:
                raise ValueError("Erreur : Opération non valide.")
             
            historique.append(f"{nombre1} {operation} {nombre2} = {resultat}")

    
            print(f"Résultat : {resultat}")
       
            effacer_historique = input(" Effacer l'historique? (Oui/Non) : ").lower()
            if effacer_historique == 'oui':
                historique = [] 


        except ValueError as e:
            print(f"Erreur : {e}")
   
        except Exception as e:
            print(f"Une erreur s'est produite: {e}")

         # Afficher l'historique
        print("Liste des calculs effectués :")
        for calcul in historique:
            print(calcul)
            
calculatrice()

import json
from joueur import creer_joueur

# Ouvre la liste de dictionnaires items et va la lire.
with open('items.json', 'r') as f:
    donnee_item = json.load(f)

def io_cli():
    nom = "404"
    joueur = creer_joueur(nom)

    # Boucle avec les choix
    en_cours = True
    while en_cours:
        print("Actions disponibles:")
        print("\n 1) Attaquer votre adversaire")
        print("\n 2) Prendre la fuite")
        print("\n 3) Utiliser un item")
        
        # Choix pris par le joueur (Attaquer, Fuire ou Utiliser un item).
        choix_pris = int(input("Prenez une décision en tapant 1, 2 ou 3 selon les actions respectives."))
        if choix_pris == 1:
            print("Vous êtes en train d'attaquer l'adversaire.")
        
        elif choix_pris == 2:
            print("Vous tentez de fuir.")
        
        elif choix_pris == 3:
            
            # Affiche l'inventaire du joueur pour lui permettre de voir les items qu'il possède.
            print("Inventaire:", joueur["Inventaire"])

            if joueur["Inventaire"]:                        # Vérifie l'existence d'item(s) dans l'inventaire
                print("Quel item voulez-vous utiliser ?")
                item_use = input().strip()                  # Permet d'enlever les espaces qui sont présent dans le input

                # Sécurité en plus pour ne pas avoir d'erreur
                if item_use == "":
                    print("Veuillez entrer un nom d'item correct.")
                    continue

                # Vérifie que l'item existe dans notre base de donnee des items
                if item_use not in donnee_item:
                    print("Cet item n'existe pas.")
                    continue
                
                # Vérifie que l'item que le joueur veut utiliser est bien dans l'inventaire du joueur.
                if item_use not in joueur["Inventaire"]:
                    print("Cet item n'est pas dans votre inventaire.")
                    continue

                item_info = donnee_item[item_use]                    # Va voir les info qu'on a de l'item
                effects = item_info["effects"]                       # Va voir les effets de l'item

                # Si Heal est l'effet de l'item, ajouter des PV au joueur.    
                if "heal" in effects:
                    joueur["PV"] = min(joueur["PV_MAX"], joueur["PV"] + effects["heal"])                                         #Prend la valeur la plus petite entre pv max et pv.
                    print(f"Vous regagnez {effects['heal']} PV ! (PV actuels : {joueur['PV']}/{joueur['PV_MAX']})")

                # Si Damage est l'effet de l'item, augmenter les dégats infliger à l'adversaire.
                elif "damage" in effects:
                    print(f"Vous infligez {effects['damage']} dégats à l'adversaire !")
                
                # Si Fuite est l'effet de l'item, ajouter un pourcentage de fuite.
                elif "fuite" in effects:
                    print(f"Vos chances de fuite ont augmenté de {effects['fuite']}% !")

                # Si l'item est de type consommable, l'enlever de l'inventaire du joueur après utilisation.    
                if item_info["type"] == "consommable":
                    joueur["Inventaire"].remove(item_use)
                    print(f"L'objet {item_use} a été consommé.")
                
                # Si l'item n'est pas de type consommable, le laisser dans l'inventaire.
                else:
                    print(f"Vous avez utilisé l'objet {item_use}, il reste dans votre inventaire.")

            # Si il n'y a aucun item dans l'inventaire.
            else:
                print("Votre inventaire est vide.")

        #Si le choix n'est ni 1, ni 2 et ni 3.        
        else:
            print("Choix invalide. Veuillez réessayer.")
import json
from player import creer_joueur


with open('items.json', 'r') as f:
    donnee_item = json.load(f)

def io_cli():
    nom = "404"
    joueur = creer_joueur(nom)

    #Boucle
    en_cours = True
    while en_cours:
        print("Actions disponibles:")
        print("\n 1) Attaquer votre adversaire")
        print("\n 2) Prendre la fuite")
        print("\n 3) Utiliser un item")
        
        choix_pris = int(input("Prenez une décision en tapant 1, 2 ou 3 selon les actions respectives."))
        if choix_pris == 1:
            print("Vous êtes en train d'attaquer l'adversaire.")
        
        elif choix_pris == 2:
            print("Vous tentez de fuir.")
        
        elif choix_pris == 3:
            
            print("Inventaire:", joueur["Inventaire"])

            if joueur["Inventaire"]:                        #Vérifie l'existence d'item(s) dans l'inventaire
                print("Quel item voulez-vous utiliser ?")
                item_use = input().strip()                  #Permet d'enlever les espaces qui sont présent dans le input

                #Sécurité en plus pour ne pas avoir d'erreur
                if item_use == "":
                    print("Veuillez entrer un nom d'item.")
                    continue

                #Vérifie que l'item existe dans notre base de donnee des items
                if item_use not in donnee_item:
                    print("Cet item n'existe pas.")
                    continue
                
                #Vérifie que l'item que le joueur veut utiliser est bien dans l'inventaire du joueur.
                if item_use not in joueur["Inventaire"]:
                    print("Cet item n'est pas dans votre inventaire.")
                    continue

                item_info = donnee_item[item_use]                    #Va voir les info qu'on a de l'item
                effects = item_info["effects"]                       #Va voir les effets de l'item
                    
                if "heal" in effects:
                    joueur["PV"] = min(joueur["PV_MAX"], joueur["PV"] + effects["heal"])                                         #Prend la valeur la plus petite entre pv max et pv.
                    print(f"Vous regagnez {effects['heal']} PV ! (PV actuels : {joueur['PV']}/{joueur['PV_MAX']})")

                elif "damage" in effects:
                    print(f"Vous infligez {effects['damage']} dégats à l'adversaire !")

                elif "fuite" in effects:
                    print(f"Vos chances de fuite ont augmenté de {effects['fuite']}% !")

                    
                if item_info["type"] == "consommable":
                    joueur["Inventaire"].remove(item_use)
                    print(f"L'objet {item_use} a été consommé.")

                else:
                    print(f"Vous avez utilisé l'objet {item_use}, il reste dans votre inventaire.")

            else:
                print("Votre inventaire est vide.")
        else:
            print("Choix invalide. Veuillez réessayer.")
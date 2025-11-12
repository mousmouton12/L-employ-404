import json
from player import creer_joueur


with open('item.json', 'r') as f:
    donnee_item = json.load(f)

def io_cli():
    nom = "404"
    joueur = creer_joueur(nom)

    #Boucle
    in_progres = True
    while in_progres:
        print("Actions disponibles:")
        print("\n 1) Attaquer votre adversaire")
        print("\n 2) Prendre la fuite")
        print("\n 3) Utiliser un item")
        
        choix_pris = int(input("Prenez une décision en tapant 1, 2 ou 3 selon les actions respectives."))
        if choix_pris == 1:
            print("Vous être en train d'attaquer l'adversaire.")
        
        elif choix_pris == 2:
            print("Vous tentez de fuir.")
        
        elif choix_pris == 3:
             if joueur["Inventaire"]:                        #Vérifie l'existence d'item(s) dans l'inventaire
                print("Quel item voulez-vous utiliser ?")
                item_use = input()

                item_info = donnee_item[item_use]                    #Va voir les info qu'on a de l'item
                effects = item_info["effects"]                       #Va voir les effets de l'item

                if item_use in joueur["Inventaire"]:
                    print("Vous avez utilisé", item_use)
                    
                    if effects == "heal":
                        joueur["PV"] = min(joueur["PV_MAX"], joueur["PV"] + effects["heal"])                                         #Prend la valeur la plus petite entre pv max et pv.
                        print(f"Vous regagnez {effects['heal']} PV ! (PV actuels : {joueur['PV']}/{joueur['PV_MAX']})")

                    elif effects == "damage":
                        print(f"Vous infligez {effects['damage']} dégats à l'adversaire !")

                    elif effects == "fuite":
                        print(f"Vos chances de fuite ont augmenté de {effects['fuite']}% !")

                    
                    if item_use["type"] == "consommable":
                        joueur["Inventaire"].remove(item.use)
                        print(f"L'objet {item_use} a été consommé.")

                    else:
                        print(f"Vous avez utilisé l'objet {item_use}, il reste dans votre inventaire.")

                else:
                    print("Item non trouvé dans l'inventaire.")
            else:
                print("Votre inventaire est vide.")
        else:
            print("Choix invalide. Veuillez réessayer.")
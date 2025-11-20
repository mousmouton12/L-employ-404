def creer_joueur(nom):

    joueur = {
        "nom":nom,
        "PV":20,          #PV initial
        "PV_MAX":20,      #PV max initial (sans boosts)
        "ATK":8,          #Attaque initial (sans boosts)
        "Inventaire": [], #Liste qui va comprendre la place de stock qu'il y a dans l'inventaire.
        "Competences": [],  #Liste qui va comprendre les différentes compétences du personnage.
        "Bouclier": 0,
        "Bonus_fuite": 0,
        "score": 0
    }

    return joueur

def ajouter_arme(joueur, arme):
    joueur["Inventaire"].append(arme)
    if "damage" in arme["effects"]:
        bonus_degats = arme["effects"]["damage"]
        joueur["ATK"] = joueur["ATK"] + bonus_degats
        print("Vous avez équipé", arme["name"],"! Votre attaque augmente de", bonus_degats,"(Total :", joueur["ATK"],")")
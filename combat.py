import random
from systems.io_cli import joueur_choix
from systems.io_cli import item_choix

def appliquer_degats(attaquant, defenseur):
    degats_infliges = 0              #Sert comme sécurité (initialisation par défaut)
    if "ATK" in attaquant:           #Pour si l'attaquant est un ennemi ou le joueur
        degats_infliges = attaquant["ATK"]
    elif "value" in attaquant:       #Pour si l'attaquant est un objet qui fait des dégats
        degats_infliges = attaquant["value"]

    bouclier_restant = 0             #Sert comme sécurité (initialisation par défaut)
    if "Bouclier" in defenseur:
        bouclier_restant = defenseur["Bouclier"]

    print("Tentative d'infliger", degats_infliges, "dégâts")

    if degats_infliges > bouclier_restant:        #Quand on casse le bouclier
        degats_restant = degats_infliges - bouclier_restant
        defenseur["Bouclier"] = 0
        defenseur["PV"] = defenseur["PV"] - degats_restant
        if bouclier_restant > 0:                  #Pour que le message ne s'affiche qu'une seule fois
            print("Le bouclier s'est brisé")
        print (defenseur["name"], "subit", degats_restant, "dégâts")

    else:                                         #Si le bouclier absorbe tout
        defenseur["Bouclier"] = defenseur["Bouclier"] - degats_infliges
        print("Le bouclier absorbe tout les dégâts. Bouclier restant :", defenseur["Bouclier"])

    if defenseur["PV"] < 0:                       #Pas de PV négatifs
        defenseur["PV"] = 0


def choisir_cible(liste_ennemis):
    vivants = []
    for ennemi in liste_ennemis:                  #Permet de check pour tout les ennemis et de les rajoutés aux vivants
        if ennemi["PV"] > 0:                      #si c'est le cas
            vivants.append(ennemi)

    tank = []                                     #Permettra de forcer à attaquer les sacs à PV avant les monstres
    for ennemi in vivants:                        #qui attaquent
        if ennemi["ability"]["type"] == "block":
            tank.append(ennemi)

    cibles_possibles = []                         #Sert comme sécurité (initialisation par défaut)
    if len(tank) > 0:                             #Si présence de tank, seul eux peuvent être des cibles)
        cibles_possibles = tank
        print("\n!!! Un ennemi protège les autres ! Vous devez éliminer le(s) tank(s) en premier !!!")
    else:
        cibles_possibles = vivants

    print("Qui voulez-vous attaquer ? ")
    for i in range(len(cibles_possibles)):
        ennemi = cibles_possibles[i]
        print(i + 1, ")", ennemi["name"], "(PV :", ennemi["PV"], ")")  #Fait la liste des ennemis attaquables 1)... 2)...

    choix = joueur_choix("Choisissez la cible de l'attaque", 1, len(cibles_possibles))
    return cibles_possibles[choix-1]              # -1 car premier element de la liste --> 0


def afficher_etat(joueur, liste_ennemis):
    bonus_fuite = 0                               #Sert comme sécurité (initialisation par défaut)
    if "Bonus_fuite" in joueur:                   #Si il y a une relique pour fuir
        bonus_fuite = joueur["Bonus_fuite"]

    chance_fuite = 10 + bonus_fuite

    bouclier_joueur = 0                           #Sert à rien en soit mais est important pour que la fonction au dessus
    if "Bouclier" in joueur:                      #marche bien ou si on veut créer un objet bouclier
        bouclier_joueur = joueur["Bouclier"]

    print("-"*40)                                 #Statut du joueur et des ennemis
    print(joueur["nom"])
    print("PV :", joueur["PV"], "/", joueur["PV_MAX"])
    print("ATK :", joueur["ATK"])
    print("Inventaire :", [item["name"] for item in joueur["Inventaire"]])
    print("Chance de fuite :", chance_fuite,"%")
    print("\nEnnemis")
    for ennemi in liste_ennemis:
        etat = ""
        if ennemi["PV"] <= 0:
            etat = "(Mort)"
        print(ennemi["name"], "PV :", ennemi["PV"], "ATK :", ennemi["ATK"], etat)
    print("-"*40)

def tenter_fuite(joueur):
    bonus_fuite = 0
    if "Bonus_fuite" in joueur:
        bonus_fuite = joueur["Bonus_fuite"]
    chance_fuite = 10 + bonus_fuite
    chance_fuite = min(chance_fuite, 100)          #Pour ne pas avoir une chance de + de 100% pour fuir
    nombre_fuite = random.randint(1, 100)
    print("Tentative de fuite...")

    if chance_fuite <= nombre_fuite:
        print("Tentative réussie ! Vous passez à l'étage suivant")
        return True
    else:
        print("Échec ! Le combat continue...")
        return False

def utiliser_objets(joueur, liste_ennemis, items):
    if not joueur["Inventaire"]:
        print("Inventaire vide. Choisissez une autre action")
        return False
    print("\nInventaire :", [item["name"] for item in joueur["Inventaire"]])
    item_utilisee = item_choix("Quel item voulez-vous utiliser ? (Entrez le nom)")

    item_inventaire = None
    for item in joueur["Inventaire"]:               #Tente de trouver l'objet dans l'inventaire
        if item["name"] == item_utilisee:
            item_inventaire = item
            break

    if item_inventaire is None:                     #Si aucun item trouvé, reste None
        print("L'item", item_utilisee, "n'est pas dans l'inventaire")
        return False
    print("Vous utilisez", item_inventaire,"!")     #On ne peut arriver ici que si l'objet à été trouvé

    effet = item_inventaire["effects"]
    if "heal" in effet:
        soin = effet["heal"]
        joueur["PV"] = min(joueur["PV_MAX"], joueur["PV"] +soin)    #Pas dépasser les PV maximums du joueur
        print("Vous regagnez", soin, "PV ! (PV actuels :",joueur["PV"],"/", joueur["PV_MAX"],")")

    if "damage" in effet:
        degats = effet["damage"]
        attaque_item = {"name" : item_inventaire, "value" : degats}  #Création d'un dictionnaire pour utiliser la fonction appliquer_degats
        cible = choisir_cible(liste_ennemis)
        appliquer_degats(attaque_item, cible)
        print("Vous infligez", degats, "dégâts à l'adversaire avec l'item")

    if "fuite" in effet:
        joueur["Bonus_fuite"] = joueur["Bonus_fuite"] + effet["fuite"]
        print("La fuite à désormais", effet["fuite"],"% de chance supplémentaire pour réussir")


    if item_inventaire["type"] == "consommable":                     #On doit supprimmer les consommables de l'inventaire
        joueur["Inventaire"].remove (item_inventaire)
        print(item_inventaire["name"],"a été consommé(e)")

    return True

def debut_combat(joueur, liste_ennemis, profondeur, items):    #Va gérer la boucle de combat et retourne True si le joueur
    print("\n-"*40)                                            #gagne/fuis ou False s'il perd
    print("|| ÉTAGE", profondeur, ": vous tombez sur au moins un ennemi)||")
    print("\n-"*40)

    combat_actif = True
    while joueur["PV"] > 0 and combat_actif:
        afficher_etat(joueur, liste_ennemis)                          #Début du tour

        print("\n===Votre Tour===")
        print("1) Attaquer")
        print("2) Utiliser un objet")
        print("3) Essayer de fuir")
        action = False
        while not action:
            choix_action = joueur_choix("Choisissez une action",1,3)

            if choix_action == "1":
                cible = choisir_cible(liste_ennemis)
                appliquer_degats(joueur, cible)
                action = True
            elif choix_action == "2":
                utiliser_objets(joueur, liste_ennemis, items)
                action = True
            elif choix_action == "3":
                if tenter_fuite(joueur):
                    return True                                  #Met directement fin au combat car fonction = True
                action = True

        nb_vivants = 0                                    #Le combat doit prendre fin quand tous les monstres sont morts
        for ennemi in liste_ennemis:
            if ennemi["PV"] > 0:
                nb_vivants = nb_vivants + 1               #Augmente nombre vivant pour chaque monstre encore debout
        if nb_vivants == 0:
            print("Victoire ! Tout les ennemis ont été vaincu")
            return True

        print("\n===Tour des ennemis===")
        for ennemi in liste_ennemis:                                #Tout les ennemis attaquent en série
            if ennemi["PV"] > 0:
                if ennemi["ability"]["type"] == "attack":
                    attaquant_temp = {"name" : ennemi["name"], "ATK" : ennemi["ATK"]}       #On crée un dictionnaire temporaire
                    appliquer_degats(attaquant_temp, joueur)
                    print(ennemi["name"], "utilise", ennemi["ability"]["name"], "et inflige", ennemi["ability"]["value"], "dégâts")
                elif ennemi["ability"]["type"] == "block":
                    defense_value = ennemi["ability"]["value"]
                    if "Bouclier" not in ennemi:
                        ennemi["Bouclier"] = 0
                    ennemi["Bouclier"] = ennemi["Bouclier"] + defense_value
                    print(ennemi["name"], "utilise", ennemi["ability"]["name"], "(gagne", ennemi["ability"]["value"],"de bouclier)")

        if joueur["PV"] <= 0:                                     #Partie perdue :(
            print("\n===Défaite ! Vos PV sont tombés à 0===")
            return False

        joueur["Bouclier"] = 0                #Sert à rien ici mais au cas ou on veut ajouter un bouclier dans le futur
        for ennemi in liste_ennemis:          #Pour que les boucliers ne s'accumulent pas à l'infini
            ennemi["Bouclier"] = 0
        print("\n Fin de tour, les boucliers sont reinitialisé")
    return joueur["PV"] > 0

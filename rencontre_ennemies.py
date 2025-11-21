import json
import random
def charger_ennemies(filepath="data/ennemies.json"):
    try:
        with open(filepath) as f:       #convertit le texte en liste de dictionnaire
            liste_ennemies = json.load(f)
            return liste_ennemies
    except FileNotFoundError:
        print("ERREUR : fichier non trouvé")
        return []
    except json.JSONDecodeError:
        print("ERREUR : le fichier contient une erreur de syntaxe")
        return []

def scaling(ennemi_template, etage):     #Pour que la difficulté augmente par étage
    d = etage
    base_pv = ennemi_template["PV"]
    base_atk = ennemi_template["ATK"]

    facteur_scale = 1 + 0.10*(d-1)       #Vient directement du PDF du prof
    new_max_pv = int(base_pv * facteur_scale)
    new_atk = base_atk + (d//3)          #Vient aussi du PDF du prof

    ability_template = ennemi_template["ability"]
    new_ability_value = 0

    if ability_template["type"] == "attack":
        new_ability_value = new_atk
    elif ability_template["type"] == "block":
        new_ability_value = int(ability_template["value"])

    nouvel_ennemi = {
        "id" : ennemi_template["id"],
        "name" : ennemi_template["name"],
        "PV" : new_max_pv,
        "ATK" : new_atk,
        "ability" : {
            "type" : ability_template["type"],
            "name" : ability_template["name"],
            "value" : new_ability_value
        }
    }
    return nouvel_ennemi

def ennemis_par_etage(liste_e, profondeur):      #Pour pas melanger car déja utiliser, etage = profondeur
    if profondeur == 50:
        for e in liste_e:
            if e["id"] == "ceo" :
                boss_copie = {         # On crée une copie pour pouvoir modifier ses stats sans changer le modèle initial
                 "id" : e["id"],
                 "name" : e["name"],
                 "PV" : e["PV"],
                 "ATK" : e["ATK"],
                 "ability" : e["ability"]
                }
                return boss_copie
        print("ERREUR : boss non trouvé")         #Si le boss est manquant
        return []

    profondeur_10 = profondeur % 10          #Les 8 prochaines lignes sont pour avoir moins de monstres au début des dizaines
    nb_spawn = 0
    if profondeur_10 == 1:
        nb_spawn = 1
    elif profondeur_10 in (8,9,0):
        nb_spawn = random.randint(1,3)
    else :
        nb_spawn = random.randint(1,2)

    ennemis_possibles = [                        #Pour filtrer les monstres en fonction des étages
        e for e in liste_e
        if e["floor_min"] <= profondeur <= e["floor_max"] and e["id"] != "ceo"   #Exclure le boss au cas où
        ]
    ennemies_spawned = []
    for e in range(nb_spawn):
        enemy_template = random.choice(ennemis_possibles)           #Choisit un monstre au "hasard"
        new_enemy_instance = scaling(enemy_template, profondeur)    #Créer une instance scalée
        ennemies_spawned.append(new_enemy_instance)                 #Rajoute à ennemies_spawned

    return ennemies_spawned





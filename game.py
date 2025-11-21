import json
import random
import os                 #Donne accès aux fonctionnalités du système d'exploitation
import models.player
import models.rencontre_ennemi
import systems.combat
import systems.seed
import systems.io_cli

import combat
import player
import rencontre_ennemies


def charger_donnees(fichier):               #Fonction générale pour charger un json
    with open(fichier) as json_file:
        donnees = json.load(json_file)
        return donnees

def donner_recompenses(joueur, liste_armes, listes_items):
    print("-"*40)
    print("Étage détruit ! Emporter un objet avant de monter :")
    print("-"*40)
    print("1) Médecine technologique (+ 5 PV MAX + soin total")
    print("2) Un objet (Aléatoire)")
    print("3) Une arme (Aléatoire. Augmente l'ATK définitivement")

    choix = joueur_choix("Votre choix", 1, 3)

    if choix == 1:
        joueur["PV_MAX"] = joueur["PV_MAX"] + 5           #+5 PV MAX
        joueur["PV"] = joueur["PV_MAX"]                   #Soin complet
        print("PV MAX augmentés à", joueur["PV_MAX"], "et santé complète")

    if choix == 2:
        item_gagne = random.choice(listes_items)
        joueur["Inventaire"].append(item_gagne)           #Ajoute l'item à l'inventaire
        print("Vous obtenez :", item_gagne)

    if choix == 3:
        arme_gagnee = random.choice(liste_armes)
        player.ajouter_arme(joueur, arme_gagnee)


def lancer_jeu():
    print("---BIENVENUE DANS LA CORPORATION---")
    print("\nDans un monde dystopique où une méga industrie du nom de The Corporation a remplacé les gouvernements et règne dans tous les domaines sans partage ni justice, vous êtes Employé 404, une personne sans visage, sans avenir, parmis des milliers d'autres comme vous, travaillant dans cette méga entreprise. Dans cette méga structure, l'humain n'est que statistique et lorsque sa courbe de rentabilité chute, il disparaît... \nEn tant qu'Employé 404, vous êtes dans cette entreprise depuis des décennies mais vous le savez très bien, votre heure est proche. Vous devez faire un choix. The Corporation, le travail c'est la mort, la révolte, c'est l'espoir.")
    seed.rng()

    liste_ennemis_data = charger_donnees(enemies.json)
    liste_items_data = charger_donnees(items.json)
    liste_armes_data = charger_donnees(armes.json)

    nom_joueur = intput("\nAbandonner votre matricule de pantin et choisissez votre nom :")
    joueur = player.creer_joueur(nom_joueur)

    etage = 1
    jeu_en_cours = True
    while jeu_en_cours:                                    #Boucle Infinie jusqu'à mort joueur
        print("\n", "#"*40)
        print ("Étage", etage)
        print("#"*40)

        groupe_ennemis = rencontre_ennemies.ennemis_par_etage(liste_ennemis_data, etage)   #Génération des ennemis à chaque étage
        if type(groupe_ennemis) == dict:              #La fonction rencontre_par_etage dans rencontre_ennemies renvoie un dict
            groupe_ennemis = [groupe_ennemis]         #que dans le cadre du boss sinon liste. Transforme boss en liste pour combat
        print("Vous aperçevez", len(groupe_ennemis), "ennemi(s) !")
        for ennemi in groupe_ennemis:
            print("-", ennemi["name"])

        Victoire = combat.debut_combat(joueur, groupe_ennemis, etage, liste_items_data)
        if not Victoire:                              #Si False est renvoyé --> PV =< 0
            print("\n---GAME OVER---")
            print(joueur["nom"], "a été licencié à l'étage", etage)
            break
        else:
            donner_recompenses(joueur, liste_armes_data, liste_items_data) #Si True est renvoyé --> combat gagné

        if etage == 50:                               #Message de victoire "final"
            print("\n !!! INCROYABLE !!! Vous avez vaincu le PDG !")
            print("Mais dans cette entreprise, le travail ne s'arrête jamais...")
            print("C'est ici que le mode Infini commence")

        etage = etage + 1
        intput("\nAppuyez sur n'importe quel bouton pour faire monter l'ascenceur...")

lancer_jeu()




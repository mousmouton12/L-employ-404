import json

#Définition des différents objets(items) du jeu
data = {
    "bouteille_eau":{
        "id":"bouteille_eau",
        "name":"Bouteille d'eau",
        "type":"consommable",
        "rarity":"commun",
        "description":"Toujours aussi rafraîchisante. Permet de restaurer quelques points de vie à celui qui la boit.",
        "effects": {
            "heal":5
            
        }
    },

    "pomme":{
        "id":"pomme",
        "name":"Pomme",
        "type":"consommable",
        "rarity":"commun",
        "description":"Il n'en existe plus beaucoup dans ce monde capitaliste. Restaure des points de vie à celui qui le mange.",
        "effects":{
            "heal":6
        }
    },

    "cafe":{
        "id":"cafe",
        "name":"Café",
        "type":"consommable",
        "rarity":"commun",
        "description":"Agit comme anesthésiant, soigne quelques points de vie de la personne qui la boit.",
        "effects":{
            "heal":3
        }
    },

    "tasse":{
        "id":"tasse",
        "name":"Tasse : le meilleur employé !",
        "type":"consommable",
        "rarity":"commun",
        "description":"Servait à la base à récompenser un employé. Jeter cet objet sur votre adversaire pour lui infliger des dégâts minimes. Cependant, vous ne pourrez pas le réutiliser.",
        "effects":{
            "damage":3
        }
    },

    "barre_chocolat":{
        "id":"barre_chocolat",
        "name":"Barre chocolatée",
        "type":"consommable",
        "rarity":"commun",
        "description":"Petite sucrerie permettant de restaurer des points de vie à la personne qui la consomme.",
        "effects":{
            "heal":4
        }
    },

    "stylo": {
        "id": "stylo",
        "name": "Stylo",
        "type": "arme",
        "rarity": "commun",
        "description": "Un simple stylo, mais peut causer certains dégâts à l'adversaire si il est utilisé avec précision.",
        "effects": {
            "damage":2
        }
    },

    "classeur": {
        "id": "classeur",
        "name": "Classeur",
        "type": "arme",
        "rarity": "commun",
        "description": "Objet remplis de documents et fichiers lourds. Un simple lancer de l'objet sur l'ennemi lui cause des dégâts.",
        "effects": {
            "damage":3
        }
    },

    "lunette":{
        "id":"lunette",
        "name":"Lunette",
        "type":"outil",
        "rarity":"commun",
        "description":"Outil permettant de voir plus aisément les attaques ennemies et qui par conséquent augmente la chance de fuite.",
        "effects":{
            "fuite":5
        }
    },

    "chaise":{
        "id":"chaise",
        "name":"Chaise",
        "type":"arme",
        "rarity":"commun",
        "description":"Lancer de chaises, une compétition jadis très connue. Objet qui permet d'infliger quelques dégâts à l'ennemi.",
        "effects":{
            "damage":2
        }
    },
    
    "chaussure":{
        "id":"chaussure",
        "name":"Chaussure",
        "type":"arme",
        "rarity":"commun",
        "description":"Les riches s'en servent pour marcher avec, les pauvres n'ont pas cette chance. Jeter cet objet sur l'ennemi lui inflige 3 dégâts.",
        "effects":{
            "damage":3
        }
    },

    "agrafeuse":{
        "id":"agrafeuse",
        "name":"Agrafeuse",
        "type":"arme",
        "rarity":"non commun",
        "description":"Outil permettant de faire très mal là où il faut.",
        "effects":{
            "damage":5
        }
    },

    "ciseau":{
        "id":"ciseau",
        "name":"Ciseau",
        "type":"arme",
        "rarity":"non commun",
        "description":"Tranchant et rapide, l'ennemi n'aura pas le temps de réagir.",
        "effects":{
            "damage":6
        }
    },

    "produit_menager":{
        "id":"produit_menager",
        "name":"Produit ménager",
        "type":"arme",
        "rarity":"non commun",
        "description":"Produit chimique irritant qui provoque des démangeaisons et des brûlures aux yeux de l’ennemi et lui inflige des dégâts modestes.",
        "effects":{
            "damage":7
        }
    },

    "objet_metallique":{
        "id":"objet_metallique",
        "name":"Objet métallique",
        "type":"arme",
        "rarity":"non commun",
        "description":"Utilisation initiale inconnue, mais c'était sûrement pour faire de l'argent.",
        "effects":{
            "damage":5
        }
    },

    "perceuse":{
        "id":"perceuse",
        "name":"Perceuse",
        "type":"arme",
        "rarity":"non commun",
        "description":"Utile pour percer les défenses adverses.",
        "effects":{
            "damage":6
        }
    },

    "couteau":{
        "id":"couteau",
        "name":"Couteau de cuisine",
        "type":"arme",
        "rarity":"rare",
        "description":"Une lame émoussée par le temps, mais dont le tranchant semble garder le souvenir de tout ce qu’elle a touché.",
        "effects":{
            "damage":15
        }
    },

    "pistolet":{
        "id":"pistolet",
        "name":"Pistolet",
        "type":"arme",
        "rarity":"rare",
        "description":"Le métal est froid, le poids rassurant. Une arme faite pour protéger...mais pas que.",
        "effects":{
            "damage":20
        }
    },

    "matraque":{
        "id":"matraque",
        "name":"Matraque",
        "type":"arme",
        "rarity":"rare",
        "description":"Solide et parfaitement équilibrée, elle inspire autant la sécurité que la crainte à celui qui la manie.",
        "effects":{
            "damage":10
        }
    },

    "dossiers_rh":{
        "id":"dossiers_rh",
        "name":"Dossiers des Recherches Humaines",
        "type":"outil",
        "rarity":"epic",
        "description":"Ces dossiers vous permettrons d'avoir un boost de +15% de chance de fuite.",
        "effects":{
            "fuite":15
        }
    },

    "casque_vr":{
        "id":"casque_vr",
        "name":"Casque VR Premium Blindé",
        "type":"outil",
        "rarity":"epic",
        "description":"Chef-d'œuvre de technologie et de puissance, ce casque VR blindé isole totalement son porteur du monde réel. Derrière sa visière fumée, la peur disparaît, remplacée par une lucidité glaciale. Rien ne semble pouvoir l’atteindre — ni balle, ni doute.",
        "effects":{
            "damage":20
        }
    },
        
    "potion_miracle":{
        "id":"potion_miracle",
        "name":"Potion Miracle",
        "type":"consommable",
        "rarity":"legendaire",
        "description":"Potion permettant d'éliminer de façon instantané tous les ennemis à proximité. Une fois utilisé, vous ne pourrez pas réutilisez la même Potion Miracle.",
        "effects":{
            "damage":999
        }
    }
}
    
with open("items.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

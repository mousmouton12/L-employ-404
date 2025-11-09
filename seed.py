import random
def rng():
    seed_input = input("Voulez-vous saisir une seed de maximum 10 chiffres ? (Laissez vide pour aléatoire)")
    if seed_input == "":
        seed = random.randint(0, 9999999999)
        print("Seed aléatoire générée :", seed)
    else:
        try:                                    # Vérifie que l'entrée est bien un int
            seed = int(seed_input)
            print("Seed choisie :", seed)
        except ValueError:                      # Si entrée incorrect, impose une seed
            seed = random.randint(0, 9999999999)
            print("Seed invalide. Attribution d'une seed aléatoire :", seed)

    return seed
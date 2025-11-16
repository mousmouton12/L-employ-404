def get_player_choice(prompt, choix_min, choix_max):      # Min et max si on veut rajouter des choix plus tard.

  while True:                                               # Permet de redemander si il y'a une entrée invalide.
        choix_input = input(prompt + " (Entrez un nombre entre " + str(choix_min) + " et " + str(choix_max) + ") > ")
        try:
            choix_num = int(choix_input)                  # Vérifie que l'entrée est bien un int
            if choix_min <= choix_num <= choix_max:
                return choix_num
            else:
                print("Erreur : Le choix " + str(choix_num) + " est en dehors de ceux autorisés.")
        except ValueError:
            print("Erreur : L'entrée '" + choix_input + "' n'est pas un nombre valide. Veuillez réessayer.")

def get_item_id_choice(prompt):
    return input(prompt + " > ").strip().lower()             # Supprime les espaces inutiles et convertir en minuscule pour faciliter la recherche

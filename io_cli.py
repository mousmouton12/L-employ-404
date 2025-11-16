def get_player_choice(prompt, min_choice, max_choice):      #Min et max pour que si on veut rajouter plus tard des choix

  while True:        #Permet de redemander s'il y'a une entrée invalide
        choice_input = input(prompt + " (Entrez un nombre entre " + str(min_choice) + " et " + str(max_choice) + ") > ")
        try:
            choice_num = int(choice_input)     #Vérifie que l'entrée est bien un int
            if min_choice <= choice_num <= max_choice:
                return choice_num
            else:
                print("Erreur : Le choix " + str(choice_num) + " est en dehors de ceux autorisés.")
        except ValueError:
            print("Erreur : L'entrée '" + choice_input + "' n'est pas un nombre valide. Veuillez réessayer.")

def get_item_id_choice(prompt):
    return input(prompt + " > ").strip().lower() #  Convertit en minuscules et supprime les espaces inutiles pour faciliter la recherche d'objet
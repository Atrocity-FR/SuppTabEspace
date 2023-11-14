# Fonction pour supprimer les tabulations et les espaces d'une chaîne de caractères
def supprimer_tabulations_espaces(chaine, compteur):
    chaine_modifiee = chaine.replace('\t', '')
    chaine_modifiee, nb_espaces_supprimes = chaine_modifiee.replace(' ', ''), chaine.count(' ') - chaine_modifiee.count(' ')
    compteur['tabulations'] += chaine.count('\t')
    compteur['espaces'] += nb_espaces_supprimes
    return chaine_modifiee

# Fonction principale pour lire, traiter et sauvegarder le contenu du fichier
def traiter_fichier(nom_fichier_entree, nom_fichier_sortie):
    try:
        # Initialiser le compteur
        compteur = {'tabulations': 0, 'espaces': 0}

        # Ouvrir le fichier en mode lecture
        with open(nom_fichier_entree, 'r') as fichier_entree:
            # Lire le contenu du fichier
            contenu = fichier_entree.read()

            # Supprimer les tabulations et les espaces du contenu
            contenu_modifie = supprimer_tabulations_espaces(contenu, compteur)

            # Afficher le contenu modifié
            print("Contenu du fichier après suppression des tabulations et des espaces :")
            print(contenu_modifie)

            # Enregistrer le contenu modifié dans un nouveau fichier
            with open(nom_fichier_sortie, 'w') as fichier_sortie:
                fichier_sortie.write(contenu_modifie)
                print(f"Le contenu modifié a été enregistré dans le fichier {nom_fichier_sortie}")

            # Afficher le nombre de tabulations et d'espaces supprimés
            print(f"\nNombre total de tabulations supprimées : {compteur['tabulations']}")
            print(f"Nombre total d'espaces supprimés : {compteur['espaces']}")

    except FileNotFoundError:
        print(f"Le fichier {nom_fichier_entree} n'a pas été trouvé.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Exemple d'utilisation avec un fichier texte appelé "exemple.txt"
# Le contenu modifié sera enregistré dans un nouveau fichier appelé "exemple_modifie.txt"
traiter_fichier("exemple.txt", "exemple_modifie.txt")

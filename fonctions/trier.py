import os
import shutil

def trier_fichiers_par_extension(chemin_dossier):
    if not os.path.exists(chemin_dossier):
        print(f"Le dossier '{chemin_dossier}' n'existe pas.")
        return

    for fichier in os.listdir(chemin_dossier):
        chemin_complet = os.path.join(chemin_dossier, fichier)
        if os.path.isfile(chemin_complet):
            extension = os.path.splitext(fichier)[1].lower()
            dossier_extension = os.path.join(chemin_dossier, extension)
            if not os.path.exists(dossier_extension):
                os.makedirs(dossier_extension)

            try:
                shutil.move(chemin_complet, os.path.join(dossier_extension, fichier))
            except PermissionError:
                print(f"Permission refusée pour le fichier : {fichier}")
            except Exception as e:
                print(f"Erreur lors du déplacement du fichier {fichier}: {e}")

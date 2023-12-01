import argparse

def argParse():
    parser = argparse.ArgumentParser( description="Entrez le chemin du dossier à trier.")
    
    parser.add_argument("-path", type=str, help="Chemin relatif ou absolut du fichier à trier")

    args = parser.parse_args()
    return args.path

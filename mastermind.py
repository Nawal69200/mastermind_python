import random

def code_secret(longueur):
    return ''.join(random.choices('RGBY', k=longueur))

def verification(solution, essai):
    position_correcte = sum(solution[i] == essai[i] for i in range(len(solution)))
    couleur_correcte = sum(min(solution.count(color), essai.count(color)) for color in 'RGBY') - position_correcte
    return position_correcte, couleur_correcte

def mastermind():
    longueur_code = 4
    solution = code_secret(longueur_code)
    print("Bienvenue dans le jeu Mastermind !")
    print("Devinez le code secret composé de 4 couleurs (R, G, B, Y).")
    print("Vous avez 10 essais.")
    print("Les couleurs peuvent être répétées et l'ordre est important.\n")

    attempts = 0
    while attempts < 10:
        attempts += 1
        essai = input(f"Essai {attempts}: ").upper()
        if len(essai) != longueur_code or not all(color in 'RGBY' for color in essai):
            print("Veuillez entrer une combinaison valide de 4 couleurs (R, G, B, Y).")
            continue
        position_correcte, couleur_correcte = verification(solution, essai)
        if position_correcte == longueur_code:
            print(f"Bravo ! Vous avez deviné le code en {attempts} essais.")
            return
        else:
            print(f"Position correcte : {position_correcte}, Couleur correcte : {couleur_correcte}\n")

    print(f"Désolé, le code secret était {solution}.")

if __name__ == "__main__":
    mastermind()

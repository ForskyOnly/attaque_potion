import random as rd
import csv 
from utils import on_attaque, il_attaque, on_prend_potion, bonus, enregistrer_score
score_notre  = 50
score_ennemi = 50
nb_potion = 0



print("\n Bienvenue dans ATTAQUE OU POTION : \n\n Voici les regles du jeu : Chaque attaque de l'ennemi vous fais perdre 5 à 15 de score. \n\n Vous devez choisir une action entre Attaquer (fait perdre 5 à 10 de score à l'ennemi) ou prendre une Potion vous fais gagner 15 à 50 de score. \n\n L'objectif est d'effectuer le meilleur score possible tout en gagnant. \n\n À la fin de la partie votre score est egale à vos pdv restant + 50 points de score par potion non utilisé...  PRET? \n....................................................................................................................\n....................................................................................................................\n ")

nom_utilisateur = input("Entrez votre nom d'utilisateur : ")
termin=False
print("Votre score est de : ", score_notre)
print("Le score de l'ennemi est de : ", score_ennemi)

while not termin:
    choix = input("Entrez une acttion : attaque ou potion : ")
    
    if choix == "attaque" :
        score_ennemi = on_attaque(score_ennemi)
        score_notre = il_attaque(score_notre)    
    elif choix == "potion" :
        nb_potion +=1   
        if nb_potion <= 3:
            score_notre = on_prend_potion(score_notre)
            score_notre = il_attaque(score_notre)
            print(" Le nb de potions utilisées est de : ", nb_potion)
        else:
             print("Vous avez utiliser toutes les potions... svp attaquez")
    else:
        print("entrer un choix valide : ")
    print("Votre score est de : ", score_notre)
    print("Le score de l'ennemi est de : ", score_ennemi)
    
    bonus(score_ennemi,score_notre)
   
    
    if score_ennemi <= 0:
        termin = True
        if nb_potion <= 3:
            score_notre += 50*(3-nb_potion)
        print("Felicitations vous avez gagner ! Votre score est de :" , score_notre, "Points")
        enregistrer_score(score_notre, nom_utilisateur,)
        
    if score_notre <= 0 :
        termin = True
        print("vous etes mort, vous serez même pas classé... bouuuh ! " )
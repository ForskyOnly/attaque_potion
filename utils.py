import random as rd
import csv


def on_attaque(score_ennemi):
    """ FR : cette fonction est faite pour calculer le score de l'ennemi apres notre attaque 
        EN : this function is made to calculate the score of the enemy after our attack 
        

    Args:
        score_ennemi (_type_):     FR : score_ennemi va représente le score du joueur ennemi
                        EN : score_ennemi  represents the score of the enemy player

    Returns:
        _type_:     FR :   la fonction  retire des point de vie à l'adversaire entre 5 et 10
                    EN :   the function removes life points from the opponent between 5 and 10
    """
    score_ennemi -= rd.randint(5,10)
    return score_ennemi

def il_attaque(score_notre):
    """ 
        FR : cette fonction est faite pour calculer notre score après l'attaque de l'ennemi  
        EN : this function is made to calculate our score after enemy attack

    Args:
        score_notre (_type_): FR : score_notre va représenter notre score 
                    EN : score_notre will represent our score

    Returns:
        _type_: FR : la fonction NOUS retire des point de vie entre 5 et 15
                EN : the function removes  life points between 5 and 15 of our score
    """
    score_notre -= rd.randint(5,15)
    return score_notre


def on_prend_potion(score_notre):
    """ FR : cette fonction permet de recalculer notre score apres avoir utilisé une potion
        EN : this function allows us to recalculate our score after using a potion

    Args:
        score_notre (_type_): FR : score_notre va représenter notre score 
                    EN : score_notre will represent our score
    Returns:
        _type_: FR : la fonction nous ajoute des point de vie entre 15 et 50
                EN : the function add life points between 15 and 50 to our score
    """
    score_notre += rd.randint(15,50)
    print("la potion nous a donner : ", score_notre)
    return score_notre

# def compteur_potion(nb_potion):
#     """ FR : cette fonction nous permet de compter les potions utilisées
#         EN : this function allows us to count the used  potions

#     Args:
#         nb_potion (_type_):    FR : nb_potion represent le nombre des potions utilisées
#                         EN : nb_potion represents the used potions number 


#     Returns:
#         _type_: FR : rajoutde +1 a chaque fois que l'on utilise une potion
#                 EN : add +1 everytime when we use a potion
#     """
#     nb_potion+= 1
#     return nb_potion

def verifie_potion(nb_potion,score_notre):
    """ FR : cette fonction limite l'utilisation de potions à 3 
        EN : this function limits  using potions to 3
        
    Args:
        nb_potion (_type_):    FR : nb_potion represente le nombre de potions utilisées
                               EN : nb_potion represents the number of used potions 
        
        score_notre (_type_):    FR : score_notre va représenter notre score 
                                 EN : score_notre will represent our score

    Returns:
        _type_: FR :    if : elle retourne notre score après la prise d'une potion 
                            puis l'attaque de l'ennemi
                        else : elle retourne un message qui nous demande d'attaquer 
                            car nous avons utilisées toutes les potions
                
                EN :    if: it returns our score after taking a potion
                             and the enemy attack
                        else: it returns a message asking us to attack
                             because we used all the potions
    """
    if nb_potion<= 3:
        score_notre = on_prend_potion(score_notre)
        score_notre = il_attaque(score_notre)
        print(" le nb de potions utilisées est : ", nb_potion)
        return score_notre
    else:
        print("on a utilisé toutes les potions svp attaquer")
        return score_notre
    

def enregistrer_score(score, nom_utilisateur, path = "score.csv"):
    """ FR : Cette fonction crée un fichier ou on retrouve tout les score des utilisateurs.
        EN : This function creates a file where all the scores of the users are saved.
    Args:
        score (_type_): FR : Représente le score finale
                        EN : Represents final score
                        
        nom_utilisateur (_type_): FR : Représente le nom d'utilisateur choisi 
                                  EN : Represents choosen username
    """
    with open(path, mode='a') as fichier_score:
        ecrire_score=csv.writer(fichier_score)
        ecrire_score.writerow([nom_utilisateur,  " : Votre score est de ", score, " Points"])


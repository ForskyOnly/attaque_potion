import random as rd
score_notre  = 50
score_ennemi = 50
nb_potion = 0

def on_attaque(y):
    y -= rd.randint(5,10)
    return y

def il_attaque(x):
    x -= rd.randint(5,15)
    return x
def on_prend_potion(x):
    x += rd.randint(15,50)
    print("la potion nous a donner : ", x)
    return x

def compteur_potion(nb):
    nb+= 1
    return nb

##############################################################

termin=False
while not termin:
    print("notre score est : ",score_notre)
    print("le score de l'ennemi est: ",score_ennemi)
    choix = input("entrer attaque ou potion : ")
    
    if choix == "attaque" :
        score_ennemi = on_attaque(score_ennemi)
        score_notre = il_attaque(score_notre)    
    elif choix == "potion" :
        nb_potion = compteur_potion(nb_potion)    
        if nb_potion <= 3:
            score_notre = on_prend_potion(score_notre)
            score_notre = il_attaque(score_notre)
            print(" le nb de potions utilisées est : ", nb_potion)
        else:
             print("on a utilisé toutes les potions svp attaquer")
    else:
        print("entrer un choix valide : ")
    
        
    if score_ennemi <= 0:
        termin = True
        print("l'ennemi est mort")
    if score_notre <= 0 :
        termin = True
        print("On est mort")
     
        
        
    
    
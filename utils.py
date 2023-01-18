import random as rd
notre_score  = 50
score_ennemi = 50
nb_potion = 0
 #################################################################################   
def on_attaque_potion(choix,x,y):
    if choix=="attaque":
        y -= rd.randint(5,10)
        print("le score de l'ennemi est", y)
        return y
    if choix=="potion":
        x += rd.randint(15,50)
        print("notre score apres une potion est", x)
        return x
    return False
#####################################################################################
def utilisation_potion(potion,nb,x,y):
    if nb <=3:
        x = on_attaque_potion(potion,x,y)
        print("nombre de potion : ",nb)
        return x
    else:
        print("on a utilisé toutes les potions")
        choix = input("entrer juste attaque: ")
        
        while choix != "attaque":
            choix = input("entrer SVP juste attaque: ")   
        y=on_attaque_potion(choix,x,y) 
        return y
##################################################################################
def notre_choix(choix,nb,x,y):
    if choix=="attaque":
        y = on_attaque_potion(choix,x,y)
        return y
    elif choix=="potion":
        nb_potion +=1
        if nb_potion <=3:
            notre_score=on_attaque_potion(choix,notre_score,score_ennemi)
            print("nombre de potion",nb_potion)
        else:
            y= utilisation_potion(choix,nb,x,y)
            return y 
    else:
        print("SVP entrer un choix valide")
##################################################################################
def compteur_potion(choix,nb):
    if choix == "potion":
        nb+= 1
        #print("nombre de potion : ",nb)
        return nb
########################################################################################
termin=False
while not termin:
    print("notre score est : ",notre_score)
    print("le score de l'ennemi est: ",score_ennemi)
    choix = input("entrer attaque ou potion : ")
    if choix=="potion":
        #nb_potion =+1
        #print("nombre de potion : ",nb_potion)
        nb_potion=compteur_potion(choix,nb_potion)
        notre_score = notre_choix(choix,nb_potion,notre_score,score_ennemi)
    elif choix == "attaque":
        score_ennemi=notre_choix(choix,nb_potion,notre_score,score_ennemi)
    
    
    
    
        
        
        
        
    # if choix=="attaque":
    #     score_ennemi=on_attaque_potion(choix,notre_score,score_ennemi)
    # elif choix=="potion":
    #     nb_potion +=1
    #     if nb_potion <= 3:
    #         notre_score = utilisation_potion(choix,nb_potion,notre_score,score_ennemi)
    #     else:
    #         score_ennemi = utilisation_potion(choix,nb_potion,notre_score,score_ennemi)
  
    # else:
    #     print("SVP entrer un choix valide")
    if score_ennemi <=0:
        termin=True
        print("l'ennemi est mort")
    else:
        notre_score -= rd.randint(5,15)
        print("notre score apres l'attaque de l'ennemi est",notre_score)
    if notre_score <=0:
        termin=True
        print("On est mort")
        








# def calculer_score_ennemi():
#     pass

# def ennemi_attaque():
#     pass

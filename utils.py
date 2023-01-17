import random as rd
notre_score  = 50
score_ennemi = 50
potion = 3

# def attaque_potion_valide(string):
#     if string == "attaque":
#         return True
#     elif string == "potion": 
#         return True
#     else:
#         return False
    
    
    
    
def on_attaque_potion(string,notre_score,score_ennemi):
    if string=="attaque":
        score_ennemi -= rd.randint(5,10)
        return True
    elif string=="potion":
        notre_score += rd.randint(15,50)
        return True
    else:
        return False

#print(on_attaque_potion("attaque",notre_score,score_ennemi))
#print(on_attaque_potion("potion",notre_score,score_ennemi))

termin=False
while not termin:
    choix = input("entrer attaque ou potion : ")
    while not on_attaque_potion(choix,notre_score,score_ennemi):
        choix = input("SVP entre un choix valide : ")
    
    if score_ennemi <=0:
        termin=True
        print("l'ennemi est mort")
    else:
        notre_score -= rd.randint(5,15)
    if notre_score <=0:
        termin=True
        print("On'est mort")
        








def calculer_score_ennemi():
    pass

def ennemi_attaque():
    pass

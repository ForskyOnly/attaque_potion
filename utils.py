import random as rd
notre_score  = 50
score_ennemi = 50
potion = 3
def on_attaque_potion(string,notre_score,score_ennemi):
    if string=="attaque":
        score_ennemi -= rd.randint(5,10)
        return score_ennemi
    if string=="potion":
        notre_score += rd.randint(15,50)
        return notre_score

print(on_attaque_potion("attaque",notre_score,score_ennemi))
print(on_attaque_potion("potion",notre_score,score_ennemi))





def calculer_score_ennemi():
    pass

def ennemi_attaque():
    pass

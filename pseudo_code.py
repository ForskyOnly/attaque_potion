


terminer = False
while not terminer:
    on_attaque_potion(choix):
        calculer_score_ennemi()

    if score_ennemi <=0:
        terminer = True
        print("l'ennemi à perdu")
    else:
        ennemi_attaque()
        if notre_score <=0:
            terminer = True
            print("on à perdu")
            
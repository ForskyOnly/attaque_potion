def on_attaque():
        pass
def il_attaque():
        pass
def on_prend_potion():
        pass
def compteut_potion():
        pass
def verifie_potion():
        pass
def enregistrer_score():
        pass


termine = False
while not termine:
    choix = input()
    if choix == "attaque" :
        '''calculer les scores'''
        on_attaque()
        il_attaque()
    elif choix == "potion" :
        '''calculer le nb de potions'''
        compteut_potion()
        verifie_potion()
        '''recalculer les scores par''' 
        on_attaque()
        il_attaque()
    else:
        "entrer un choix valide"  
    if "test de scores":
     "si il y a au moins un score qui vaut <= 0"
    enregistrer_score()
    "si le jouer gagne "
    termin= True

    
        
            
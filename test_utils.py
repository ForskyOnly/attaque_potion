import unittest
import random as rd
from utils import on_attaque, il_attaque, on_prend_potion ,verifie_potion, compteur_potion ,enregistrer_score
score_notre  = 50
score_ennemi = 50
nb_potion = 1

class TestOnAttaqueWithUnittest(unittest.TestCase):
    
    def test_on_attaque(self):
        rd.seed(35)
        self.assertEqual( on_attaque(50) , 50-9)
        
    def test_il_attaque(self):
        rd.seed(35)
        self.assertEqual( il_attaque(50) , 50-13)
        
    def test_on_prend_potion(self):
        rd.seed(35)
        self.assertEqual( on_prend_potion(50) , 50+50)
               
    def test_verifie_potion(self):
        rd.seed(44)
        self.assertEqual( verifie_potion(3,score_notre), 78) 
        
    def test_compteur_potion(self):
        self.assertEqual(compteur_potion(0) , 1)
        self.assertEqual(compteur_potion(1) , 2)
        self.assertNotEqual(compteur_potion(1) , 1)
        
    # def test_enregistrer_score(self):
    #     self.
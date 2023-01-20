import unittest, shutil, tempfile
import random as rd
from utils import on_attaque, il_attaque, on_prend_potion ,verifie_potion ,enregistrer_score
from os import path
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

        
class EnregistrerScoreTestCase(unittest.TestCase):
    def setUp(self):
        self.test_dir = tempfile.mkdtemp()
    
    def tearDown(self):
        shutil.rmtree(self.test_dir)
    
    def test_enregistrer_score(self):
      path_to_file = path.join(self.test_dir, 'scores.txt')        
      
      enregistrer_score(10, "test", path_to_file) 
      
      with open(path_to_file,"r") as fichier_score:
        self.assertIn("test", fichier_score.read())

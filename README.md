# Description du Projet

Ce projet a été réalisé par Jonathan, Rubic et Ahmad. Le but est de faire fonctionner un jeu en utilisant le langage de prommation Python. 

Le principe du jeu est comme le suivant : Le jeu comporte deux joueurs, vous et un ennemi. Vous commencez tous les deux avec 50 points de vie. Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie. L'ennemi ne dispose d'aucune potion. Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50. Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie. L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie. Lorsque vous utilisez une potion, vous passez le prochain tour.

Pour ce faire, nous avons créé cinq fonctions. La première est appelée **on_attaque()** et a pour but de calculer le score de l'ennemi quand on attaque. Parallèlement, il existe une deuxième fonction appelée **il_attaque()** dont le but est de calculer notre score après l'attaque de l'ennemi. Ensuite, il y a la fonction **on_prend_potion()** qui permet de recalculer notre score après la prise d'une potion. Vu que le nombre de potions est limité, les deux dernières fonctions **compteur_potion()** et **verifie_potion()** sont faites pour gérer cette contrainte, i y en a une donc qui compte le nombre de potions et l'autre elle recalcule notre score sous resèrve que le nombre de potions soit moins que 3, sinon elle redemnade d'attaquer.  





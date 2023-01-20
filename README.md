# Description du Projet

Ce projet a été réalisé par Jonathan, Rubic et Ahmad pendant la formation Tech IA chez Simplon Roubaix. Le but est de faire fonctionner un jeu en utilisant le langage de prommation Python. 

Le principe du jeu est comme le suivant : Le jeu comporte deux joueurs, vous et un ennemi. Vous commencez tous les deux avec 50 points de vie. Votre personnage dispose de 3 potions qui vous permettent de récupérer des points de vie. L'ennemi ne dispose d'aucune potion. Chaque potion vous permet de récupérer un nombre aléatoire de points de vie, compris entre 15 et 50. Votre attaque inflige à l'ennemi des dégâts aléatoires compris entre 5 et 10 points de vie. L'attaque de l'ennemi vous inflige des dégâts aléatoires compris entre 5 et 15 points de vie. Lorsque vous utilisez une potion, vous passez le prochain tour.

Pour ce faire, nous avons créé des fonctions. La première est appelée **on_attaque()** et a pour but de calculer le score de l'ennemi quand on attaque. Parallèlement, il existe une deuxième fonction appelée **il_attaque()** dont le but est de calculer notre score après l'attaque de l'ennemi. Ensuite, il y a la fonction **on_prend_potion()** qui permet de recalculer notre score après la prise d'une potion. Vu que le nombre de potions est limité, la fonction **verifie_potion()** est faite pour gérer cette contrainte, elle recalcule donc notre score sous resèrve que le nombre de potions soit inférieur ou égal à 3, sinon elle redemande d'attaquer. Nous sommes généreux! pour cela nous avons donné aléatoirement à l'un des joueurs, une petite chance pour gagner 15 points de vie, c'est la fonction **bonus(,)** qui s'en occupe. 
Finalement, la fonction **enregistrer_score(,)** demande un nom d'utilisateur et enregistre le score du joueur gagnant sur un fichier csv. 


# ORGANISATION DU DOSSIER

Dans le dossier on retrouve plusieurs fichier: 
- Main : on retrouve le programme principal du jeu 
- Pseudo code : un exemple de code simplifier
- Test_utils : pour test les fonctions
- utils : regroupe toutes les fonction avec un doctring pour expliquer chaque fontion

# Utiliser le jeu 

Pour utiliser le jeu il suffit de clone le projet depuis github/ForskyOnly/attaque_potion
Avoir installé Python sur sa machine
Installer les modules CSV et Random si ils ne sont présent dans la distribution de Python


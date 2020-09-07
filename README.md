 
# Blackjack

## Énoncer :

Développer un jeu de Blackjack en Python, en utilisant differentes classes et méthodes.

Le jeu demandera des données au joueur (ex: prendre une carte) et lui montrera le résultat dans le terminal (ex: votre score est de 17).

Après une partie, le jeu demandera de quitter ou de recommencer.


**N'oubliez pas d'utiliser github**

## But du jeu :
Après avoir reçu deux cartes, le joueur tire des cartes pour s’approcher de la valeur 21 sans la dépasser. Le but du joueur est de battre le croupier en obtenant un total de points supérieur à celui-ci ou en voyant ce dernier dépasser 21. Chaque joueur joue contre le croupier, qui représente la banque, ou le casino, et non contre les autres joueurs.

## Valeur des carte :
* L’As vaut 1 point ou 11 points, au choix du joueur
* Les valets, les dames et les rois (les figures), ont une valeur de 10 points
* Chaque carte numérotée de 2 à 10 a sa valeur nominale (égale au numéro sur la carte)

## Le Jeu :

* Le croupier distribue deux cartes visibles à chaque joueur.
* Le croupier se distribue se distribue une carte face visibles et une carte face caché.
* Le joueur doit décider s’il veut demander une autre carte pour se rapprocher de 21 ou s’il veut arrêter.
* Jusqu’à ce que le score du joueur soit de 21 ou moins, il peut décider de demander des cartes supplémentaires, une à la fois.

Si le score du joueur est supérieur à 21, le croupier gagne et le jeu s’arrête.

## Le jeu du croupier:

Le croupier présentera sa carte face cachée :

* si le total est de 17 ou plus, il doit arrêter.
* si le total est de 16 ou moins, il doit prendre une nouvelle carte.
* si le croupier a un as, et que le compter comme 11 porte le total à 17 et 21 compris, dans ce cas il le compte comme 11 et arrête.

Si le score du croupier est supérieur à 21, le joueur gagne.

## Gagnant :

Si ni le joueur ni le croupier n’a plus de 21, celui qui a le plus gros score gagne.
Si le joueur a le même score que le croupier, ce dernier l'emporte.
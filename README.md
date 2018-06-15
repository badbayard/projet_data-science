RC3-Yannis Hutt 11408376 Julien Cadier 11510421
=======

Auteurs
-------
Yannis Hutt
Julien Cadier

liste des fichiers
-------------------
* ./_pycache_
 * lireGraph2.cpython-36.pyc
  *test_lireGraph.cpython-36.pyc
  
* ./data
  *  ./bb
      BB_S01E01_000.graphml
    ...
*  ./got
    *  GoT_S01E01_000.graphml
    ...
*  ./hoc
  *  HoC_S01E01_000.graphml
    ...
* ./images

* ./doc
  * Rapport LIFPROJET HUTT_CADIER.pdf


* lireGraph2.py
* main.py
* test_lireGraph.py
* Readme.md


Comment le lancer
----------------
On lance le programme depuis le fichier main.py dans une console python
python main.py

Mode d'emploi
---------------
Le main.py lance une interface graphique qui se compose d'une zone d'affichage pour le résultat,
et de commande sur le côté droit pour faire les différentes opérations, ainsi qu'un menu sur le haut de la fenêtre pour charger une image depuis les fichiers ainsi qu'un "About".
Le premier menu déroulant permet de choisir une série à charger.
Les options en dessous permettent de choisir le style de graphique que l'on veut, ainsi on peut cliquer sur "Drawing graphs" pour afficher.

Le deuxième menu déroulant permet de choisir une opération à appliquer sur un nombre de scène.
On dispose en-dessous d'une zone de texte pour écrire le nom du personnage et un bouton "Ok" pour débuter le traitement.

Bibliothèque
-------------
* Networkx
* Seaborn
* matplotlib
* PYQT5
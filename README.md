
# Détection de défauts sur les routes :  Road Damage Detection Challenge

----

## 1. Overview du projet

L'état des routes est, à l'échelle d'une commune, d'une région ou même d'un pays, un sujet important puisqu'il a un impact direct et significatif sur la vie des usagers. L'entretien et la gestion des routes doivent être fait de façon régulière et exhaustive : en effet, un défaut de petite ampleur peut vite dégénérer notamment en raison d'infiltrations.

Cependant, cette évaluation peut être traditionnellement menée visuellement par des opérateurs humains, procédure très coûteuse en temps, en argent et en ressources humaines, tout en restant assez subjective et sujette à erreurs. Il est donc *nécessaire de créer un système d'évaluation performant, rapide, automatique, économique et homogène*. L'intelligence artificielle peut alors être une excellente candidate. 

De cette problématique est né le Global Road Detection Challenge en 2018, réitéré en 2020 puis récemment en 2022. Chaque nouveau challenge est l'occasion d'enrichir les données en provenance de nouveaux pays, afin d'inclure plus d'environnements et de situations afin de rendre les algorithmes de plus en plus efficients et généralisables. 

Le challenge de 2020 est celui sur lequel se base ce projet. Le dataset de cette édition est constitué de 21 041 photos prises avec un smartphone directement depuis un véhicule. Les photos sont en provenance de 3 pays : 
  * Inde : 7 706
  * Japon : 10 506
  * Tchéquie : 2 829
 
L'édition 2022 a vu le dataset s'étoffer considérablement avec maintenant dans les données d'entrainement : Chine (3500), Inde (9000), Japon (10000), Norvège (9000), Tchéquie (2000) et USA (5000).

Les photos fournies par les organisateurs du challenge sont toutes labellisées via un fichier annotations qui contient pour chaque photo les coordonnées des bounding box (les carrés qui localisent les défauts dans la photo) et la catégorie de défaut associé à chaque bounding box. 

![image](https://user-images.githubusercontent.com/38078432/188320042-d89043f7-b5d1-4d92-b277-44defd81ccdb.png)

En 2020, différents types de défauts sont annotés, de façon différente selon le pays, en différentes catégories : 
![image](https://user-images.githubusercontent.com/38078432/188277730-ae96420d-8f98-4f05-94ae-cd2d97e11713.png)

----

## 2. Objectifs

Le challenge a pour vocation première la détection de 4 principales catégories : D00, D10, D20, D40.

Néanmoins, en vue d'appliquer cet algorithme à une problématique métier spécifique, nous avons considéré 7 catégories de défauts donc les regroupements sont indiqués par le code couleur dans la table ci-dessus :
  * Fissures linéaires longitudinales : D00 + D01
  * Fissures linéaires latérales : D10 + D11
  * Fissures de type alligator : D20
  * Nids-de-poules, bosses, ornières : D40
  * Lignes blanches ou jaunes dont passages piétons : D43 + D44
  * Bouches d'égout : D50
  * Autres : D0w0

----

## 3. Comment procéder ?

### Pré-requis

Les notebooks ont été développés avec Google Colab et gèrent les données en ligne via Google Drive. Il convient donc d'avoir un compte actif. 

YoloV5 nécessite une grosse capacité de calcul. Pour ma part, j'ai opté pour un abonnement à Google Colab Pro pour bénéficier des GPU / RAM supplémentaires qu'offre ce système. Selon la puissance de votre ordinateur, l'abonnement peut ne pas être indispensable, mais le calcul est très long et peut couper après une trop longue période perçue comme inactive. 

L'outil Wandb n'est pas indispensable mais offre une visualisation très ergonomique de l'évolution des epochs et des performances des différents modèles entrainés. 

### Fichiers 

  * Le notebook *Part 1 - EDA.ipynb* permet de visualiser les données brutes (images et annotations) ainsi qu'une première EDA. 
  * Le notebook *Part 2 - Yolov5.ipynb* formatte les données pour l'utilisation de YoloV5 et permet d'entrainer le modèle
  * Le notebook *Part 3 - Deployment.ipynb* se base sur le meilleur modèle choisi par l'utilisateur et le déploie grâce à outil en ligne qui permet à l'utilisateur de charger une photo sur laquelle il souhaite détecter les défauts.

----

## 4. Overview des principaux résultats 

### Analyse descriptive exploratoire

Les défauts sont annotés de manière différentielle entre les 3 pays puisque la Tchéquie n'a annoté que les 4 principaux types de défauts concernés par le challenge, le Japon a annoté 7 types de défauts et l'Inde a annoté tous les types de défauts. 

![image](https://user-images.githubusercontent.com/38078432/188320253-9079e0d3-d1bb-4b5c-a440-097317b2aa4c.png)

Les défauts "annexes" sont donc moins bien annotés que les 4 défauts principaux, il y a donc dans les photos d'apprentissage plus d'erreurs, de "bruit" pour les catégories annexes, ce qui laisser supposer que nous aurons de moins bonnes performances sur ces catégories que sur les catégories principales, annotés correctement sur toutes les photos. 

### Yolov5

Yolo (You Only Look Once) est un des outils de détection d'objets les plus populaires grâce à sa précision, la possibilité d'utilisation en temps réel et sa simplicité d'utilisation. L'algorithme utilise un Convolutional Neural Network (CNN) pré-entraîné et ré-entraînable qui traite l'image en une seule fois, en la découpant en plusieurs parties et en prédisant des bounding box (localisation de l'objet cherché dans l'image) et leur probabilité. 

L'évaluation des performances du modèle peut se faire sur différentes métriques, notamment le F1-score et la mAP (mean Average Precision), métrique spécifique aux modèles de détection. Pour comparer différents modèles (différentes paramétrisations de YoloV5), Wandb est une interface très agréable :  

![image](https://user-images.githubusercontent.com/38078432/188439802-478dd008-e62b-4cdf-b36c-3c70e3e6bad1.png)

Le modèle choisi ici a des performances relativement intéressantes, d'autant plus que, rappelons le, nous entrainons un modèle à détecter des défauts non annotés dans toutes les images d'entrainement :

![image](https://user-images.githubusercontent.com/38078432/188442882-bc05e8fe-79ea-4000-b288-4a835362731a.png)

### Déploiement 

Pour finir, nous proposons d'utiliser le modèle choisi pour détecter des défauts de route sur de nouvelles photos sélectionnées par l'utilisateur. Pour cela, nous avons utilisé Gradio : 

![image](https://user-images.githubusercontent.com/38078432/188445700-8c36c831-6cf5-4441-9d88-33a2af796fc4.png)

----

## 5. Informations

### Outils

  * Les notebooks ont été développés avec [Google Colab](https://colab.research.google.com/). 
  * YoloV5 est disponible [ici](https://github.com/ultralytics/yolov5) et YoloV7 [ici](https://github.com/WongKinYiu/yolov7).
  * Wandb est disponible [ici](https://wandb.ai/site).
  * L'information sur Gradio est disponible [ici](https://gradio.app/).

### Auteurs & contributeurs

Auteur : 
  * Helene alias [@Bebock](https://github.com/Bebock/)

La dream team :
  * Henri alias [@HenriPuntous](https://github.com/HenriPuntous/)
  * Jean alias [@Chedeta](https://github.com/Chedeta/)
  * Nicolas alias [@NBridelance](https://github.com/NBridelance/)
  
### Sites sources des données

[Road Damage Detection Challenge 2020](https://rdd2020.sekilab.global/)

[Crowdsensing-Based Road Damage Detection Challenge 2022](https://crddc2022.sekilab.global/)

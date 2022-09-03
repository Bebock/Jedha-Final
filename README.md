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
 L'édition 2022 a vu le dataset s'étoffer considérablement avec maintenant dans les données d'entrainement : 
  * Chine : 3500
  * Inde : 9000
  * Japon : 10000
  * Norvège : 9000
  * Tchéquie : 2000
  * USA : 5000

Les photos fournies par les organisateurs du challenge sont toutes labellisées via un fichier annotations qui contient pour chaque photo les coordonnées des bounding box (les carrés qui localisent les défauts dans la photo) et la catégorie de défaut associé à chaque bounding box. 

En 2020, différents types de défauts sont annotés, de façon différente selon le pays, en différentes catégories : 
![image](https://user-images.githubusercontent.com/38078432/188277168-9b5d8833-3350-4daa-b150-cc9e346089dc.png)

----

## 2. Objectifs

Le challenge a pour vocation première la détection de 4 principales catégories : 
  * D00
  * D10
  * D20
  * D40

Néanmoins, en vue d'appliquer cet algorithme à une problématique métier spécifique, nous avons considéré 7 catégories de défauts donc les regroupements sont indiqués par le code couleur dans la table ci-dessus. 

----

## 3. Comment procéder ?

### Pré-requis

### Fichiers 

----

## 4. Overview des principaux résultats 

### Analyse descriptive exploratoire

### Yolov5

----

## 5. Informations

### Outils

Les notebooks ont été développés avec [Visual Studio Code](https://code.visualstudio.com/) et [Google Colab](https://colab.research.google.com/). 

YoloV5 est disponible [ici](https://github.com/ultralytics/yolov5) et YoloV7 [ici](https://github.com/WongKinYiu/yolov7). 

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
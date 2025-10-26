# Projet de Web Scraping – Books to Scrape

## Objectif du projet

Le projet a pour but de concevoir un **script Python automatisé** permettant de scraper un site web (en l’occurrence [Books to Scrape](https://books.toscrape.com)) afin de récupérer des données sur des livres.  

Les informations extraites incluent notamment :
- Le titre du livre
- Son prix
- Sa disponibilité
- Sa note
- Le lien et l’image associée

Les données sont ensuite organisées par catégories et enregistrées dans des dossiers structurés avec :
- Des fichiers CSV contenant les informations textuelles des livres  
- Des fichiers JPG contenant les images correspondantes  

---

## Contexte du projet

L’équipe marketing d’une librairie en ligne souhaite mieux comprendre son catalogue.  
Elle veut collecter des informations sur tous les livres, analyser les catégories, les prix, les notes et la disponibilité en stock.  

En tant que data scientist, votre mission est de **scraper le site web** et de livrer des jeux de données structurés ainsi que des premiers insights.

---

## Installation des dépendances

Avant d’exécuter le script, installez les dépendances nécessaires :

```bash
pip install -r requirements.txt
```

Assurez-vous d'utiliser une versiion récente de Python

---

## Exécution du scraper :
Le script principal s’exécute via la ligne de commande :

```bash
python scrape.py [options]
```

## Options disponibles :

- categories [Nom] -> permet de choisir la ou les catégories à scraper (séparées par des virgules).

- max-pages [Nombre] -> limite le nombre de livres à scraper par catégorie.

- delay [Secondes] -> ajoute un délai entre chaque requête.

- outdir [Chemin] -> définit le dossier de sortie où seront enregistrés les CSV et images.

## Exemples de commandes :

Scraper uniquement la catégorie Travel et limiter à une seule page :

```bash
python scrape.py --categories Travel --max-pages 1
```

Scraper les catégories Travel et Poetry avec un délai d’une seconde entre chaque requête :
```bash
python scrape.py --categories Travel,Poetry --delay 1
```

Changer le dossier de sortie :
```bash
python scrape.py --outdir resultats_scraping
```
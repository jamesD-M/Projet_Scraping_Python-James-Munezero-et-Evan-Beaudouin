# Projet de Web Scraping – Books to Scrape

## Objectif du projet

Ce projet a pour but de concevoir un **script Python automatisé** permettant de scraper le site web [Books to Scrape](https://books.toscrape.com) afin de récupérer des données sur des livres.  

Les informations extraites incluent notamment :
- Le **titre** du livre  
- Son **prix**  
- Sa **disponibilité**  
- Sa **note**  
- Le **lien** et l’**image** associée  

Les données sont ensuite organisées **par catégories** et enregistrées dans des dossiers structurés, comprenant :
- Des fichiers **CSV** contenant les informations textuelles des livres  
- Des fichiers **JPG** contenant les images correspondantes  

## Contexte du projet

L’équipe marketing d’une librairie en ligne souhaite mieux comprendre son catalogue.  
Elle veut collecter des informations sur tous les livres, analyser :
- Les **catégories**
- Les **prix**
- Les **notes**
- La **disponibilité en stock**

En tant que **data scientist**, votre mission est de :
1. Scraper le site web complet  
2. Structurer les données  
3. Livrer un jeu de données exploitable et des **premiers insights**

---

## Installation des dépendances

Avant d’exécuter le script, installez les dépendances nécessaires :

```bash
pip install -r requirements.txt

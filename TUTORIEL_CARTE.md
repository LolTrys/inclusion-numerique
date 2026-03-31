# Guide Méthodologique : Création d'une Carte Interactive de l'Inclusion Numérique

Ce document détaille la démarche pas à pas pour transformer une base de données brute (CSV) en une visualisation géographique interactive déployée sur le web.

---

## 📋 Étape 1 : Préparation de la base de données (Le CSV)
Avant toute chose, votre fichier de données doit être structuré pour être "compris" par une carte.
1.  **Coordonnées GPS** : Assurez-vous d'avoir deux colonnes distinctes pour la Latitude et la Longitude (format décimal, ex: 44.83).
2.  **Colonnes de filtrage** : Identifiez les critères que vous voulez voir apparaître (Nom du lieu, Commune, Public cible).
3.  **Nettoyage** : Vérifiez qu'il n'y a pas de lignes vides ou de coordonnées erronées qui pourraient faire planter l'affichage.

## 🗺️ Étape 2 : Choix des composants de la carte
Une carte interactive se compose de trois couches superposées :
1.  **Le fond de carte** : C'est le dessin des rues et des paysages. Nous avons choisi un style "Voyager" (épuré et clair) pour que les données restent lisibles.
2.  **Le calque administratif** : Ce sont les limites des communes (GeoJSON). Cela permet de situer les points dans leur contexte politique et territorial (Bordeaux Métropole).
3.  **Les données (Marqueurs)** : Ce sont les points issus de votre CSV.

## 🎨 Étape 3 : Logique visuelle et catégorisation
Pour que la carte appuie votre hypothèse (ex: l'insuffisance de l'offre), il faut une lecture visuelle immédiate :
*   **Code couleur** : Nous avons attribué une couleur à chaque niveau de service (Rouge pour Expert, Orange pour Maîtrise, Bleu pour Basique).
*   **Forme des marqueurs** : L'utilisation de "pins" (épingles) avec une pastille centrale permet de mieux localiser le point précis qu'un simple cercle.
*   **Points d'intérêt** : Il est possible d'ajouter des marqueurs spéciaux (comme la Maison Rouge) pour signaler des lieux symboliques ou des anomalies.

## 🖱️ Étape 4 : Interactivité et Informations
La carte ne doit pas être une image fixe, elle doit parler à l'utilisateur :
*   **Les Info-bulles (Popups)** : Au clic, une fenêtre s'ouvre pour donner le détail du lieu (Tarifs, Horaires, Public).
*   **Les Étiquettes permanentes (Tooltips)** : Pour les points cruciaux, le nom s'affiche directement sans avoir besoin de cliquer (ex: "Label Bouse").
*   **Le survol des communes** : Passer la souris sur une zone affiche son nom pour faciliter la navigation géographique.

## 🚀 Étape 5 : Publication et Mise en ligne (GitHub Pages)
Une fois la structure prête, la mise en ligne suit un processus simple :
1.  **Stockage** : On dépose le fichier HTML, le CSV et les limites communales sur un dépôt GitHub.
2.  **Activation** : Dans les réglages (Settings > Pages), on active l'hébergement gratuit.
3.  **Accessibilité** : La carte devient consultable via une adresse URL unique, partageable instantanément.

---

## 💡 Avantages de cette méthode
*   **Mise à jour instantanée** : Si vous modifiez le fichier CSV et que vous le renvoyez sur GitHub, la carte se met à jour toute seule.
*   **Zéro coût** : Toute la chaîne (outils de carte, hébergement) est gratuite.
*   **Mobilité** : La carte est consultable aussi bien sur ordinateur que sur smartphone.

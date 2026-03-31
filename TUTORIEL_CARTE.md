# Étude de cas : Création de la Carte de l'Inclusion Numérique à Bordeaux Métropole

Ce document retrace le cheminement méthodologique suivi pour démontrer, par la donnée et la cartographie, l'hypothèse d'une répartition inégale des efforts d'inclusion numérique sur le territoire.

---

## 🧐 1. L'Audit de la Donnée brute
Tout commence par l'analyse du fichier `RAW_met_lieux_inclusion_numerique.csv`. 
- **Identification des leviers** : Parmi les 42 colonnes, nous avons isolé les plus critiques pour l'analyse : la localisation (GPS), le niveau de service (Expert/Maîtrise/Basique) et le statut de la structure (Public/Privé).
- **Le constat chiffré** : L'analyse statistique a révélé que 45% de l'offre "Expert" est concentrée à Bordeaux centre, laissant les communes périphériques avec une offre très limitée (parfois 1 seul lieu pour 60 000 habitants).

## 💡 2. La Stratégie de Visualisation
Pour transformer ce constat en preuve visuelle, nous avons opté pour une carte interactive "Serverless" (sans base de données) :
- **Lecture directe** : Utilisation de la bibliothèque `PapaParse` pour que le navigateur lise le fichier CSV en temps réel. Cela permet une mise à jour simplifiée : changez le CSV, la carte change.
- **Le moteur de carte** : Choix de `Leaflet.js` pour sa légèreté et sa compatibilité mobile, avec un fond de carte `CartoDB Voyager` pour privilégier la lisibilité des données sur le plan urbain.

## 🗺️ 3. Contextualisation Territoriale
Un point sur une carte vide ne dit rien. Pour prouver "l'insuffisance", il fallait montrer les frontières :
- **Intégration GeoJSON** : Nous avons ajouté les limites administratives des 28 communes de la Métropole. 
- **Résultat** : Les "zones blanches" (villes sans aucun point rouge "Expert") apparaissent immédiatement, rendant l'argument géographique indiscutable.

## 🎨 4. Personnalisation et Narration (Storytelling)
La carte a été "éditorialisée" pour porter un message :
- **Code couleur sémantique** : Rouge pour l'expertise complète, orange pour la maîtrise, bleu pour l'initiation.
- **Marqueurs personnalisés** : Utilisation de "pins" SVG pour une précision chirurgicale.
- **Ajout de points d'intérêt** : Insertion manuelle d'un marqueur symbolique (Grosse Maison Rouge au 1 rue Jacques Ellul) avec un label permanent "**Label Bouse**" pour souligner des zones spécifiques ou des points d'intérêt particuliers.

## 🚀 5. Déploiement et Pérennité
La réussite du projet repose sur sa facilité de partage :
- **GitHub Pages** : Hébergement du code et des données sur la même plateforme.
- **Automatisation** : En utilisant Git, chaque modification du code ou des données est déployée en moins d'une minute sur l'URL publique.

---

## 🏆 Résultat final
Vous avez réussi à créer un outil qui ne se contente pas d'afficher des adresses, mais qui **raconte une situation politique et sociale**. Cette carte est désormais un support de plaidoyer prêt à être présenté, montrant clairement la concentration de l'offre et les inégalités de couverture numérique de la Métropole.

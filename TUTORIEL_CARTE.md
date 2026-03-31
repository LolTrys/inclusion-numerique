# Tutoriel : Créer une Carte Interactive à partir d'un CSV

Ce guide récapitule la méthodologie utilisée pour transformer le fichier `RAW_met_lieux_inclusion_numerique.csv` en une carte interactive web utilisant **Leaflet.js**, **PapaParse** et **GitHub Pages**.

---

## 🚀 Vue d'ensemble de la solution
L'objectif est de créer une application cartographique sans base de données ("Serverless"), où le navigateur lit directement un fichier CSV pour positionner des points sur un fond de carte dynamique.

### Technologies utilisées :
- **Leaflet.js** : Bibliothèque JavaScript de référence pour les cartes interactives.
- **PapaParse** : Analyseur de CSV ultra-rapide pour JavaScript.
- **CartoDB Voyager** : Fond de carte esthétique et lisible (alternative à OpenStreetMap).
- **GitHub Pages** : Hébergement gratuit et automatique du projet.

---

## 🛠️ Étapes de réalisation

### 1. Préparation des données (CSV)
Pour que la carte fonctionne, votre fichier CSV doit impérativement contenir deux colonnes nommées (ou identifiables) :
- `latitude` (ex: 44.8377)
- `longitude` (ex: -0.5791)

*Astuce : Utilisez des noms de colonnes simples sans caractères spéciaux pour faciliter l'intégration.*

### 2. Structure du fichier HTML (`index.html`)
Nous utilisons des liens CDN pour charger les bibliothèques sans installation locale.

```html
<!-- Leaflet CSS & JS -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>

<!-- PapaParse (Analyseur CSV) -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.4.1/papaparse.min.js"></script>

<!-- Conteneur de la carte -->
<div id="map" style="height: 100vh;"></div>
```

### 3. Initialisation de la carte et du fond de carte
On initialise la vue sur Bordeaux et on ajoute les limites des communes via un fichier GeoJSON pour donner du contexte.

```javascript
const map = L.map('map').setView([44.83, -0.57], 11);

// Fond de carte CartoDB Voyager
L.tileLayer('https://{s}.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}{r}.png').addTo(map);

// Optionnel : Ajout des limites communales (GeoJSON)
fetch('communes_bordeaux_metropole.geojson')
    .then(res => res.json())
    .then(data => L.geoJSON(data).addTo(map));
```

### 4. Lecture dynamique du CSV avec PapaParse
Cette étape est cruciale car elle lie vos données brutes à la visualisation géographique.

```javascript
Papa.parse('votre_fichier.csv', {
    download: true,
    header: true,
    dynamicTyping: true,
    complete: function(results) {
        results.data.forEach(row => {
            if (row.latitude && row.longitude) {
                // Création d'un marqueur personnalisé
                const marker = L.marker([row.latitude, row.longitude]).addTo(map);
                
                // Popup au clic avec les infos du CSV
                marker.bindPopup(`<b>${row.nom}</b><br>${row.adresse_commune}`);
            }
        });
    }
});
```

### 5. Personnalisation avancée
- **Icônes SVG (Pins)** : Utilisez `L.divIcon` pour injecter du code SVG et changer la couleur selon une donnée (ex: Rouge pour "Expert", Bleu pour "Basique").
- **Labels permanents** : Utilisez `.bindTooltip("Texte", { permanent: true })` pour afficher des noms (comme "Label Bouse") sans action de l'utilisateur.

---

## 🌍 Déploiement sur le Web (GitHub Pages)

1. **Pousser les fichiers sur GitHub** :
   ```bash
   git add .
   git commit -m "Mise en ligne de la carte"
   git push origin main
   ```
2. **Activer l'hébergement** :
   - Allez sur votre dépôt GitHub.
   - **Settings** > **Pages**.
   - Dans "Branch", sélectionnez `main` (ou la branche de votre choix) et cliquez sur **Save**.
   - Votre carte sera accessible à l'adresse : `https://[votre-pseudo].github.io/[nom-du-depot]/`

---

## 💡 Maintenance
Pour mettre à jour votre carte, il vous suffit de remplacer le fichier CSV par une nouvelle version portant le même nom et de faire un `git push`. La carte se mettra à jour automatiquement pour tous les utilisateurs.

import csv
from collections import Counter

def analyser_donnees(file_path):
    # Hiérarchie des niveaux de service
    hierarchy = {'Expert': 3, 'Maîtrise': 2, 'Basique': 1, 'Non': 0}
    
    stats_niveaux = Counter()
    stats_communes_expert = Counter()
    stats_statut = Counter()
    total_lieux = 0

    try:
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                total_lieux += 1
                ns = row.get('niveau_service', '')
                commune = row.get('adresse_commune', 'Inconnue').strip()
                statut = row.get('statut', 'Inconnu').strip()
                
                # 1. Calcul du niveau max par lieu
                max_val = -1
                max_label = 'Non renseigné'
                is_expert = False
                
                if ns:
                    items = ns.split(',')
                    for item in items:
                        if '/' in item:
                            level = item.split('/')[-1].strip()
                            val = hierarchy.get(level, -1)
                            if val > max_val:
                                max_val = val
                                max_label = level
                            if level == 'Expert':
                                is_expert = True
                
                stats_niveaux[max_label] += 1
                
                # 2. Compte des experts par commune
                if is_expert:
                    stats_communes_expert[commune] += 1
                
                # 3. Répartition Public/Privé
                if statut:
                    stats_statut[statut] += 1

        # Affichage des résultats
        print(f"--- ANALYSE DE L'INCLUSION NUMÉRIQUE (Total: {total_lieux} lieux) ---")
        
        print("\n1. Répartition par niveau de service maximal :")
        for level in ['Expert', 'Maîtrise', 'Basique', 'Non', 'Non renseigné']:
            count = stats_niveaux[level]
            pct = (count / total_lieux) * 100 if total_lieux > 0 else 0
            print(f"   - {level}: {count} ({pct:.1f}%)")

        print("\n2. Top 10 des communes par nombre de lieux 'Expert' :")
        for commune, count in stats_communes_expert.most_common(10):
            print(f"   - {commune}: {count}")

        print("\n3. Répartition par statut juridique :")
        for statut, count in stats_statut.most_common():
            pct = (count / total_lieux) * 100 if total_lieux > 0 else 0
            print(f"   - {statut}: {count} ({pct:.1f}%)")

    except FileNotFoundError:
        print(f"Erreur : Le fichier {file_path} est introuvable.")

if __name__ == "__main__":
    CSV_FILE = 'RAW_met_lieux_inclusion_numerique - RAW_met_lieux_inclusion_numerique.csv'
    analyser_donnees(CSV_FILE)

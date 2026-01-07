# Magic Background Remover 🪄

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![PySide6](https://img.shields.io/badge/PySide6-6.5%2B-purple)
![Rembg](https://img.shields.io/badge/Rembg-AI%20Powered-green)
![License](https://img.shields.io/badge/License-MIT-yellow)

Une application GUI élégante et puissante pour supprimer automatiquement les arrière-plans des images grâce à l'IA. Transformez vos photos en quelques clics !

## ✨ Fonctionnalités

### 🪄 Suppression Intelligente d'Arrière-plan
- **Technologie IA avancée** : Utilise le modèle U²-Net pour une détection précise
- **Préservation des détails** : Contours nets et conservations des textures
- **Traitement rapide** : Génération en quelques secondes
- **Haute qualité** : Résolution conservée, pas de compression destructive

### 🖼️ Support Multi-format
- **Formats d'entrée** : PNG, JPG, JPEG, BMP, TIFF
- **Format de sortie** : PNG avec transparence
- **Résolution native** : Conservation des dimensions originales
- **Couleurs préservées** : Pas d'altération des teintes

### 🎨 Interface Moderne
- **Design élégant** : Interface sombre/thème clair au choix
- **Comparaison côte à côte** : Avant/Après en temps réel
- **Feedback visuel** : Barre de progression et messages d'état
- **Interface intuitive** : Boutons clairs et organisation logique

### ⚡ Performance Optimisée
- **Traitement asynchrone** : Pas de blocage de l'interface
- **Gestion mémoire** : Traitement efficace des grandes images
- **Thread dédié** : CPU utilisé efficacement
- **Réduction automatique** : Prévisualisation optimisée

## 🖼️ Aperçu de l'Application

```
┌─────────────────────────────────────────────────────┐
│          🪄 Magic Background Remover                 │
├─────────────────────────────────────────────────────┤
│  [📷 Upload Image]  [✨ Remove Background]  [💾 Save]│
├─────────────────────────────────────────────────────┤
│  ┌─────────────────┐     ┌─────────────────┐       │
│  │  Original Image │     │ Processed Image │       │
│  │                 │     │                 │       │
│  │  [Votre image]  │     │  [Arrière-plan  │       │
│  │                 │     │    supprimé]    │       │
│  │  Before         │     │  After          │       │
│  └─────────────────┘     └─────────────────┘       │
│                                                     │
│  [██████████████████████████████░░░░░░░░] 75%       │
│  Processing image with AI... ⏳                     │
│                                                     │
│  Ready to remove backgrounds! 🚀                   │
└─────────────────────────────────────────────────────┘
```

## 🚀 Installation Rapide

### Prérequis
- Python 3.8 ou supérieur
- 2GB d'espace disque libre
- Connexion internet (pour télécharger le modèle IA)

### Installation en 4 Étapes

```bash
# 1. Cloner le dépôt
git clone https://github.com/votre-username/magic-background-remover.git
cd magic-background-remover

# 2. Créer un environnement virtuel (recommandé)
python -m venv venv

# 3. Activer l'environnement
# Sur Windows :
venv\Scripts\activate
# Sur Linux/Mac :
source venv/bin/activate

# 4. Installer les dépendances
pip install -r requirements.txt
```

### Fichier requirements.txt
```txt
PySide6>=6.5.0
rembg>=2.0.50
pillow>=10.0.0
opencv-python>=4.8.0
numpy>=1.24.0
```

## 📦 Téléchargement du Modèle IA

Au premier lancement, l'application télécharge automatiquement le modèle U²-Net :
- **Taille** : ~176MB
- **Type** : Modèle ONNX optimisé
- **Stockage** : `~/.u2net/u2net.onnx`
- **Une seule fois** : Téléchargement initial seulement

**Note** : Le téléchargement peut prendre 1-2 minutes selon votre connexion.

## 🎮 Guide d'Utilisation

### 1. **Lancement de l'Application**
```bash
python background_remover.py
```

### 2. **Chargement d'une Image**
1. Cliquez sur **"📷 Upload Image"**
2. Sélectionnez une image depuis votre ordinateur
3. L'image originale s'affiche dans la zone de gauche

### 3. **Suppression de l'Arrière-plan**
1. Cliquez sur **"✨ Remove Background"**
2. Observez la barre de progression
3. L'image traitée apparaît dans la zone de droite

### 4. **Sauvegarde du Résultat**
1. Cliquez sur **"💾 Save Result"**
2. Choisissez l'emplacement et le nom de fichier
3. L'image est sauvegardée en PNG avec transparence

## 🎛️ Fonctionnalités Avancées

### 🔄 Traitement par Lots
```python
# Exemple de script pour traiter plusieurs images
import os
from rembg import remove
from PIL import Image

input_folder = "input_images/"
output_folder = "output_images/"

for filename in os.listdir(input_folder):
    if filename.endswith(('.png', '.jpg', '.jpeg')):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, f"processed_{filename}")
        
        with open(input_path, 'rb') as f:
            input_data = f.read()
            output_data = remove(input_data)
        
        with open(output_path, 'wb') as f:
            f.write(output_data)
```

### 🎨 Personnalisation
L'application supporte plusieurs paramètres de traitement :

| Paramètre | Description | Valeur par défaut |
|-----------|-------------|-------------------|
| Modèle | Modèle IA utilisé | u2net (recommandé) |
| Alpha Matting | Améliore les cheveux/fourrures | Désactivé |
| Post-processing | Nettoyage des contours | Activé |

## 📊 Performances

| Type d'Image | Temps de Traitement | Taille du Modèle | Usage Mémoire |
|--------------|---------------------|------------------|---------------|
| Portrait (1MB) | 2-3 secondes | 176MB | ~500MB |
| Paysage (3MB) | 4-5 secondes | 176MB | ~800MB |
| HD (5MB+) | 8-10 secondes | 176MB | 1-2GB |

**Recommandations** :
- Images < 10MP pour un traitement optimal
- Éclairage uniforme pour de meilleurs résultats
- Contraste élevé entre sujet et arrière-plan

## 🛠️ Développement

### Architecture du Code
```
magic-background-remover/
├── background_remover.py     # Application principale
├── requirements.txt          # Dépendances
├── README.md                # Documentation
└── assets/                  # Ressources
    ├── icons/              # Icônes de l'application
    └── screenshots/        # Captures d'écran
```

### Structure de l'Application
```python
# Architecture MVC simplifiée
class BackgroundRemoverApp(QMainWindow):
    """
    Vue : Interface utilisateur PySide6
    """
    def initUI(self): ...

class WorkerThread(QThread):
    """
    Modèle : Traitement IA dans un thread séparé
    """
    def run(self): ...

# Contrôleur : Signaux/Slots PySide6
worker.finished.connect(self.on_processing_finished)
```

### Extensibilité
```python
# Ajouter de nouveaux modèles IA
MODELS_AVAILABLE = {
    'u2net': 'u2net.onnx',           # Modèle généraliste
    'u2netp': 'u2netp.onnx',         # Modèle léger
    'u2net_human_seg': 'u2net_human_seg.onnx',  # Spécialisé visages
    'silueta': 'silueta.onnx',       # Silhouettes
}

# Ajouter des filtres post-traitement
def apply_post_processing(image):
    """Filtres optionnels après suppression d'arrière-plan"""
    # Nettoyage des bords
    # Ajout d'ombre portée
    # Changement de couleur d'arrière-plan
    # Ajout de bordures
    return processed_image
```

## 🐛 Dépannage

### Problèmes Courants

| Symptôme | Solution |
|----------|----------|
| "No module named 'rembg'" | `pip install rembg pillow` |
| Modèle non téléchargé | Vérifiez la connexion internet |
| Mémoire insuffisante | Réduisez la taille de l'image |
| Interface figée | Attendez la fin du traitement |
| Qualité médiocre | Utilisez des images avec bon contraste |

### Mode Debug
```bash
# Activer les logs détaillés
export U2NET_DEBUG=1
python background_remover.py
```

## 🌟 Cas d'Utilisation

### 🏢 Professionnels
- **Photographes** : Préparation d'images pour montages
- **E-commerce** : Suppression d'arrière-plan pour produits
- **Designers** : Création de ressources graphiques
- **Réseaux sociaux** : Optimisation des photos de profil

### 🎓 Éducation
- **Projets scolaires** : Création de présentations
- **Recherche** : Traitement d'images scientifiques
- **Art numérique** : Préparation d'assets créatifs

### 👤 Personnel
- **Photos de profil** : Création d'avatars transparents
- **Création de mèmes** : Isolation de sujets
- **Art amateur** : Montages photo simples

## 🔮 Roadmap

### Version 1.1 (Prochainement)
- [ ] Traitement par lots
- [ ] Glisser-déposer des fichiers
- [ ] Prévisualisation en temps réel
- [ ] Sélection de modèle IA

### Version 1.2
- [ ] Éditeur intégré (recadrage, ajustements)
- [ ] Bibliothèque d'arrière-plans
- [ ] Export vers différents formats
- [ ] Plugins et extensions

### Version 2.0
- [ ] API web
- [ ] Application desktop native
- [ ] Intégration cloud
- [ ] Fonctionnalités collaboratives

## 🤝 Contribution

Les contributions sont les bienvenues !

### Comment contribuer
1. **Fork** le dépôt
2. **Créez une branche** : `git checkout -b feature/nouvelle-fonctionnalite`
3. **Commitez** vos changements : `git commit -am 'Ajout de fonctionnalité'`
4. **Push** vers la branche : `git push origin feature/nouvelle-fonctionnalite`
5. **Ouvrez une Pull Request**

### Bonnes pratiques
- Suivez les conventions PEP 8
- Ajoutez des tests pour les nouvelles fonctionnalités
- Documentez votre code
- Mettez à jour le README si nécessaire

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

```
MIT License

Copyright (c) 2024 Magic Background Remover

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```

## 👥 Auteurs

- **Développeur Principal** - [ omar badrani](https://github.com/omarbadrani)
- **Contributeurs** -(https://github.com/omarbadrani/remove_background)

## 🙏 Remerciements

- **Rembg** : Pour la bibliothèque IA exceptionnelle
- **PySide6** : Pour le framework GUI robuste
- **U²-Net** : Pour le modèle de segmentation avancé
- **Tous les utilisateurs** : Pour les retours et suggestions

## 📞 Support

Besoin d'aide ?

1. **Consultez** les [Issues](https://github.com/votre-username/magic-background-remover/issues)
2. **Créez une nouvelle issue** avec :
   - Description claire du problème
   - Étapes pour reproduire
   - Capture d'écran
   - Version de l'application
3. **Contact** : votre-email@example.com

## 🌐 Liens Utiles

- [Documentation Rembg](https://github.com/danielgatis/rembg)
- [Documentation PySide6](https://doc.qt.io/qt-6/pyside6.html)
- [Modèle U²-Net](https://github.com/xuebinqin/U-2-Net)
- [Guide de contribution](CONTRIBUTING.md)

---

⭐ **Si vous aimez ce projet, n'oubliez pas de mettre une étoile sur GitHub !** ⭐

---

## 📱 Téléchargements

### Version Portable (Bientôt disponible)
- **Windows** : `.exe` autonome
- **macOS** : `.dmg` avec installation facile
- **Linux** : `.AppImage` universel

### Installation via Pip (Planifiée)
```bash
pip install magic-background-remover
magic-bg-remover
```

---

**Dernière mise à jour** : Janvier 2024  
**Version** : 1.0.0  
**Support Python** : 3.8+  
**Systèmes supportés** : Windows 10+, macOS 10.15+, Linux

---

*Magic Background Remover - Donnez vie à vos images en supprimant l'arrière-plan en un clic !* 🪄✨

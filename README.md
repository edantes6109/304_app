# QCM — Annales d'examens & simulateur (UT2J, L2 Psychologie)

Applications web statiques d'entraînement aux examens, une par UE. Chaque UE a son propre dossier (`304/`, `301/`, …) ; le code HTML/JS est **partagé** et généré par un unique script de build.

## 🚀 Fonctionnalités
- **Annales officielles** (QCM + questions ouvertes avec réponses détaillées).
- **Entraînement flexible** : par thématique de cours ou par document d'annale source.
- **Générateur IA intégré** : banque de questions complémentaires (Gemini / OpenAI avec votre propre clé).
- **Accès restreint par email + PIN** (hachage SHA-256, liens magiques en 1 clic).
- **Mode sombre**, raccourcis clavier, accessibilité clavier.

## 📂 Structure du projet
```
qcm_project/
├── build.py                 # Script de build unique (python3 build.py [UE...])
├── template/app.html        # Gabarit HTML/JS partagé (source de vérité de l'interface)
├── index.html               # Page d'accueil générée (liste des UE) — servie par GitHub Pages
├── package.json             # Outil de build : CLI Tailwind
├── tailwind.config.js
├── archive/                 # Anciennes maquettes (ignoré par git)
├── 304/                     # UE 304 — Psychologie Clinique
│   ├── ue.json              # Identité de l'UE (code, titre, niveau)
│   ├── data/                # questions_database.json, open_questions.json, embedded_ai_bank.json
│   ├── docs/                # PDF de cours, fichiers Excel (local uniquement)
│   ├── scripts/             # Scripts de maintenance des données
│   ├── allowed_emails.json  # Accès autorisés (local uniquement, voir l'exemple)
│   └── index.html           # Application générée pour cette UE
└── 301/                     # (à créer) même structure
```
Ne modifiez jamais les `index.html` à la main : ils sont écrasés à chaque build. Modifiez `template/app.html` (interface) ou les fichiers de `data/`.

## ➕ Ajouter une UE (ex. 301)
1. Créez `301/ue.json` :
   ```json
   { "code": "301", "title": "Titre de l'UE", "short_title": "Titre court", "level": "L2 Psychologie" }
   ```
2. Ajoutez `301/data/questions_database.json`, `open_questions.json` et `embedded_ai_bank.json` (même format que `304/data/`).
3. Ajoutez `301/allowed_emails.json` (voir `304/allowed_emails.example.json`).
4. `python3 build.py 301` — la page d'accueil se met à jour automatiquement.

> ⚠️ **Limite actuelle** : l'identité (code, titre) et les données sont paramétrées, mais la structure thématique de l'interface (Parties 1 & 2, chapitres et filtres de `CHAPTER_CATEGORIES`, liste `OFFICIAL_DOCUMENTS`, liste des thèmes du générateur IA et textes des prompts IA) est encore propre à l'UE 304 dans `template/app.html`. Elle devra être adaptée/paramétrée selon le plan de cours de la 301.

## 🛠️ Utilisation locale

### 1. Configurer les emails autorisés
Modifiez `304/allowed_emails.json` :
```json
[
  { "email": "mon.email@gmail.com", "pin": "1234" },
  { "email": "ami1@gmail.com", "pin": "5678" }
]
```

### 2. Générer
```bash
npm install            # une seule fois (installe le CLI Tailwind, outil de build uniquement)
python3 build.py       # toutes les UE + la page d'accueil
python3 build.py 304   # une seule UE
```
Le script précompile Tailwind (CSS inliné, aucun CDN requis ; repli sur le CDN si `npm install` n'a pas été fait), injecte les empreintes cryptographiques anonymisées et affiche les liens magiques (`304/?email=…&pin=…`).

## ⌨️ Raccourcis clavier (onglet Quiz)
- `←` / `→` : question précédente / suivante
- `A`–`E` : cocher/décocher une proposition
- `Entrée` : valider la réponse
- `Échap` : fermer le générateur IA

> ⚠️ **Note sécurité** : l'accès par email + PIN est une barrière légère côté navigateur. Les questions sont embarquées dans la page et restent lisibles via le code source.

## 🌐 Déploiement GitHub Pages
1. Dépôt GitHub : `https://github.com/edantes6109/304_app`
2. Dans **Settings** > **Pages** > **Build and deployment** > **Branch**, sélectionnez `main` et le dossier `/ (root)`.
3. Après build, committez `index.html` (accueil) et les `<UE>/index.html` générés. L'application est en ligne à :
   - Accueil : `https://edantes6109.github.io/304_app/`
   - UE 304 : `https://edantes6109.github.io/304_app/304/`

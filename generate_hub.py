# -*- coding: utf-8 -*-
from pathlib import Path
import json

# =====================================================================
# CONFIGURATION DE L'ÉCOSYSTÈME (À MODIFIER FACILEMENT)
# =====================================================================
SITE_TITLE = "Guides & Recommandations Audio Experts"
SITE_DESC = "Sélection d'équipements audio haute performance avec guides d'achat indépendants."

# Base de données produits ultra-pro (Simplicité de maintenance)
PRODUCTS = [
    {
        "name": "Focusrite Scarlett 2i2",
        "category": "Interface Audio",
        "summary": "L'interface audio USB de référence pour le home studio, le podcast et l'enregistrement de voix de qualité professionnelle.",
        "affiliate_url": "https://example.com/aff-link-focusrite",
        "badge_color": "#0f766e"
    },
    {
        "name": "Audio-Technica ATH-M50x",
        "category": "Casque Studio",
        "summary": "Un casque professionnel fermé plébiscité par les ingénieurs du son pour sa précision de monitoring incomparable.",
        "affiliate_url": "https://example.com/aff-link-athm50x",
        "badge_color": "#b45309"
    }
]

# =====================================================================
# MOTEUR DE GÉNÉRATION INDUSTRIEL
# =====================================================================
def build_structure():
    """Garantit une structure propre directement à la racine pour GitHub"""
    for folder in ["public/assets", ".github/workflows", "data"]:
        Path(folder).mkdir(parents=True, exist_ok=True)

def save_data_backup():
    """Sauvegarde les données au format JSON pour une utilisation future ou API"""
    with open("data/products.json", "w", encoding="utf-8") as f:
        json.dump(PRODUCTS, f, indent=2, ensure_ascii=False)

def generate_html():
    """Génère l'interface HTML5 Premium optimisée SEO & Conversion"""
    cards_html = []
    
    for p in PRODUCTS:
        card = f"""
        <article class="product-card">
            <span class="badge" style="color: {p['badge_color']}; border-color: {p['badge_color']}1a; background: {p['badge_color']}0d;">
                {p['category']}
            </span>
            <h2>{p['name']}</h2>
            <p class="summary">{p['summary']}</p>
            <div class="disclosure">ℹ️ Recommandation indépendante avec lien d'affiliation officiel sponsorisé.</div>
            <a class="btn-purchase" href="{p['affiliate_url']}" target="_blank" rel="noopener noreferrer nofollow sponsored">
                Vérifier la disponibilité en ligne
            </a>
        </article>
        """
        cards_html.append(card)

    html_template = f"""<!doctype html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>{SITE_TITLE}</title>
    <meta name="description" content="{SITE_DESC}">
    
    <meta property="og:title" content="{SITE_TITLE}">
    <meta property="og:description" content="{SITE_DESC}">
    <meta property="og:type" content="website">
    
    <link rel="stylesheet" href="./public/assets/style.css">
</head>
<body>
    <header class="hero-section">
        <div class="container">
            <h1>{SITE_TITLE}</h1>
            <p class="subtitle">{SITE_DESC}</p>
        </div>
    </header>

    <main class="container grid-layout">
        {"".join(cards_html)}
    </main>
</body>
</html>
"""
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_template.strip())

def generate_css():
    """Génère un design minimaliste premium (Ergonomie de Gagnant)"""
    css_content = """
    :root {
        --bg-global: #f8fafc;
        --bg-card: #ffffff;
        --text-main: #0f172a;
        --text-muted: #64748b;
        --border-color: #e2e8f0;
        --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05), 0 2px 4px -2px rgb(0 0 0 / 0.05);
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body {
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif;
        background-color: var(--bg-global);
        color: var(--text-main);
        line-height: 1.5;
    }

    .container {
        width: min(1200px, 90%);
        margin: 0 auto;
    }

    .hero-section {
        padding: 60px 0 40px;
        text-align: center;
    }

    .hero-section h1 {
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.05em;
        margin-bottom: 12px;
    }

    .hero-section .subtitle {
        font-size: 1.15rem;
        color: var(--text-muted);
    }

    .grid-layout {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
        gap: 30px;
        padding-bottom: 60px;
    }

    .product-card {
        background: var(--bg-card);
        border: 1px solid var(--border-color);
        border-radius: 16px;
        padding: 28px;
        box-shadow: var(--shadow);
        display: flex;
        flex-direction: column;
    }

    .badge {
        display: inline-block;
        align-self: flex-start;
        padding: 4px 12px;
        font-size: 0.75rem;
        font-weight: 700;
        border-radius: 9999px;
        border: 1px solid;
        margin-bottom: 16px;
    }

    .product-card h2 {
        font-size: 1.35rem;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .summary {
        color: var(--text-muted);
        font-size: 0.95rem;
        margin-bottom: 20px;
        flex-grow: 1;
    }

    .disclosure {
        font-size: 0.8rem;
        color: var(--text-muted);
        background: var(--bg-global);
        padding: 10px;
        border-radius: 8px;
        margin-bottom: 16px;
    }

    .btn-purchase {
        display: block;
        text-align: center;
        background: #0f172a;
        color: #ffffff;
        text-decoration: none;
        padding: 14px;
        border-radius: 10px;
        font-weight: 600;
        font-size: 0.95rem;
        transition: background 0.2s;
    }

    .btn-purchase:hover {
        background: #1e293b;
    }
    """
    with open("public/assets/style.css", "w", encoding="utf-8") as f:
        f.write(css_content.strip())

def generate_workflow():
    """Génère la configuration GitHub Action pour un déploiement GitHub Pages instantané"""
    workflow_content = """
name: Deploy Hub Custom

on:
  push:
    branches: ["main"]
  workflow_dispatch:

permissions:
  contents: read
  pages: write
  id-token: write

jobs:
  deploy:
    environment:
      name: github-pages
      url: ${{ steps.deployment.outputs.page_url }}
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4

      - name: Setup Pages
        uses: actions/configure-pages@v5

      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.' # Déploiement direct depuis la racine (Optimisé !)

      - name: Deploy to GitHub Pages
        id: deployment
        uses: actions/deploy-pages@v4
"""
    with open(".github/workflows/pages.yml", "w", encoding="utf-8") as f:
        f.write(workflow_content.strip())

def main():
    build_structure()
    save_data_backup()
    generate_html()
    generate_css()
    generate_workflow()
    print("✅ Écosystème d'affiliation généré avec succès à la racine du projet.")

if __name__ == "__main__":
    main()

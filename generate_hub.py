# -*- coding: utf-8 -*-
from pathlib import Path
import json

def build_structure():
    """Garantit la présence des dossiers requis"""
    for folder in ["public/assets", ".github/workflows", "data"]:
        Path(folder).mkdir(parents=True, exist_ok=True)

def load_catalogue():
    """Charge les données de configuration et de produits depuis le fichier JSON"""
    json_path = Path("data/catalogue.json")
    if not json_path.exists():
        # Si le fichier n'existe pas, on lève une erreur claire
        raise FileNotFoundError("❌ Le fichier 'data/catalogue.json' est introuvable. Veuillez le créer d'abord.")
    
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_html(config, products):
    """Génère l'interface HTML5 Premium basée sur le catalogue JSON"""
    cards_html = []
    
    for p in products:
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
    <title>{config['site_title']}</title>
    <meta name="description" content="{config['site_description']}">
    
    <meta property="og:title" content="{config['site_title']}">
    <meta property="og:description" content="{config['site_description']}">
    <meta property="og:type" content="website">
    
    <link rel="stylesheet" href="./public/assets/style.css">
</head>
<body>
    <header class="hero-section">
        <div class="container">
            <h1>{config['site_title']}</h1>
            <p class="subtitle">{config['site_description']}</p>
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
    """Génère le design épuré haute conversion"""
    css_content = """
    :root {
        --bg-global: #f8fafc;
        --bg-card: #ffffff;
        --text-main: #0f172a;
        --text-muted: #64748b;
        --border-color: #e2e8f0;
        --shadow: 0 4px 6px -1px rgb(0 0 0 / 0.05);
    }
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; background-color: var(--bg-global); color: var(--text-main); line-height: 1.5; }
    .container { width: min(1200px, 90%); margin: 0 auto; }
    .hero-section { padding: 60px 0 40px; text-align: center; }
    .hero-section h1 { font-size: 2.5rem; font-weight: 800; margin-bottom: 12px; letter-spacing: -0.05em; }
    .hero-section .subtitle { font-size: 1.15rem; color: var(--text-muted); }
    .grid-layout { display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; padding-bottom: 60px; }
    .product-card { background: var(--bg-card); border: 1px solid var(--border-color); border-radius: 16px; padding: 28px; box-shadow: var(--shadow); display: flex; flex-direction: column; }
    .badge { display: inline-block; align-self: flex-start; padding: 4px 12px; font-size: 0.75rem; font-weight: 700; border-radius: 9999px; border: 1px solid; margin-bottom: 16px; }
    .product-card h2 { font-size: 1.35rem; font-weight: 700; margin-bottom: 12px; }
    .summary { color: var(--text-muted); font-size: 0.95rem; margin-bottom: 20px; flex-grow: 1; }
    .disclosure { font-size: 0.8rem; color: var(--text-muted); background: var(--bg-global); padding: 10px; border-radius: 8px; margin-bottom: 16px; }
    .btn-purchase { display: block; text-align: center; background: #0f172a; color: #ffffff; text-decoration: none; padding: 14px; border-radius: 10px; font-weight: 600; font-size: 0.95rem; }
    .btn-purchase:hover { background: #1e293b; }
    """
    with open("public/assets/style.css", "w", encoding="utf-8") as f:
        f.write(css_content.strip())

def generate_workflow():
    """Génère la configuration GitHub Action de déploiement"""
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
    runs-on: ubuntu-latest
    steps:
      - name: Checkout
        uses: actions/checkout@v4
      - name: Setup Pages
        uses: actions/configure-pages@v5
      - name: Upload artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: '.'
      - name: Deploy to GitHub Pages
        uses: actions/deploy-pages@v4
"""
    with open(".github/workflows/pages.yml", "w", encoding="utf-8") as f:
        f.write(workflow_content.strip())

def main():
    try:
        build_structure()
        # Nouvelle logique : On charge d'abord le JSON extérieur
        catalogue = load_catalogue()
        config = catalogue["theme_configuration"]
        products = catalogue["products"]
        
        # Ensuite on génère à partir de ces données
        generate_html(config, products)
        generate_css()
        generate_workflow()
        print("✅ Machine synchronisée ! Votre site a été mis à jour à partir de data/catalogue.json.")
    except Exception as e:
        print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    main()

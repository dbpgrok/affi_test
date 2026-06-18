# -*- coding: utf-8 -*-
from pathlib import Path
import json
import subprocess

def build_structure():
    """Garantit la présence des dossiers requis"""
    for folder in ["public/assets", ".github/workflows", "data"]:
        Path(folder).mkdir(parents=True, exist_ok=True)

def load_catalogue():
    """Charge les données de configuration et de produits depuis le fichier JSON"""
    json_path = Path("data/catalogue.json")
    if not json_path.exists():
        raise FileNotFoundError("❌ Le fichier 'data/catalogue.json' est introuvable.")
    with open(json_path, "r", encoding="utf-8") as f:
        return json.load(f)

def generate_html(config, products):
    """Génère l'interface HTML5 Premium validée pour le SEO et la Haute Conversion"""
    cards_html = []
    
    for p in products:
        # Piliers SEO : Construction des données structurées Google (JSON-LD)
        json_ld_product = {
            "@context": "https://schema.org",
            "@type": "Product",
            "name": p['name'],
            "description": p['summary'],
            "brand": {"@type": "Brand", "name": p.get('brand', 'Premium Selection')}
        }
        
        card = f"""
        <script type="application/ld+json">{json.dumps(json_ld_product)}</script>

        <article class="product-card">
            <span class="badge" style="color: {p['badge_color']}; border-color: {p['badge_color']}1a; background: {p['badge_color']}0d;">
                🎯 {p['category']}
            </span>
            <h2>{p['name']}</h2>
            <p class="summary">{p['summary']}</p>
            
            <div class="disclosure-box">
                <span class="icon">ℹ️</span>
                <p>Avis indépendant. En cliquant sur le bouton ci-dessous, vous êtes redirigé vers l'offre officielle sécurisée. Nous pouvons percevoir une commission sans aucun surcoût pour vous.</p>
            </div>
            
            <a class="btn-purchase" href="{p['affiliate_url']}" target="_blank" rel="noopener noreferrer nofollow sponsored">
                Vérifier la disponibilité et les avis ➔
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
    """Génère le design épuré type 'Apple-like' axé sur la clarté et le contraste"""
    css_content = """
    :root {
        --bg-global: #f8fafc;
        --bg-card: #ffffff;
        --text-main: #0f172a;
        --text-muted: #64748b;
        --border-color: #e2e8f0;
        --shadow: 0 10px 15px -3px rgb(0 0 0 / 0.05), 0 4px 6px -4px rgb(0 0 0 / 0.05);
    }
    
    * { box-sizing: border-box; margin: 0; padding: 0; }
    
    body { 
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; 
        background-color: var(--bg-global); 
        color: var(--text-main); 
        line-height: 1.6; 
    }
    
    .container { width: min(1200px, 90%); margin: 0 auto; }
    
    .hero-section { padding: 80px 0 50px; text-align: center; }
    .hero-section h1 { font-size: 2.8rem; font-weight: 800; margin-bottom: 16px; letter-spacing: -0.05em; color: #0f172a; }
    .hero-section .subtitle { font-size: 1.25rem; color: var(--text-muted); max-width: 600px; margin: 0 auto; }
    
    .grid-layout { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 32px; padding-bottom: 80px; }
    
    .product-card { 
        background: var(--bg-card); 
        border: 1px solid var(--border-color); 
        border-radius: 20px; 
        padding: 32px; 
        box-shadow: var(--shadow); 
        display: flex; 
        flex-direction: column; 
        transition: transform 0.2s, box-shadow 0.2s;
    }
    .product-card:hover {
        transform: translateY(-2px);
        box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1);
    }
    
    .badge { display: inline-block; align-self: flex-start; padding: 6px 16px; font-size: 0.8rem; font-weight: 700; border-radius: 9999px; border: 1px solid; margin-bottom: 20px; }
    
    .product-card h2 { font-size: 1.5rem; font-weight: 700; margin-bottom: 14px; letter-spacing: -0.03em; }
    
    .summary { color: var(--text-muted); font-size: 1rem; margin-bottom: 24px; flex-grow: 1; }
    
    .disclosure-box { 
        display: flex;
        gap: 12px;
        font-size: 0.85rem; 
        color: var(--text-muted); 
        background: #f1f5f9; 
        padding: 16px; 
        border-radius: 12px; 
        margin-bottom: 24px; 
    }
    .disclosure-box .icon { font-size: 1.1rem; }
    
    .btn-purchase { 
        display: block; 
        text-align: center; 
        background: #0f172a; 
        color: #ffffff; 
        text-decoration: none; 
        padding: 16px; 
        border-radius: 12px; 
        font-weight: 600; 
        font-size: 1rem; 
        transition: background 0.2s;
    }
    .btn-purchase:hover { background: #1e293b; }
    """
    with open("public/assets/style.css", "w", encoding="utf-8") as f:
        f.write(css_content.strip())

def generate_workflow():
    """Génère la configuration GitHub Action de déploiement automatique"""
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

def deploy_to_github():
    """Exécute la séquence de push Git automatiquement en arrière-plan"""
    print("⚡ Séquence Git automatique en cours...")
    try:
        subprocess.run(["git", "add", "."], check=True)
        subprocess.run(["git", "commit", "-m", "Mise à jour automatique du catalogue via Python"], check=True)
        subprocess.run(["git", "push", "origin", "main"], check=True)
        print("🚀 [SUCCÈS GIT] Les modifications ont été poussées. Actualisez votre page dans 60s !")
    except subprocess.CalledProcessError as e:
        print(f"⚠️ Note Git : Rien à mettre à jour ou conflit mineur ({e})")

def main():
    try:
        build_structure()
        catalogue = load_catalogue()
        config = catalogue["theme_configuration"]
        products = catalogue["products"]
        
        generate_html(config, products)
        generate_css()
        generate_workflow()
        print("✅ Fichiers locaux générés avec succès.")
        
        # Déclenchement de la mise en ligne automatique
        deploy_to_github()
        
    except Exception as e:
        print(f"❌ Erreur générale : {e}")

if __name__ == "__main__":
    main()

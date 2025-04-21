from flask import Flask

# Créer une instance de l'application Flask
app = Flask(__name__)

# Définir une route pour la page d'accueil
@app.route('/')
def home():
    return "Bonjour ! Votre application fonctionne correctement."

# Point d'entrée principal
if __name__ == '__main__':
    # Lancer l'application sur le port 8080
    app.run(host='0.0.0.0', port=8080)
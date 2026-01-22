import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    # Simulamos la obtención de un secreto de un Vault
    db_password = os.getenv('DB_PASSWORD', 'default_pass')
    return f"App segura. Secreto recuperado."

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

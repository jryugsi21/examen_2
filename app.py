import os
import psycopg2
from flask import Flask

app = Flask(__name__)

# Configuración
APP_NAME = os.getenv("APP_NAME", "Mi Aplicación")
APP_VERSION = os.getenv("APP_VERSION", "1.0.0")
DB_HOST = os.getenv("DB_HOST")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

# Estilos CSS Futuristas
STYLE = """
<style>
    body { background-color: #0a0e14; color: #00f2ff; font-family: 'Courier New', monospace; padding: 50px; }
    h1 { text-transform: uppercase; letter-spacing: 5px; border-bottom: 2px solid #00f2ff; padding-bottom: 10px; }
    table { width: 100%; border-collapse: collapse; margin-top: 20px; background: #161b22; }
    th, td { padding: 15px; border: 1px solid #30363d; text-align: left; }
    th { color: #ff007f; }
    a { color: #00f2ff; text-decoration: none; font-weight: bold; display: block; margin-top: 20px; }
    a:hover { color: #ff007f; text-decoration: underline; }
</style>
"""

def check_db():
    try:
        conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
        conn.close()
        return "ONLINE"
    except:
        return "OFFLINE"

@app.route("/")
def home():
    return f"""
    {STYLE}
    <h1>{APP_NAME}</h1>
    <h3>Version: {APP_VERSION}</h3>
    <h3>Estado PostgreSQL: {check_db()}</h3>
    <a href="/productos">VER PRODUCTOS [ACCESS DB]</a>
    """

@app.route("/productos")
def productos():
    conn = psycopg2.connect(host=DB_HOST, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()
    cur.execute("SELECT * FROM productos")
    data = cur.fetchall()

    html = f"{STYLE}<h1>Inventario de Productos</h1><table>"
    for p in data:
        html += f"<tr><td>{'</td><td>'.join(map(str, p))}</td></tr>"
    html += "</table>"

    cur.close()
    conn.close()

    html += '<br><a href="/">« VOLVER AL INICIO</a>'
    return html

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
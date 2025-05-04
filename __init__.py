from flask import Flask
import sqlite3

def create_app():
    app = Flask(__name__)

    from .routes import main
    app.register_blueprint(main)

    with sqlite3.connect('database.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS customers (id INTEGER PRIMARY KEY, name TEXT)')
        conn.execute('CREATE TABLE IF NOT EXISTS sales (id INTEGER PRIMARY KEY, item TEXT, amount REAL)')

    return app
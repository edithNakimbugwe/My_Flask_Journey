# app.py
from flask import Flask
from books import books
from book_clients import clients

# Create Flask app
app = Flask(__name__)

# Register Blueprints
app.register_blueprint(books, url_prefix="/books")
app.register_blueprint(clients, url_prefix="/clients")

if __name__ == "__main__":
    app.run(debug=True)

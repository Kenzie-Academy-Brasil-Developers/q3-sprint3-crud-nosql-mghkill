from flask import Flask

from app.routes.publication_routes import all_routes

def init_app(app: Flask):
    
    all_routes(app)
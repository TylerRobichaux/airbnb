# web_app/__init__.py

from flask import Flask

#from web_app.routes.home_routes import home_routes
#from web_app.app import app
# from . import app1

def create_app():
    app1 = Flask(__name__)
    #app.register_blueprint(home_routes)
    #app.register_blueprint(book_routes)
    return app1

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)